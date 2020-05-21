import threading

import cv2
import time
from copy import deepcopy
#import serial

NO_FACE = (-1, -1, -1, -1)

class FaceFollower():
    def __init__(self):
        self.running = False
        self.k = 0x0
        self.input_image = []
        self.input_image_lock = threading.Lock()
        self.face = []
        self.face_lock = threading.Lock()

        threads = []
        try:
            self.running = True

            # video thread
            v_thread = threading.Thread(target=self.video_thread)
            v_thread.start()
            threads.append(v_thread)

            # faces thread
            time.sleep(5)
            f_thread = threading.Thread(target=self.opencv_thread)
            f_thread.start()
            threads.append(f_thread)
        except:
            print ("Error creating threads")
            self.running = False

        while self.running:
            # Stop if escape key is pressed
            if self.k == 27:
                self.running = False
                for thread in threads:
                    thread.join()
                break

    def video_thread(self):
        # To capture video from webcam.
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) # I know my cam is 720p video
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        zooming = False

        while self.running:
            # Read the frame
            self.input_image_lock.acquire()
            _, self.input_image = cap.read()
            cv2.flip(self.input_image, 1, self.input_image)
            self.input_image_lock.release()

            if zooming:
                # Add face boxes to the frame
                self.input_image_lock.acquire()
                self.face_lock.acquire()
                if self.face is not NO_FACE:
                    x, y, w, h = self.face
                    #get the webcam size
                    height, width, channels = self.input_image.shape

                    min_x, max_x, min_y, max_y = self.find_zoom_window(x, y, w, h, width, height)

                    output_image = self.input_image
                    #cv2.rectangle(output_image, (min_x, min_y), (max_x, max_y), (255, 255, 255), 2)

                    cropped = self.input_image[min_y:max_y, min_x:max_x]
                    output_image = cv2.resize(cropped, (width, height))
                else:
                    output_image = self.input_image

                self.face_lock.release()
                self.input_image_lock.release()

            else:
                self.input_image_lock.acquire()
                output_image = deepcopy(self.input_image)
                self.input_image_lock.release()
                

            # Display
            cv2.imshow('OpenCV Window', output_image)

            # Stop if escape key is pressed
            self.k = cv2.waitKey(30) & 0xff
            if self.k == 122: # z key
                zooming = not zooming

        cap.release()

    def find_zoom_window(self, face_x, face_y, face_width, face_height, width, height):
        #prepare the crop
        centerX, centerY = int(face_x + face_width / 2), int(face_y + face_height / 2)
        radiusY = int(face_height/2)
        radiusX = int(face_height * width/height/2)

        min_x, max_x = centerX-radiusX, centerX+radiusX
        if (min_x < 0):
            min_x = 0
            max_x = 2 * radiusX
        elif (max_x > width):
            min_x = width - 2 * radiusX
            max_x = width

        min_y, max_y = centerY-radiusY, centerY+radiusY
        if (min_y < 0):
            min_y = 0
            max_y = 2 * radiusY
        elif (max_y > height):
            min_y = height - 2 * radiusY
            max_y = height
               

        return min_x, max_x, min_y, max_y

    def opencv_thread(self):
        # Load the cascade
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        while self.running:

            # Convert to grayscale
            self.input_image_lock.acquire()
            gray = cv2.cvtColor(self.input_image, cv2.COLOR_BGR2GRAY)
            self.input_image_lock.release()

            #gray_height = gray.shape[0]
            #gray_width = gray.shape[1]

            #print(imgWidth, imgHeight)
            local_faces = face_cascade.detectMultiScale(gray,
                                                       scaleFactor=1.1,
                                                       minNeighbors=5,
                                                       minSize=(200, 200),
                                                       flags=cv2.CASCADE_SCALE_IMAGE)

            # Detect the faces
            self.face_lock.acquire()
            if len(local_faces) > 0:
                self.face = deepcopy(local_faces[0])
            else:
                self.face = NO_FACE
            self.face_lock.release()


FACE = FaceFollower()



# connect to the arduino through serial
# arduino = serial.Serial('COM5', 9600, timeout=1)


    # Send face center to arduino
    # if arduino.in_waiting > 0:
    # fromArduino = arduino.readline()
    # print(fromArduino)
