import numpy as np
import skimage
from scipy import ndimage
from scipy.stats import kurtosis
from skimage.feature import graycomatrix, graycoprops
from skimage.io import imread
import dcm2png
import os
import csv

import features

if __name__ == "__main__":
    fields = ['Mean', 'Entropy', 'Variance', 'Kurtosis', 'Co-relation', 'Homogeneity']
    csvFilename = "output.csv"
    dcm2png.convert_to_png()
    inputdir = './output'
    test_list = [f for f in os.listdir(inputdir)]
    with open(csvFilename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        for f in test_list:
            list = []
            image = imread("./output/" + f)
            g = graycomatrix(image, [1], [0], symmetric=False, normed=True)
            list.append(image.mean())
            list.append(skimage.measure.shannon_entropy(image))
            list.append(ndimage.variance(image))
            list.append(kurtosis(image, axis=None))
            list.append(graycoprops(g, 'correlation')[0][0])
            list.append(graycoprops(g, 'homogeneity')[0][0])
            csvwriter.writerow(list)
