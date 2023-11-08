'''
Author: Sai Vignesh Golla
LinkedIn: https://www.linkedin.com/in/saivigneshgolla
Version: 1.0.0
'''

############# Config #############

# Total time the program needs to run in seconds
total_time =  8 * 60 * 60 

# Time between each press in seconds
intervals =  30

# How many seconds would you like to extend time when asked?
extend_time =  30 * 60

##################################



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
        if pyautogui.confirm("Extend time by {} secs?".format(extend_time), buttons=['Yes','No']) == "Yes": countdown("Extended time.\nWhen done press 'Ctrl + C' or close this window to exit.", extend_time)
    except KeyboardInterrupt:
        print("Script terminated by the user")

if __name__ == "__main__":
    try:    countdown("Program started. Will run for {} secs.\nFeel free to minimize the screen and carry on with your work.\nWhen done press 'Ctrl + C' or close this window to exit.".format(total_time), total_time)
    except Exception as error:  print("Error Occurred! ",error)
