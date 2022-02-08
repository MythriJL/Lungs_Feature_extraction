import numpy as np
import skimage.measure
from cv2 import imread
from scipy import ndimage
from skimage.color import rgb2gray
from skimage.feature import greycomatrix, greycoprops
from PIL import Image, ImageStat

def getcorrelation(image):
    image = imread(image)
    g = greycomatrix(image, [0, 1], [0, np.pi/2], levels=256)
    correlation = greycoprops(g, 'correlation')
    print('contrast is: ', contrast)
