import numpy as np
import scipy.ndimage as ndi
import imageio
print (np.average(np.absolute(ndi.filters.laplace(imageio.imread('image_test.png').astype(float) / 255.0))))