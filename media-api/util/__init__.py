def find_file_csv_fieno(folder_path: str, file_path: str):
    '''
    Process file_path to extract the last sub folder and filename.
    Then lookup in the folder to get file .csv and sequence no of file.
    :param folder_path: contains files of .csv such as L01_V001.csv, L01_V002.csv,...L12_V030.csv
    :param file_path: is a string such as '…\L01_V001\001.jpg', …/L01_V001/001.jpg
    :return: filename .csv in the folder_path, n
    Ex: L01_V001.csv, 1
    '''

    return "", 0