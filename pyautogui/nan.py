import pyautogui
import time

chats = [
    100072943683131,
]  

time.sleep(3)
pyautogui.keyDown("alt")
pyautogui.keyDown("tab")
pyautogui.keyUp("tab")
pyautogui.keyUp("alt")


pyautogui.keyDown("ctrl")
pyautogui.keyDown("t")
pyautogui.keyUp("t")
pyautogui.keyUp("ctrl")

for i in range(len(chats)):
    link = "https://www.messenger.com/t/" + str(chats[i])
    pyautogui.typewrite(link)
    pyautogui.keyDown("enter")
    pyautogui.keyUp("enter")
    time.sleep(10)

pyautogui.typewrite("im Bot")

pyautogui.keyDown("enter")
pyautogui.keyUp("enter")
