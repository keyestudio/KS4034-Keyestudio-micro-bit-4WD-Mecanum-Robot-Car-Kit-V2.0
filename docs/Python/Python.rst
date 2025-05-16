Python Tutorial
===============

|image1|

Getting started with Python
---------------------------

This tutorial is written for Python language. If you want to use
graphical code programming, please refer to the manual "Makecode
Tutorial". In the root directory of the resource you downloaded, there
is a folder named "Python tutorial", which stores all the Python code of
the Micro:bit 4WD Mecanum Robot Car V2.0. The Python code file is a file
ending with ".py".

What is MicroPython?
~~~~~~~~~~~~~~~~~~~~

Python is a text-based language, which is widely used in education and
is also used by professional programmers in fields such as data science
and machine learning.

Micro: bit can be programmed in Python, which is a microcontroller, and
the hardware differences prevent micro: bit from fully supporting
Python. The MicroPython is dedicated to micro：bit，which is an
efficient implementation of the Python3 programming language. It
contains a small portion of the Python standard library and is optimized
to run on micro: bit microcontrollers.

The version of Python used by BBC micro: bit is called MicroPython. The
MicroPython is perfect for those who want to learn more about
programming, which helps you program with a series of code snippets, a
variety of pre-made graphics and music.

Link for BBC microbit MicroPyth：\ `BBC micro:bit
MicroPython <https://microbit-micropython.readthedocs.io/en/latest/tutorials/introduction.html>`__

**Python has two types of editors: web version and offline version**

1. Web version: https://python.microbit.org/v/1.1

|image2|

2. The other one is the offline compiler too-----Mu |image3|

Official Website of Mu：\ https://codewith.mu/

Mu
~~

Mu, a Python code editor, is suitable for starters. It doesn’t support
32-bit Windows.

1. **Download Mu**

Click“This PC”and right- click to select Properties to check the versio
f your computer.

|image4|

Check the system type of your computer.

|image5|

Enter the link of MU: https://codewith.mu/en/download to download the
corresponding version of Mu.

|image6|

2. **Run Setup**

Open the file below

|image7|

Mac OSX：\ https://codewith.mu/en/howto/1.1/install_macos.

Linux：\ https://codewith.mu/en/howto/1.2/install_linux.

**Windows 10**

You will view the page pop-up, then click “More info”.

|image8|

Then click“Run anyway”.

|image9|

3. License Agreement

Click “Install”.

|image10|

|image11|

After installed , click “finish”.

|image12|

4. Start Mu

Next, find it according to the following picture

|image13|

Its main interface is shown as below:

|image14|

.. _using-modes--menu-bar:

Using Modes & Menu Bar
~~~~~~~~~~~~~~~~~~~~~~

Set “Mode” to BBC micro:bit .

On the menu, click “\ **Mode**\ ” to set it to “\ **BBC micro：bit**\ ”.
The micro:bit mode understands how to interact with and connect to a
micro:bit.

|image15|

Click to `Start with Mu <https://codewith.mu/en/tutorials/1.1/start>`__.

For more tutorials on using Mu, please visit:
https://codewith.mu/en/tutorials/

How Mu Import Library to Micro:bit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

\ **Before importing libraries, we need to upload a .py code (empty code
is also ok) to the micro:bit board. Here we take an empty code as an
example.**\ 

Connect the board to computer via USB cable. Open the Mu and click
“Flash” to upload the .py code (empty code) to the board.

|Img|

In this tutorial, "keyes_mecanum_Car_V2.py" library file are used.
Therefore, import the "keyes_mecanum_Car_V2.py" library file into the
micro:bit. This file contains the control method of the Micro:bit 4WD
Mecanum Robot Car V2.0.

The default directory for Mu to save files is “mu_code”in the root
directory of the user’s directory.

References link: https://codewith.mu/en/tutorials/1.0/files

**the Methods of finding the "mu_code" folder:**

**Method One:**

For example, on the windows system, suppose your system is installed on
the C driver of the computer, and the user name is "**Administrator**",
then the path of the "**mu_code**" directory is
"**C:\\Users\\Administrator\\mu\_ code**". On Linux systems, the path of
the "**mu_code**" directory is "**~/home/mu_code**".

Open the “\ **mu_code**\ ”folder.

|image16|

**Method Two:**

Search for the “mu_code” folder on the Disk(C:).

|image17|

|image18|

Open “mu_code”.

|image19|

The path of the data folder where the “keyes_mecanum_Car.py”library file
we provide are located is as follows:

|image20|

Copy“keyes_mecanum_Car.py”library file to the folder“mu_code”。When the
copy is done, as shown below:

|image21|

First open the Mu software and connect the micro:bit to your computer
then click the "Files" button, and drag the "keyes_mecanum_Car.py"
library file to the micro:bit.

|image22|

After a few seconds, the import is complete and you can see it in the
box on the left.

|image23|

Projects
--------

**Note:** project 1 to 12 will be conducted with the built-in sensors an
LED dot matrix of the Micro:bit mainboard V2

Project 1：Heart Beat
~~~~~~~~~~~~~~~~~~~~~

|image24|

1. **Description**

This project is easy to conduct solely with a micro:bit main board and
icro USB cable. This experiment serves as a starter for your to entr o
the magical programming world of the micro:bit.

2. **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the offline version of Mu.

3. **Test Code**

Open the Mu software, tap“Load”, select““microbit-Heartbeat.py“ file and
click“open”:

|image25|

|image26|

There is another way to import code. Open the Mu software and drag
file”microbit-Heartbeat.py”into it.

|image27|

You can also input code in the edit window yourself.

(**Note: All English words and symbols must be written in English.**)

|image28|

.. code:: python

   from microbit import *

   while True:
       display.show(Image.HEART)
       sleep(500)
       display.show(Image.HEART_SMALL)
       sleep(500)

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

• Image.NO

• Image.CLOCK12, Image.CLOCK11, Image.CLOCK10, Image.CLOCK9 mage.CLOCK8,
Image.CLOCK7, Image.CLOCK6, Image.CLOCK5,

Image.CLOCK4, Image.CLOCK3, Image.CLOCK2,Image.CLOCK1

• Image.ARROW_N, Image.ARROW_NE, Image.ARROW_E, Image.ARROW_SE
mage.ARROW_S, Image.ARROW_SW, Image.ARROW_W, Image.ARROW_NW

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

Connect the micro:bit board to computer via an USB cable, click“Flash”to
download code to the board.

|image29|

|image30|

|image31|

The code, even it is wrong, can be downloaded to the micro:bit board
successfully, but can not work on micro:bit board.

Click“Flash”to download code to micro:bit.

|image32|

Click“REPL”and press the reset button on micro:bit, the error
information will be displayed on the REPL window, as shown below:

|image33|

Click“REPL”again to turn off the REPL mode, then you could refresh new
code.

To make sure the correct code, you only need to tap“Check”. The errors
will be shown on the window.

|image34|

Modify the code according to the prompt and click“Check”.

|image35|

Please log in the website for more
tutorials：\ https://codewith.mu/en/tutorials/

4. **Test Result**

Click “\ **Flash**\ ” to load the code to the micro:bit board.

|image36|

After downloading the code to the board successfully, **power on via
micro USB cable or external power supply(turn the DIP switch to ON)**,
and press the reset button on the board.

|image37|

The LED dot matrix shows the pattern “❤”and then
“\ |image38|\ ”alternatively.

5. **Code Explanation**

+---------------------------------+-----------------------------------+
| from microbit import\*          | Import the library file of        |
|                                 | micro：bit                        |
+=================================+===================================+
| while True:                     | This is a permanent loop that     |
|                                 | makes micro:bit execute the code  |
|                                 | i his loop forever.               |
+---------------------------------+-----------------------------------+
| display.show(Image.HEART)       | micro：bit shows “❤”              |
+---------------------------------+-----------------------------------+
| sleep(500)                      | Delay in 500ms                    |
+---------------------------------+-----------------------------------+
| display.show(Image.HEART_SMALL) | The LED dot matrix                |
|                                 | displays“\ |image41|\ ”           |
+---------------------------------+-----------------------------------+

Project 2：Light A Single LED
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image42|

1. **Description**

