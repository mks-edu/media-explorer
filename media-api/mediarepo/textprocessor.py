import os
import easyocr
import glob
from util import  get_last_subfolder_and_filename

class TextExtractor:
    reader = easyocr.Reader(['vi', 'en'])

    def extract_text(self, img_path, separator = ' '):
        '''
        @param img_path Ex: 'data/aic-2024/keyframes/L01_V017/065.jpg'
        @param separator used to combine found texts
        '''

        img_text = self. reader.readtext(img_path)
        final_text = ""

        for _, text, __ in img_text:  # _ = bounding box, text = text and __ = confident level
            final_text += text
            final_text += separator

        return final_text

    def extract_text_folder(self, folder_path: str, out_folder_path = None):
        '''
        Extract text from image folder.
        @param folder_path

        '''
        print('Processing folder: ', os.path.realpath(folder_path))
        if out_folder_path is None:
            out_folder_path = folder_path

        if not os.path.exists(out_folder_path):
            os.makedirs(out_folder_path)
        n = 0
        # Walk through the directory
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                filePath = os.path.join(root, file)

                try:
                    text = self.extract_text(filePath)
                    parentFolder, filename_no_ext = get_last_subfolder_and_filename(filePath)

                    self.createFile(out_folder_path, parentFolder, filename_no_ext + ".txt", text)

                    n += 1
                except Exception as ex:
                    print('Could not process file ' + filePath, ex)

        return n

    def createFile(self, rootPath, parentFolder, filename, text):
        folderPath = os.path.join(rootPath, parentFolder)
        filePath = os.path.join(folderPath, filename)

        # Create folder
        if not os.path.exists(folderPath):
            os.mkdir(folderPath)
            print(f"Created folder {folderPath}")
        else:
            print(f"Existing folder {folderPath}")

        # Open a file for writing in UTF-8 encoding
        with open(filePath, "w", encoding="utf-8") as file:
            # Write some text to the file
            file.write(text)
        print(f"Created file {filePath}")


