# Jugular Vein Detection System

A modern web application for AI-powered jugular vein detection in medical images using YOLOv11 segmentation models.

## Features

- 🧠 **AI-Powered Detection**: Uses YOLOv11 segmentation models for accurate jugular vein identification
- 🖼️ **Image Upload**: Drag & drop or click to upload medical images (JPEG, PNG, BMP, TIFF)
- 🎯 **Adjustable Confidence**: Fine-tune detection sensitivity with confidence thresholds
- 📊 **Detailed Results**: View detection statistics, areas, and confidence scores
- 💾 **Export Results**: Download processed images with highlighted veins
- 📱 **Responsive Design**: Works on desktop, tablet, and mobile devices
- ⚡ **Real-time Processing**: Fast inference with visual feedback

## Architecture

- **Backend**: Flask API with YOLOv11 model integration
- **Frontend**: React.js with modern UI components
- **Model**: YOLOv11 segmentation for medical image analysis

## Installation

### Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher
- CUDA-compatible GPU (optional, for faster inference)

### Backend Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd jug_vein
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare your model**:
   - Place your trained YOLOv11 model file as `jugular_yolo11_seg.pt` in the root directory
   - Or use the pretrained model (will be downloaded automatically)

5. **Start the backend server**:
   ```bash
   python app.py
   ```
   The API will be available at `http://localhost:5000`

### Frontend Setup

1. **Navigate to the frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install Node.js dependencies**:
   ```bash
   npm install
   ```

3. **Start the development server**:
   ```bash
   npm start
   ```
   The frontend will be available at `http://localhost:3000`

## Usage

1. **Open the application** in your web browser at `http://localhost:3000`

2. **Upload an image**:
   - Drag and drop a medical image onto the upload area
   - Or click to select a file from your computer

3. **Adjust settings** (optional):
   - Set the confidence threshold (0.1 to 1.0)
   - Higher values = more confident detections only
   - Lower values = more detections, including uncertain ones

4. **Run detection**:
   - Click "Detect Jugular Veins" to analyze the image
   - Wait for processing to complete

5. **View results**:
   - See detection statistics and highlighted veins
   - Compare original vs. processed images
   - Download results if needed

## API Endpoints

### Health Check
```
GET /api/health
```
Returns server status and model loading information.

### Detection
```
POST /api/detect
Content-Type: application/json

{
  "image": "data:image/jpeg;base64,...",
  "confidence": 0.2
}
```

### Model Information
```
GET /api/model/info
```
Returns information about the loaded model.

## Model Training

To train your own model:

1. **Prepare your dataset** in YOLO format
2. **Create a dataset configuration file** (`jugular.yaml`)
3. **Run training**:
   ```bash
   python train.py
   ```
4. **Use the trained model** by placing `best.pt` in the appropriate directory

## Configuration

### Model Paths
The application looks for models in this order:
1. `jugular_yolo11_seg.pt` (root directory)
2. `runs/jugular_training/yolo11-jugular-seg/weights/best.pt`
3. Downloads pretrained YOLOv11 model (fallback)

### Environment Variables
- `FLASK_ENV`: Set to `development` for debug mode
- `PORT`: Backend port (default: 5000)

## Troubleshooting

### Common Issues

1. **Model not loading**:
   - Ensure the model file exists and is accessible
   - Check file permissions
   - Verify the model is compatible with YOLOv11

2. **CUDA errors**:
   - Install CUDA-compatible PyTorch version
   - Or set device to 'cpu' in the code

3. **Frontend not connecting**:
   - Ensure backend is running on port 5000
   - Check CORS settings
   - Verify proxy configuration in package.json

4. **Memory issues**:
   - Reduce batch size in model configuration
   - Use smaller image sizes
   - Close other applications

### Performance Tips

- Use GPU acceleration for faster inference
- Optimize image sizes before upload
- Adjust confidence thresholds for your use case
- Consider model quantization for deployment

## Medical Disclaimer

⚠️ **Important**: This tool is for research and educational purposes only. It should not be used as the sole basis for medical diagnosis or treatment decisions. Always consult with qualified healthcare professionals for clinical applications.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions:
- Check the troubleshooting section
- Review the API documentation
- Open an issue on GitHub

## Acknowledgments

- YOLOv11 by Ultralytics
- React.js community
- Medical imaging research community
