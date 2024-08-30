import glob

# Specify the directory path
directory = '/map-keyframes/*'

# List all files in the directory
files = glob.glob(directory)

# Print the list of files
for file in files:
    print(file)
