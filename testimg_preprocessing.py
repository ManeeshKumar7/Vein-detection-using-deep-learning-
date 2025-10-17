# import cv2
# import torch
# import numpy as np
# from ultralytics import YOLO

# # -------------------------------------
# # Preprocessing Function
# # -------------------------------------
# def preprocess_image(img, target_size=640):
#     # Convert to grayscale
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # CLAHE (Contrast Limited Adaptive Histogram Equalization)
#     clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
#     clahe_img = clahe.apply(gray)

#     # Gaussian blur
#     blurred = cv2.GaussianBlur(clahe_img, (3, 3), 0)

#     # Normalize and resize
#     norm = cv2.normalize(blurred, None, 0, 255, cv2.NORM_MINMAX)
#     resized = cv2.resize(norm, (target_size, target_size))

#     # Convert to 3 channels (YOLO expects 3-channel input)
#     three_channel = cv2.merge([resized, resized, resized])  # Shape: (640, 640, 3)

#     return three_channel, resized

# # -------------------------------------
# # Load and Preprocess Image
# # -------------------------------------
# img_path = r"C:/Users/cmane/OneDrive/Desktop/jug veins images/frames4_frame_0077.jpg"
# original_img = cv2.imread(img_path)
# preprocessed_img, gray_resized = preprocess_image(original_img)

# # -------------------------------------
# # Load YOLOv11 Segmentation Model
# # -------------------------------------
# model_path = r"C:/Users/cmane/Downloads/jugveins_ncnn/best.pt"  # ← Replace with your model path
# model = YOLO(model_path)

# # Run inference
# results = model(preprocessed_img)[0]  # Ultralytics handles conversion internally

# # -------------------------------------
# # Draw Segmentation Mask on Output Image
# # -------------------------------------
# output_img = cv2.cvtColor(gray_resized, cv2.COLOR_GRAY2BGR)

# if results.masks is not None:
#     for mask in results.masks.data:
#         mask = mask.cpu().numpy()  # [640, 640]
#         colored_mask = (mask * 255).astype(np.uint8)
#         contours, _ = cv2.findContours(colored_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#         cv2.drawContours(output_img, contours, -1, (0, 255, 0), 2)

# # -------------------------------------
# # Display
# # -------------------------------------
# cv2.imshow("Vein Detection", output_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
import cv2
import torch
import numpy as np
from ultralytics import YOLO

# -------------------------------
# Load model (YOLOv11, Segmentation)
# -------------------------------
model = YOLO(r"C:\Users\cmane\OneDrive\Desktop\new_jugular_final\jug_train\weights\best.pt" )  # 🔁 Replace with your model path

# -------------------------------
# Load image and extract red channel
# -------------------------------
img = cv2.imread(r"C:\Users\cmane\OneDrive\Desktop\new_final_jugular_testing\input\frames19_frame_0014.jpg")  # 🔁 Replace with your test image path
img_resized = cv2.resize(img, (416, 416))

# Extract red channel (OpenCV uses BGR)
red_channel = img_resized[:, :, 2]  # shape: (416, 416)

# Convert to 3-channel format (R, R, R) so YOLO accepts it
img_input = cv2.merge([red_channel, red_channel, red_channel])

# -------------------------------
# Run inference
# -------------------------------
results = model(img_input, conf=0.1)[0]  # Lower conf for testing

# -------------------------------
# Draw predicted masks
# -------------------------------
output_img = cv2.cvtColor(red_channel, cv2.COLOR_GRAY2BGR)  # for display

if results.masks is not None:
    for mask in results.masks.data:
        mask = mask.cpu().numpy()
        binary_mask = (mask * 255).astype(np.uint8)
        contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(output_img, contours, -1, (0, 255, 0), 2)

# -------------------------------
# Show Result
# -------------------------------
cv2.imshow("Vein Detection", output_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
