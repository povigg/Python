import pyautogui
import time
import keyboard

# while Keyboard.is_pressed('q') == False:
#     time.sleep(0.5)
#     print("hello")

    #break when statement is reached (3 times hello in this case)

    for i in range(0, 5, 1):
        if i == 3:
            break
        print("hello")
    print("loop ended")      

#another way to move mouse and click instead of pyautogui
    win32api.SetCursorPos((100, 100))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# [0] = R, [1] = G, [2] = B
if pyautogui.pixel(664, 133) [0] == 28:
    print(' we are on vsc window ')