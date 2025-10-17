from ultralytics import YOLO
import torch
import matplotlib.pyplot as plt



# Load a pretrained YOLOv11 model (small version)
my_new_model = YOLO(r"C:\Users\cmane\OneDrive\Desktop\new_jugular_final\jug_train\weights\best.pt") 

new_image = r"C:\Users\cmane\OneDrive\Desktop\new_final_jugular_testing\input\frames19_frame_0014.jpg"
new_results = my_new_model.predict(new_image, conf=0.2)  #Adjust conf threshold

new_result_array = new_results[0].plot()
plt.figure(figsize=(12, 12))
plt.imshow(new_result_array)
plt.show()