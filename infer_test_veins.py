from ultralytics import YOLO
import cv2
import os
import numpy as np

# === Load YOLOv11 segmentation model ===
model = YOLO(r"C:\Users\cmane\OneDrive\Desktop\new_jugular_final\jug_train\weights\best.pt", task="segment")

# === Input and output directories ===
test_dir = r"C:\Users\cmane\OneDrive\Desktop\new_final_jugular_testing\input2"
output_dir = r"C:\Users\cmane\OneDrive\Desktop\new_final_jugular_testing\output2"
os.makedirs(output_dir, exist_ok=True)

# === Process each image ===
for file_name in os.listdir(test_dir):
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(test_dir, file_name)
        results = model(img_path, imgsz=640)
        original = results[0].orig_img.copy()

        # Draw blue masks if available
        if results[0].masks is not None:
            for mask_tensor in results[0].masks.data:
                mask = mask_tensor.cpu().numpy()
                mask = cv2.resize(mask, (original.shape[1], original.shape[0]))
                binary = (mask > 0.2).astype(np.uint8)

                blue_mask = np.zeros_like(original)
                blue_mask[binary == 1] = [255, 0, 0]  # Blue (BGR)

                original = cv2.addWeighted(original, 1.0, blue_mask, 0.5, 0)

        save_path = os.path.join(output_dir, file_name)
        cv2.imwrite(save_path, original)
        print(f"Saved: {save_path}")
