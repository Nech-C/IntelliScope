import os
import shutil

def flatten_folder_structure(source_path, target_path):
    """Flattens nested folder structures."""
    for root, dirs, files in os.walk(source_path):
        for file in files:
            original_path = os.path.join(root, file)
            relative_path = os.path.relpath(original_path, source_path)
            target_file_path = os.path.join(target_path, relative_path)

            # Create target directory if it doesn't exist
            os.makedirs(os.path.dirname(target_file_path), exist_ok=True)

            # Move file to the target directory
            shutil.copy2(original_path, target_file_path)

    # Remove empty directories
    for root, dirs, files in os.walk(source_path, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)

def process_datasets(source_base_path, target_base_path):
    """Processes the dataset folders based on the described adjustments."""
    if not os.path.exists(target_base_path):
        os.makedirs(target_base_path)

    dataset_folders = os.listdir(source_base_path)

    for folder in dataset_folders:
        source_folder_path = os.path.join(source_base_path, folder)
        target_folder_path = os.path.join(target_base_path, folder)

        if not os.path.exists(target_folder_path):
            os.makedirs(target_folder_path)

        if folder == "bkai-igh-neopolyp":
            flatten_folder_structure(source_folder_path, target_folder_path)

        elif folder == "CP-CHILD":
            # Combine CP-CHILD-A and CP-CHILD-B
            for subfolder in ["CP-CHILD-A", "CP-CHILD-B"]:
                subfolder_path = os.path.join(source_folder_path, subfolder)
                for dataset_type in ["Test", "Train"]:
                    source = os.path.join(subfolder_path, dataset_type)
                    target = os.path.join(target_folder_path, dataset_type)
                    if os.path.exists(source):
                        shutil.copytree(source, target, dirs_exist_ok=True)
                if os.path.exists(subfolder_path):
                    shutil.rmtree(subfolder_path)

        elif folder == "CPC-Paired":
            # Flatten classification_pub structure
            pub_path = os.path.join(source_folder_path, "classification_pub")
            flatten_folder_structure(pub_path, target_folder_path)

        elif folder.startswith("curated-colon-dataset-for-deep-learning"):
            shutil.copytree(source_folder_path, target_folder_path, dirs_exist_ok=True)

        elif folder.startswith("EDD2020"):
            flatten_folder_structure(source_folder_path, target_folder_path)

        elif folder.startswith("ETIS-LaribPolypDB"):
            flatten_folder_structure(source_folder_path, target_folder_path)

        elif folder.startswith("kvasir-dataset"):
            flatten_folder_structure(source_folder_path, target_folder_path)

        elif folder.startswith("piccolo dataset"):
            # Remove intermediate folder level
            intermediate_folder = os.path.join(source_folder_path, "piccolo dataset-release0.1")
            if os.path.exists(intermediate_folder):
                for item in os.listdir(intermediate_folder):
                    shutil.move(os.path.join(intermediate_folder, item), target_folder_path)
                shutil.rmtree(intermediate_folder)

        elif folder.startswith("PolypGen2021_MultiCenterData_v3"):
            flatten_folder_structure(source_folder_path, target_folder_path)

        elif folder == "PS-NBI2K":
            flatten_folder_structure(source_folder_path, target_folder_path)

        elif folder == "the-nerthus-dataset":
            flatten_folder_structure(source_folder_path, target_folder_path)

        print(f"Processed {folder}.")

if __name__ == "__main__":
    source_dir = "../cache/data/ori_dataset_download_backup"
    target_dir = "../cache/data/ori_dataset_download"
    process_datasets(source_dir, target_dir)
    print("Dataset adjustment completed.")
