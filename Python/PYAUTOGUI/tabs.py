import pyautogui
import webbrowser
import time


time.sleep(3)


webbrowser.open("https://www.google.com")

while 1 > 100:
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("t")
    pyautogui.keyUp("t")
    pyautogui.keyUp("ctrl")