The LED dot matrix consists of 25 Diodes arranged in a 5 by 5 square and
placed at the intersection of row lines (X) and column lines (Y). We can
control one of the 25 LEDs by setting coordinate points. For example,
the first LED sits in the first line is (0,0）and the third LED
positioned in the first line is (2,0）and others likewise.

|image43|

2. **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the offline version of Mu.

3. **Test Code**

Enter the Mu software and open the“Single LED display.py.”file to import
code.You can also input code in the editing window yourself.

(**Note: All English words and symbols must be written in English**)

|image44|

.. code:: python

   from microbit import *

   val1 = Image("09000:""00000:""00000:""00000:""00000:")
   val2 = Image("00000:""00000:""00000:""00000:""00090:")
   val3 = Image("00000:""00000:""00000:""00000:""00000:")

   while True:
       display.show(val1)
       sleep(500)
       display.show(val3)
       sleep(500)
       display.show(val2)
       sleep(500)
       display.show(val3)
       sleep(500)

Click“Check”to examine error in the code. The program proves wrong if
underlines and cursors are shown.

|image45|

If the code is correct, connect the micro:bit to your computer and
click“Flash”to download code to micro:bit board.

|image46|

4. **Test Result**

After downloading the code to the board successfully, **power on via
micro USB cable or external power supply(turn the DIP switch to ON)**,
and press the reset button on the board.

|image47|

The LED in (1,0) will be on and off for 0.5s and the one in (3,4) will
be on and off for 0.5s and repeat this sequence.

5. **Code Explanation**

|image48|

6. **Reference**

sleep(ms) : delay time

For more details about delay, please refer to the link:
https://microbit-micropython.readthedocs.io/en/latest/utime.html

Project 3：5*5 LED Dot Matrix
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image49|

1. **Description**

Dot matrix is very commonplace in daily life, which has found wide
applications in LED advertisement screens, elevator floor display, bus
stop announcement and so on. The LED dot matrix of Micro: Bit main board
contains 25 Diodes. Previously, we have succeeded in controlling a
certain LED via its position point. Supported by the same theory, we can
turn on many LEDs at the same time to showcase patterns, digits and
characters.

What’s more, we can also click”show icon“ to choose the pattern we like
to display. Last but not the least, we can design patterns by ourselves
as well.

2. **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the offline version of Mu.

3. **Test Code1**

You could open“5×5 LED Dot Matrix-1.py”file to import the code. You can
also input code in the editing window yourself.

(**Note: All words and symbols must be written in English.**)

|image50|

.. code:: python

   from microbit import *

   val = Image("00900:""00900:""90909:""09990:""00900")

   display.show(val)

Click“Check”to examine the error in the code. The program proves wrong
if underlines and cursors are shown.

|image51|

If the code is correct, connect micro:bit to computer and click“Flash”to
download code to micro:bit board.

|image52|

4. **Test Result1**

After downloading the code to the board successfully, **power on via
micro USB cable or external power supply(turn the DIP switch to ON)**,
and press the reset button on the board.

|image53|

We will find that the 5*5 dot matrix start to show a downward arrow
|image54|.

5. **Test Code2**

You could open “5×5 LED Dot Matrix-2.py“ file to import the code. You
can also input code in the editing window yourself.

(**Note: All words and symbols must be written in English.**)

|image55|

.. code:: python

   from microbit import *
   val = Image("00900:""00900:""90909:""09990:""00900")
   display.show('1')
   sleep(500)
   display.show('2')
   sleep(500)
   display.show('3')
   sleep(500)
   display.show('4')
   sleep(500)
   display.show('5')
   sleep(500)
   display.show(val)
   sleep(500)
   display.scroll("hello!")
   sleep(200)
   display.show(Image.HEART)
   sleep(500)
   display.show(Image.ARROW_NE)
   sleep(500)
   display.show(Image.ARROW_SE)
   sleep(500)
   display.show(Image.ARROW_SW)
   sleep(500)
   display.show(Image.ARROW_NW)
   sleep(500)
   display.clear()

Click“Check”to examine errors in the code. The program proves wrong if
underlines and cursors are shown.

|image56|

If the code is correct, connect the micro:bit to the computer and
click“Flash”to download code to micro:bit board.

|image57|

6. **Test Result2**

After downloading the code to the board successfully, **power on via
micro USB cable or external power supply(turn the DIP switch to ON)**,
and press the reset button on the board.

|image58|

We will find that the 5*5 dot matrix start to show numbers 1,2,3,4 and 5
and then it alternatively shows a downward arrow
word\ |image59|,“Hello”, a heart pattern |image60|, a rrow pointing at
northeast |image61|, then at southeast |image62| then at southwest
|image63| and then at northwest |image64|.

7. **Code Explanation**

|image65|

6. **Reference**

display.scroll() ：

The display scrolls to show the values, if it is integer or float, w ill
use str（）to transfer it into character strings.

More details, please refer to th
ink：\ https://microbit-micropython.readthedocs.io/en/latest/utime.html

Project 4：Programmable Buttons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image66|

1. **Description**

|image67|

Buttons can be used to control circuits. In an integrated circuit with a
push button, the circuit is connected when pressing the button and but
after release, it will break again. 

Both ends of the button like two mountains. There is a river in between.
The internal metal piece connect the two sides to let the current pass,
just like building a bridge to connect two mountains.

The internal structure of the button is shown as follows: before
pressing the button, 1 ,2 , 3 and 4 are turned on. However, 1, 3 or 1, 4
or 2, 3 or 2 and 4 are disconnected, which is only enabled when the
button is pressed. |image68|

Micro: Bit main board boasts three push buttons, two are programmable
buttons(marked with A and B), and the one on the other side is a reset
button. By pressing the two programmable buttons can input three
different signals. We can press button A or B alone or press them
together and the LED dot matrix shows A,B and AB respectively. Let’s get
started.

2. **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the offline version of Mu.

3. **Test Code1**

Enter Mu software and open the file“Programmable Buttons-1.py”to import
the code. You can also input code in the editing window yourself.

(**Note: All words and symbols must be written in English.**)

|image69|

.. code:: python

   from microbit import *

   while True:
       if button_a.is_pressed():
           display.show("A")
       elif button_a.is_pressed() and button_b.is_pressed():
           display.scroll("AB")
       elif button_b.is_pressed():
           display.show("B")

Click“Check”to examine errors in the code. The program proves wrong if
underlines and cursors are shown.

|image70|

If the code is correct, connect the micro:bit to your computer and
click“Flash”to download the code to the micro:bit board.

|image71|

4. **Test Result1**

After downloading the code to the board successfully, **power on via
micro USB cable or external power supply(turn the DIP switch to ON)**,
and press the reset button on the board.

|image72|

The 5*5 LED dot matrix shows “A”if button A is pressed, then“B” if
button B is pressed, and “AB” if button A and B are pressed together.

5. **Test Code2**

Enter Mu software and open the file“Programmable Buttons-2.py”to import
the code. You can also input code in the editing window yourself.

(**Note: All words and symbols must be written in English.**)

|image73|

|image74|

.. code:: python

   from microbit import *
   a = 0
   b = 0
   val1 = Image("00000:""00000:""00000:""00000:""00900")
   val2 = Image("00000:""00000:""00000:""00900:""99999")
   val3 = Image("00000:""00000:""00900:""99999:""99999")
   val4 = Image("00000:""00900:""99999:""99999:""99999")
   val5 = Image("00900:""99999:""99999:""99999:""99999")
   val6 = Image("99999:""99999:""99999:""99999:""99999")
   display.show(val1)

   while True:
       while button_a.is_pressed() == True:
           sleep(10)
           if button_a.is_pressed() == False:
               a = a + 1
               if(a >= 5):
                   a = 5
               break
       while button_b.is_pressed() == True:
           sleep(10)
           if button_b.is_pressed() == False:
               a = a - 1
               if(a <= 0):
                   a = 0
               break
       if a == 0:
           display.show(val1)
       if a == 1:
           display.show(val2)
       if a == 2:
           display.show(val3)
       if a == 3:
           display.show(val4)
       if a == 4:
           display.show(val5)
       if a == 5:
           display.show(val6)

Click“Check”to examine errors in the code. The program proves wrong if
underlines and cursors are shown.

|image75|

|image76|

If the code is correct, connect the micro:bit to your computer and
click“Flash”to download the code to the micro:bit board.

|image77|

|image78|

6. **Test Result2**

After downloading the code to the board successfully, **power on via
micro USB cable or external power supply(turn the DIP switch to ON)**,
and press the reset button on the board.

|image79|

If the button A is pressed, the LEDs turning red increase while if the
button B pressed, the LEDs turning red reduce.

7. **Code Explanation**

|image80|

|image81|

Project 5：Temperature Detection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Description**

The Micro:bit main board is not equipped with a temperature sensor, but
uses the built-in temperature sensor in NFR52833 chip for temperature
detection. Therefore, the detected temperature is more closer to the
temperature of the chip, and there maybe deviation from the ambient
temperature.

In this project, we will seek to use the sensor to test the temperature
in the current environment, and display the test results in the display
data (device). And then control the LED dot matrix to display different
patterns by setting the temperature range detected by the sensor.

**Note: the temperature sensor of Micro:bit main board is shown below:**

|image82|

2. **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the offline version of Mu.

3. **Test Code1**

Enter Mu software and open the file“Temperature Measurement -1.py “ to
import code. You can also input code in the editing window yourself.

(**Note: All words and symbols must be written in English.**)

|image83|

.. code:: python

   from microbit import *

   while True:

       Temperature = temperature()

       print("Temperature:", Temperature, "C")

       sleep(500)

Click“Check”to examine error in the code. The program proves wrong if
underlines and cursors are shown.

|image84|

If the code is correct, connect micro:bit to computer and click“Flash”to
download code to micro:bit board.

|image85|

4. **Test Result1**

After downloading the code to the board successfully, **power on via
micro USB cable or external power supply(turn the DIP switch to ON)**.
Click“REPL”and press the reset button on micro:bit.

|image86|

Then REPL window will show the ambient temperature value, as shown
below: (C stands for temperature unit)

|image87|

5. **Test Code2**

Enter Mu software and open the file“Temperature Measurement -2.py “ to
import code. You can also input code in the editing window yourself.

(**Note: All words and symbols must be written in English.**)

The temperature value can be set in compliance with the rea emperature.

|image88|

.. code:: python

   from microbit import *

   while True:

       if temperature() >= 35:
           display.show(Image.HEART)

       else:
           display.show(Image.HEART_SMALL)

Click“Check”to examine error in the code. The program proves wrong if
underlines and cursors are shown.

|image89|

If the code is correct, connect the micro:bit to the computer and
click“Flash”to download the code to the micro:bit board.

|image90|

6. **Test Result2**

After downloading the code to the board successfully, **power on via
micro USB cable or external power supply(turn the DIP switch to ON)**,
and press the reset button on micro:bit.

|image91|

When the ambient temperature is less than 35℃, the 5*5 LED dot matrix
shows |image92|. When the temperature is equivalent to or greater than
35℃, the pattern |image93| appears.

7. **Code Explanation**

|image94|

Project 6：Geomagnetic Sensor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image95|

1. **Description**

This project mainly introduces the use of the micro:bit’s
geomagnetic sensor. In addition to detecting the strength of the
magnetic field, it can also be used to determine the direction, which is
an important part of the heading and attitude reference system (AHRS) as
well.

It uses FreescaleMAG3110 three-axis magnetometer. Its I2C interface
communicates with the outside, and the range is ±1000µT, the maximum
data update rate is 80Hz. Combined with an accelerometer, it can
calculate the position. Additionally, it is applied to magnetic
detection and compass blocks. Then we could read the value detected by
it to determine the location. We need to calibrate the micro:bit board
when the magnetic sensor works. The correct calibration method is to
rotate the micro:bit board.

In addition, the objects nearby may affect the accuracy of readings and
calibration.

2. **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the offline version of Mu.

3. **Test Code1**

Enter Mu software and open the file“Magnetic sensor -1.py“ to import
code. You can also input the code in the editing window yourself.

(**Note: All words and symbols must be written in English**.)

|image96|

.. code:: python

   from microbit import *

   compass.calibrate()

   while True:

       if button_a.is_pressed():
           display.scroll(compass.heading())

Click“Check”to examine errors in the code. The program proves wrong if
underlines and cursors are shown.

|image97|

If the code is correct, connect micro:bit to the computer and
click“Flash”to download the code to the micro:bit board.

|image98|

4. **Test Result1**

After downloading the code to the board successfully, **power on via
micro USB cable or external power supply(turn the DIP switch to ON)**,
and press the reset button on micro:bit.

|image99|

The LED dot matrix shows “TILT TO FILL SCREEN”. Pressing the button A,
the board asks us to calibrate the compass. Then enter the calibration
page. Rotate the board until all 25 red LEDs are on, as shown below.

|image100|

After that, a smile pattern |image101| appears, which implies the
calibration is done. When the calibration process is completed, pressing
the button A will make the magnetometer reading display directly on the
screen. And the direction north, east, south and west correspond to 0°,
90°, 180° and 270° respectively.

5. **Test Code2**

For the below picture, the arrow will work to point to the upper right
when the value ranges from 292.5 to 337.5. Since 0.5 can’t be input in
the code, the values we get are 293 and 338.

Then add other statements to make a set of complete code.

|image102|

Enter Mu software and open the file“Magnetic sensor -2.py“ to import the
code. You can also input code in the editing window yourself.

(**Note: All words and symbols must be written in English.**)

|image103|

.. code:: python

   from microbit import *
   compass.calibrate()
   x = 0
   while True:
       x = compass.heading()
       if x >= 293 and x < 338:
           display.show(Image("00999:""00099:""00909:""09000:""90000"))
       elif x >= 23 and x < 68:
           display.show(Image("99900:""99000:""90900:""00090:""00009"))
       elif x >= 68 and x < 113:
           display.show(Image("00900:""09000:""99999:""09000:""00900"))
       elif x >= 113 and x < 158:
           display.show(Image("00009:""00090:""90900:""99000:""99900"))
       elif x >= 158 and x < 203:
           display.show(Image("00900:""00900:""90909:""09990:""00900"))
       elif x >= 203 and x < 248:
           display.show(Image("90000:""09000:""00909:""00099:""00999"))
       elif x >= 248 and x < 293:
           display.show(Image("00900:""00090:""99999:""00090:""00900"))
       else:
           display.show(Image("00900:""09990:""90909:""00900:""00900"))

Click“Check”to examine errors in the code. The program proves wrong if
underlines and cursors are shown.

|image104|

If the code is correct, connect the micro:bit to your computer and
click“Flash”to download the code to the micro:bit board.

|image105|

6. **Test Result**

After downloading the code to the board successfully, **power on via
micro USB cable or external power supply(turn the DIP switch to ON)**,
and press the reset button on micro:bit.

|image106|

After calibration, rotate the micro:bit board, then the LED dot matrix
displays the direction signs.

7. **Code Explanation**

|image107|

Project 7：Accelerometer
~~~~~~~~~~~~~~~~~~~~~~~~

|image108|

1. **Description**

The micro: bit main board V2 has a built-in LSM303AGR gravity
acceleration sensor, also known as accelerometer, with a resolution of
8/10/12 bits. The code section sets the range to 1g, 2g, 4g, and 8g.

We often use an accelerometer to detect the status of machines.

In this project, we will work to introduce how to measure the position
of the board with the accelerometer. And then have a look at the
original three-axis data output by the accelerometer.

2. **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the offline version of Mu.

3. **Test Code1**

Enter Mu software and open the file“Three-axis acceleration sensor
-1.py“ to import the code. You can also input the code in the editing
window yourself.

(**Note: All words and symbols must be written in English.**)

|image109|

.. code:: python

   from microbit import *

   while True:
       gesture = accelerometer.current_gesture()

       if gesture == "shake":
           display.show("1")
       if gesture == "up":
           display.show("2")
       if gesture == "down":
           display.show("3")
       if gesture == "face up":
           display.show("4")
       if gesture == "face down":
           display.show("5")
       if gesture == "left":
           display.show("6")
       if gesture == "right":
           display.show("7")
       if gesture == "freefall":
           display.show("8")

Click“Check”to examine errors in the code. The program proves wrong if
underlines and cursors are shown.

|image110|

If the code is correct, connect the micro:bit to your computer and
click“Flash”to download the code to the micro:bit board.

|image111|

4. **Test Result1**

After downloading the code to the board successfully, **power on via
micro USB cable or external power supply(turn the DIP switch to ON)**,
and press the reset button on micro:bit.

|image112|

When we shake the micro: bit main board，no matter at any direction, the
LED dot matrix displays the digit “1”.

When it is kept upright（make its logo above the LED dot matrix）, the
number 2 appears.

|image113|

When it is kept upside down( make its logo below the LED dot matrix) ,
it shows as below.

|image114|

When it is placed still on the desk, showing its front side, the number
4 appears.

|image115|

When it is placed still on the desk, showing its back side, the number 5
exhibits.

When the board is tilted to the left , the LED dot matrix shows the
number 6, as shown below:

|image116|

When the board is tilted to the right , the LED dot matrix displays the
number 7, as shown below：

|image117|

When the board is knocked to the floor, this process can be considered
as a free fall and the LED dot matrix shows the number 8. (Please note
that this test is not recommended for it may damage the main board.)

\**Attention: If you’d like to try this function, you can also set the
acceleration to 3g, 6g or 8g. \*\*

5. **Test Code2**

Enter Mu software and open the file“Three-axis acceleration sensor
-2.py“ to import the code. You can also input the code in the editing
window yourself.

(**Note: All words and symbols must be written in English.**)

|image118|

.. code:: python

   from microbit import *

   while True:

       x = accelerometer.get_x()

       y = accelerometer.get_y()

       z = accelerometer.get_z()

       print("x, y, z:", x, y, z)

       sleep(100)

Click“Check”to examine errors in the code. The program proves wrong if
underlines and cursors are shown.

|image119|

If the code is correct, connect the micro:bit to your computer and
click“Flash”to download the code to the micro:bit board.

|image120|

6. **Test Result2**

After downloading the code to the board successfully, **power on via
micro USB cable or external power supply(turn the DIP switch to ON)**.
Click“REPL”and press the reset button on micro:bit.

|image121|

Then REPL window will show the value of the acceleration on X axis, Y
axis and Z axis are shown below:

|image122|

After referring to the MMA8653FC data manual and the hardware schematic
diagram of the micro: bit main board, the accelerometer coordinate of
the micro: bit is shown in the figure below:

|image123|

7. **Code Explanation**

|image124|

|image125|

Project 8：Light Detection
~~~~~~~~~~~~~~~~~~~~~~~~~~

|image126|

1. **Description**

In this project, we will focus on the light detection function of the
Micro: Bit main board. It is achieved by the LED dot matrix since the
main board is not equipped with a photoresistor.

2. **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the offline version of Mu.

3. **Test Code**

Enter Mu software and open the file“Detect Light Intensity by
Microbit.py”to import the code. You can also input code in the edit
window yourself.

(**Note: All English words and symbols must be written in English.**)

|image127|

.. code:: python

   from microbit import *

   while True:

       Lightintensity = display.read_light_level()

       print("Light intensity:", Lightintensity)

       sleep(100)

Click“Check”to examine errors in the code. The program proves wrong if
underlines and cursors are shown.

|image128|

If the code is correct, connect the micro:bit to your computer and
click“Flash”to download code to the micro:bit board.

|image129|

4. **Test Result**

After downloading the code to the board successfully, **power on via
micro USB cable or external power supply(turn the DIP switch to ON)**.
Click“REPL”and press the reset button on micro:bit.

|image130|

Then REPL window will show the light intensity value, as shown below.

When the LED dot matrix is covered by hand, the light intensity showed
is approximately 0; when the LED dot matrix is exposed to light, the
light intensity displayed gets stronger with the light.

|image131|

5. **Code Explanation**

|image132|

Project 9：Speaker
~~~~~~~~~~~~~~~~~~

|image133|

1. **Description**

Micro: Bit main board has an built-in speaker, which makes adding sound
to the programs easier. It can also be programmed to produce all kinds
of tones, like playing the song *Ode to Joy.*

2. **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the offline version of Mu.

3. **Test Code**

Enter Mu software and open the file“Speaker.py”to import code. You can
also input code in the editing window yourself.

(**Note: All words and symbols must be written in English**.)

|image134|

.. code:: python

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

Click“Check”to examine errors in the code. The program proves wrong if
underlines and cursors are shown.

|image135|

If the code is correct, connect the micro:bit to your computer and
click“Flash”to download the code to the micro:bit board.

|image136|

4. **Test Result**

After downloading the code to the board successfully, **power on via
micro USB cable or external power supply(turn the DIP switch to
ON)**,and press the reset button on micro:bit.

|image137|

The speaker utters sound and the LED dot matrix shows the logo of music.

5. **Code Explanation**

|image138|

Project 10: Touch-sensitive Logo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image139|

1. **Description**

The Micro: Bit main board V2 is equipped with a golden touch-sensitive
logo, which can act as an input component like an button.

It contains a capacitive touch sensor that senses small changes in the
electric field when pressed (or touched), just like your phone or tablet
screen. When you press it , the program can be activated.

2. **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the offline version of Mu.

3. **Test Code**

Enter Mu software and open the file“Touch-sensitive Logo.py”to import
code.You can also input code in the edit window yourself.

(**Note: All English words and symbols must be written in English**.)

|image140|

.. code:: python

   from microbit import *
   time = 0
   start = 0
   running = False

   while True:

       if button_a.was_pressed():
           running = True
           start = running_time()
       if button_b.was_pressed():
           if running:
               time += running_time() - start
           running = False
       if pin_logo.is_touched():
           if not running:
               display.scroll(int(time/1000))

       if running:
           display.show(Image.HEART)
           sleep(300)
           display.show(Image.HEART_SMALL)
           sleep(300)
       else:
           display.show(Image.ASLEEP)

**How Micro:bit works?**

A. The runtime is recorded in milliseconds(ms) .

B. When you press button A, a variable named start will be set to the
current running time.

C. When you press button B, the start time will be subtracted from the
new running time to calculate the passed time since you started the
stopwatch. This difference is added to the total time, which is stored
in a variable named time.

D. If you press the golden logo, the program will display the total
elapsed time on the LED display. It converts time from milliseconds
(thousandths of a second) to seconds by dividing by 1000. It uses the
integer division operator to give an integer (integer) result.

E. The program is also controlled by a Boolean variable named running.
Boolean variable only has two values: true or false. If "running" is
"true", it means that the stopwatch has started. If "running" is false,
it means that the stopwatch has not started or has stopped.

F. If "running" is true, the beating heart pattern will be displayed on
the LED dot matrix screen.

G. (7) If the stopwatch has stopped and the "running" is false, when you
press the golden logo, it will only display the time.

H. If the stopwatch has been started and"running" is true, it only need
to ensure that the time variable will change when button B is pressed,
and the code can also prevent false readings.

Click“Check”to examine errors in the code. The program proves wrong if
underlines and cursors are shown.

|image141|

If the code is correct, connect the micro:bit to your computer and
click“Flash”to download code to the micro:bit board.

|image142|

4. **Test Result**

After downloading the code to the board successfully, **power on via
micro USB cable or external power supply(turn the DIP switch to
ON)**,and press the reset button on micro:bit.

|image143|

Press button A to start the stopwatch. When timing, the beating heart
pattern will be displayed on the LED dot matrix screen. Press button B
to stop it and you can start and stop it at any time.

It will keep recording time, just like a real stopwatch. Press the
golden logo in the front of the micro:bit to display the measured time
in seconds. And the time can be reset to zero by pressing the reset
button on the back of it.

Project 11: Microphone
~~~~~~~~~~~~~~~~~~~~~~

|image144|

|image145|

1. **Description**

The Micro: Bit main board has a built-in microphone, which can test the
volume of ambient environment. When you clap, the microphone LED
indicator turns on. Furthermore, it can measure the intensity of sound,
thereby you can make a noise scale or disco lighting changing with
music.

The microphone is placed on the opposite side of the microphone LED
indicator and in proximity with holes that lets sound pass. When the
board detects the sound, the LED indicator lights up.

2. **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the offline version of Mu.

3. **Test Code1**

Enter Mu software and open the file“Microphone-1.py”to import the code.
You can also input code in the editing window yourself.

(**Note: All words and symbols must be written in English**.)

|image146|

.. code:: python

   from microbit import *

   while True:
       if microphone.current_event() == SoundEvent.LOUD:
           display.show(Image.HEART)
           sleep(200)
       if microphone.current_event() == SoundEvent.QUIET:
           display.show(Image.HEART_SMALL)

Click“Check”to examine errors in the code. The program proves wrong if
underlines and cursors are shown.

|image147|

If the code is correct, connect the micro:bit to your computer and
click“Flash”to download code to the micro:bit board.

|image148|

4. **Test Result1**

After downloading the code to the board successfully, **power on via
micro USB cable or external power supply(turn the DIP switch to
ON)**,and press the reset button on micro:bit.

|image149|

The LED dot matrix displays the pattern “❤”when you clap and the pattern
|image150| when it is quiet around.

5. **Test Code2**

Enter Mu software and open the file“Microphone-2.py”to import the code.
You can also input code in the editing window yourself.

(**Note: All words and symbols must be written in English.**)

|image151|

.. code:: python

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

Click“Check”to examine errors in the code. The program proves wrong if
underlines and cursors are shown.

|image152|

If the code is correct, connect the micro:bit to your computer and
click“Flash”to download code to the micro:bit board.

|image153|

6. **Test Result2**

After downloading the code to the board successfully, **power on via
micro USB cable or external power supply(turn the DIP switch to
ON)**,and press the reset button on micro:bit.

|image154|

When the button A is pressed, the LED dot matrix displays the value of
the biggest volume( **please note that the biggest volume can be reset
via the Reset button on the other side of the board** ). When clapping,
the louder the tested sound, the brighter the 25 LEDs on the LED dot
matrix screen.

7. **Code Explanation**

|image155|

Project 12: Control Speaker
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Description**

In the previous projects, we have learned about the touch-sensitive logo
and the speaker respectively. In the project, we will combine these two
components to play music.

2. **Components Needed**

\|\ |image156|\ \|\ |image157|\ \| \|-\|-\|-\| \|Micro:bit main board
\*1|USB cable*1\|

3. **Wiring Diagram**

Attach the Micro:bit main board to your computer via the USB cable.

|image158|\ A

4. **Test Code**

Enter Mu software and open the file“Touch the Logo to control the
speaker.py”to import code. You can also input code in the editing window
yourself.

(**Note: All words and symbols must be written in English**.)

|image159|

.. code:: python

   from microbit import *

   import music

   display.show(Image.MUSIC_QUAVER)

   while True:

       if pin_logo.is_touched():
           music.play(music.BIRTHDAY)

Click“Check”to examine errors in the code. The program proves wrong if
underlines and cursors are shown.

|image160|

If the code is correct, connect the micro:bit to your computer and
click“Flash”to download the code to the micro:bit board.

|image161|

5. **Test Result**

After downloading the code to the board successfully, **power on via
micro USB cable or external power supply(turn the DIP switch to
ON)**,and press the reset button on micro:bit.

|image162|

The speaker plays the song “\ *Happy Birthday to You”* when the logo is
touched.

6. **Code Explanation**

|image163|

Bluetooth Wireless Communication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The micro:bit owns a low-consumption Bluetooth module to communicate but
with 16k RAM. However, BLE heap stack occupies 12K RAM, thereby there is
no enough space to run microPython.

At present, microPython doesn’t support the Bluetooth service.

https://microbit-micropython.readthedocs.io/en/latest/ble.html

The former projects are the introduction of sensors and modules. The
further lessons are challenging for new starters.

(**Note: In order to refrain the micro:bit board from being burned,
disconnect the micro USB cable from it and turn off the power on the
micro:bit motor driver base plate before installing it on the car
expansion board and dial the POWER switch to the OFF end. Likewise,
before removing the the main board from the car expansion board,
disconnect the micro USB cable from it and turn off the power on the
micro:bit motor driver base plate.**)

Project 13: Seven-Color LED
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image164|\\

1. **Description**

This module consists of a commonly used LED with 7colors but in whit
ppearance. It can automatically flash different colors to creat antastic
light effects when high level is input like a normal LED.

2. **Preparation**

- Insert the micro:bit board into the slot of keyestudi
  4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the offline version of Mu.

3. **Test Code**

Enter Mu software and open the file“Colorful lights.py”to import code.
You can also input code in the editing window yourself.

(**Note: All words and symbols must be written in English**.)

|image165|

.. code:: python

   from microbit import *
   from keyes_mecanum_Car_V2 import *

   mecanumCar = Mecanum_Car_Driver_V2()

   while True:
       mecanumCar.left_led(1)
       mecanumCar.right_led(1)
       sleep(3000)
       mecanumCar.left_led(0)
       mecanumCar.right_led(0)
       sleep(3000)

**Important Notice:** If the library file 'keyes_mecanum_Car_V2.py' has
not yet been imported to the microbit board, it is essential to first
import the library file to the microbit board. The method for importing
the library can be found by clicking the link：\ `How to Import Library
to
Micro:bit <https://docs.keyestudio.com/projects/KS4034/en/latest/docs/Python/Python.html#how-mu-import-library-to-micro-bit>`__
and following the instructions provided; otherwise, the code will not
run.

After the library file is imported successfully, you also need to click
the "Check" button to check the code. If a cursor or an underline
appears on a certain line, then errors appear in the program.

|image166|

However, during this process, the following prompt will appear even if
there is no error in the code. These prompts are just warnings not the
code error prompts.

|image167|

|image168|

If the code is correct, connect the micro:bit to your computer and
click“Flash”to download the code to the micro:bit board.

|image169|

If errors appear after clicking the "Flash" button, please confirm
whether you have imported the provided "keyes_mecanum_Car_V2.py" library
file.

**Note:** Before programming with Micropython, you need to import the
"keyes_mecanum_Car_V2.py" library file to the micro:bit. If you program
with different micro:bit, the library file"keyes_mecanum_Car_V2.py"
needs to be imported again to a new micro:bit.

4. **Test Result**

After downloading the code to the board successfully, **external power
supply(turn the DIP switch to ON)**,and press the reset button on
micro:bit.

|image170|

The seven-color LED will flash in 3s and then stop in 3s and repeat this
pattern.

5. **Code Explanation**

|image171|

Project 14: 4 WS2812 RGB LEDs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image172|

1. **Description**

The driver shield cooperates 4 pcs WS2812 RGB LEDs, compatible with
micro:bit board and controlled by P7. In this lesson, we will make the
RGB LEDs display different colors by P7. In this lesson, 3 sets of test
code are provided to make the 4 WS2812 RGB LEDs display different
effects.

+-------+-------+-------+-------+-------+-------+-------+-------+
| S     | Color | RGB   | Color | S     | Color | RGB   | Color |
| ample |       | Valu  | Co    | ample |       | Valu  | Co    |
|       |       | e（R, | de(16 |       |       | e（R, | de(16 |
|       |       | G,B） | co    |       |       | G,B） | colo  |
|       |       |       | lors) |       |       |       | rs)） |
+=======+=======+=======+=======+=======+=======+=======+=======+
| |imag | Red   | 255,  | #F    | |imag | O     | 255,  | #F    |
| e193| |       | 0, 0  | F0000 | e194| | range | 165,  | FA500 |
|       |       |       |       |       |       | 0     |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| |imag | Y     | 255,  | #F    | |imag | Green | 0,    | #0    |
| e195| | ellow | 255,  | FFF00 | e196| |       | 255,  | 0FF00 |
|       |       | 0     |       |       |       | 0     |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| |imag | Blue  | 0,    | #0    | |imag | I     | 75,   | #4    |
| e197| |       | 255,  | 000FF | e198| | ndigo | 0,    | B0082 |
|       |       | 0     |       |       |       | 130   |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| |imag | V     | 238,  | #E    | |imag | P     | 160,  | #A    |
| e199| | iolet | 130,  | E82EE | e200| | urple | 32,   | 020F0 |
|       |       | 238   |       |       |       | 240   |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| |imag | Black | 0, 0, | #0    | |imag | White | 255,  | #F    |
| e201| |       | 0     | 00000 | e202| |       | 255,  | FFFFF |
|       |       |       |       |       |       | 255   |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| .     | .     | ..    | .     | .     | .     | .     | .     |
| ..... | ..... | ..... | ..... | ..... | ..... | ..... | ..... |
+-------+-------+-------+-------+-------+-------+-------+-------+
| C     | the   | value | R,G   | to    | get   | dif   | olors |
| hange |       | of    | and B |       |       | feren |       |
|       |       | the   |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+

2. **Preparation**

- Insert micro:bit board into the slot of keyestudio
  4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the offline version of Mu.

3. **Test Code1**

Enter Mu software and open the file“4 WS2812 RGB LEDs-1.py”to import
code\\ You can also input code in the edit window yourself.

(**Note: All English words and symbols must be written in English.**)

Click“Check”to examine errors in the code. The program proves wrong if
underlines and cursors are shown.

|image203|

.. code:: python

   from microbit import *
   import neopixel
   np = neopixel.NeoPixel(pin7, 4)
   while True:
       for pixel_id1 in range(0, len(np)):
           np[pixel_id1] = (255, 0, 0)
           np.show()
       sleep(1000)
       for pixel_id2 in range(0, len(np)):
           np[pixel_id2] = (255, 165, 0)
           np.show()
       sleep(1000)
       for pixel_id3 in range(0, len(np)):
           np[pixel_id3] = (255, 255, 0)
           np.show()
       sleep(1000)
       for pixel_id4 in range(0, len(np)):
           np[pixel_id4] = (0, 255, 0)
           np.show()
       sleep(1000)
       for pixel_id5 in range(0, len(np)):
           np[pixel_id5] = (0, 0, 255)
           np.show()
       sleep(1000)
       for pixel_id6 in range(0, len(np)):
           np[pixel_id6] = (75, 0, 130)
           np.show()
       sleep(1000)
       for pixel_id7 in range(0, len(np)):
           np[pixel_id7] = (238, 130, 238)
           np.show()
       sleep(1000)
       for pixel_id8 in range(0, len(np)):
           np[pixel_id8] = (160, 32, 240)
           np.show()
       sleep(1000)
       for pixel_id9 in range(0, len(np)):
           np[pixel_id9] = (255, 255, 255)
       sleep(1000)

If the code is correct, connect the micro:bit to your computer and
click“Flash”to download the code to the micro:bit board.

|image204|

4. **Test Result1**

After downloading the code to the board successfully, **external power
supply(turn the DIP switch to ON)**,and press the reset button on
micro:bit.

|image205|

The 4 WS2812RGB LEDs light up a different color a time cyclically.

5. **Test Code2**

Enter Mu software and open the file“4 WS2812 RGB LEDs-2.py”to import
code. You can also input code in the edit window yourself.

(**Note: All English words and symbols must be written in English**.)

Click“Check”to examine errors in the code. The program proves wrong if
underlines and cursors are shown.

If the code is correct, connect the micro:bit to your computer and
click“Flash”to download the code to the micro:bit board.

|image206|

.. code:: python

   from microbit import *
   import neopixel
   np = neopixel.NeoPixel(pin7, 4)
   while True:
       for index in range(0, 4):
           np.clear()
           np[index] = (255, 0, 0)
           np.show()
           sleep(100)
       for index1 in range(0, 4):
           np.clear()
           np[index1] = (255, 165, 0)
           np.show()
           sleep(100)
       for index2 in range(0, 4):
           np.clear()
           np[index2] = (255, 255, 0)
           np.show()
           sleep(100)
       for index3 in range(0, 4):
           np.clear()
           np[index3] = (0, 255, 0)
           np.show()
           sleep(100)
       for index4 in range(0, 4):
           np.clear()
           np[index4] = (0, 0, 255)
           np.show()
           sleep(100)
       for index5 in range(0, 4):
           np.clear()
           np[index5] = (75, 0, 130)
           np.show()
           sleep(100)
       for index6 in range(0, 4):
           np.clear()
           np[index6] = (238, 130, 238)
           np.show()
           sleep(100)
       for index7 in range(0, 4):
           np.clear()
           np[index7] = (160, 32, 240)
           np.show()
           sleep(100)
       for index8 in range(0, 4):
           np.clear()
           np[index8] = (255, 255, 255)
           np.show()
           sleep(100)

6. **Test Result2**

After downloading the code to the board successfully, **external power
supply(turn the DIP switch to ON)**,and press the reset button on
micro:bit.

|image207|

The WS2812RGB LEDs display like a flow light.

7. **Test Code3**

Enter Mu software and open the file“4 WS2812 RGB LEDs-3.py”to import
code. You can also input code in the edit window yourself.

(**Note: All English words and symbols must be written in English.**)

Click“Check”to examine errors in the code. The program proves wrong if
underlines and cursors are shown.

If the code is correct, connect the micro:bit to your computer and
click“Flash”to download the code to the micro:bit board.

|image208|

.. code:: python

   from microbit import *
   import neopixel
   np = neopixel.NeoPixel(pin7, 4)
   from random import randint
   R = 0
   G = 0
   B = 0
   while True:
      for index in range(0, 4):
           R = randint(10, 255)
           G = randint(10, 255)
           B = randint(10, 255)
           np.clear()
           np[index] = (R, G, B)
           np.show()
           sleep(500)

8. **Test Result3**

After downloading the code to the board successfully, **external power
supply(turn the DIP switch to ON)**,and press the reset button on
micro:bit.

|image209|

Every WS2812RGB light shows random color one by one.

5. **Code Explanation**

|image210|

Project 15：Servo
~~~~~~~~~~~~~~~~~

|image211|

1. **Description**

The DIY smart cars usually contain the function of automatic obstacle
avoidance. In the DIY process, we need a servo to control the ultrasonic
module to rotate left and right, and then detect the distance between
the car and the obstacle, so as to control the car to avoid the
obstacle.

If other microcontrollers are used to control the rotation of the servo,
we need to set a certain frequency and width of pulse to control the
servo angle. But if the micro:bit main board is used to control the
servo angle, we only need to set the control angle in the development
environment where the corresponding pulse will be automatically set to
control the servo rotation. In this project, you will learn how to
control the servo to rotate back and forth between 0° and 90°.

Servo motor is a position control rotary actuator, which mainly consists
of housing, circuit board, core-less motor, gear and position
sensor. Its working principle is that the servo receives the signal sent
by MCU or receiver, and produces a reference signal with a period of
20ms and width of 1.5ms, then compares the acquired DC bias voltage to
the voltage of the potentiometer and obtains the voltage difference
output.

For the servo used in this project, the brown wire is the ground, the
red one is the positive wire, and the orange one is the signal wire.

|image212|

2. **Information of the Servo**

The rotation angle of servo motor is controlled by regulating the duty
cycle of PWM (Pulse-Width Modulation) signal. The standard cycle of PWM
signal is 20ms (50Hz). Theoretically, the width is distributed
between 1ms-2ms, but in fact, it's between 0.5ms-2.5ms. The width
corresponds to the rotation angle from 0° to 180°. But note that for
different brand motor, the same signal may have different rotation
angle. 

|image213|

After measurement, the pulse range of the servo is 0.65ms~2.5ms. For a
180 degree servo, the corresponding control relationship is as follow:

+--------------------+--------------------+-------------------------------------+
| Time on High Level | Angle of the Servo | Reference Signal Cycle Time（20ms） |
+====================+====================+=====================================+
| 0.65ms             | 0 degree           | 0.65ms high level+19.35ms low level |
+--------------------+--------------------+-------------------------------------+
| 1.5ms              | 90 degrees         | 1.5ms high level+18.5ms low level   |
+--------------------+--------------------+-------------------------------------+
| 2.5ms              | 180degrees         | 2.5ms high level+17.5ms low level   |
+--------------------+--------------------+-------------------------------------+

3. **Parameters**

- Working voltage: DC 4.8V ~ 6V

- Operating angle range: about 180 ° (at 500 → 2500 μsec)

- Dimension: 22.9*12.2*30mm

- Pulse width range: 500 → 2500 μsec

- No-load speed: 0.12 ± 0.01 sec / 60 (DC 4.8V), 0.1 ± 0.01 sec / 60 (DC
  6V)

- No-load current: 200 ± 20mA (DC 4.8V), 220 ± 20mA (DC 6V)

- Stopping torque: 1.3 ± 0.01kg · cm (DC 4.8V) ,1.5 ± 0.1kg · cm (DC 6V)

- Stop current: ≦ 850mA (DC 4.8V) ≦ 1000mA (DC 6V)

- Standby current: 3 ± 1mA (DC 4.8V), 4 ± 1mA (DC 6V)

- Weight: 9±1g (without servo horn)

- Working temperature: -30℃~60℃

**It should be noted that do not use a computer for power supply,
because if the current demand is greater than 500mA, the servo may be
burned out. It is recommended to use an external battery for power
supply.**

4. **Preparation**

- Insert micro:bit board into the slot of keyestudio
  4WD Mecanum Robot CarV2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect micro:bit to computer via an USB cable

- Open the offline version of Mu.

5. **Test Code**

Enter Mu software and open the file“Servo.py”to import code. You can
also input code in the edit window yourself.

(**Note: All English words and symbols must be written in English**.)

Click“Check”to examine errors in the code. The program proves wrong if
underlines and cursors are shown.

If the code is correct, connect the micro:bit to your computer and
click“Flash”to download the code to the micro:bit board.

|image214|

.. code:: python

   from microbit import *

   class Servo:
       def __init__(self, pin, freq=50, min_us=600, max_us=2400, angle=180):
           self.min_us = min_us
           self.max_us = max_us
           self.us = 0
           self.freq = freq
           self.angle = angle
           self.analog_period = 0
           self.pin = pin
           analog_period = round((1/self.freq) * 1000)  # hertz to miliseconds
           self.pin.set_analog_period(analog_period)

       def write_us(self, us):
           us = min(self.max_us, max(self.min_us, us))
           duty = round(us * 1024 * self.freq // 1000000)
           self.pin.write_analog(duty)
           sleep(100)
           self.pin.write_analog(0)

       def write_angle(self, degrees=None):
           if degrees is None:
               degrees = math.degrees(radians)
           degrees = degrees % 360
           total_range = self.max_us - self.min_us
           us = self.min_us + total_range * degrees // self.angle
           self.write_us(us)

   Servo(pin14).write_angle(0)
   display.show(Image.HAPPY)

   while True:
           Servo(pin14).write_angle(0)
           sleep(1000)
           Servo(pin14).write_angle(45)
           sleep(1000)
           Servo(pin14).write_angle(90)
           sleep(1000)
           Servo(pin14).write_angle(135)
           sleep(1000)
           Servo(pin14).write_angle(180)
           sleep(1000)

4. **Test Result**

After downloading the code to the board successfully, **external power
supply(turn the DIP switch to ON)**,and press the reset button on
micro:bit.

|image215|

The LED dot matrix shows a smiley pattern and the servo rotates in the
pattern 0°~45°~90°~135°~180°~0°.

Project 16：Motor
~~~~~~~~~~~~~~~~~

|image216|

1. **Description**

The Keyestudio 4WD Mecanum Robot Car is equipped with 4 DC reduction
motors, also called gear reduction motor, which is developed on the
ordinary DC motor. It has a matching gear reduction box which provides a
lower speed but a larger torque. Furthermore, different reduction ratios
of the box can provide different speeds and torques.

Gear motor is the integration of gearmotor and motor, which is applied
widely in steel and machine industry

Micro:bit motor driver shield comes with a STC8G and HR8833 chip. In
order to save the IO port resource, we control the rotation direction
and speed of 4 DC gear motors with the HR8833 chip.

**Details about chips:**

|image217|

Front

|image218|

Back

|image219|

STC8G1K08 Chip circuit

|image220|

HR8833 Motor driver circuit

2. **Preparation**

- Insert micro:bit board into the slot of keyestudio
  4WD Mecanum Robot CarV2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect micro:bit to the computer via an USB cable

- Open the offline version of Mu.

3. **Test Code1**

Enter Mu software and open the file“microbit-Motor Driving-1.py”to
import code. You can also input code in the edit window yourself.

(**Note: All English words and symbols must be written in English**.)

Click“Files”to import“keyes_mecanum_Car.py“library file to micro:bit .

Click“Check”to examine errors in the code. The program proves wrong if
underlines and cursors are shown.

If the code is correct, connect the micro:bit to your computer and
click“Flash”to download the code to the micro:bit board.

|image221|

.. code:: python

   from microbit import *
   from keyes_mecanum_Car_V2 import *
   mecanumCar = Mecanum_Car_Driver_V2()
   while True:
       display.show(Image.ARROW_S)
       mecanumCar.Motor_Upper_L(1, 100)
       mecanumCar.Motor_Lower_L(1, 100)
       mecanumCar.Motor_Upper_R(1, 100)
       mecanumCar.Motor_Lower_R(1, 100)
       sleep(1000)
       display.show(Image.ARROW_N)
       mecanumCar.Motor_Upper_L(0, 100)
       mecanumCar.Motor_Lower_L(0, 100)
       mecanumCar.Motor_Upper_R(0, 100)
       mecanumCar.Motor_Lower_R(0, 100)
       sleep(1000)
       display.show(Image.ARROW_E)
       mecanumCar.Motor_Upper_L(0, 100)
       mecanumCar.Motor_Lower_L(0, 100)
       mecanumCar.Motor_Upper_R(1, 100)
       mecanumCar.Motor_Lower_R(1, 100)
       sleep(1000)
       display.show(Image.ARROW_W)
       mecanumCar.Motor_Upper_L(1, 100)
       mecanumCar.Motor_Lower_L(1, 100)
       mecanumCar.Motor_Upper_R(0, 100)
       mecanumCar.Motor_Lower_R(0, 100)
       sleep(1000)
       display.show(Image("00900:""09990:""99999:""99999:""09090"))
       mecanumCar.Motor_Upper_L(0, 0)
       mecanumCar.Motor_Lower_L(0, 0)
       mecanumCar.Motor_Upper_R(0, 0)
       mecanumCar.Motor_Lower_R(0, 0)
       sleep(1000)

4. **Test Result1**

After downloading the code to the board successfully, **external power
supply(turn the DIP switch to ON)**,and press the reset button on
micro:bit.

|image222|

Then the car will go forward for 1s, back for 1s, turn left for 1s,
right for 1s, turn anticlockwise for 1s, clockwise for 1 and stop 1s.
Matrix also displays the patterns.

5. **Test Code2**

Enter Mu software and open the file“microbit-Motor Driving-2.py”to
import code. You can also input code in the edit window yourself.

(**Note: All English words and symbols must be written in English**.)

Click“Files”to import“keyes_mecanum_Car.py“library file to micro:bit .

Click“Check”to examine errors in the code. The program proves wrong if
underlines and cursors are shown.

If the code is correct, connect the micro:bit to your computer and
click“Flash”to download the code to the micro:bit board.

|image223|

.. code:: python

   from microbit import button_a, button_b, display, Image, sleep
   from keyes_mecanum_Car_V2 import *
   mecanumCar = Mecanum_Car_Driver_V2()

   show_L = Image("90000:""90000:""90000:""90000:""99999")
   show_O = Image("09990:""90009:""90009:""90009:""09990")
   a = 0
   b = 0
   def run_L():
       global b
       sleep(1000)
       mecanumCar.Motor_Upper_L(1, 100)
       mecanumCar.Motor_Lower_L(1, 100)
       mecanumCar.Motor_Upper_R(1, 100)
       mecanumCar.Motor_Lower_R(1, 100)
       sleep(1000)
       mecanumCar.Motor_Upper_L(0, 100)
       mecanumCar.Motor_Lower_L(0, 100)
       mecanumCar.Motor_Upper_R(1, 100)
       mecanumCar.Motor_Lower_R(1, 100)
       sleep(650)
       mecanumCar.Motor_Upper_L(1, 100)
       mecanumCar.Motor_Lower_L(1, 100)
       mecanumCar.Motor_Upper_R(1, 100)
       mecanumCar.Motor_Lower_R(1, 100)
       sleep(1000)
       mecanumCar.Motor_Upper_L(0, 0)
       mecanumCar.Motor_Lower_L(0, 0)
       mecanumCar.Motor_Upper_R(0, 0)
       mecanumCar.Motor_Lower_R(0, 0)
       b = 0
   def run_O():
       global b
       sleep(1000)
       mecanumCar.Motor_Upper_L(1, 100)
       mecanumCar.Motor_Lower_L(1, 100)
       mecanumCar.Motor_Upper_R(1, 100)
       mecanumCar.Motor_Lower_R(1, 100)
       sleep(1000)
       mecanumCar.Motor_Upper_L(0, 100)
       mecanumCar.Motor_Lower_L(0, 100)
       mecanumCar.Motor_Upper_R(1, 100)
       mecanumCar.Motor_Lower_R(1, 100)
       sleep(620)
       mecanumCar.Motor_Upper_L(1, 100)
       mecanumCar.Motor_Lower_L(1, 100)
       mecanumCar.Motor_Upper_R(1, 100)
       mecanumCar.Motor_Lower_R(1, 100)
       sleep(1000)
       mecanumCar.Motor_Upper_L(0, 100)
       mecanumCar.Motor_Lower_L(0, 100)
       mecanumCar.Motor_Upper_R(1, 100)
       mecanumCar.Motor_Lower_R(1, 100)
       sleep(620)
       mecanumCar.Motor_Upper_L(1, 100)
       mecanumCar.Motor_Lower_L(1, 100)
       mecanumCar.Motor_Upper_R(1, 100)
       mecanumCar.Motor_Lower_R(1, 100)
       sleep(1000)
       mecanumCar.Motor_Upper_L(0, 100)
       mecanumCar.Motor_Lower_L(0, 100)
       mecanumCar.Motor_Upper_R(1, 100)
       mecanumCar.Motor_Lower_R(1, 100)
       sleep(620)
       mecanumCar.Motor_Upper_L(1, 100)
       mecanumCar.Motor_Lower_L(1, 100)
       mecanumCar.Motor_Upper_R(1, 100)
       mecanumCar.Motor_Lower_R(1, 100)
       sleep(1000)
       mecanumCar.Motor_Upper_L(0, 0)
       mecanumCar.Motor_Lower_L(0, 0)
       mecanumCar.Motor_Upper_R(0, 0)
       mecanumCar.Motor_Lower_R(0, 0)
       b = 0
   while True:
       if button_a.was_pressed():
           a = a + 1
           if a >= 3:
               a = 0
       if button_b.was_pressed():
           b = 1
       if (a == 1):
           display.show(show_L)
           if b == 1:
               run_L()
       elif a == 2:
           display.show(show_O)
           if b == 1:
               run_O()

6. **Test Result2**

After downloading the code to the board successfully, **external power
supply(turn the DIP switch to ON)**,and press the reset button on
micro:bit.

|image224|

When the button A and B are firstly pressed, micro:bit will show “L”,
the route of the car is“L”. When they are pressed again,“口”is shown on
micro:bit, and route of the car is“口”. The car will repeat this
pattern.

7. **Code Explanation**

|image225|

|image226|

Project 17：Line Tracking Sensor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _project-171detect-line-tracking-sensor:

Project 17.1：Detect Line Tracking Sensor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|image227|

1. **Description**

The motor driver board of the Keyestudio 4WD Mecanum Robot Car comes
with a 3-channel line tracking sensor, which adopts TCRT5000 IR tubes
and 3 potentiometers.

The TCRT5000 IR tube contains an IR emitting tube and an IR receiving
tube. When the infrared signals of the emitting tube is received by the
receiving tube through reflection, the resistance of the receiving tube
will change, which is generally reflected in the voltage change on the
circuit.  

The resistance varies depending on the intensity of the infrared signals
received by the receiving tube, which is often in the color of the
reflecting surface and the distance of the reflecting surface receiving
tube.  At the time of detection, black is high level active and white is
low level active. 

2. **Working Principle**

When the car runs above a white road, the IR emitting tube installed
under the car emits infrared signals to detect the road and the
receiving tube will receive signals sending back. Then the output end
outputs low level(0); when it detects black lines, it outputs high
level(1).

The 3-channel tracking sensor integrated port on the 4WD Mecanum Robot
Car is connected to the collection port of G ,5V ,P10, P4 and P3 on the
micro:bit expansion board, which is controlled by the P10, P4 and P3 of
the micro:bit. The left TCRT5000 infrared pair tube on the sensor is
controlled by P3, the middle one is by P4 and the right one is by P10.

After putting a white paper on the bottom of the 4WD Mecanum Robot Car,
we will rotate the potentiometers on the 3-way tracking sensor. When the
indicator light on the sensor module is on, pick up the car to make the
two wheels on the 4WD Mecanum Robot Car separate. The height of the
white paper is about 1.5cm, when the indicator light on the sensor
module is off, and then the sensitivity is adjusted.

\**Note that since the 5*5 dot matrix uses the P3P4P6P7P10, we must turn
off the dot matrix function when using the line tracking sensor. \*\*

3. **Preparation**

- Insert micro:bit board into the slot of keyestudio
  4WD Mecanum Robot CarV2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect micro:bit to computer via an USB cable

- Open the offline version of Mu.

4. **Test Code**

Enter Mu software and open the file“Line tracking detection.py”to import
code. You can also input code in the edit window yourself.

(**Note: All English words and symbols must be written in English**.)

Click“Check”to examine errors in the code. The program proves wrong if
underlines and cursors are shown.

If the code is correct, connect the micro:bit to your computer and
click“Flash”to download the code to the micro:bit board.

|image228|

.. code:: python

   from microbit import *
   display.off()

   val_L = 0
   val_C = 0
   val_R = 0
   while True:
       val_L = pin3.read_digital()
       val_C = pin4.read_digital()
       val_R = pin10.read_digital()
       print("digital signal:", end = ' ')
       print(val_L, end = ' ')
       print(val_C, end = ' ')
       print(val_R)
       sleep(200)

5. **Test Result**

After downloading the code to the board successfully and don’t plug off
the USB cable. Click“REPL”and then press the reset button.

|image229|

The readings detected by the left TCRT5000 IR tube will be displayed on
monitor.

When the left TCRT5000 IR tube detects the white object, 0 will be shown
and the left indicator will be on; when there is only black object
detected, 1 will be displayed and the indicator will be off, as shown
below:

|image230|

6. **Code Explanation**

|image231|

.. _project-172tracking-smart-car:

Project 17.2：Tracking Smart Car
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|image232|

1. Description

In this lesson we will combine a line tracking sensor with a motor to
make a line tracking smart car.

The micro:bit board will analyze the signals and control the smart car
to show the line tracking function.

2. **Working Principle**

The smart car will make different moves according to the value received
by the 3-channel line tracking sensor.

|image233|

3. **Preparation**

- Insert micro:bit board into the slot of keyestudio
  4WD Mecanum Robot CarV2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect micro:bit to computer via an USB cable

- Open the offline version of Mu.

**Warning:** The 3-way tracking sensor should be used in environment
ithout infrared interference such as sunlight. Sunlight contains a lo f
invisible light, such as infrared and ultraviolet. In an environmen ith
strong sunlight, the 3-way tracking sensor cannot work properly.

4. **Flow Chart**

|image234|

5. **Test Code**

Enter Mu software and open the file“Line tracking car.py”to import code.
You can also input code in the edit window yourself.

(**Note: All English words and symbols must be written in English**.)

Click“Files”to import“keyes_mecanum_Car.py“library file to micro:bit.

Click“Check”to examine errors in the code. The program proves wrong if
underlines and cursors are shown.

If the code is correct, connect the micro:bit to your computer and
click“Flash”to download the code to the micro:bit board.

|image235|

.. code:: python

   from microbit import *
   from keyes_mecanum_Car_V2 import *
   mecanumCar = Mecanum_Car_Driver_V2()
   display.off()

   val_L = 0
   val_C = 0
   val_R = 0
   while True:
       val_L = pin3.read_digital()
       val_C = pin4.read_digital()
       val_R = pin10.read_digital()
       if val_C == 0:
           if val_L == 0 and val_R == 1:
               mecanumCar.Motor_Upper_L(1, 80)
               mecanumCar.Motor_Lower_L(1, 80)
               mecanumCar.Motor_Upper_R(0, 80)
               mecanumCar.Motor_Lower_R(0, 80)
           elif val_L == 1 and val_R == 0:
               mecanumCar.Motor_Upper_L(0, 80)
               mecanumCar.Motor_Lower_L(0, 80)
               mecanumCar.Motor_Upper_R(1, 80)
               mecanumCar.Motor_Lower_R(1, 80)
           else:
               mecanumCar.Motor_Upper_L(0, 0)
               mecanumCar.Motor_Lower_L(0, 0)
               mecanumCar.Motor_Upper_R(0, 0)
               mecanumCar.Motor_Lower_R(0, 0)
       else :
           if val_L == 0 and val_R == 1:
               mecanumCar.Motor_Upper_L(1, 80)
               mecanumCar.Motor_Lower_L(1, 80)
               mecanumCar.Motor_Upper_R(0, 80)
               mecanumCar.Motor_Lower_R(0, 80)
           elif val_L == 1 and val_R == 0:
               mecanumCar.Motor_Upper_L(0, 80)
               mecanumCar.Motor_Lower_L(0, 80)
               mecanumCar.Motor_Upper_R(1, 80)
               mecanumCar.Motor_Lower_R(1, 80)
           else:
               mecanumCar.Motor_Upper_L(1, 80)
               mecanumCar.Motor_Lower_L(1, 80)
               mecanumCar.Motor_Upper_R(1, 80)
               mecanumCar.Motor_Lower_R(1, 80)

6. **Test Result**

After downloading the code to the board successfully, **external power
supply(turn the DIP switch to ON)**,and press the reset button on
micro:bit.

|image236|

The line tacking car goes forward along the black line .

**Note:** （1）The width of black line should be equal to or larger than
the width of the line tracking sensor when tracking.

（2)Avoid to test the smart car under the strong light.

7. **Code Explanation**

|image237|

|image238|

Project 18：Ultrasonic Sensor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _project-181ultrasonic-ranging:

Project 18.1：Ultrasonic Ranging
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. **Description**

|image239|

The ultrasonic sensor uses sonar to determine distance to an object like
bats do. It offers excellent non-contact range detection with high
accuracy and stable readings in an easy-to-use package. It comes
complete with ultrasonic transmitter and receiver modules.

The ultrasonic sensor is being used in a wide range of electronics
projects for creating obstacle detection and distance measuring
application as well as various other applications.

|image240|

The ultrasonic module will emit the ultrasonic waves after trigger
signals. When the ultrasonic waves encounter the object and are
reflected back, the module outputs an echo signal, so it can determine
the distance of object from the time difference between trigger signal
(TRIG)and echo signal(ECHO).

As the picture shows, it is like two eyes. One is transmitting end, the
other is receiving end.

According to the above wiring diagram, the integrated port of the
ultrasonic sensor module is connected to the 5V G P15 P16 port on the
micro:bit motor driver base plate. The Trig (T) pin is controlled by P15
of the micro:bit and the pin of Echo (E) the P16.

|image241|

2. **Working Principle**

|image242|

(1) Pull down TRIG then trigger high level signals with least 10us;

(2) After triggering, the module will automatically send eight 40KH
ltrasonic pulses and detect whether there is a signal return;

(3) If there is a signal return, when ECHO (E) outputs a high level, the
he duration of the high level is the time from transmission t eception
of the ultrasonic waves. Then test distance = high leve uration
\*340m/s*0.5. 

3. **Parameters**

- Working voltage: 3-5.5V (DC)

- Working current: 15mA

- Working frequency: 40khz

- Maximum detection distance: about 3m

- Minimum detection distance: 2-3cm

- Precision: up to 0.2cm

- Sensing angle: less than 15 degrees

- Input trigger pulse: 10us TTL level

- Output echo signal: output TTL level signal (high), proportional t
  range

4. **Preparation**

- Insert micro:bit board into the slot of keyestudio
  4WD Mecanum Robot CarV2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect micro:bit to the computer via an USB cable

- Open the offline version of Mu.

5. **Test Code**

Enter Mu software and open the file“Ultrasonic Ranging.py”to import
code. You can also input code in the edit window yourself.

(**Note: All English words and symbols must be written in English**.)

Click“Files”to import“keyes_mecanum_Car_V2.py“library file to micro:bit
(How to import files? ).

Click“Check”to examine errors in the code. The program proves wrong if
underlines and cursors are shown.

If the code is correct, connect the micro:bit to your computer and
click“Flash”to download the code to the micro:bit board.

|image243|

.. code:: python

   from microbit import *
   from keyes_mecanum_Car_V2 import *
   mecanumCar = Mecanum_Car_Driver_V2()
   import music
   tune = ["C4:4"]
   distance_val = 0

   while True:
       i = 0
       distance_val = mecanumCar.get_distance()
       print("distance:", distance_val)
       if distance_val < 10:
           while i < 1:
               music.play(tune)
               sleep(200)
               music.play(tune)
               sleep(200)
               i += 1

6. **Test Result**

After downloading the code to the board successfully and don’t plug off
the USB cable. Click“REPL”and then press the reset button.

|image244|

The distance value of obstacle will be displayed, as shown below.

When the distance is less than 10cm, the passive buzzer of smart will
emit sound.

|image245|

7. **Code Explanation**

|image246|

.. _project-182ultrasonic-avoidance:

Project 18.2：Ultrasonic Avoidance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|image247|

1. **Description**

In this project, we will integrate an ultrasonic sensor and a car to
make an ultrasonic avoidance car.

Its principle is to detect the distance between the car and obstacle via
the ultrasonic sensor to control the motion of smart car.

2. **Preparation**

- Insert micro:bit board into the slot of keyestudio
  4WD Mecanum Robot CarV2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect micro:bit to the computer via an USB cable

- Open the offline version of Mu.

3. **Flow Chart**

|image248|

4. **Test Code**

Enter Mu software and open the file“Ultrasonic Avoid Smart Car.py”to
import code. You can also input code in the edit window yourself.

(**Note: All English words and symbols must be written in English**.)

Click“Files”to import“keyes_mecanum_Car_V2.py“library file to micro:bit
.

Click“Check”to examine errors in the code. The program proves wrong if
underlines and cursors are shown.

If the code is correct, connect the micro:bit to your computer and
click“Flash”to download the code to the micro:bit board.

|image249|

.. code:: python

   from microbit import *
   from keyes_mecanum_Car_V2 import *
   mecanumCar = Mecanum_Car_Driver_V2()
   distance_val = 0
   distance_l = 0
   distance_r = 0
   class Servo:
       def __init__(self, pin, freq=50, min_us=600, max_us=2400, angle=180):
           self.min_us = min_us
           self.max_us = max_us
           self.us = 0
           self.freq = freq
           self.angle = angle
           self.analog_period = 0
           self.pin = pin
           analog_period = round((1/self.freq) * 1000)  # hertz to miliseconds
           self.pin.set_analog_period(analog_period)

       def write_us(self, us):
           us = min(self.max_us, max(self.min_us, us))
           duty = round(us * 1024 * self.freq // 1000000)
           self.pin.write_analog(duty)
           sleep(100)
           self.pin.write_analog(0)

       def write_angle(self, degrees=None):
           if degrees is None:
               degrees = math.degrees(radians)
           degrees = degrees % 360
           total_range = self.max_us - self.min_us
           us = self.min_us + total_range * degrees // self.angle
           self.write_us(us)

   Servo(pin14).write_angle(90)

   while True:

       distance_val = mecanumCar.get_distance()

       if distance_val < 20:
           mecanumCar.Motor_Upper_L(0, 0)
           mecanumCar.Motor_Lower_L(0, 0)
           mecanumCar.Motor_Upper_R(0, 0)
           mecanumCar.Motor_Lower_R(0, 0)
           sleep(500)
           Servo(pin14).write_angle(180)
           sleep(500)
           distance_l = mecanumCar.get_distance()
           sleep(500)

           Servo(pin14).write_angle(0)
           sleep(500)
           distance_r = mecanumCar.get_distance()
           sleep(500)

           if distance_l > distance_r:
               mecanumCar.Motor_Upper_L(0, 100)
               mecanumCar.Motor_Lower_L(0, 100)
               mecanumCar.Motor_Upper_R(1, 100)
               mecanumCar.Motor_Lower_R(1, 100)
               Servo(pin14).write_angle(90)
               sleep(300)
           else:
               mecanumCar.Motor_Upper_L(1, 100)
               mecanumCar.Motor_Lower_L(1, 100)
               mecanumCar.Motor_Upper_R(0, 100)
               mecanumCar.Motor_Lower_R(0, 100)
               Servo(pin14).write_angle(90)
               sleep(300)

       else:
           mecanumCar.Motor_Upper_L(1, 100)
           mecanumCar.Motor_Lower_L(1, 100)
           mecanumCar.Motor_Upper_R(1, 100)
           mecanumCar.Motor_Lower_R(1, 100)

5. **Test Result**

After downloading the code to the board successfully, **external power
supply(turn the DIP switch to ON)**,and press the reset button on
micro:bit.

|image250|

When the obstacle distance is greater than 20cm, the car goes forward ;
on the contrary, the smart car turns left.

6. **Code Explanation**

|image251|

|image252|

.. _project-183ultrasonic-following:

Project 18.3：Ultrasonic Following
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|image253|

1. **Description**

In previous lesson, we’ve learned the basic principle of line tracking
sensor. Next, we will combine the ultrasonic sensor with the car to make
an ultrasonic following car.

The ultrasonic sensor detects the obstacle distance and control the
motion status of car.

2. **Preparation**

- Insert micro:bit board into the slot of keyestudio
  4WD Mecanum Robot CarV2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect micro:bit to the computer via an USB cable

- Open the offline version of Mu.

2. **Flow Chart**

|image254|

3. **Test Code**

Enter Mu software and open the file“Ultrasonic Follow Smart Car.py”to
import code. You can also input code in the edit window yourself.

(**Note: All English words and symbols must be written in English**.)

Click“Files”to import“keyes_mecanum_Car_V2.py“library file to micro:bit.

Click“Check”to examine errors in the code. The program proves wrong if
underlines and cursors are shown.

If the code is correct, connect the micro:bit to your computer and
click“Flash”to download the code to the micro:bit board.

|image255|

.. code:: python

   from microbit import *
   from keyes_mecanum_Car_V2 import *
   import neopixel
   display.off()

   mecanumCar = Mecanum_Car_Driver_V2()
   np = neopixel.NeoPixel(pin7, 4)

   class Servo:
       def __init__(self, pin, freq=50, min_us=600, max_us=2400, angle=180):
           self.min_us = min_us
           self.max_us = max_us
           self.us = 0
           self.freq = freq
           self.angle = angle
           self.analog_period = 0
           self.pin = pin
           analog_period = round((1/self.freq) * 1000)  # hertz to miliseconds
           self.pin.set_analog_period(analog_period)

       def write_us(self, us):
           us = min(self.max_us, max(self.min_us, us))
           duty = round(us * 1024 * self.freq // 1000000)
           self.pin.write_analog(duty)
           sleep(100)
           self.pin.write_analog(0)

       def write_angle(self, degrees=None):
           if degrees is None:
               degrees = math.degrees(radians)
           degrees = degrees % 360
           total_range = self.max_us - self.min_us
           us = self.min_us + total_range * degrees // self.angle
           self.write_us(us)

   Servo(pin14).write_angle(90)

   while True:
       distance_val = 0
       distance_val = mecanumCar.get_distance()
       if distance_val >= 20 and distance_val <= 40:
           mecanumCar.Motor_Upper_L(1, 80)
           mecanumCar.Motor_Lower_L(1, 80)
           mecanumCar.Motor_Upper_R(1, 80)
           mecanumCar.Motor_Lower_R(1, 80)
           for pixel_id1 in range(0, len(np)):
               np[pixel_id1] = (255, 0, 0)
               np.show()
       if distance_val <= 10:
           mecanumCar.Motor_Upper_L(0, 80)
           mecanumCar.Motor_Lower_L(0, 80)
           mecanumCar.Motor_Upper_R(0, 80)
           mecanumCar.Motor_Lower_R(0, 80)
           for pixel_id1 in range(0, len(np)):
               np[pixel_id1] = (255, 255, 0)
               np.show()
       if distance_val > 10 and distance_val < 20 or distance_val > 40:
           mecanumCar.Motor_Upper_L(0, 0)
           mecanumCar.Motor_Lower_L(0, 0)
           mecanumCar.Motor_Upper_R(0, 0)
           mecanumCar.Motor_Lower_R(0, 0)
           for pixel_id1 in range(0, len(np)):
               np[pixel_id1] = (255, 255, 255)
               np.show()

4. **Test Result**

After downloading the code to the board successfully, **external power
supply(turn the DIP switch to ON)**, and press the reset button on
micro:bit.

|image256|

The smart car could follow the obstacle to move and 4 WS2812 RGB lights
will display different colors.

**Note:** the obstacle can only move in front of smart car.

5. **Code Explanation**

|image257|

|image258|

Resources
---------

1. BBC microbit
MicroPython：\ https://microbit-micropython.readthedocs.io/en/latest/tutorials/introduction.html

2. MicroPython：\ https://docs.openmv.io/reference/index.html

3. math library：\ https://docs.openmv.io/library/math.html

Common Problem
--------------

1. **The car has no reaction**

Please check whether the batteries are sufficient

Please check whether the wirings are correct

2. **Computers can't recognize the USB ports**

Please ensure whether the microbit driver is installed

Please check whether the USB wire is in good condition.

3. **Code fails to burn and dot matrix displays expressions**

Please check whether the keyes_mecanum_Car_V2.py library file i mported

.. |image1| image:: ./media/159646652b5b0d41bd6bd955e61220a3.jpg
.. |image2| image:: ./media/693f76f5975fc256dbc1d2880c80edeb.png
.. |image3| image:: ./media/153c77edd571f12fce0e3282ab6fb530.png
.. |image4| image:: ./media/3a58be549e85e640654494c09f3a219f.png
.. |image5| image:: ./media/e774ae15dcb81968d9a2a553af57ac96.png
.. |image6| image:: ./media/ceb4cfa6c81ce3959cec504412767e39.png
.. |image7| image:: ./media/8bcfe24cd37e0e5accae1f94cf155640.png
.. |image8| image:: ./media/877beb7b3f5ccf7e5d849b7aaa8d661d.png
.. |image9| image:: ./media/c87475e50dd03a0d0d2dcf166f33a837.png
.. |image10| image:: ./media/cc52e57332beae056b2dc9cd7fdd1651.png
.. |image11| image:: ./media/d75042c926b6e89463ef41c47220cdcc.png
.. |image12| image:: ./media/62abaf11f6dfe7ba9d61b278bb7031b8.png
.. |image13| image:: ./media/c4adbdd1b2bf01cee8783ce659ac420f.png
.. |image14| image:: ./media/0da0b5ea4599202e02b009567d5120cf.png
.. |image15| image:: ./media/ce7538ad76100ce9f54d9f05870ba0ef.png
.. |Img| image:: ./media/img-20250512145240.png
.. |image16| image:: ./media/d271a92404720dbd8cf7c858732b7767.png
.. |image17| image:: ./media/img-20250512150224.png
.. |image18| image:: ./media/img-20250512150252.png
.. |image19| image:: ./media/img-20250512150313.png
.. |image20| image:: ./media/img-20250512150826.png
.. |image21| image:: ./media/f44f176de1d6415052e254f2b9327f29.png
.. |image22| image:: ./media/5576cc606f3d5f1b568a1316365698c9.png
.. |image23| image:: ./media/2be967cab8ae73fe0da29d41078f9450.png
.. |image24| image:: ./media/8c3f540a07aab97e1608ba8770837f7b.png
.. |image25| image:: ./media/528306ef33a9ace70c2708ded273a7b8.png
.. |image26| image:: ./media/59ab5cac1103b6688819290199cd7007.png
.. |image27| image:: ./media/6345d52d1ea149ba26de4f473b15d03a.png
.. |image28| image:: ./media/163f83acd2b1fffa1cfb7409736ecd48.png
.. |image29| image:: ./media/f00f946e1f194811b1c84725e0eb5d16.png
.. |image30| image:: ./media/18c70cf16dcf8c9694a1af8b12530cf9.png
.. |image31| image:: ./media/fee2f0f238a623c727b7a43418d97948.png
.. |image32| image:: ./media/b3617881628ec4860245d42668343769.png
.. |image33| image:: ./media/e4388c58829ba85568d1e054b0c8d233.png
.. |image34| image:: ./media/f8c25d32fdafcfa24d8df86bc63be25f.png
.. |image35| image:: ./media/448a50c26bc943e863e0cbf00f2e5677.png
.. |image36| image:: ./media/img-20250513134158.png
.. |image37| image:: ./media/img-20250513134324.png
.. |image38| image:: ./media/04fdfc9060943954e7938bb1a741d626.png
.. |image39| image:: ./media/04fdfc9060943954e7938bb1a741d626.png
.. |image40| image:: ./media/04fdfc9060943954e7938bb1a741d626.png
.. |image41| image:: ./media/04fdfc9060943954e7938bb1a741d626.png
.. |image42| image:: ./media/8c3f540a07aab97e1608ba8770837f7b.png
.. |image43| image:: ./media/41c834c1592b4ecbec3066082c25f10b.png
.. |image44| image:: ./media/6eea2059c73a5fc2b96ecdd5d56df806.png
.. |image45| image:: ./media/b8022e717770b105d50d87a40a1c67ea.png
.. |image46| image:: ./media/b53bb74cd132c97edb9a70b2a2190b4a.png
.. |image47| image:: ./media/img-20250513134324.png
.. |image48| image:: ./media/img-20250512155027.png
.. |image49| image:: ./media/8c3f540a07aab97e1608ba8770837f7b.png
.. |image50| image:: ./media/51a85130300778be775f923907b83214.png
.. |image51| image:: ./media/1fc05cf964a5d7927ec704c6b7f1acdd.png
.. |image52| image:: ./media/7f87636ae757d87584c8d5552e00c513.png
.. |image53| image:: ./media/img-20250513134324.png
.. |image54| image:: ./media/d4e278da768e447ed344d581e671f57a.png
.. |image55| image:: ./media/71fdb7b5d22c029a351e5cd323ea9a38.png
.. |image56| image:: ./media/4d2888634c7d86e2cb6186d8c50b7174.png
.. |image57| image:: ./media/98f588b6c1b4a2d3ef4efca3e7c030e6.png
.. |image58| image:: ./media/img-20250513134324.png
.. |image59| image:: ./media/d4e278da768e447ed344d581e671f57a.png
.. |image60| image:: ./media/9b18b2b8dfaa0533d8859d08ff12611e.png
.. |image61| image:: ./media/364f2e355d6c354155b2e6db80830a62.png
.. |image62| image:: ./media/fb3ba009a20245ab6076e537159a229c.png
.. |image63| image:: ./media/7ec21961398787ca5155f0648bbd82cc.png
.. |image64| image:: ./media/ced0bb410c8269205fe18554aa2c9926.png
.. |image65| image:: ./media/img-20250512155738.png
.. |image66| image:: ./media/06be84fb11b1fd07cd0cbb392132b903.png
.. |image67| image:: ./media/2ff75a1d81bfe0228b83931a0b7cc860.png
.. |image68| image:: ./media/d2a204e61c768f18924150db58aee093.png
.. |image69| image:: ./media/c38f71ee2b3fb1a405484e76c370f92d.png
.. |image70| image:: ./media/093160b7639ca86ad83ae4d7ea389871.png
.. |image71| image:: ./media/a2662ba8f13554b031daa944993f0fb1.png
.. |image72| image:: ./media/img-20250513134324.png
.. |image73| image:: ./media/6c6d92557229c8479f1005bd8093fa74.png
.. |image74| image:: ./media/94849305cba4d1cb307d2d73376f4e18.png
.. |image75| image:: ./media/1140fc004ffa65ecdf206193919f2f0f.png
.. |image76| image:: ./media/94849305cba4d1cb307d2d73376f4e18.png
.. |image77| image:: ./media/e1fe9b6dc1304cae9a190b55a8b22892.png
.. |image78| image:: ./media/94849305cba4d1cb307d2d73376f4e18.png
.. |image79| image:: ./media/img-20250513134324.png
.. |image80| image:: ./media/img-20250512160341.png
.. |image81| image:: ./media/img-20250512160416.png
.. |image82| image:: ./media/206c8ec1c3f11d2de8d0f42fdf5b6b47.png
.. |image83| image:: ./media/a6f5bc1877626a63ebf1b1c9f64f4002.png
.. |image84| image:: ./media/ebfabcefe31fd4f4093fd63e5d284ad9.png
.. |image85| image:: ./media/7eb957d5c7b39372af31a4b2bd264525.png
.. |image86| image:: ./media/img-20250513134324.png
.. |image87| image:: ./media/db5c433810c37c8d9f75a62ff99eb1e5.png
.. |image88| image:: ./media/45aefaf18e12a50acbf2299347ef741e.png
.. |image89| image:: ./media/de39f120be5bc9a7a0834bc4e3b5bc00.png
.. |image90| image:: ./media/2262cefaaa9143fc37ad6d53d6404b49.png
.. |image91| image:: ./media/img-20250513134324.png
.. |image92| image:: ./media/4b1765e12b413dc5d562f2a16d32392f.png
.. |image93| image:: ./media/f2705fbc4886efcfaac96589ca255f66.png
.. |image94| image:: ./media/img-20250512160908.png
.. |image95| image:: ./media/24c31bb0174e2ac672203e5c36c6875e.png
.. |image96| image:: ./media/560f0a2d84bd36e23acb99dbb01f836a.png
.. |image97| image:: ./media/c5cf34a6b570ed75af57634daf62796b.png
.. |image98| image:: ./media/d9bbfd110a525e5a43c76abd0a22f43b.png
.. |image99| image:: ./media/img-20250513134324.png
.. |image100| image:: ./media/acf3b8c0dee027d9e555fc708831f874.jpg
.. |image101| image:: ./media/55ad39536dff7bdf66379a1da7a4c137.png
.. |image102| image:: ./media/d1a4e9f62bdf690ba809ae35c347b233.png
.. |image103| image:: ./media/3cbda62783a32cf8e32d27e26ca754e2.png
.. |image104| image:: ./media/70cd7ec37561e9e2d512d2e9dd9166ca.png
.. |image105| image:: ./media/4de55e27643528af326ebf9cabe4054c.png
.. |image106| image:: ./media/img-20250513134324.png
.. |image107| image:: ./media/img-20250512163258.png
.. |image108| image:: ./media/24c31bb0174e2ac672203e5c36c6875e.png
.. |image109| image:: ./media/8a0749aabe41f2ef708b842c797da519.png
.. |image110| image:: ./media/d0a621d072f0be197fe69020da3c7f0c.png
.. |image111| image:: ./media/9e717d740c0fc72d7d064dcf1b68b51b.png
.. |image112| image:: ./media/img-20250513134324.png
.. |image113| image:: ./media/1600323e3e61e331c248cbeda5ccdcfc.jpg
.. |image114| image:: ./media/3be80acf957e53117f695801ce19c449.jpg
.. |image115| image:: ./media/5797dd7be9a9c2d3226123e0c29db0bd.jpg
.. |image116| image:: ./media/326095934bcff0a925b4f9a09d6cf7d2.jpg
.. |image117| image:: ./media/185b0ac204e9b2c54dd8fa93d852568c.jpg
.. |image118| image:: ./media/447206b1ac0a750d818c394f34008bca.png
.. |image119| image:: ./media/a481a470354fd3ebc573f621041ee9dd.png
.. |image120| image:: ./media/7ba7c6eb2373317f2de54eab3ddf0336.png
.. |image121| image:: ./media/img-20250513134324.png
.. |image122| image:: ./media/6d30d1f183087e759b85403b0bddcbbd.png
.. |image123| image:: ./media/6303a0ac122680207fe856d9be38d01c.png
.. |image124| image:: ./media/img-20250512164026.png
.. |image125| image:: ./media/img-20250512164040.png
.. |image126| image:: ./media/8c3f540a07aab97e1608ba8770837f7b.png
.. |image127| image:: ./media/19d950f9e45c8d59b5ef0bd12bdabd5f.png
.. |image128| image:: ./media/b19b1c95da181d658ce08532c6f75040.png
.. |image129| image:: ./media/ebcd15db1728149955b26857a0ae726f.png
.. |image130| image:: ./media/img-20250513134324.png
.. |image131| image:: ./media/0ec112824972ca026fcad43dc61aa5bc.png
.. |image132| image:: ./media/img-20250512164836.png
.. |image133| image:: ./media/ac515b9ae8891dc32f368a29f194a2fb.png
.. |image134| image:: ./media/813a25b97aa4abe3a0ed0389d7bab0ea.png
.. |image135| image:: ./media/23e333e566a34d9236571e7ef868eb71.png
.. |image136| image:: ./media/6a9eb140e75e4e837254b26fb1e9164b.png
.. |image137| image:: ./media/img-20250513134324.png
.. |image138| image:: ./media/img-20250512165225.png
.. |image139| image:: ./media/644695850097c5ade080bb4848b4b481.png
.. |image140| image:: ./media/c4031d7a41deaeee71cac6191eeaa45e.png
.. |image141| image:: ./media/171ad82abb6d81dc520c2cd75a21c4f7.png
.. |image142| image:: ./media/e631d635ef02b0bb96855437fd93913d.png
.. |image143| image:: ./media/img-20250513134324.png
.. |image144| image:: ./media/3073a8af772ab91ecf264843b37d3b74.png
.. |image145| image:: ./media/7f0741158e734ff8449d5b87d5ba85f4.png
.. |image146| image:: ./media/ab001da03963a768bb52f47a3fc11827.png
.. |image147| image:: ./media/56f1289435344510fe6bddacc8048d01.png
.. |image148| image:: ./media/8bd0888f9d83fe537e1d459be1c758f9.png
.. |image149| image:: ./media/img-20250513134324.png
.. |image150| image:: ./media/04fdfc9060943954e7938bb1a741d626.png
.. |image151| image:: ./media/f0e5a346c7f9442d28acc12485f70d3a.png
.. |image152| image:: ./media/579f51b2a0292d31d7ef4535e1b02155.png
.. |image153| image:: ./media/eacd0b4e2ba068ed3fc5d171cd8bfa3a.png
.. |image154| image:: ./media/img-20250513134324.png
.. |image155| image:: ./media/img-20250512170021.png
.. |image156| image:: ./media/e8f92efebfb955ca8a5f092f1eddce91.png
.. |image157| image:: ./media/81bfee2741c94f7e5cb7f8ec66b83945.jpg
.. |image158| image:: ./media/18c70cf16dcf8c9694a1af8b12530cf9.png
.. |image159| image:: ./media/823f061aa388150a575bca16cde3ac9f.png
.. |image160| image:: ./media/5c6d153e9e0bdf85b811618a9218b017.png
.. |image161| image:: ./media/df1d3cff8799373f8377383d79f450f5.png
.. |image162| image:: ./media/img-20250513134324.png
.. |image163| image:: ./media/img-20250512170309.png
.. |image164| image:: ./media/804e502bd0692ecb92e2f2ac16727bfc.png
.. |image165| image:: ./media/b26c1fad8aa10688ca88a957e6c51a29.png
.. |image166| image:: ./media/5c04135d614a9dabce0fd716fad6a11b.png
.. |image167| image:: ./media/863bb61bc88064b6fe7c7cc9621a401e.png
.. |image168| image:: ./media/ccfbfa562649017dd8ba9a78aa173022.png
.. |image169| image:: ./media/fa73a6dab71fa7327fdac64b8b83b5da.png
.. |image170| image:: ./media/img-20250513134324.png
.. |image171| image:: ./media/img-20250513084928.png
.. |image172| image:: ./media/eecf79fe278bc8107ce6827f9668f560.png
.. |image173| image:: ./media/8eb18c098e9fb43de8e4bc1d6bcbb998.png
.. |image174| image:: ./media/a9a509e976933b06b2fdaf8f47b21f9f.png
.. |image175| image:: ./media/02cfaa9a127b2757c4d3b9a76db06fb2.png
.. |image176| image:: ./media/d97b84ea891c1f77c96f13ff06336b5d.png
.. |image177| image:: ./media/8e632fcb718937b3b391df553a830950.png
.. |image178| image:: ./media/a3cdf397029f4625fffbb34c65d6e1c7.png
.. |image179| image:: ./media/e7ceadb386175c67dea8f22bc891fdea.png
.. |image180| image:: ./media/fb86ba2b7c59633c285d0cd2fc7d31c0.png
.. |image181| image:: ./media/9383aa73e392f24384c7fecaf9b58cd4.png
.. |image182| image:: ./media/648da100dfbc3c36e9e8e08a36ebeada.png
.. |image183| image:: ./media/8eb18c098e9fb43de8e4bc1d6bcbb998.png
.. |image184| image:: ./media/a9a509e976933b06b2fdaf8f47b21f9f.png
.. |image185| image:: ./media/02cfaa9a127b2757c4d3b9a76db06fb2.png
.. |image186| image:: ./media/d97b84ea891c1f77c96f13ff06336b5d.png
.. |image187| image:: ./media/8e632fcb718937b3b391df553a830950.png
.. |image188| image:: ./media/a3cdf397029f4625fffbb34c65d6e1c7.png
.. |image189| image:: ./media/e7ceadb386175c67dea8f22bc891fdea.png
.. |image190| image:: ./media/fb86ba2b7c59633c285d0cd2fc7d31c0.png
.. |image191| image:: ./media/9383aa73e392f24384c7fecaf9b58cd4.png
.. |image192| image:: ./media/648da100dfbc3c36e9e8e08a36ebeada.png
.. |image193| image:: ./media/8eb18c098e9fb43de8e4bc1d6bcbb998.png
.. |image194| image:: ./media/a9a509e976933b06b2fdaf8f47b21f9f.png
.. |image195| image:: ./media/02cfaa9a127b2757c4d3b9a76db06fb2.png
.. |image196| image:: ./media/d97b84ea891c1f77c96f13ff06336b5d.png
.. |image197| image:: ./media/8e632fcb718937b3b391df553a830950.png
.. |image198| image:: ./media/a3cdf397029f4625fffbb34c65d6e1c7.png
.. |image199| image:: ./media/e7ceadb386175c67dea8f22bc891fdea.png
.. |image200| image:: ./media/fb86ba2b7c59633c285d0cd2fc7d31c0.png
.. |image201| image:: ./media/9383aa73e392f24384c7fecaf9b58cd4.png
.. |image202| image:: ./media/648da100dfbc3c36e9e8e08a36ebeada.png
.. |image203| image:: ./media/8e4f35f0d0e814ddbef328c064f33242.png
.. |image204| image:: ./media/e867465fcb79419fe4b384b1dbaa7d1e.png
.. |image205| image:: ./media/img-20250513134324.png
.. |image206| image:: ./media/ab756f2a477de67e2e906904f1395940.png
.. |image207| image:: ./media/img-20250513134324.png
.. |image208| image:: ./media/5feb6bdf19d556ac2ab171175a1e406b.png
.. |image209| image:: ./media/img-20250513134324.png
.. |image210| image:: ./media/img-20250513085728.png
.. |image211| image:: ./media/6f0776b01b35f18b0568158ffbbc7a77.png
.. |image212| image:: ./media/69be958142b773acdae33eeef12afed7.png
.. |image213| image:: ./media/0982cb7b28f4accde7d378ba812c8bcb.png
.. |image214| image:: ./media/cdf4b1e2d82ed40e69fb3e4873b1373c.png
.. |image215| image:: ./media/img-20250513134324.png
.. |image216| image:: ./media/02a16adfdabb92d6de1796019e909b44.png
.. |image217| image:: ./media/232ea759b16ab27e7daff5da721c8e0c.jpg
.. |image218| image:: ./media/4919ce3b3fa299f13aa33348165ed728.png
.. |image219| image:: ./media/fbfa17f7fa922825bb7ec3d40643bdde.png
.. |image220| image:: ./media/47cdde6bceccc0678bf21d2904f15943.png
.. |image221| image:: ./media/49c4dfc3a1b1e0f73c2ad5908e50c2b9.png
.. |image222| image:: ./media/img-20250513134324.png
.. |image223| image:: ./media/f9322bc9c32a8bbca8f554e782304da4.png
.. |image224| image:: ./media/img-20250513134324.png
.. |image225| image:: ./media/img-20250513090853.png
.. |image226| image:: ./media/img-20250513090915.png
.. |image227| image:: ./media/ea7f6c8c87ab8a6aa921ad35f6569523.png
.. |image228| image:: ./media/f49e8c4d69ade7f6b49d5ca286100be6.png
.. |image229| image:: ./media/img-20250513134324.png
.. |image230| image:: ./media/98eb2994f993d836dcec9c6c8ff4e9fe.png
.. |image231| image:: ./media/img-20250513091339.png
.. |image232| image:: ./media/c1c066e5bd49cdae64140981097baefb.jpg
.. |image233| image:: ./media/img-20250513091511.png
.. |image234| image:: ./media/img-20250513091617.png
.. |image235| image:: ./media/73474b8d103ac0a640521572847333ac.png
.. |image236| image:: ./media/img-20250513134324.png
.. |image237| image:: ./media/img-20250513092316.png
.. |image238| image:: ./media/img-20250513092417.png
.. |image239| image:: ./media/9810ae67a9c903f3dff413e21fe2d585.jpg
.. |image240| image:: ./media/0180b169a1c3b228394b43df704fac32.png
.. |image241| image:: ./media/19b45a230fa57eba71f49206505b8f18.jpg
.. |image242| image:: ./media/8ff02741199a0f03d8d814a4b72f27d7.png
.. |image243| image:: ./media/a94935055ab9d2aee8a35b69ba1e322c.png
.. |image244| image:: ./media/img-20250513134324.png
.. |image245| image:: ./media/a4fd72297ae145f5b5eb0ac20821c791.png
.. |image246| image:: ./media/img-20250513092923.png
.. |image247| image:: ./media/d9926e9b70cbbb48efd07b0d0d2a1566.jpg
.. |image248| image:: ./media/img-20250513093037.png
.. |image249| image:: ./media/9196c878a727aca1eed63e22597f0113.png
.. |image250| image:: ./media/img-20250513134324.png
.. |image251| image:: ./media/img-20250513093456.png
.. |image252| image:: ./media/img-20250513093559.png
.. |image253| image:: ./media/aa2df8357e1b56db95e2c040541f79b7.jpg
.. |image254| image:: ./media/img-20250513093734.png
.. |image255| image:: ./media/1ffd142f4a857daeedca2ffbf3d752e4.png
.. |image256| image:: ./media/img-20250513134324.png
.. |image257| image:: ./media/img-20250513094058.png
.. |image258| image:: ./media/img-20250513094159.png
