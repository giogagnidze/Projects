import pyautogui
import pyautogui as pag
import webbrowser
import time

time.sleep(3)


webbrowser.open("https://clickspeedtest.com/")


time.sleep(5)

pag.moveTo(700, 620)

time.sleep(2)

while 1 < 100:
    pyautogui.leftClick()