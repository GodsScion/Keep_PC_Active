'''
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla
Version:    1.0.0
'''

import pyautogui
pyautogui.FAILSAFE = False
from config import *

def countdown(message, timeLeft):
    try:
        print(message)
        while timeLeft > 0:
            # pyautogui.move(+1, 0)
            # pyautogui.move(-1, 0)
            pyautogui.press('shiftleft')
            pyautogui.sleep(min(intervals, timeLeft))
            timeLeft -= intervals
        h = int(extend_time/3600)
        m = int(extend_time/60 - h*60)
        s = extend_time%60
        if pyautogui.confirm("Extend time by  {} hr {} min {} sec?".format(h, m, s), buttons=['Yes','No']) == "Yes":
            countdown("Extended time by  {} hr {} min {} sec.\nWhen done press 'Ctrl + C' or close this window to exit.".format(h, m, s), extend_time)
    except KeyboardInterrupt:
        print("Script terminated by the user")

if __name__ == "__main__":
    try:
        h = int(total_time/3600)
        m = int(total_time/60 - h*60)
        countdown("Program started. Will run for  {} hr {} min {} sec.\nFeel free to minimize the screen and carry on with your work.\nWhen done press 'Ctrl + C' or close this window to exit.".format(h, m, total_time%60), total_time)
    except Exception as error:
        print("Error Occurred! ",error)