import pyautogui
import time

def koordinatAl():
    time.sleep(2)
    x,y = pyautogui.position()
    print(f"Koordinat: ({x}, {y})")
    return x,y

ekranx,ekrany = koordinatAl()

print(ekranx,ekrany)

