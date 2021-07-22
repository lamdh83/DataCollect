import cv2
import os

def CatHinhChu(img, scale=0.2):

    h,w,c = img.shape
    x = int(w*scale)
    y = int(h*scale)
    imgCrop = img[h-y:h, w-x:w]
    # print(f'h{h} / w {w} / c {c}')
    return w, h, imgCrop

def CatHinhHinh(img):

    h,w,c = img.shape
    x1 = int(w/4)
    x2 = int(w*3/4)
    y1 = int(h*3/4)
    imgCrop = img[y1:h, x1:x2]
    # print(f'h{h} / w {w} / c {c}')
    return w, h, imgCrop

def DocVaLuuHinh(pathDoc, pathLuu):
    myList = os.listdir(pathDoc)
    for x in range (0, len(myList)):
        # print(f'{pathDoc}//{myList[x]}')
        img = cv2.imread(f'{pathDoc}//{myList[x]}')
        w, h, imgCrop = CatHinhChu(img)
        # w, h, imgCrop = CatHinhHinh(img)
        imgCrop = cv2.resize(imgCrop,(224,224))
        cv2.imwrite(f'{pathLuu}//{myList[x]}',imgCrop)
    print('XONG ROIIIIIIII')





if __name__=="__main__":
    while True:
        # success, img = cap.read()
        # DocVaLuuHinh('Screencapture','Test')
        DocVaLuuHinh('2', 'QqChu')