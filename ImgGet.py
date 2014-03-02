import numpy as np
import cv2

COLORS = [
    np.array([0, 0, 0]),
    np.array([170, 0, 0]),
    np.array([0, 170, 0]),
    np.array([170, 85, 0]),
    np.array([0, 0, 170]),
    np.array([170, 0, 170]),
    np.array([0, 170, 170]),
    np.array([170, 170, 170]),
    np.array([255, 255, 255]),
    ]

def getClosestColor(x):
    bestIndex = -1
    minDist = float("infty")
    for i in range(len(COLORS)):
        diff = COLORS[i]-x
        normSq = np.dot(diff,diff)
        if normSq < minDist:
            minDist = normSq
            bestIndex = i
    return i

class ImgGetter():
    TRUECHAR="+"
    FALSECHAR="+"
    def __init__(self, nCharX, nCharY):
        self.cam = cv2.VideoCapture(-1)
        self.nCharX=nCharX
        self.nCharY=nCharY

    def getImg(self):
        success, raw_data = self.cam.read()
        if not success:
            raise Exception("Failed to acquire webcam image.")

        #Resize and compute to greyscale
        data = cv2.cvtColor(cv2.resize(raw_data,(3*40,2*40)),cv2.COLOR_BGR2GRAY)

        #Compute hpfs
        canny = cv2.Canny(data,100,200)

        width = len(data[0])
        height = len(data)

        out = ""

        blockIncX = int(width/self.nCharX)
        blockIncY = int(height/self.nCharY)

        for y in range(0,height,blockIncY):
            for x in range(0,width,blockIncX):
                block_c = np.ndarray.flatten(canny[y:y+blockIncY,x:x+blockIncX])

                if sum(block_c)==0:
                    out+="\033[0;34m{0}".format(self.FALSECHAR)
                else:
                    out+="\033[1;32m{0}".format(self.TRUECHAR)
            out+="\n"
        return out

    def __del__(self):
        self.cam.release()

imGet = ImgGetter(13*5,8*5)

while True:
    print imGet.getImg()

del imGet
