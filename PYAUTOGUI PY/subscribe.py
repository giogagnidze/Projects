import pyautogui
import pyautogui as pag
import webbrowser
import time

webbrowser.open("https://www.google.com")

pyautogui.keyDown("ctrl")
pyautogui.keyDown("t")
pyautogui.keyUp("t")
pyautogui.keyUp("ctrl")


link = "https://www.youtube.com/results?search_query=goal+oriented+academy"
pyautogui.typewrite(link)
pyautogui.keyDown("enter")
pyautogui.keyUp("enter")
time.sleep(10)
pag.moveTo(1700, 310)
pyautogui.click(button='left')