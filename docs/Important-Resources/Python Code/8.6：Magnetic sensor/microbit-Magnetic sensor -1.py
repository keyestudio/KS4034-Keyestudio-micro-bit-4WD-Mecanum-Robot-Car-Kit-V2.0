from microbit import *

compass.calibrate()

while True:

    if button_a.is_pressed():
        display.scroll(compass.heading())


