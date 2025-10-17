
from ultralytics import YOLO
import cv2
import os

# Load trained YOLOv11 segmentation model
# model = YOLO(r'D:\IIT HYDERABAD INTERNSHIP\JUGULAR VEINS\epochs300\weights\best.pt',task="segment")  # replace with your model path
# model = YOLO(r'D:\IIT HYDERABAD INTERNSHIP\JUGULAR VEINS\secondepochs300\weights\best.pt',task="segment")  # replace with your model path
# model = YOLO(r'D:\IIT HYDERABAD INTERNSHIP\JUGULAR VEINS\yolo12epochs300\weights\best.pt',task="segment")  # replace with your model path
model = YOLO(r"C:\Users\cmane\OneDrive\Desktop\new_jugular_final\jug_train\weights\best.pt")  # replace with your model path


# Path to test images
test_dir = r"C:\Users\cmane\OneDrive\Desktop\new_final_jugular_testing\input"

# output_dir = r'D:\IIT HYDERABAD INTERNSHIP\JUGULAR VEINS\testing\1st epochs 300\frames3' 
# output_dir = r'D:\IIT HYDERABAD INTERNSHIP\JUGULAR VEINS\testing\2nd epochs 300\frames38' 
output_dir = r"C:\Users\cmane\OneDrive\Desktop\new_final_jugular_testing\output"
''
# output_dir = r'D:\JUGULAR VEINS PROJECT\testing\frames004'
os.makedirs(output_dir, exist_ok=True)

# Run inference on all images in the test directory
for file_name in os.listdir(test_dir):
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(test_dir, file_name)

        # Run prediction
        results = model(img_path)

        # Plot and save result with segmentation masks
        result_img = results[0].plot(boxes = False, labels = False, conf=False)  # overlay masks, boxes, labels
        save_path = os.path.join(output_dir, file_name)
        cv2.imwrite(save_path, result_img)

        print(f"Saved: {save_path}") 


# from ultralytics import YOLO
# import cv2
# import os
# import numpy as np

# # Load trained YOLOv11 segmentation model
# model = YOLO(r'D:\JUGULAR VEINS PROJECT\best.pt')  # Replace with your model path

# # Path to test images
# test_dir = r'D:\IIT HYDERABAD INTERNSHIP\JUGULAR VEINS PROJECT\New Frames\frames4'
# output_dir = r'D:\JUGULAR VEINS PROJECT\test results\one'
# os.makedirs(output_dir, exist_ok=True)

# # Run inference on all images in the test directory
# for file_name in os.listdir(test_dir):
#     if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
#         img_path = os.path.join(test_dir, file_name)

#         # Load the original image
#         img = cv2.imread(img_path)
#         if img is None:
#             print(f"Failed to load image: {img_path}")
#             continue

#         # Run prediction
#         results = model(img_path)

#         # Check if there are segmentation results
#         if results[0].masks is not None:
#             # Get the segmentation masks
#             masks = results[0].masks.data.cpu().numpy()  # Shape: (num_masks, H, W)

#             # Iterate over each mask
#             for mask in masks:
#                 # Convert mask to binary (0 or 1)
#                 mask = (mask > 0).astype(np.uint8) * 255

#                 # Resize mask to match image dimensions if necessary
#                 if mask.shape != img.shape[:2]:
#                     mask = cv2.resize(mask, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_NEAREST)

#                 # Create a colored overlay for the mask (blue color)
#                 colored_mask = np.zeros_like(img)
#                 colored_mask[mask == 255] = [255, 0, 0]  # Blue in BGR format

#                 # Overlay the mask on the original image
#                 img = cv2.addWeighted(img, 0.7, colored_mask, 0.3, 0)

#         # Save the result
#         save_path = os.path.join(output_dir, file_name)
#         cv2.imwrite(save_path, img)
#         print(f"Saved: {save_path}")