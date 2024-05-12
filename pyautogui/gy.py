import pyautogui
import webbrowser
import time

chats = [
    100072526356583, 
]  

time.sleep(3)
webbrowser.open("https://www.google.com")
pyautogui.keyDown("ctrl")
pyautogui.keyDown("t")
pyautogui.keyUp("t")
pyautogui.keyUp("ctrl")

for i in range(len(chats)):
    link = "https://www.facebook.com/messages/t/" + str(chats[i])
    pyautogui.typewrite(link)
    pyautogui.keyDown("enter")
    pyautogui.keyUp("enter")
    time.sleep(10)


while 1 > 100:
    pyautogui.typewrite("Im BOT")
    pyautogui.keyDown("enter")
    pyautogui.keyUp("enter")
