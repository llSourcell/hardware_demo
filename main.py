import numpy
import cv2

from mypivideostream import PiVideoStream
from blinds import Blinds

if __name__ == '__main__':
    cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)

    # start and get contents of stream
    vs = PiVideoStream().start()
    vs.camera.rotation = -90
    
    # create blinds object
    blinds = Blinds()

    while(True):
        image = vs.read()
        if image is None:
            continue
        
        cv2.imshow("Frame", image)
        # this is needed if we want to see the debug output in the opencv
        # frame. but this increases flicker since will wait 1ms for key press
        # and 1ms is perceptible to our eyes when watch display refresh
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break 

        # get matching rects
        rects = vs.read_rects()
        
        # there is a face in the frame so there are bounding rectangles that match
        if len(rects) > 0:
            blinds.close()
        else:
            blinds.open()

    cv2.destroyAllWindows()
