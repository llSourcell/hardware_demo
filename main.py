import numpy
import cv2

from mypivideostream import PiVideoStream
from blinds import Blinds

if __name__ == '__main__':
    cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)

    # start and get contents of stream
    vs = PiVideoStream().start()
    
    # create blinds object
    blinds = Blinds()

    while(True):
        image = vs.read()
        if image is None:
            continue
        
        cv2.imshow("Frame", image)

        # get matching rects
        rects = vs.read_rects()
        
        # there is a face in the frame so there are bounding rectangles that match
        if len(rects) > 0:
            blinds.close()
        else:
            blinds.open()

    cv2.destroyAllWindows()
