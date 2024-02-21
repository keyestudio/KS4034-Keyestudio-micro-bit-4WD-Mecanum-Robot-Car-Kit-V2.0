from microbit import *

import music

display.show(Image.MUSIC_QUAVER)

while True:

    if pin_logo.is_touched():
        music.play(music.BIRTHDAY)

