# import os
# import cv2
# import numpy as np

# # === Paths ===
# input_dir = r"D:\JUGULAR_VEINS_PROJECT\FINAL DATASET\labels"         # Folder with black & white .png mask images
# output_dir = r"D:\JUGULAR_VEINS_PROJECT\FINAL DATASET\polygon"           # Folder to store output .txt files
# os.makedirs(output_dir, exist_ok=True) # Create output directory if not exist

# # === Process each image ===
# for filename in os.listdir(input_dir):
#     if filename.endswith(".png"):
#         image_path = os.path.join(input_dir, filename)

#         # Read the mask image in grayscale
#         mask = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

#         # Threshold to ensure binary (in case it's not strictly 0 and 255)
#         _, binary = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)

#         # Find contours of the white regions (jugular vein)
#         contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#         # Prepare polygon list
#         polygons = []
#         for contour in contours:
#             polygon = [(int(point[0][0]), int(point[0][1])) for point in contour]
#             polygons.append(polygon)

#         # Save polygons to .txt with the same base name
#         txt_filename = os.path.splitext(filename)[0] + ".txt"
#         txt_path = os.path.join(output_dir, txt_filename)

#         with open(txt_path, 'w') as f:
#             for polygon in polygons:
#                 f.write(f"{polygon}\n")

# print("✅ Done! Polygon coordinates saved in:", output_dir)



# import os
# import cv2

# # Paths
# input_dir = r"D:\JUGULAR_VEINS_PROJECT\FINAL DATASET\labels"
# output_dir = r"D:\JUGULAR_VEINS_PROJECT\FINAL DATASET\polygon"
# os.makedirs(output_dir, exist_ok=True)

# # Process images
# for filename in os.listdir(input_dir):
#     if filename.endswith(".png"):
#         image_path = os.path.join(input_dir, filename)
#         image = cv2.imread(image_path)

#         gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if image.ndim == 3 else image
#         _, binary = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
#         contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#         height, width = binary.shape

#         all_polygons = []
#         for contour in contours:
#             polygon = [(
#                 round(float(pt[0][0]) / width, 6),
#                 round(float(pt[0][1]) / height, 6)
#             ) for pt in contour]
#             all_polygons.append(polygon)

#         txt_filename = os.path.splitext(filename)[0] + ".txt"
#         txt_path = os.path.join(output_dir, txt_filename)

#         with open(txt_path, 'w') as f:
#             for polygon in all_polygons:
#                 # Convert list of tuples to string before writing
#                 f.write(f"{polygon}\n")

# print("✅ Done! Clean normalized polygons saved in:", output_dir)



# import os
# import cv2

# def convert_masks_to_yolo_polygon(input_folder, output_folder, class_id=0):
#     """
#     Converts PNG mask annotations to YOLOv11-style polygon text files.
    
#     Args:
#         input_folder (str): Path to the folder containing annotation PNG images.
#         output_folder (str): Path to the folder to save YOLO .txt files.
#         class_id (int): Class ID to assign to each polygon (default: 0).
#     """
#     os.makedirs(output_folder, exist_ok=True)

#     for filename in os.listdir(input_folder):
#         if not filename.lower().endswith(".png"):
#             continue

#         mask_path = os.path.join(input_folder, filename)
#         mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

#         if mask is None:
#             print(f"Warning: Could not read image {mask_path}")
#             continue

#         height, width = mask.shape
#         contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#         yolo_lines = []

#         for contour in contours:
#             if len(contour) < 3:
#                 continue  # skip too small or invalid polygons

#             contour = contour.squeeze()
#             if contour.ndim != 2:
#                 continue

#             coords = []
#             for x, y in contour:
#                 x_norm = x / width
#                 y_norm = y / height
#                 coords.append(f"{x_norm:.6f} {y_norm:.6f}")

#             line = f"{class_id} " + " ".join(coords)
#             yolo_lines.append(line)

#         txt_filename = os.path.splitext(filename)[0] + ".txt"
#         txt_path = os.path.join(output_folder, txt_filename)

