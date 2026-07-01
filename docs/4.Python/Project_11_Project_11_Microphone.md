### Project 11: Microphone

![](./media/Python_3073a8af.png)

![](./media/Python_7f074115.png)

1\.  **Description**

The Micro: Bit main board has a built-in microphone, which can test the volume of ambient environment. When you clap, the microphone LED indicator turns on. Furthermore, it can measure the intensity of sound, thereby you can make a noise scale or disco lighting changing with music. 

The microphone is placed on the opposite side of the microphone LED indicator and in proximity with holes that lets sound pass. When the board detects the sound, the LED indicator lights up.

2\.  **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the offline version of Mu.

3\.  **Test Code1**

Enter Mu software and open the file“Microphone-1\.py”to import the code. You can also input code in the editing window yourself.

(**Note: All words and symbols must be written in English**.)

![](./media/Python_19b38832.png)

```python
from microbit import *

while True:
    if microphone.current_event() == SoundEvent.LOUD:
        display.show(Image.HEART)
        sleep(200)
    if microphone.current_event() == SoundEvent.QUIET:
        display.show(Image.HEART_SMALL)
```

Click“Check”to examine errors in the code. The program proves wrong if underlines and cursors are shown. 

![](./media/Python_36a669c7.png)

If the code is correct, connect the micro:bit to your computer and click“Flash”to download code to the micro:bit board.

![](./media/Python_0515bf32.png)

4\.  **Test Result1**

After downloading the code to the board successfully, **power on via micro USB cable or external power supply(turn the DIP switch to ON)**,and press the reset button on micro:bit.

![Img](./media/Python_bb3e1312.png)

The LED dot matrix displays the pattern “❤”when you clap and the pattern ![](./media/04fdfc9060943954e7938bb1a741d626.png) when it is quiet around.

5\.  **Test Code2**

Enter Mu software and open the file“Microphone-2\.py”to import the code. You can also input code in the editing window yourself.

(**Note: All words and symbols must be written in English.**)

![](./media/Python_f0e5a346.png)

```python
from microbit import *
maxSound = 0
lights = Image("11111:"
              "11111:"
              "11111:"
              "11111:"
              "11111")
# ignore first sound level reading
soundLevel = microphone.sound_level()
sleep(200)

while True:
    if button_a.is_pressed():
        display.scroll(maxSound)
    else:
        soundLevel = microphone.sound_level()
        display.show(lights * soundLevel)
        if soundLevel > maxSound:
            maxSound = soundLevel
```

Click“Check”to examine errors in the code. The program proves wrong if underlines and cursors are shown. 

![](./media/Python_d0c79871.png)

If the code is correct, connect the micro:bit to your computer and click“Flash”to download code to the micro:bit board.

![](./media/Python_d828b9ee.png)

6\.  **Test Result2**

After downloading the code to the board successfully, **power on via micro USB cable or external power supply(turn the DIP switch to ON)**,and press the reset button on micro:bit.

![Img](./media/Python_bb3e1312.png)

 When the button A is pressed, the LED dot matrix displays the value of the biggest volume( **please note that the biggest volume can be reset via the Reset button on the other side of the board** ). When clapping, the louder the tested sound, the brighter the 25 LEDs on the LED dot matrix screen.

7\.  **Code Explanation**

![Img](./media/Python_980f62b3.png)
