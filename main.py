import pyautogui
pyautogui.FAILSAFE = False

def movements():
    try:
        while True:    
            # pyautogui.move(+1, 0)
            # pyautogui.move(-1, 0)
            pyautogui.press('shiftleft')
            pyautogui.sleep(30)
    except KeyboardInterrupt:
        print("Script terminated by the user")

if __name__ == "__main__":
    try:
        movements()
    except Exception as error:
        print("Error Occurred! ",error)
