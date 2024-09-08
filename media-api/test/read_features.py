import os
import numpy as np

# Loading the precomputed embedding from .npy
image_embedding = np.load('image_feature.npy')

# Using the embedding for similarity search or further processing

# Path to the folder containing clip feature files
folder_path = "data/aic-2024/clip-features-32"

for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        file_path = os.path.join(folder_path, filename)
        image_embedding = np.load(file_path)