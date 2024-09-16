import pyautogui
from PIL import ImageGrab
import time

def get_mouse_color():
    time.sleep(2)
    x, y = pyautogui.position()
    screen = ImageGrab.grab(bbox=(x, y, x+1, y+1))
    
    color = screen.getpixel((0, 0))
    
    return color

def rgb_to_percentage(rgb_color):
    return tuple(round(value / 255, 3) for value in rgb_color)

color_at_mouse = get_mouse_color()

color_percentage = rgb_to_percentage(color_at_mouse)

print(f"RGB Color at mouse: {color_at_mouse} ")
print(f"RGB Color in percentage (decimal): {color_percentage }")