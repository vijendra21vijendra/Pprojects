import pyautogui  # pip install pyautogui
from PIL import Image, ImageGrab  # pip install pillow
# from numpy import asarray
import time


def hit(key):
    pyautogui.keyDown(key)
    return


def isCollide(data):
    # Draw the rectangle for birds

    for i in range(220, 270):
        for j in range(380, 460):
            if data[i, j] < 100:
                hit("up")
                return
    for i in range(250, 300):
        for j in range(260, 350):
            if data[i, j] < 100:
                hit("down")
                return
    return


if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    # hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
        # print(asarray(image))
    #      '''
    #     # Draw the rectangle for cactus
    #     for i in range(220, 270):
    #         for j in range(380, 460):
    #             data[i, j] = 0

    #     # Draw the rectangle for birds
    #     for i in range(250, 300):
    #         for j in range(300, 400):
    #             data[i, j] = 171

    #     # image.show()
    #     break
    #    '''