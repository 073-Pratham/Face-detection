import os
import zipfile
import shutil

# --- Configuration ---
zip_path = 'archive.zip'  # Ensure your zip file is here.
output_dir = 'data'       # Folder where we want to extract the contents.

# --- Step 1: Extract the zip file if not already extracted ---
if os.path.exists(output_dir):
    print("Data folder already exists, skipping extraction.")
else:
    print("Extracting zip file into data folder...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(output_dir)
    print("Extraction complete!")

# --- Step 2 (Optional): Merge train and test subsets into one folder ---
# If you want to combine both train and test data into a single folder (e.g., for further splitting)
merge_into = os.path.join(output_dir, "all")
if not os.path.exists(merge_into):
    os.makedirs(merge_into)
    # Assuming the zip contains 'train' and 'test' folders directly under data/
    for subset in ['train', 'test']:
        subset_dir = os.path.join(output_dir, subset)
        if not os.path.isdir(subset_dir):
            print(f"Warning: {subset_dir} not found!")
            continue
        # For each emotion folder in the current subset folder
        for emotion in os.listdir(subset_dir):
            emotion_src_path = os.path.join(subset_dir, emotion)
            if not os.path.isdir(emotion_src_path):
                continue
            # Create target emotion folder if it doesn't exist
            emotion_target_path = os.path.join(merge_into, emotion)
            os.makedirs(emotion_target_path, exist_ok=True)
            # Copy all files from this emotion folder to the target, prefixing the file name with subset name
            for filename in os.listdir(emotion_src_path):
                src_file = os.path.join(emotion_src_path, filename)
                dst_file = os.path.join(emotion_target_path, f"{subset}_{filename}")
                shutil.copy(src_file, dst_file)
    print("Merged train and test into a single folder: data/all")
else:
    print("Merged folder already exists, skipping merge.")
