import os
import shutil

def split_food101_dataset(dataset_dir):
    images_dir = os.path.join(dataset_dir, "images")
    meta_dir = os.path.join(dataset_dir, "meta/meta")
    train_file = os.path.join(meta_dir, "train.txt")
    test_file = os.path.join(meta_dir, "test.txt")
    
    train_dir = os.path.join(dataset_dir, "train")
    test_dir = os.path.join(dataset_dir, "test")
    
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    def move_files(file_list, dest_dir):
        with open(file_list, "r") as f:
            for line in f:
                image_path = line.strip() + ".jpg"
                class_name, image_name = image_path.split("/")
                src_path = os.path.join(images_dir, class_name, image_name)
                dest_class_dir = os.path.join(dest_dir, class_name)
                os.makedirs(dest_class_dir, exist_ok=True)
                shutil.copy(src_path, os.path.join(dest_class_dir, image_name))

    print("Splitting training dataset...")
    move_files(train_file, train_dir)

    print("Splitting testing dataset...")
    move_files(test_file, test_dir)

    print("Dataset splitting complete!")

if __name__ == "__main__":
    dataset_directory = "dataset/food_images/Food-101"
    split_food101_dataset(dataset_directory)
