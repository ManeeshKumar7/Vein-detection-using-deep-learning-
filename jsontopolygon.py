import json
import os
import shutil
import yaml


def convert_to_yolo(input_images_path, input_json_path, output_images_path, output_labels_path):
    # Load COCO-format annotations
    with open(input_json_path) as f:
        data = json.load(f)

    os.makedirs(output_images_path, exist_ok=True)
    os.makedirs(output_labels_path, exist_ok=True)

    file_names = [f for f in os.listdir(input_images_path) if f.endswith(".png")]

    # Copy all images to YOLO image folder
    for filename in file_names:
        shutil.copy(os.path.join(input_images_path, filename),
                    os.path.join(output_images_path, filename))

    # Helper: get image metadata
    def get_img(filename):
        return next((img for img in data['images'] if img['file_name'] == filename), None)

    # Helper: get annotations by image ID
    def get_img_ann(image_id):
        return [ann for ann in data['annotations'] if ann['image_id'] == image_id]

    for filename in file_names:
        img = get_img(filename)
        if not img:
            continue

        img_id = img['id']
        img_w = img['width']
        img_h = img['height']
        img_ann = get_img_ann(img_id)

        label_file_path = os.path.join(output_labels_path, f"{os.path.splitext(filename)[0]}.txt")
        with open(label_file_path, "w") as f:
            for ann in img_ann:
                class_id = ann['category_id']  # already 0 for vein
                polygon = ann['segmentation'][0]

                # Normalize polygon coordinates
                normalized = [format(coord / img_w if i % 2 == 0 else coord / img_h, '.6f')
                              for i, coord in enumerate(polygon)]

                f.write(f"{class_id} " + " ".join(normalized) + "\n")


def create_yaml(input_json_path, output_yaml_path, train_path, val_path, test_path=None):
    with open(input_json_path) as f:
        data = json.load(f)

    names = [category['name'] for category in data['categories']]
    yaml_data = {
        'names': names,
        'nc': len(names),
        'train': train_path,
        'val': val_path,
        'test': test_path if test_path else ''
    }

    with open(output_yaml_path, 'w') as f:
        yaml.dump(yaml_data, f, default_flow_style=False)

if __name__ == "__main__":
    # Convert validation set
    convert_to_yolo(
        input_images_path=r"C:\Users\cmane\Downloads\phantom_raw\val_img_maskdataset\val\images",
        input_json_path=r"C:\Users\cmane\Downloads\phantom_raw\json dataset\val.json",
        output_images_path=r"C:\Users\cmane\Downloads\phantom_raw\final\valid\images",
        output_labels_path=r"C:\Users\cmane\Downloads\phantom_raw\final\valid\labels"
    )

    # Convert training set
    convert_to_yolo(
        input_images_path=r"C:\Users\cmane\Downloads\phantom_raw\train_img_dataset",
        input_json_path=r"C:\Users\cmane\Downloads\phantom_raw\json dataset\train.json",
        output_images_path=r"C:\Users\cmane\Downloads\phantom_raw\final\train\images",
        output_labels_path=r"C:\Users\cmane\Downloads\phantom_raw\final\train\labels"
    )

    # # Generate dataset YAML
create_yaml(
        input_json_path=r"C:\Users\cmane\Downloads\phantom_raw\json dataset\train.json",
        output_yaml_path=r"C:\Users\cmane\Downloads\phantom_raw\yaml\data.yaml",
        train_path=r"C:\Users\cmane\Downloads\phantom_raw\final\train\images",
        val_path=r"C:\Users\cmane\Downloads\phantom_raw\final\valid\images",
        
    )
