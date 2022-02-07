
import pydicom
import pydicom.data
import cv2
import os


def convert_to_png():
    inputdir = './image'
    # os.mkdir("output")
    outdir = './output/'
    test_list = [f for f in os.listdir(inputdir)]
    for f in test_list:
        ds = pydicom.read_file("./image/"+f)  # read dicom image
        img = ds.pixel_array  # get image array
        cv2.imwrite(outdir + f.replace('.dcm', '.png'), img)

