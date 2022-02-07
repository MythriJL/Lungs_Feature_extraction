import numpy as np
import matplotlib.pyplot as plt
import pydicom
import pydicom.data
import cv2
import os


def convert_to_png():


    inputdir = './image'
    outdir = './'


    test_list = [f for f in os.listdir(inputdir)]

    for f in test_list[:10]:  # remove "[:10]" to convert all images
        print(f)
        ds = pydicom.read_file("./image/0000a175-0e68-4ca4-b1af-167204a7e0bc.dcm")  # read dicom image
        img = ds.pixel_array  # get image array
        cv2.imwrite(outdir + f.replace('.dcm', '.png'), img)
convert_to_png()
