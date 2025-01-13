import os
import subprocess
from pathlib import Path
import argparse

def extract_all(source_dir, target_dir):
    # Get the path to the 7zz executable
    script_dir = Path(__file__).parent
    seven_zip_path = script_dir / "7zz"

    # Check if the 7zz executable exists
    if not seven_zip_path.exists():
        raise FileNotFoundError(f"7zz executable not found at {seven_zip_path}")

    # Create the target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)

    # Scan all files in the source directory
    for archive_path in Path(source_dir).iterdir():
        if archive_path.is_file():  # Process only files
            folder_name = archive_path.stem  # Get file name without extension
            extract_path = os.path.join(target_dir, folder_name)

            try:
                # Ensure the extraction folder exists
                os.makedirs(extract_path, exist_ok=True)

                # Use 7zz to extract the archive
                subprocess.run([
                    str(seven_zip_path), "x", str(archive_path), f"-o{extract_path}"
                ], check=True)
 
                print(f"Extracted {archive_path} to {extract_path}")

            except subprocess.CalledProcessError as e:
                print(f"Failed to extract {archive_path}: {e}")

if __name__ == "__main__":
    source_dir = "../cache/data/ColonINST"
    target_dir = "../cache/data/ori_dataset_download_backup"

    # Create the target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)

    # Call the extraction function with the provided paths
    extract_all(source_dir, target_dir)
