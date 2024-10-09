import csv
import random

def select_random_pictures(csv_file):
    # Dictionary to store image indices for each feature
    feature_indices = []

    # Read the CSV file
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Get header
        # Initialize feature indices list
        for i, column_name in enumerate(header[1:], start=1):  # Start from index 1, skipping first column (image index)
            feature_indices.append({'name': column_name, 'indices': []})

        # Collect image indices for each feature
        for row in csv_reader:
            image_index = row[0]
            for i in range(1, len(row)):
                if row[i] == '1':
                    feature_indices[i-1]['indices'].append(image_index)

    # Select 10 random images for each feature
    random_pictures = {}
    for feature_data in feature_indices:
        indices = feature_data['indices']
        if len(indices) >= 10:
            random_pictures[feature_data['name']] = random.sample(indices, 10)
        else:
            random_pictures[feature_data['name']] = indices

    return random_pictures

# Example usage:
csv_file = r'C:\Users\H\Desktop\VC\test01.csv'
random_pictures = select_random_pictures(csv_file)
for feature_data in random_pictures:
    print("Feature {}: {}".format(feature_data, random_pictures[feature_data]))
