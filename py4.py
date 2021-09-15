import os
import pyautogui
import time
import keyboard


# def rightClick(x, y):
#     pyautogui.moveTo(x, y, 0.5)
#     pyautogui.click(x=x, y=y, button="right")
# rightClick(432, 150) 

#locate cat pic
while keyboard.is_pressed('q') == False:
    if pyautogui.locateOnScreen('cat.png') != None:
        print('we can see the picture')
        time.sleep(0.5)
    else:
        print("we can't see the picture")    
        time.sleep(0.5)

#center coordinate of cat pic
cor = pyautogui.locateOnScreen('cat.png')        
print(cor)
corPoint = pyautogui.center(cor)
print(corPoint)

#right click cat pic
pyautogui.click('cat.png', button="right")