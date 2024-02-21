from microbit import *

while True:

    Lightintensity = display.read_light_level()

    print("Light intensity:", Lightintensity)

    sleep(100)
