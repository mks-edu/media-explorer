import os
import easyocr
import cv2
import pytesseract
from util import  get_last_subfolder_and_filename

class TextExtractor:
    reader = easyocr.Reader(['vi', 'en'])

    def extract_text(self, img_path, separator = ' '):
        '''
        @param img_path Ex: 'data/aic-2024/keyframes/L01_V017/065.jpg'
        @param separator used to combine found texts
        '''

        img_text = self. reader.readtext(img_path)
        final_text = ''

        for _, text, __ in img_text:  # _ = bounding box, text = text and __ = confident level
            final_text += text
            final_text += separator

        return final_text

    def extract_text_video(self, video_path, separator =' '):
        '''
        @param img_path Ex: 'data/aic-2024/keyframes/L01_V017/065.jpg'
        @param separator used to combine found texts
        '''

        # Load the video
        cap = cv2.VideoCapture(video_path)
        final_text = ''
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Convert the frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Apply image preprocessing
            gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
            gray = cv2.medianBlur(gray, 3)

            # Extract text from the frame
            text = pytesseract.image_to_string(gray)
            final_text += text
            final_text += separator

        cap.release()

        return final_text
    def extract_text_folder(self, folder_path: str, out_folder_path = None, source_type = 0):
        '''
        Extract text from image folder.
        @param folder_path
        @param out_folder_path
        @param source_type

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
                    if source_type == 0:
                        text = self.extract_text(filePath)
                    else:
                        text = self.extract_text_video(filePath, separator='\n')

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


