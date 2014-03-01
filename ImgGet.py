import numpy as np
import matplotlib.pyplot as plt
import cv2
from time import sleep

class ImgGetter():
    def __init__(self, nCharX, nCharY):
        self.cam = cv2.VideoCapture(-1)
        self.nCharX=nCharX
        self.nCharY=nCharY

    def getImg(self):
        success, data = self.cam.read()
        if not success:
            raise Exception("Failed to acquire webcam image.")
        return data

    def __del__(self):
        self.cam = cv2.VideoCapture(-1)

imGet = ImgGetter()
print imGet.getImg()
del imGet
