### Project 9：Speaker

![](./media/Python_ac515b9a.png)

1\.  **Description**

Micro: Bit main board has an built-in speaker, which makes adding sound to the programs easier. It can also be programmed to produce all kinds of tones, like playing the song *Ode to Joy.*

2\.  **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the offline version of Mu.

3\.  **Test Code**

Enter Mu software and open the file“Speaker\.py”to import code. You can also input code in the editing window yourself.

(**Note: All words and symbols must be written in English**.)

![](./media/Python_eec7f643.png)

```python
from microbit import *

import audio

display.show(Image.MUSIC_QUAVER)

while True:
    audio.play(Sound.GIGGLE)
    sleep(1000)
    audio.play(Sound.HAPPY)
    sleep(1000)
    audio.play(Sound.HELLO)
    sleep(1000)
    audio.play(Sound.YAWN)
    sleep(1000)
```

Click“Check”to examine errors in the code. The program proves wrong if underlines and cursors are shown. 

![](./media/Python_f8852abf.png)

If the code is correct, connect the micro:bit to your computer and click“Flash”to download the code to the micro:bit board.

![](./media/Python_3fd94e43.png)

4\.  **Test Result**

After downloading the code to the board successfully, **power on via micro USB cable or external power supply(turn the DIP switch to ON)**,and press the reset button on micro:bit.

![Img](./media/Python_bb3e1312.png)

 The speaker utters sound and the LED dot matrix shows the logo of music.

5\.  **Code Explanation**

![Img](./media/Python_18c047bd.png)
