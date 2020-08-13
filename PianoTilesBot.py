from pyautogui import *
import pyautogui
import time
import win32api, win32con

#X position for each of 4 tiles on the screen
x1 = 580
x2 = 680
x3 = 780
x4 = 880

#Y value for the tiles
y = 455

#Y value offest
yoffset = 10

#Red color value of the tile.
#Since tiles in the game are black it's enough to check just the red value (which is zero).
#You can change it if your tiles are a different color.
red = 0

#Click delay
delay = 0.05

#Click finction
def click(x,y):
    win32api.SetCursorPos((x,y)) #Move the mouse to the tile
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) #Click button down
    time.sleep(delay) #For some games it is needed to have a click delay or the click won't register.
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0) #Click button up

while True:

    if pyautogui.pixel(x1, y) [0] == red: #if the pixel on the tile is black click it
        click(x1, y + yoffset)

    if pyautogui.pixel(x2, y) [0] == red:
        click(x2, y + yoffset)

    if pyautogui.pixel(x3, y) [0] == red:
        click(x3, y + yoffset)

    if pyautogui.pixel(x4, y) [0] == red:
        click(x4, y + yoffset)
