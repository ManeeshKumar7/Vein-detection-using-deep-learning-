import os
import shutil
import random

# Paths to your original folders
image_folder = r'C:\Users\admin\Documents\final dataset\images'
binary_folder = r'C:\Users\admin\Documents\final dataset\labels'

# Output folders
output_base = r'C:\Users\admin\Desktop\final_dataset'
train_img_dir = os.path.join(output_base, 'train/images')
train_bin_dir = os.path.join(output_base, 'train/binary_images')
val_img_dir = os.path.join(output_base, 'val/images')
val_bin_dir = os.path.join(output_base, 'val/binary_images')

# Create output directories if they don't exist
for folder in [train_img_dir, train_bin_dir, val_img_dir, val_bin_dir]:
    os.makedirs(folder, exist_ok=True)

# Get list of files and shuffle
all_files = sorted(os.listdir(image_folder))
all_files = [f for f in all_files if os.path.isfile(os.path.join(image_folder, f))]
random.seed(42)  # for reproducibility
random.shuffle(all_files)

# Split 80/20
split_index = int(len(all_files) * 0.8)
train_files = all_files[:split_index]
val_files = all_files[split_index:]

# Copy files
for fname in train_files:
    shutil.copy(os.path.join(image_folder, fname), os.path.join(train_img_dir, fname))
    shutil.copy(os.path.join(binary_folder, fname), os.path.join(train_bin_dir, fname))

for fname in val_files:
    shutil.copy(os.path.join(image_folder, fname), os.path.join(val_img_dir, fname))
    shutil.copy(os.path.join(binary_folder, fname), os.path.join(val_bin_dir, fname))

print(f"Training files: {len(train_files)}, Validation files: {len(val_files)}")
