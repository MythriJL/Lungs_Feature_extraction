import numpy as np
import skimage
from scipy import ndimage
from scipy.stats import kurtosis
from scipy.stats import skew
from skimage.feature import graycomatrix, graycoprops
from skimage.io import imread
import dcm2png
import os
import csv
import cv2
from PIL import Image,ImageStat
from pywt import dwt2

import features

if __name__ == "__main__":
    fields = ['Mean', 'Standard Deviation', 'Entropy', 'Root Mean Square', 'Variance', 'Smoothness', 'Kurtosis', 'Skewness', 'Contrast', 'Co-relation', 'Energy', 'Homogeneity', 'Disease']
    csvFilename = "output.csv"
    dcm2png.convert_to_png()
    inputdir = './output'
    test_list = [f for f in os.listdir(inputdir)]
    with open(csvFilename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        for f in test_list:
            list = []
            img = cv2.imread("./output/" + f)
            im = Image.open("./output/" + f)
            image = imread("./output/" + f)
            g = graycomatrix(image, [1], [0], symmetric=False, normed=True)
           
            stat = ImageStat.Stat(im)                         
           
            img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
            
            Ener = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            _, (cH, cV, cD) = dwt2(Ener.T, 'db1')
            Energy = (cH**2 + cV**2 + cD**2).sum()/Ener.size
           
            thresh = cv2.threshold(img_grey, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
            thresh = 255 - thresh
            result = img.copy()
            contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            contours = contours[0] if len(contours) == 2 else contours[1]
            num_contours = 0
            sum = 0
            for cntr in contours:
                cv2.drawContours(result, [cntr], 0, (0,0,255), 1)
                num_vertices = len(cntr)
                sum = sum + num_vertices
                num_contours = num_contours + 1
            smoothness = (sum / num_contours)

            list.append(image.mean())
            list.append(image.std())
            list.append(skimage.measure.shannon_entropy(image))
            list.append((stat.rms)[0])
            list.append(ndimage.variance(image))
            list.append(smoothness)
            list.append(kurtosis(image, axis=None))
            list.append(skew(image, axis=None))
            list.append(img_grey.std())
            list.append(graycoprops(g, 'correlation')[0][0])
            list.append(Energy)
            list.append(graycoprops(g, 'homogeneity')[0][0])
            list.append('Covid')
            # change the value to Non-covid for non covid input
            csvwriter.writerow(list)
