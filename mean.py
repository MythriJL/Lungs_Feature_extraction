from cv2 import imread

def getmean(img):
    img = img[:, 0, 0]
    mean = img.mean()
    return mean
