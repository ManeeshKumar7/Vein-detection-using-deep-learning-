from PIL import Image
import os

# Input and output directories
input_dir = r"C:\Users\cmane\OneDrive\Desktop\IITH_jug_final\masks"
output_dir = r"C:\Users\cmane\OneDrive\Desktop\IITH_jug_final\new_masks"
os.makedirs(output_dir, exist_ok=True)

# Supported formats
extensions = ('.jpg', '.jpeg', '.png')

# Loop through all files
for filename in os.listdir(input_dir):
    if filename.lower().endswith(extensions):
        file_path = os.path.join(input_dir, filename)
        
        try:
            # Open image
            img = Image.open(file_path).convert("RGB")  # Convert to RGB (for PNG with alpha)
            
            # Create output filename with .jpg extension
            new_filename = os.path.splitext(filename)[0] + ".jpg"
            output_path = os.path.join(output_dir, new_filename)
            
            # Save as JPG
            img.save(output_path, "JPEG", quality=95)
        
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")

print("✅ Conversion complete.")
