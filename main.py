from cv2 import imread
import dcm2png
import os

import mean

if __name__ == "__main__":
    dcm2png.convert_to_png()
    inputdir = './output'
    test_list = [f for f in os.listdir(inputdir)]
    for f in test_list[:10]:
        image = imread("./output/"+f)
        print(mean.getmean(image))