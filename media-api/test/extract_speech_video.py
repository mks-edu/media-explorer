import cv2
import pytesseract

# Load the video
cap = cv2.VideoCapture('data/aic-2024/videos/Videos_L12_a/L12_V016.mp4')

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
    print(text)

cap.release()
