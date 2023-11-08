'''
Author: Sai Vignesh Golla
LinkedIn: https://www.linkedin.com/in/saivigneshgolla
Version: 1.0.0
'''

########################### Config ###########################

# Total time the program needs to run in seconds
total_time =    8*60*60 + 30*60 + 0

# Time between each press in seconds
intervals =     30

# How many seconds would you like to extend time when asked?
extend_time =   1*60*60

##############################################################


import pyautogui
pyautogui.FAILSAFE = False

def countdown(message, timeLeft):
    try:
        print(message)
        while timeLeft > 0:
            # pyautogui.move(+1, 0)
            # pyautogui.move(-1, 0)
            pyautogui.press('altleft')  # Or replace with 'shiftleft' if you want to use Left Shift key instead of Left Alt key.
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