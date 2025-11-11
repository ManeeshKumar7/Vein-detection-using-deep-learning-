from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from ultralytics import YOLO
import cv2
import numpy as np
import os
import base64
import io
from PIL import Image
import math

app = Flask(__name__)
CORS(app)

# Global model variable
model = None

def load_model():
    """Load the YOLO model for jugular vein detection"""
    global model
    if model is not None:
        return True
    try:
        # Try to load the trained model, fallback to pretrained if not found
        model_paths = [
            "jugular_yolo11_seg.pt",
            "runs/jugular_training/yolo11-jugular-seg/weights/best.pt",
            "yolo11n-seg.pt"  # fallback to pretrained
        ]
        
        for path in model_paths:
            if os.path.exists(path):
                model = YOLO(path, task="segment")
                print(f"✅ Model loaded from: {path}")
                return True
        
        # If no model found, use pretrained
        model = YOLO("yolo11n-seg.pt", task="segment")
        print("⚠️ Using pretrained model (trained model not found)")
        return True
        
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return False


def ensure_model_loaded():
    """Ensure that a YOLO model instance is available."""
    if model is None and not load_model():
        raise RuntimeError("Jugular vein model could not be loaded")
    return model


def sanitize_confidence(raw_value, default=0.2):
    """Convert incoming confidence values into a safe float within [0, 1]."""
    try:
        confidence = float(raw_value)
    except (TypeError, ValueError):
        return default

    if math.isnan(confidence):
        return default

    return max(0.0, min(1.0, confidence))

def process_image(image_data, confidence_threshold=0.2):
    """Process image and return detection results"""
    try:
        model_instance = ensure_model_loaded()

        # Convert base64 to image
        image_bytes = base64.b64decode(image_data.split(',')[1])
        image = Image.open(io.BytesIO(image_bytes))
        
        # Convert PIL to OpenCV format
        opencv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        
        # Run inference
        results = model_instance(opencv_image, imgsz=640, conf=confidence_threshold)
        
        # Process results
        original = results[0].orig_img.copy()
        detections = []
        
        if results[0].masks is not None:
            for i, mask_tensor in enumerate(results[0].masks.data):
                mask = mask_tensor.cpu().numpy()
                mask = cv2.resize(mask, (original.shape[1], original.shape[0]))
                binary = (mask > 0.2).astype(np.uint8)
                
                # Create blue overlay for jugular vein
                blue_mask = np.zeros_like(original)
                blue_mask[binary == 1] = [255, 0, 0]  # Blue (BGR)
                original = cv2.addWeighted(original, 1.0, blue_mask, 0.5, 0)
                
                # Calculate area
                area = np.sum(binary)
                detections.append({
                    "id": i,
                    "area": int(area),
                    "confidence": float(results[0].boxes.conf[i]) if results[0].boxes is not None else 0.0
                })
        
        # Convert result back to base64
        _, buffer = cv2.imencode('.jpg', original)
        result_base64 = base64.b64encode(buffer).decode('utf-8')
        
        return {
            "success": True,
            "result_image": f"data:image/jpeg;base64,{result_base64}",
            "detections": detections,
            "total_detections": len(detections)
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


@app.before_first_request
def initialize_model():
    """Attempt to load the model before handling any requests."""
    try:
        ensure_model_loaded()
    except RuntimeError as exc:
        app.logger.error("Model initialization failed: %s", exc)

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    model_ready = model is not None or load_model()
    return jsonify({
        "status": "healthy",
        "model_loaded": model_ready
    })

@app.route('/api/detect', methods=['POST'])
def detect_veins():
    """Main endpoint for jugular vein detection"""
    try:
        data = request.get_json()
        
        if not data or 'image' not in data:
            return jsonify({
                "success": False,
                "error": "No image data provided"
            }), 400
        
        confidence = sanitize_confidence(data.get('confidence'))
        ensure_model_loaded()
        result = process_image(data['image'], confidence)
        
        return jsonify(result)
        
    except RuntimeError as e:
        return jsonify({
            "success": False,
            "error": f"Model error: {str(e)}"
        }), 500
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Server error: {str(e)}"
        }), 500

@app.route('/api/model/info', methods=['GET'])
def model_info():
    """Get information about the loaded model"""
    if model is None:
        return jsonify({
            "success": False,
            "error": "Model not loaded"
        }), 500
    
    return jsonify({
        "success": True,
        "model_type": "YOLOv11 Segmentation",
        "task": "jugular_vein_detection",
        "input_size": 640
    })

@app.route('/')
def serve_frontend():
    """Serve the HTML frontend"""
    return send_from_directory('.', 'simple_frontend.html')

if __name__ == '__main__':
    print("🚀 Starting Jugular Vein Detection API...")
    
    if load_model():
        print("✅ Model loaded successfully")
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        print("❌ Failed to load model. Exiting...")
