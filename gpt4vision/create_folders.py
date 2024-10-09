import os

# Directory where you want to create the new folders
base_dir = r'C:\Users\H\Desktop\VC'

# Create 20 new folders
for i in range(4, 21):
    new_folder_name = f"new{i}"
    new_folder_path = os.path.join(base_dir, new_folder_name)
    
    # Check if folder already exists, if not, create it
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
        print(f"Created folder: {new_folder_path}")
    else:
        print(f"Folder {new_folder_path} already exists.")
