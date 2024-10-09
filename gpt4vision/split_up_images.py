import os
import shutil
import random

# Path to the directory containing the original images
source_dir = r'C:\Users\H\Desktop\VC\newpics2'

# Base path for the directories where you want to copy the images
target_base_dir = r'C:\Users\H\Desktop\VC\all_folders2'

# List all the images in the source directory
images = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]

# Shuffle the images to ensure randomness
random.shuffle(images)

# Calculate the number of required folders
num_folders = len(images) // 7 + (1 if len(images) % 7 else 0)

for i in range(num_folders):
    # Create a target directory for the current chunk of images
    target_dir = os.path.join(target_base_dir, f'folder_{i+1}')
    os.makedirs(target_dir, exist_ok=True)
    
    # Get the next chunk of 7 images (or fewer if we're at the end of the list)
    image_chunk = images[i*7:(i+1)*7]
    
    # Copy each image in the chunk to the target directory
    for image in image_chunk:
        source_path = os.path.join(source_dir, image)
        target_path = os.path.join(target_dir, image)
        shutil.copy(source_path, target_path)

print("Images have been copied to the target folders.")
