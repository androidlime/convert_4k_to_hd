import os
import ffmpeg

# Path to your folder containing MP4 files
input_folder = r'C:\Users\andrew\Desktop\week_1_houdini_hobbiests'
output_folder = r'C:\Users\andrew\Desktop\hd_version'

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Iterate through each file in the input folder
for file_name in os.listdir(input_folder):
    if file_name.lower().endswith('.mp4'):
        input_file = os.path.join(input_folder, file_name)
        output_file = os.path.join(output_folder, f'1080p_{file_name}')

        try:
            # Use ffmpeg to resize the video
            ffmpeg.input(input_file).output(output_file, vf='scale=1920:1080').run()
            print(f'Processed {file_name} -> {output_file}')
        except ffmpeg.Error as e:
            print(f'Error processing {file_name}: {e}')
