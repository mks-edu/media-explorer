import os
import pandas as pd

def get_frame_idx_for_n(df, n_value):
    # Filter the DataFrame where 'n' equals 'n_value'
    result = df[df['n'] == n_value]

    # Check if any row matches the condition
    if not result.empty:
        # Get the value of 'frame_idx' for the matched row
        frame_idx = result.iloc[0]['frame_idx']
        print('Type of var frame_idx:', frame_idx.dtype)

        return int(frame_idx)
    else:
        return None  # Return None if no matching row is found

def find_file_csv_fieno_frame_idx(folder_path: str, file_path: str):
    '''
    Process file_path to extract the last sub folder and filename.
    Then lookup in the folder to get file .csv, sequence no of file, and frame index
    :param folder_path: contains files of .csv such as L01_V001.csv, L01_V002.csv,...L12_V030.csv
    :param file_path: is a string such as '…\L01_V001\001.jpg', …/L01_V001/001.jpg
    :return: filename .csv in the folder_path, n, frame idex
    Ex: L01_V001.csv, 1, 0
    '''

    filecsv, fileno = find_file_csv_fieno(folder_path, file_path)

    filecsv_path = os.path.join(folder_path, filecsv)

    # Read the CSV file into a DataFrame
    df = pd.read_csv(filecsv_path)

    frame_idx = get_frame_idx_for_n(df, fileno)

    return filecsv, fileno, frame_idx

def find_file_csv_fieno(folder_path: str, file_path: str):
    '''
    Process file_path to extract the last sub folder and filename.
    Then lookup in the folder to get file .csv and sequence no of file.
    :param folder_path: contains files of .csv such as L01_V001.csv, L01_V002.csv,...L12_V030.csv
    :param file_path: is a string such as '…\L01_V001\001.jpg', …/L01_V001/001.jpg
    :return: filename .csv in the folder_path, n
    Ex: L01_V001.csv, 1
    '''

    last_subfolder, file_name_without_extension = get_last_subfolder_and_filename(file_path)

    filecsv = last_subfolder + ".csv"
    fileno = int(file_name_without_extension)

    return filecsv, fileno

def get_last_subfolder_and_filename(file_path):
    # Get the last subfolder
    last_subfolder = os.path.basename(os.path.dirname(file_path))

    # Get the file name without extension
    file_name_without_extension = os.path.splitext(os.path.basename(file_path))[0]

    return last_subfolder, file_name_without_extension