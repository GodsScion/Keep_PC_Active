'''
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla
Version:    1.1.0
'''

import pyautogui
pyautogui.FAILSAFE = False
from config import *

def actions():
    pyautogui.press('shiftright')
    # pyautogui.move(+1, 0)
    # pyautogui.move(-1, 0)

def convertTime(secs):
    h = int(secs/3600)
    return (h, int(secs/60 - h*60), secs%60)

def printTimeLeft(timeLeft):
    h, m, s = convertTime(timeLeft)
    print("Time Left: {} hr {} min".format(h,m), end="\r") if h > 0 or m > 0 else print("Less than a minute left...", end="\r")

def countdown(timeLeft):
    while timeLeft > 0:
        currentInterval = intervals
        actions()
        while currentInterval >= 60:
            printTimeLeft(timeLeft)
            pyautogui.sleep(60)
            currentInterval -= 60
        pyautogui.sleep(min(currentInterval, timeLeft))
        timeLeft -= currentInterval
        printTimeLeft(timeLeft)
    h, m, s = convertTime(extend_time)
    if pyautogui.confirm("Extend time by  {} hr {} min {} sec?".format(h, m, s), buttons=['Yes','No']) == "Yes":
        print("Extended time by  {} hr {} min {} sec.\nWhen done press 'Ctrl + C' or close this window to exit.\n...".format(h, m, s))
        countdown(extend_time)

if __name__ == "__main__":
    try:
        h, m, s = convertTime(total_time)
        print("Program started. Will run for  {} hr {} min {} sec.\nFeel free to minimize the screen and carry on with your work.\nWhen done press 'Ctrl + C' or close this window to exit.\n...".format(h, m, s))
        countdown(total_time)
    except KeyboardInterrupt:
        print("Script terminated by the user")
    except Exception as error:
        print("Error Occurred! ",error)