# cvzone 1.3.3
#tensorflow
import cvzone
import cv2
from ScreenCapture import *
from utils import *

cap = cv2.VideoCapture(0)
myClassifier = cvzone.Classifier('Mymodels//keras_model.h5','Mymodels//labels.txt')
fpsReader = cvzone.FPS()

if __name__ == '__main__':
    while True:
        # _, img = cap.read()
        screenCapture()
        img = cv2.imread('Screencapture//screencapture.png')
        w, h, imgT = CatHinhHinh(img)
        # imgT = cv2.imread('QqChu//2.png')
        # imgT = cv2.resize(imgT,(224,224))
        prediction, index = myClassifier.getPrediction(imgT)
        print(prediction, index)
        fps, img = fpsReader.update(img, pos=(20, 100))
        cv2.imshow('KQ', img)
        cv2.imshow('hinh cat', imgT)
        cv2.waitKey(1)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
