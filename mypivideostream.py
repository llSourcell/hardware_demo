import os
import cv2

from picamera.array import PiRGBArray
from picamera import PiCamera
from threading import Thread

# path to training data for HAAR face classifier
FACE_DETECTOR_PATH  = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                   'haarcascade_frontalface_default.xml')

# http://www.pyimagesearch.com/2015/12/21/increasing-webcam-fps-with-python-and-opencv/
class PiVideoStream:
    def __init__(self, resolution=(640, 480), framerate=32, save_image_interval=1):
        '''
        @param save_image_interval, interval in sec to save imave
        '''
        # initialize the camera and stream
        self.camera = PiCamera()
        self.camera.resolution = resolution
        self.camera.framerate = framerate
        self.rawCapture = PiRGBArray(self.camera, size=resolution)
        self.stream = self.camera.capture_continuous(self.rawCapture,
            format="bgr", use_video_port=True)

        # initialize the frame and the variable used to indicate
        # if the thread should be stopped
        self.frame = None
        self.rects = [] # list of matching faces
        self.stopped = False

    def start(self):
        # start the thread to read frames from the video stream
        t = Thread(target=self.update, args=())
        t.daemon = True
        t.start()
        return self

    def update(self):
        # keep looping infinitely until the thread is stopped
        for f in self.stream:
            # grab the frame from the stream and clear the stream in
            # preparation for the next frame
            self.frame = f.array
            self.rawCapture.truncate(0)

            # convert the image to grayscale, load the face cascade detector,
            # and detect faces in the image
            # Using data trained from here:
            #   http://www.pyimagesearch.com/2015/05/11/creating-a-face-detection-api-with-python-and-opencv-in-just-5-minutes/
            image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            detector = cv2.CascadeClassifier(FACE_DETECTOR_PATH)
            rects = detector.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5,minSize=(30, 30), flags=cv2.cv.CV_HAAR_SCALE_IMAGE)
            
            # construct a list of bounding boxes from the detection
            self.rects = [(int(x), int(y), int(x + w), int(y + h)) for (x, y, w, h) in rects]

            # if the thread indicator variable is set, stop the thread
            # and resource camera resources
            if self.stopped:
                self.stream.close()
                self.rawCapture.close()
                self.camera.close()
                return

    def read(self):
        # return the frame most recently read
        return self.frame

    def read_rects(self):
        # return the matching rectangles most recently read after processing
        return self.rects

    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True
