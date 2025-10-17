from ultralytics import YOLO

# Load a pretrained YOLOv11 segmentation model
model = YOLO("yolo11n-seg.pt")   # you can also use yolo11s-seg.pt or larger models

# Train the model
results = model.train(
    data="jugular.yaml",   # dataset config file
    epochs=200,            # train for 200 epochs
    imgsz=640,             # image size
    batch=8,               # batch size (adjust to your GPU memory)
    device=0,              # GPU id (use 'cpu' if no GPU)
    project="runs/jugular_training",
    name="yolo11-jugular-seg"
)

# Save final weights
model.save("jugular_yolo11_seg.pt")
print("✅ Training complete. Model saved as jugular_yolo11_seg.pt")
