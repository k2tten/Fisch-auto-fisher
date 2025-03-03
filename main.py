import cv2
import numpy as np
import pydirectinput
import time
import mss

SHAKE_DELAY = .35 # user .3 (faster) to .4 (little slower but stable) # adjust to what works best for you!

template = cv2.imread("assets/shake.png")
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
w, h = template_gray.shape[::-1]
threshold = 0.8

with mss.mss() as sct:
    while True:
        screenshot = np.array(sct.grab(sct.monitors[0]))
        screen_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2GRAY)
        result = cv2.matchTemplate(screen_gray, template_gray, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)
        for pt in zip(*loc[::-1]):
            cx = pt[0] + w // 2
            cy = pt[1] + h // 2
            print(cx, cy)
            pydirectinput.moveTo(cx, cy, duration=0)
            pydirectinput.moveTo(cx, cy - 3, duration=0.1)
            pydirectinput.click()
        time.sleep(SHAKE_DELAY)
