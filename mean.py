import numpy as np
import mahotas
from cv2 import imread
from pylab import imshow, show

# loading image
import DicomRead
import dcm2png


def getmean(image):
    img = imread(image)
    img = img[:,0, 0]
    mean = img.mean()
    return mean
