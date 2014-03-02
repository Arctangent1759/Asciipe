import numpy as np
import cv2

class ImgGetter():
    TRUECHAR="1"#"\033[34m+"
    FALSECHAR="0"#"\033[32m+"
    def __init__(self, nCharX, nCharY):
        self.cam = cv2.VideoCapture(-1)
        self.nCharX=nCharX
        self.nCharY=nCharY

    def getImg(self):
        success, raw_data = self.cam.read()

        if not success:
            raise Exception("Failed to acquire webcam image.")

        #Resize and compute to greyscale
        grey = cv2.cvtColor(cv2.resize(raw_data,(3*40,2*40)),cv2.COLOR_BGR2GRAY)

        #Compute hpfs
        canny = cv2.Canny(grey,100,200)

        width = len(grey[0])
        height = len(grey)

        out = ""

        blockIncX = float(width)/self.nCharX
        blockIncY = float(height)/self.nCharY

        for y in np.arange(0,height,blockIncY):
            for x in reversed(np.arange(0,width,blockIncX)):
                x=int(x)
                y=int(y)
                block_c = np.ndarray.flatten(canny[y:y+blockIncY,x:x+blockIncX])

                if sum(block_c)==0:
                    out+=self.FALSECHAR
                else:
                    out+=self.TRUECHAR
            out+="\n"
        return out

    def __del__(self):
        self.cam.release()

#imGet = ImgGetter(13*5,8*5)
#imGet = ImgGetter(120,40)

#while True:
#    print imGet.getImg()

#del imGet
