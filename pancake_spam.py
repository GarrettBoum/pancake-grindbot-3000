import keyboard
import time 
import random
from pynput.keyboard import Key, Controller
import pyautogui

time.sleep(3)
keyboard = Controller()
keyboard.type("grindbot V2.5.5 online")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
while True:
    i = random.randint(1,3)
    
    keyboard.type("p!work")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(3)
    f=0
    sell= pyautogui.pixelMatchesColor(502,900,(64,185,124), tolerance=5)
    if i == 1:
        keyboard.type("p!deposit all")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(0.5)
       ## pyautogui.leftClick
    while f<=4:
        keyboard.type("p!fish")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        keyboard.type("p!buy fishing rod")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(0.5)
        sell= pyautogui.pixelMatchesColor(502,900,(64,185,124), tolerance=5)
        if sell== True:
            pyautogui.leftClick(502,900)
        
        time.sleep(62)
        f=f+1
        if sell == True:
            pyautogui.leftClick(502,900)
            sell= pyautogui.pixelMatchesColor(502,900,(64,185,124), tolerance=5)
    f=0
    keyboard.type("p!sell all")
    if sell == True:
        pyautogui.leftClick(502,900)
    
    time.sleep(60)