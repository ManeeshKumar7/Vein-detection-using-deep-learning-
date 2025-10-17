##from ultralytics import YOLO

# # Load the YOLO11 model
# model = YOLO(r"D:\IIT HYDERABAD INTERNSHIP\JUGULAR VEINS\epochs300\weights\best.pt")

# # Export the model to NCNN format
# model.export(format="ncnn")  # creates '/yolo11n_ncnn_model'

# # # Load the exported NCNN model
## ncnn_model = YOLO(r"D:\IIT HYDERABAD INTERNSHIP\JUGULAR VEINS\epochs300\yolo11n_ncnn_model")

# # # Run inference
# # # results = ncnn_model("https://ultralytics.com/images/bus.jpg")



from ultralytics import YOLO

# Load the trained YOLO model
model = YOLO(r"C:\Users\cmane\OneDrive\Desktop\new_jugular_final\jug_train\weights\best.pt")

# Export the model to NCNN format with image size 416x416
model.export(format="ncnn", imgsz=(416,416))

ncnn_model = YOLO(r"C:\Users\cmane\Downloads\new_jugular_final_ncnn")