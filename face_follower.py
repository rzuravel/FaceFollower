import cv2
import serial

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# connect to the arduino through serial
# arduino = serial.Serial('COM5', 9600, timeout=1)

# To capture video from webcam. 
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    _, img = cap.read()
    #imgHeight = img.shape[0]
    #imgWidth = img.shape[1]

    #print(imgWidth, imgHeight)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    # faces = face_cascade.detectMultiScale(gray,
    #                                       scaleFactor=1.1,
    #                                       minNeighbors=5,
    #                                       minSize=(30,30),
    #                                       flags=cv2.CASCADE_SCALE_IMAGE)
    # Draw the rectangle around each face
    #averageWidth = 128
    #averageHeight = 128
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 255), 2)
    #    averageWidth = x + w / 2
    #    averageHeight = y + h / 2

    
    #if len(faces) > 0 and imgWidth > 0:
    #    averageWidth = int((averageWidth / len(faces) / imgWidth) * 255)
        # arduino.write(averageWidth.to_bytes(1,'big'))
        #print(averageWidth.to_bytes(1,'big'))
        

    
    #if len(faces) > 0 and imgHeight > 0:
    #    averageHeight = averageHeight / len(faces) / imgHeight

    # Send face center to arduino
    # if arduino.in_waiting > 0:
    # fromArduino = arduino.readline()
    # print(fromArduino)

    # Display
    cv2.flip(img, 1, img)
    cv2.imshow('OpenCV Window', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()