import keyboard
import pyautogui
import cv2
#1920 x 1080
path = 1

def screenCapture(path='screencapture'):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(f'Screencapture\{path}.png')

# img = cv2.imread('screencapture\screencapture.png')
# frameWidth = 1920
# framHeight = 1080
#
#
# img = cv2.resize(img,(frameWidth,framHeight))
#
#
# cv2.imshow('screen', img)
# cv2.waitKey(0)


if __name__ == '__main__':
    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('s'):  # if key 'q' is pressed
                for i in range(0,100):
                    path = path + 1
                    screenCapture(path)
            elif keyboard.is_pressed('q'):
                break

        except:
            break  # if user pressed a key other than the given key the loop will break

