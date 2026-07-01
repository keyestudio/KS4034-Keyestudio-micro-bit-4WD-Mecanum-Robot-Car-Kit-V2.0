### Project 1：Heart Beat

![](./media/Python_b855274f.png)

1\.  **Description**

This project is easy to conduct solely with a micro:bit main board and  icro USB cable. This experiment serves as a starter for your to entr o the magical programming world of the micro:bit.

2\.  **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the offline version of Mu.

3\.  **Test Code**

Open the Mu software, tap“Load”, select““microbit-Heartbeat\.py“ file and click“open”:

![](./media/Python_1ec17d44.png)

![](./media/Python_4bda2b61.png)

There is another way to import code. Open the Mu software and drag file”microbit-Heartbeat\.py”into it.

![](./media/Python_c5b7322b.png)

You can also input code in the edit window yourself.

(**Note: All English words and symbols must be written in English.**)

![](./media/Python_80af4cb3.png)

```python
from microbit import *

while True:
    display.show(Image.HEART)
    sleep(500)
    display.show(Image.HEART_SMALL)
    sleep(500)
```
The following are a list of built-in images:

• Image.HEART

• Image.HEART_SMALL

• Image.HAPPY

• Image.SMILE

• Image.SAD

• Image.CONFUSED

• Image.ANGRY

• Image.ASLEEP

• Image.SURPRISED

• Image.SILLY

• Image.FABULOUS

• Image.MEH

• Image.YES

• Image\.NO

• Image.CLOCK12, Image.CLOCK11, Image.CLOCK10, Image.CLOCK9 mage.CLOCK8, Image.CLOCK7, Image.CLOCK6, Image.CLOCK5,

Image.CLOCK4, Image.CLOCK3, Image.CLOCK2,Image.CLOCK1

• Image.ARROW_N, Image.ARROW_NE, Image.ARROW_E, Image.ARROW_SE mage.ARROW_S, Image.ARROW_SW, Image.ARROW_W, Image.ARROW_NW

• Image.TRIANGLE

• Image.TRIANGLE_LEFT

• Image.CHESSBOARD

• Image.DIAMOND

• Image.DIAMOND_SMALL

• Image.SQUARE

• Image.SQUARE_SMALL

• Image.RABBIT

• Image.COW

• Image.MUSIC_CROTCHET

• Image.MUSIC_QUAVER

• Image.MUSIC_QUAVERS

• Image.PITCHFORK

• Image.PACMAN

• Image.TARGET

• Image.TSHIRT

• Image.ROLLERSKATE

• Image.DUCK

• Image.HOUSE

• Image.TORTOISE

• Image.BUTTERFLY

• Image.STICKFIGURE

• Image.GHOST

• Image.SWORD

• Image.GIRAFFE

• Image.SKULL

• Image.UMBRELLA

• Image.SNAKE，Image.ALL_CLOCKS，Image.ALL_ARROWS

Connect the micro:bit board to computer via an USB cable, click“Flash”to  download code to the board.

![](./media/Python_93e18731.png)


![](./media/Python_48e78948.png)


![](./media/Python_cc33f1a9.png)

The code, even it is wrong, can be downloaded to the micro:bit board successfully, but can not work on micro:bit board.

Click“Flash”to download code to micro:bit. 

![](./media/Python_8982d0b0.png)

Click“REPL”and press the reset button on micro:bit, the error information will be displayed on the REPL window, as shown below: 

![](./media/Python_0c2abf18.png)

Click“REPL”again to turn off the REPL mode, then you could refresh new code. 

To make sure the correct code, you only need to tap“Check”. The errors will be shown on the window.

![](./media/Python_b994c0d3.png)

Modify the code according to the prompt and click“Check”.

![](./media/Python_bc5cbed3.png)

 Please log in the website for more tutorials：[https://codewith.mu/en/tutorials/](https://codewith.mu/en/tutorials/)

4\.  **Test Result**

Click “<span style="color: rgb(255, 76, 65);">**Flash**</span>” to load the code to the micro:bit board.

![Img](./media/Python_ed83ac25.png)

After downloading the code to the board successfully, **power on via micro USB cable or external power supply(turn the DIP switch to ON)**, and press the reset button on the board.

![Img](./media/Python_bb3e1312.png)

The LED dot matrix shows the pattern “❤”and then “![](./media/Python_04fdfc90.png)”alternatively.

5\.  **Code Explanation**

|from microbit import*|Import the library file of micro：bit|
|-|-|
|while True:|This is a permanent loop that makes micro:bit execute the code i his loop forever.|
|display.show(Image.HEART)|micro：bit shows “❤”|
|sleep(500)|Delay in 500ms|
|display.show(Image.HEART_SMALL)|The LED dot matrix displays“![](./media/Python_04fdfc90.png)”|
