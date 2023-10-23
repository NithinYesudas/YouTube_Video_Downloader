import os
from pydub import AudioSegment

# Define the input folder containing MP4 audio files
input_folder = "D:\Python\Side_Projects\Youtube_Video_Downloader"

# Define the output folder for MP3 files
output_folder = "D:\Python\Side_Projects\Youtube_Video_Downloader"

# Ensure the output folder exists, or create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate through files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".mp4"):
        input_path = os.path.join(input_folder, filename)
        output_filename = os.path.splitext(filename)[0] + ".mp3"
        output_path = os.path.join(output_folder, output_filename)

        # Load the MP4 audio and convert to MP3
        audio = AudioSegment.from_file(input_path, "mp4")
        audio.export(output_path, format="mp3")

        print(f"Converted {input_path} to {output_path}")

print("Conversion complete!")
