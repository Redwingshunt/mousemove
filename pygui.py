import pyautogui as pg
import random as rd
import time
while True :

    x = rd.randint(800, 1500)
    y = rd.randint(400, 800)
    pg.moveTo(x,y,0.4)
    time.sleep(2)


