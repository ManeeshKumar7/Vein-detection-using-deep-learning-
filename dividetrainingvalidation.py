<<<<<<< HEAD
import os
import shutil
import random

# === INPUT FOLDERS ===
image_dir = r"C:\Users\cmane\OneDrive\Desktop\IITH_jugular_final\final_jug_img_total"
mask_dir = r"C:\Users\cmane\OneDrive\Desktop\IITH_jugular_final\final_jug_mask_total"

# === OUTPUT FOLDERS ===
train_image_dir = r"C:\Users\cmane\OneDrive\Desktop\organized_jugular_final\train_jug_images"
train_mask_dir = r"C:\Users\cmane\OneDrive\Desktop\organized_jugular_final\train_jug_masks\veins"
val_image_dir = r"C:\Users\cmane\OneDrive\Desktop\organized_jugular_final\valid_jug_images"
val_mask_dir = r"C:\Users\cmane\OneDrive\Desktop\organized_jugular_final\valid_jug_masks\veins"

# === Number of samples ===
train_count = 6500
val_count = 1640

# === Create output dirs ===
for d in [train_image_dir, train_mask_dir, val_image_dir, val_mask_dir]:
    os.makedirs(d, exist_ok=True)

# === Collect and shuffle image filenames ===
image_filenames = [f for f in os.listdir(image_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
image_filenames.sort()  # Ensure consistent matching
random.shuffle(image_filenames)

# === Split ===
train_files = image_filenames[:train_count]
val_files = image_filenames[train_count:train_count + val_count]

def copy_images_and_masks(file_list, image_src, mask_src, image_dst, mask_dst):
    for fname in file_list:
        base_name = os.path.splitext(fname)[0]
        
        # Copy image
        shutil.copy(os.path.join(image_src, fname), os.path.join(image_dst, fname))
        
        # Find and copy corresponding mask (same name, any extension)
        possible_masks = [f for f in os.listdir(mask_src) if os.path.splitext(f)[0] == base_name]
        if not possible_masks:
            print(f"⚠️ No mask found for {fname}")
            continue
        
        mask_file = possible_masks[0]
        shutil.copy(os.path.join(mask_src, mask_file), os.path.join(mask_dst, mask_file))

# === Copy files ===
copy_images_and_masks(train_files, image_dir, mask_dir, train_image_dir, train_mask_dir)
copy_images_and_masks(val_files, image_dir, mask_dir, val_image_dir, val_mask_dir)

print("✅ Splitting complete:")
print(f"- Training: {len(train_files)} images + masks")
print(f"- Validation: {len(val_files)} images + masks")
=======
import os
import shutil
import random

# === INPUT FOLDERS ===
image_dir = r"C:\Users\cmane\OneDrive\Desktop\IITH_jugular_final\final_jug_img_total"
mask_dir = r"C:\Users\cmane\OneDrive\Desktop\IITH_jugular_final\final_jug_mask_total"

# === OUTPUT FOLDERS ===
train_image_dir = r"C:\Users\cmane\OneDrive\Desktop\organized_jugular_final\train_jug_images"
train_mask_dir = r"C:\Users\cmane\OneDrive\Desktop\organized_jugular_final\train_jug_masks\veins"
val_image_dir = r"C:\Users\cmane\OneDrive\Desktop\organized_jugular_final\valid_jug_images"
val_mask_dir = r"C:\Users\cmane\OneDrive\Desktop\organized_jugular_final\valid_jug_masks\veins"

# === Number of samples ===
train_count = 6500
val_count = 1640

# === Create output dirs ===
for d in [train_image_dir, train_mask_dir, val_image_dir, val_mask_dir]:
    os.makedirs(d, exist_ok=True)

# === Collect and shuffle image filenames ===
image_filenames = [f for f in os.listdir(image_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
image_filenames.sort()  # Ensure consistent matching
random.shuffle(image_filenames)

# === Split ===
train_files = image_filenames[:train_count]
val_files = image_filenames[train_count:train_count + val_count]

def copy_images_and_masks(file_list, image_src, mask_src, image_dst, mask_dst):
    for fname in file_list:
        base_name = os.path.splitext(fname)[0]
        
        # Copy image
        shutil.copy(os.path.join(image_src, fname), os.path.join(image_dst, fname))
        
        # Find and copy corresponding mask (same name, any extension)
        possible_masks = [f for f in os.listdir(mask_src) if os.path.splitext(f)[0] == base_name]
        if not possible_masks:
            print(f"⚠️ No mask found for {fname}")
            continue
        
        mask_file = possible_masks[0]
        shutil.copy(os.path.join(mask_src, mask_file), os.path.join(mask_dst, mask_file))

# === Copy files ===
copy_images_and_masks(train_files, image_dir, mask_dir, train_image_dir, train_mask_dir)
copy_images_and_masks(val_files, image_dir, mask_dir, val_image_dir, val_mask_dir)

print("✅ Splitting complete:")
print(f"- Training: {len(train_files)} images + masks")
print(f"- Validation: {len(val_files)} images + masks")
>>>>>>> 0bfae16b44f97944a5a0288c35d59f3aba3739bb
