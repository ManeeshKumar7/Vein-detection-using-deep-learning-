import React, { useState, useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import { Upload, Brain, Activity, Eye, Download, Settings } from 'lucide-react';
import axios from 'axios';
import './App.css';

function App() {
  const API_BASE =
    process.env.REACT_APP_API_BASE && process.env.REACT_APP_API_BASE.trim() !== ''
      ? process.env.REACT_APP_API_BASE.trim()
      : (typeof window !== 'undefined' && (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'))
        ? 'http://localhost:5000'
        : '';
  const [image, setImage] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [confidence, setConfidence] = useState(0.2);

  const onDrop = useCallback((acceptedFiles) => {
    const file = acceptedFiles[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = () => {
        setImage(reader.result);
        setResult(null);
        setError(null);
      };
      reader.readAsDataURL(file);
    }
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'image/*': ['.jpeg', '.jpg', '.png', '.bmp', '.tiff']
    },
    multiple: false
  });

  const detectVeins = async () => {
    if (!image) return;

    setLoading(true);
    setError(null);

    try {
      const response = await axios.post(`${API_BASE}/api/detect`, {
        image: image,
        confidence: confidence
      });

      if (response.data.success) {
        setResult(response.data);
      } else {
        setError(response.data.error || 'Detection failed');
      }
    } catch (err) {
      setError('Failed to connect to the detection service. Please make sure the backend is running.');
      console.error('Detection error:', err);
    } finally {
      setLoading(false);
    }
  };

  const downloadResult = () => {
    if (!result?.result_image) return;

    const link = document.createElement('a');
    link.href = result.result_image;
    link.download = `jugular-vein-detection-${Date.now()}.jpg`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  const reset = () => {
    setImage(null);
    setResult(null);
    setError(null);
  };

  return (
    <div className="App">
      <div className="container">
        <header className="header">
          <h1>
            <Brain className="inline-icon" />
            Jugular Vein Detection
          </h1>
          <p>AI-powered medical imaging analysis for jugular vein identification</p>
        </header>

        <div className="card">
          <h2>
            <Upload className="inline-icon" />
            Upload Medical Image
          </h2>
          
          <div
            {...getRootProps()}
            className={`image-container ${image ? 'has-image' : ''} ${isDragActive ? 'dragover' : ''}`}
          >
            <input {...getInputProps()} />
            {image ? (
              <img src={image} alt="Uploaded medical image" />
            ) : (
              <div className="upload-area">
                <Upload size={48} color="#94a3b8" />
                <p style={{ marginTop: '16px', fontSize: '16px', color: '#64748b' }}>
                  {isDragActive
                    ? 'Drop the image here...'
                    : 'Drag & drop a medical image here, or click to select'}
                </p>
                <p style={{ marginTop: '8px', fontSize: '14px', color: '#94a3b8' }}>
                  Supports JPEG, PNG, BMP, TIFF formats
                </p>
              </div>
            )}
          </div>

          {image && (
            <div className="controls">
              <div className="control-group">
                <label htmlFor="confidence">Confidence Threshold</label>
                <input
                  id="confidence"
                  type="number"
                  min="0.1"
                  max="1.0"
                  step="0.1"
                  value={confidence}
                  onChange={(e) => setConfidence(parseFloat(e.target.value))}
                />
              </div>
              
              <button
                className="btn btn-primary"
                onClick={detectVeins}
                disabled={loading}
              >
                {loading ? (
                  <>
                    <div className="loading" />
                    Analyzing...
                  </>
                ) : (
                  <>
                    <Eye />
                    Detect Jugular Veins
                  </>
                )}
              </button>

              <button className="btn btn-secondary" onClick={reset}>
                Reset
              </button>
            </div>
          )}

          {error && (
            <div className="error-message">
              <strong>Error:</strong> {error}
            </div>
          )}
        </div>

        {result && (
          <div className="card">
            <h2>
              <Activity className="inline-icon" />
              Detection Results
            </h2>
            
            <div className="detection-stats">
              <div className="stat-card">
                <div className="stat-value">{result.total_detections}</div>
                <div className="stat-label">Veins Detected</div>
              </div>
              <div className="stat-card">
                <div className="stat-value">
                  {result.detections.length > 0 
                    ? Math.round(result.detections.reduce((sum, d) => sum + d.confidence, 0) / result.detections.length * 100)
                    : 0}%
                </div>
                <div className="stat-label">Avg Confidence</div>
              </div>
              <div className="stat-card">
                <div className="stat-value">
                  {result.detections.length > 0 
                    ? Math.round(result.detections.reduce((sum, d) => sum + d.area, 0) / result.detections.length)
                    : 0}
                </div>
                <div className="stat-label">Avg Area (pixels)</div>
              </div>
            </div>

            <div className="results-grid">
              <div>
                <h3>Original Image</h3>
                <img src={image} alt="Original" style={{ width: '100%', borderRadius: '8px' }} />
              </div>
              <div>
                <h3>Detection Results</h3>
                <div style={{ position: 'relative' }}>
                  <img 
                    src={result.result_image} 
                    alt="Detection results" 
                    style={{ width: '100%', borderRadius: '8px' }} 
                  />
                  <button
                    className="btn btn-primary"
                    onClick={downloadResult}
                    style={{ 
                      position: 'absolute', 
                      top: '12px', 
                      right: '12px',
                      padding: '8px 12px',
                      fontSize: '12px'
                    }}
                  >
                    <Download size={16} />
                    Download
                  </button>
                </div>
              </div>
            </div>

            {result.detections.length > 0 && (
              <div style={{ marginTop: '24px' }}>
                <h3>Detection Details</h3>
                <div style={{ 
                  display: 'grid', 
                  gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', 
                  gap: '12px',
                  marginTop: '16px'
                }}>
                  {result.detections.map((detection, index) => (
                    <div key={index} style={{
                      background: '#f8fafc',
                      padding: '16px',
                      borderRadius: '8px',
                      border: '1px solid #e2e8f0'
                    }}>
                      <div style={{ fontWeight: '600', marginBottom: '8px' }}>
                        Vein #{detection.id + 1}
                      </div>
                      <div style={{ fontSize: '14px', color: '#64748b' }}>
                        <div>Confidence: {Math.round(detection.confidence * 100)}%</div>
                        <div>Area: {detection.area} pixels</div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}

        <div className="card" style={{ textAlign: 'center', background: 'rgba(255, 255, 255, 0.8)' }}>
          <h3>
            <Settings className="inline-icon" />
            About This Tool
          </h3>
          <p style={{ marginTop: '12px', color: '#64748b', lineHeight: '1.6' }}>
            This application uses YOLOv11 segmentation models to detect and highlight jugular veins in medical images. 
            The detected veins are highlighted in blue with adjustable confidence thresholds for optimal results.
          </p>
          <p style={{ marginTop: '8px', fontSize: '14px', color: '#94a3b8' }}>
            For medical use only. Always consult with healthcare professionals for clinical decisions.
          </p>
        </div>
      </div>
    </div>
  );
}

export default App;
