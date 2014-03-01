import numpy as np
import matplotlib.pyplot as plt
import cv2
from time import sleep

class ImgGetter():
    def __init__(self):
        self.cam = cv2.VideoCapture(-1)

    def getImg(self):
        success, data = self.cam.read()
        if not success:
            raise Exception("Failed to acquire webcam image.")
        return data

    def __del__(self):
        self.cam = cv2.VideoCapture(-1)

img = ImgGetter()
print img.getImg()
del img
