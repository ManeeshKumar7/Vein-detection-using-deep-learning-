# Vein-detection-using-deep-learning-
This project focuses on real-time detection and segmentation of jugular and peripheral veins using deep learning, specifically YOLOv11-based instance segmentation. Developed as part of a research internship at IIT Hyderabad, the goal was to create a lightweight, deployable system for non-invasive medical imaging, especially useful in emergency

Key Features

Custom YOLOv11-segmentation model trained on grayscale and stereo images

Manual mask annotation for precise vein segmentation

Real-time inference on Raspberry Pi with camera module

PyQt5 GUI interface with live feed, blue overlay masks, and system control buttons

Optimized for low latency and edge-device performance


🧠 Technologies Used

Python, PyTorch, YOLOv11-seg

OpenCV, PyQt5, NumPy

Raspberry Pi, Picamera

Matplotlib, Seaborn


📌 Highlights

End-to-end AI pipeline: Data collection → Annotation → Training → Deployment

GUI designed for field usability with stop/shutdown controls

Supports real-time stereo or grayscale camera feeds with segmentation overlays


 Applications

Emergency vein visualization

Low-cost diagnostic support

AI-assisted clinical tools for IV insertion and vascular assessments
