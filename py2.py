#get mouse cordinates. Code runs after 2sec delay
from _typeshed import OpenTextMode
from tkinter import Message
import pyautogui
import time
import keyboard

Message = input("Type here: ")
time.sleep(2)
print(pyautogui.position())
#pyautogui.displayMousePosition()

pyautogui.moveTo(559, 1426, 3, pyautogui.easeInQuad)
pyautogui.click(x=559,y=1426, button=pyautogui.leftClick, clicks=1)


#should be cmd for Ctrl+c (check sytax)
pyautogui.keyDown("ctrl")
pyautogui.press("c")
pyautogui.keyUp("ctrl")


