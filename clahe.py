import cv2
import os

def apply_clahe_to_folder(input_folder, output_folder, clip_limit=1.0, tile_grid_size=(8, 8)):
    # Create output directory if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get list of files in input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tif')):
            input_path = os.path.join(input_folder, filename)

            # Read image in grayscale
            image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
            if image is None:
                print(f"Skipping unreadable image: {filename}")
                continue

            # Apply CLAHE
            clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
            clahe_image = clahe.apply(image)

            # Save output image
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, clahe_image)

    print(f"CLAHE applied to all images in: {input_folder}\nSaved to: {output_folder}")

# Example usage
input_dir = r"C:\Users\cmane\OneDrive\Desktop\IITH_jugular_final\images"
output_dir = r"C:\Users\cmane\OneDrive\Desktop\IITH_jugular_final\images3"
apply_clahe_to_folder(input_dir, output_dir)
