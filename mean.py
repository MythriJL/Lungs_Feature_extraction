import numpy as np
import mahotas
from pylab import imshow, show

# loading image
import DicomRead
import dcm2png

dicom = DicomRead.read("/Users/mythrijl/Documents/VII/Project/Codes/Feature Extraction/image","0000a175-0e68-4ca4-b1af-167204a7e0bc.dcm")
img =  dcm2png.convert_to_png(dicom)


# filtering the image
img = img[:, 0]

print("Image with filter")


# getting mean value
mean = img.mean()

# printing mean value
print("Mean Value for 0 channel : " + str(mean))

