from pynput.mouse import Button, Controller
import time

mouse = Controller()

i = 0
while i < 1000:
    mouse.press(Button.left)
    time.sleep(0.01)
    mouse.release(Button.left)
    time.sleep(0.01)
    i += 1
