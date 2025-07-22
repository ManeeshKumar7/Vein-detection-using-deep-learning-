import cv2
import os
import numpy as np

# === Input/Output Paths ===
input_folder = r"C:\Users\cmane\OneDrive\Desktop\IITH_jugular_final\masks"
output_folder = r"C:\Users\cmane\OneDrive\Desktop\IITH_jugular_final\final_jug_mask_total"
os.makedirs(output_folder, exist_ok=True)

# === Rotation Angles: 10° to 360° ===
angles = list(range(10, 361, 10))  # 10, 20, ..., 360

# === Loop through images ===
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".png", ".jpeg")):
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)
        h, w = img.shape[:2]
        center = (w // 2, h // 2)

        # Save original image too (optional)
        original_output = os.path.join(output_folder, filename)
        cv2.imwrite(original_output, img)

        # Generate 10° to 360° rotations
        for angle in angles:
            # Rotation matrix
            M = cv2.getRotationMatrix2D(center, angle, 1.0)
            rotated = cv2.warpAffine(img, M, (w, h), borderValue=(0, 0, 0))  # black padding

            # Output filename
            name, ext = os.path.splitext(filename)
            rotated_filename = f"{name}_rot{angle}{ext}"
            output_path = os.path.join(output_folder, rotated_filename)

            cv2.imwrite(output_path, rotated)

print("✅ Augmentation complete: +10° to +360° rotations saved.")
