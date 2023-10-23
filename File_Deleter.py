import os

# Specify the folder path where you want to delete .mp4 files
folder_path = "D:\Python\Side_Projects\Youtube_Video_Downloader"

# List all files in the folder
files = os.listdir(folder_path)

# Iterate through the files and delete .mp4 files
for file in files:
    if file.endswith(".mp3"):
        file_path = os.path.join(folder_path, file)
        os.remove(file_path)
        print(f"Deleted: {file}")

print("Deletion of .mp4 files completed.")
