# 🩺 Jugular Vein Detection System using YOLOv11 Segmentation

An AI-powered medical image analysis system designed to automatically detect and segment jugular veins from ultrasound and medical imaging data using a custom-trained YOLOv11 segmentation model.

The system provides an intuitive web interface for uploading images, running real-time vein segmentation, visualizing results, and exporting processed outputs for further analysis.

---

## 🚀 Project Overview

Jugular vein identification plays an important role in various clinical procedures such as venous access, catheter placement, and vascular assessment. Manual localization can be challenging due to anatomical variations and image quality differences.

This project leverages Deep Learning and Computer Vision techniques to automatically identify and segment jugular veins with high accuracy, enabling faster and more consistent analysis.

---

## ✨ Key Features

* 🧠 **Deep Learning-Based Detection**

  * Custom-trained YOLOv11 segmentation model for jugular vein identification.

* 🎯 **Pixel-Level Segmentation**

  * Generates precise vein masks rather than simple bounding boxes.

* 📤 **Medical Image Upload**

  * Supports JPEG, PNG, BMP, and TIFF image formats.

* ⚙️ **Configurable Confidence Threshold**

  * Adjust detection sensitivity according to clinical requirements.

* 📊 **Detailed Detection Analytics**

  * Detection confidence scores
  * Segmentation mask statistics
  * Vein area measurements

* 🖼️ **Visual Result Comparison**

  * Original image
  * Segmentation overlay
  * Processed output

* 💾 **Export & Download Results**

  * Save segmented images for documentation and further analysis.

* 📱 **Responsive User Interface**

  * Compatible with desktop, tablet, and mobile devices.

* ⚡ **Fast Inference**

  * Real-time prediction with GPU acceleration support.

---

## 🏗️ System Architecture

```text
Medical Image
       │
       ▼
React Frontend
       │
       ▼
Flask REST API
       │
       ▼
YOLOv11 Segmentation Model
       │
       ▼
Segmentation Mask + Detection Results
```

### Technology Stack

| Component        | Technology           |
| ---------------- | -------------------- |
| Frontend         | React.js             |
| Backend          | Flask                |
| AI Model         | YOLOv11 Segmentation |
| Image Processing | OpenCV               |
| Deep Learning    | PyTorch              |
| Deployment       | Local/Cloud Ready    |

---

## 📂 Project Structure

```text
jugular-vein-detection/
│
├── frontend/
│   ├── src/
│   └── public/
│
├── backend/
│   ├── app.py
│   ├── model/
│   └── utils/
│
├── models/
│   └── best.pt
│
├── uploads/
├── outputs/
├── train.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Prerequisites

* Python 3.8+
* Node.js 16+
* npm or yarn
* CUDA-compatible GPU (Optional)

---

### Backend Setup

```bash
git clone <repository-url>
cd jugular-vein-detection

python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

pip install -r requirements.txt
```

Start the Flask server:

```bash
python app.py
```

---

### Frontend Setup

```bash
cd frontend

npm install

npm start
```

The application will launch at:

```text
http://localhost:3000
```

---

## 🖥️ Usage

### 1. Upload an Image

* Drag and drop a medical image
* Or browse and select a file

### 2. Configure Detection

Adjust the confidence threshold:

```text
0.1 → More detections
1.0 → Higher confidence detections only
```

### 3. Run Segmentation

Click:

```text
Detect Jugular Veins
```

The uploaded image will be processed using the trained YOLOv11 model.

### 4. Review Results

View:

* Segmentation masks
* Confidence scores
* Detection statistics
* Processed images

### 5. Export Results

Download the segmented output for reporting or future analysis.

---

## 🔌 REST API

### Health Check

```http
GET /api/health
```

Returns:

```json
{
  "status": "healthy",
  "model_loaded": true
}
```

---

### Detect Jugular Veins

```http
POST /api/detect
```

Request:

```json
{
  "image": "base64_image",
  "confidence": 0.25
}
```

Response:

```json
{
  "success": true,
  "detections": [],
  "processed_image": "base64_output"
}
```

---

### Model Information

```http
GET /api/model/info
```

Returns model metadata and configuration details.

---

## 🤖 Model Training

### Dataset Preparation

Prepare images and segmentation annotations in YOLO segmentation format.

```text
dataset/
├── images/
│   ├── train/
│   └── val/
│
└── labels/
    ├── train/
    └── val/
```

### Training

```bash
python train.py
```

Or directly using Ultralytics:

```bash
yolo segment train \
model=yolo11n-seg.pt \
data=jugular.yaml \
epochs=100 \
imgsz=640
```

### Using a Trained Model

Place the trained weights file:

```text
models/best.pt
```

The system will automatically load the model during startup.

---

## 📈 Performance Highlights

* Custom-trained on manually annotated jugular vein images
* Pixel-level segmentation output
* Real-time inference capability
* Supports CPU and GPU execution
* Scalable for clinical research applications

---

## 🔧 Configuration

### Model Search Priority

The application searches for models in the following order:

```text
1. models/best.pt
2. jugular_yolo11_seg.pt
3. runs/.../weights/best.pt
4. Pretrained fallback model
```

### Environment Variables

```env
FLASK_ENV=development
PORT=5000
```

---

## 🛠️ Troubleshooting

### Model Not Loading

* Verify model path
* Check file permissions
* Ensure compatibility with YOLOv11 segmentation

### CUDA Issues

```bash
pip install torch torchvision torchaudio
```

Or switch inference to CPU mode.

### Frontend Cannot Connect

* Verify Flask server is running
* Confirm backend port configuration
* Check CORS settings

### Memory Limitations

* Reduce image size
* Use batch size = 1
* Close unused applications

---

## ⚠️ Medical Disclaimer

This project is intended for research, educational, and development purposes only.

The system should not be used as a standalone diagnostic tool or as the sole basis for clinical decision-making. Any medical interpretation should be performed by qualified healthcare professionals.

---

## 👨‍💻 Author

**Maneesh Kumar**

Designed, developed, trained, and deployed the complete end-to-end Jugular Vein Detection Pipeline, including:

* Dataset preparation and annotation
* YOLOv11 segmentation training
* Flask API development
* React frontend development
* Model integration and deployment
* Performance evaluation and optimization

---

## 🙏 Acknowledgements

* Ultralytics YOLOv11
* PyTorch
* OpenCV
* Flask
* React.js
* Medical Imaging Research Community

---


