from PIL import ImageGrab
from PIL import ImageOps
import pyautogui
import time
from numpy import *

class Coordinates():
# THE Coordinates may differ due to different size
    replaybtn = (340,390)
    dinosaur = (171,395)

def restartGame():
    pyautogui.click(Coordinates.replaybtn)
    pyautogui.keyDown('down')

def press_Space():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    print("jump")
    time.sleep(0.18)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')

def image_grab():
# Here also ,THE Coordinates may differ due to different size
    box = (Coordinates.dinosaur[0]+60,Coordinates.dinosaur[1],Coordinates.dinosaur[0]+150,Coordinates.dinosaur[1]+5 )
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return a.sum()

def main():
    restartGame()
    while True:
        if(image_grab()!= 697):
            press_Space()
            time.sleep(0.1)

main()



