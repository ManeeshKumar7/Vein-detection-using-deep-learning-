import os
from PIL import Image, ImageOps
import numpy as np

def apply_perspective_transform(img):
    width, height = img.size
    coeffs = find_coeffs(
        [(0, 0), (width, 0), (width, height), (0, height)],
        [(0, 0), (width * 0.9, height * 0.1), (width, height), (width * 0.1, height * 0.9)]
    )
    return img.transform(img.size, Image.PERSPECTIVE, coeffs, Image.BICUBIC)

def find_coeffs(pa, pb):
    matrix = []
    for p1, p2 in zip(pa, pb):
        matrix.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0]*p1[0], -p2[0]*p1[1]])
        matrix.append([0, 0, 0, p1[0], p1[1], 1, -p2[1]*p1[0], -p2[1]*p1[1]])
    A = np.array(matrix, dtype=np.float32)
    B = np.array(pb).reshape(8)
    res = np.linalg.lstsq(A, B, rcond=None)[0]
    return res

def rotate_and_augment_images(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    for image_file in image_files:
        base_name = os.path.splitext(image_file)[0]
        image_path = os.path.join(input_folder, image_file)
        img = Image.open(image_path).convert("RGB")

        # Save original image
        img.save(os.path.join(output_folder, f"{base_name}.png"))

        # Horizontal flip
        img_hf = ImageOps.mirror(img)
        img_hf.save(os.path.join(output_folder, f"{base_name}_horizontal_flip.png"))

        # Vertical flip
        img_vf = ImageOps.flip(img)
        img_vf.save(os.path.join(output_folder, f"{base_name}_vertical_flip.png"))

        # Perspective transform
        img_persp = apply_perspective_transform(img)
        img_persp.save(os.path.join(output_folder, f"{base_name}_perspective.png"))

        # Rotate in 10° steps from 10 to 360
        for angle in range(10, 361, 10):
            img_rot = img.rotate(angle, expand=True)
            img_rot.save(os.path.join(output_folder, f"{base_name}_rotate_{angle}.png"))

    print("✅ Augmentation complete!")

# Example usage
input_folder = r'C:\Users\admin\Documents\images'
output_folder = r'C:\Users\admin\Documents\FINAL DATASET\images'
rotate_and_augment_images(input_folder, output_folder)
