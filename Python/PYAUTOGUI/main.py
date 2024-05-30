import pyautogui
import webbrowser
import time

chats = [
    100077685018016,   # dati
]  

time.sleep(3)

webbrowser.open("https://www.google.com")

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

pyautogui.typewrite("Im Gela")

pyautogui.keyDown("enter")
pyautogui.keyUp("enter")
