import os

# Specify the directory path
directory = '/map-keyframes'

# List all files in the directory
files = os.listdir(directory)

# Print the list of files
for file in files:
    print(file)
