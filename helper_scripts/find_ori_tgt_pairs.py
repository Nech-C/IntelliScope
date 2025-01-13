import pandas as pd

# Load the CSV file
file_path = '../cache/data/data_reorganize.csv'
data = pd.read_csv(file_path)

# Extract only folder paths (remove file names) for target and original
data['target_folder'] = data['target'].apply(lambda x: "/".join(x.split("/")[:-1]))
data['original_folder'] = data['original'].apply(lambda x: "/".join(x.split("/")[:-1]))

# Get unique pairs of target and original folder paths
unique_folder_pairs = data[['target_folder', 'original_folder']].drop_duplicates()

# Save the unique folder pairs to a CSV file
unique_pairs_output_path = '../cache/data/reorganize_unique_pairs.csv'
unique_folder_pairs.to_csv(unique_pairs_output_path, index=False)

# Extract original file names from the original path
data['original_file_name'] = data['original'].apply(lambda x: x.split("/")[-1])

# Create a new DataFrame with original file names and their target paths (allow duplicates)
file_mapping = data[['target', 'original_file_name']].copy()
file_mapping.columns = ['Target Path', 'Original File Name']

# Save the file mappings to a CSV file
file_mapping_output_path = '../cache/data/original_file_to_target_paths.csv'
file_mapping.to_csv(file_mapping_output_path, index=False)

print(f"Unique folder pairs saved to {unique_pairs_output_path}")
print(f"File mappings (with original file names) saved to {file_mapping_output_path}")