#         with open(txt_path, 'w') as f:
#             f.write("\n".join(yolo_lines))

#     print(f"✅ Conversion complete. YOLO polygon .txt files saved to: {output_folder}")


# # ✅ Call the function below with your paths:
# convert_masks_to_yolo_polygon(
#     input_folder=r"D:\JUGULAR_VEINS_PROJECT\FINAL DATASET\labels",
#     output_folder=r"D:\JUGULAR_VEINS_PROJECT\FINAL DATASET\labels"
# )


import cv2
import numpy as np
import os

def convert_mask_to_yolo(mask_path, image_path, output_path, class_id=0):
    """
    Convert a binary mask to YOLO polygon format and save the annotation.
    
    Args:
        mask_path (str): Path to the binary mask image.
        image_path (str): Path to the corresponding original image.
        output_path (str): Path to save the YOLO annotation file.
        class_id (int): Class ID for the object (default is 0 for jugular vein).
    """
    # Load the mask and original image
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.imread(image_path)
    
    if mask is None or img is None:
        print(f"Error: Could not load mask ({mask_path}) or image ({image_path})")
        return
    
    # Get image dimensions
    img_height, img_width = mask.shape
    
    # Ensure mask is binary (0 or 255)
    _, mask = cv2.threshold(mask, 128, 255, cv2.THRESH_BINARY)
    
    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if not contours:
        print(f"No contours found in mask: {mask_path}")
        return
    
    # Prepare YOLO annotation
    annotations = []
    for contour in contours:
        # Skip small contours (e.g., noise)
        if cv2.contourArea(contour) < 10:
            continue
            
        # Flatten and normalize coordinates
        contour = contour.squeeze()
        if len(contour.shape) == 1:  # Single point case
            continue
            
        normalized_coords = []
        for point in contour:
            x, y = point
            x_norm = x / img_width
            y_norm = y / img_height
            normalized_coords.extend([x_norm, y_norm])
            
        # Ensure coordinates are within [0, 1]
        normalized_coords = [max(0.0, min(1.0, coord)) for coord in normalized_coords]
        
        # Format: class_id x1 y1 x2 y2 ...
        annotation_line = f"{class_id} {' '.join(map(str, normalized_coords))}"
        annotations.append(annotation_line)
    
    if not annotations:
        print(f"No valid annotations for mask: {mask_path}")
        return
    
    # Save annotations to a .txt file
    output_file = os.path.splitext(os.path.basename(image_path))[0] + '.txt'
    output_file_path = os.path.join(output_path, output_file)
    
    with open(output_file_path, 'w') as f:
        f.write('\n'.join(annotations))
    print(f"Saved annotation: {output_file_path}")

def process_folder(mask_folder, image_folder, output_folder, class_id=0):
    """
    Process all mask images in a folder and generate YOLO annotations.
    
    Args:
        mask_folder (str): Path to the folder containing binary mask images.
        image_folder (str): Path to the folder containing original images.
        output_folder (str): Path to save YOLO annotation files.
        class_id (int): Class ID for the object (default is 0).
    """
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Process each mask file
    for mask_file in os.listdir(mask_folder):
        if mask_file.endswith('.png'):
            mask_path = os.path.join(mask_folder, mask_file)
            # Assume corresponding image has the same name (without '_mask' if present)
            image_name = mask_file.replace('_mask', '')  # Adjust based on naming convention
            image_path = os.path.join(image_folder, image_name)
            
            if not os.path.exists(image_path):
                print(f"Image not found for mask: {mask_path}")
                continue
                
            convert_mask_to_yolo(mask_path, image_path, output_folder, class_id)

# Example usage
mask_folder = r'D:\JUGULAR_VEINS_PROJECT\FINAL DATASET\labels'  # Replace with your mask folder path
image_folder = r'D:\JUGULAR_VEINS_PROJECT\FINAL DATASET\images'  # Replace with your original images folder path
output_folder = r'D:\JUGULAR_VEINS_PROJECT\FINAL DATASET\polygon'  # Replace with your output folder path

process_folder(mask_folder, image_folder, output_folder, class_id=0)