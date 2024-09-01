import os


def get_last_subfolder_and_filename(file_path):
    # Get the last subfolder
    last_subfolder = os.path.basename(os.path.dirname(file_path))

    # Get the file name without extension
    file_name_without_extension = os.path.splitext(os.path.basename(file_path))[0]

    return last_subfolder, file_name_without_extension


# Example usage:
file_path = "data/aic-2024/keyframes/L01_V001/001.jpg"
last_subfolder, file_name_without_extension = get_last_subfolder_and_filename(file_path)

print("Last subfolder:", last_subfolder)
print("File name without extension:", file_name_without_extension)
