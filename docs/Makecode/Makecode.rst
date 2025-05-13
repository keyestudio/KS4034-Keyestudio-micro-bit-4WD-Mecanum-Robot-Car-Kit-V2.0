Makecode Tutorial
=================

|image1|

Get Started with Makecode
-------------------------

The following instructions are applied for Windows system but can also
serve as a reference if you are using a different system.

Write code and program
~~~~~~~~~~~~~~~~~~~~~~

This chapter describes how to write program and load it to the Micro:
Bit main board V2.

Please browse the link for more details:
https://microbit.org/guide/quick/

**Step 1: Connect the Micro: Bit**

Firstly, link the Micro: Bit main board with your computer via the USB
cable. Macs, PCs, Chromebooks and Linux（including Raspberry Pi）systems
are all compatible with the Micro: Bit main board.

**Note that if you are about to pair the board with your phone or
tablet, please refer to this link:**
`https:/microbit.org/get-started/user-guide/mobile/ <https://microbit.org/get-started/user-guide/mobile/>`__

|image2|

|image3|

Secondly, if the red LED on the back of the board is on, that means the
board is powered. When your computer communicates with the main board
via the USB cable, the yellow LED on it will flashes. For example, it
will flicker when you burn a “.hex”file.

Then Micro: bit main board will display a driver named “MICROBIT(E:)”on
your computer. Please note that it is not an ordinary USB disk, as shown
below.

|image4|

**Step 2: Write programs**

Access the link：\ https://makecode.microbit.org/\ ，then click “\ **New
Project**\ ”, when the dialog box‘\ **Create a Project**\ ’ appears,
input‘\ **heartbeat**\ ’in it and click ‘\ **Create √**\ ’to edit.

(If you are running Windows 10 system, it is also viable to edit on the
Windows 10 APP, which is exactly like editing in the website.Link of the
Windows 10 APP: `Windows 10
APP <https://www.microsoft.com/zh-cn/p/makecode-for-micro-bit/9pjc7sv48lcx?ocid=badgep&rtc=1&activetab=pivot:overviewtab>`__)

|image5|

|image6|

Write a set of micro:bit code. You can drag some blocks from the modules
to the editing area and then run your program in Simulator of MakeCode
editor, as shown in the picture below, which demonstrates how to edit
‘\ **heartbeat**\ ’ program .

Here's a demo video(path):
``...\Important Resources\Makecode Code\Project 1：Heartbeat\heartbeat.mp4``.

|Img|

|image7|

Click “\ **JS JavaScript**\ ”，then we enable to find the corresponding
program in JavaScript language, as shown below:

|image8|

You also can click the“\ **JS JavaScript**\ ”and slide the button to
choose“\ **Python**\ ”and you will find the corresponding as shown
below:

|image9|

**Step 3: Download Code**

If your computer is Windows 10, you solely need to click the
‘\ **Download**\ ’ button to download the program to your micro: bit
main board.

If you are writing program through the website, following these steps:

Click the ‘\ **Download**\ ’ button in the editor to download a
"**.hex**" file, which can be read by the Micro: Bit main board. Once
the hexadecimal file is downloaded, copy it to your board just like the
process that you copy the file to the USB driver. If you are running
Windows system, you can also right-click and select ‘\ **Send to →
MICROBIT(E:)**\ ’ to copy the hex file to the Micro: Bit main board.

|image10|

|image11|

You can also directly drag the "**.hex**" file onto the MICROBIT (E:)
disk.

|image12|

|image13|

During the process of copying the downloaded hex file to the Micro: bit
main board, the yellow signal light on the back side of the board
flashes. When the copy is completed, the yellow signal light will stop
flashing and remain on.

**Step 4: Run the program**

After the program is uploaded to the Micro: bit main board, you could
still power it via an USB cable or an external power. The 5 x 5 LED dot
matrix on the board displays the heartbeat pattern.

|image14|

Power via USB cable

|image15|

Power via external power（3V）

**Caution:**

When programming, the MICROBIT driver will automatically eject and
return and your hexadecimal files will disappear. And the board can only
have access to hexadecimal files (.hex) and won’t save other files.

**Step5：Other programming languages**

Go to the link: ：\ https://microbit.org/code/ for different programming
languages .

Makecode
~~~~~~~~

Access the link：\ https://makecode.microbit.org/\ ，and enter the
online editor of makecode or open the APP makecode for micro:bit Windows
10.

|image16|

Click“\ **New Project**\ ”, and input“\ **heartbeat**\ ”in the dialog
box, then click “\ **create √**\ ”to enter Makecode editor, as shown
below:

|image17|

There are blocks“\ **on start**\ ”and“\ **forever**\ ”in the code
editing area.

When the power is plugged or reset,“\ **on start**\ ”means that the code
in the block only executes once, while“\ **forever**\ ”implies that the
code runs cyclically.

Quick Download
~~~~~~~~~~~~~~

As mentioned before, if your computer is Windows 10 and you have
downloaded the MakeCode APP for micro:bit, then the code can be quickly
downloaded to the Micro: Bit main board by
clicking‘\ **Download**\ ’button.

While it is a little more trickier if you are using a browser to enter
Makecode. However, if you use Google Chrome for
Android，ChromeOS，Linux，macOS and Windows 10, the process can be
quicker too.

We use the webUSB function of Chrome to access the micro USB hardware
device.

You could refer to the following steps to connect and pair devices.

**Device pairing:**

Connect micro:bit to your computer by USB cable.

Click“\ **...**\ ”beside to“\ **Download**\ ”and tap“\ **Connect
device**\ ”;

|image18|

Click“\ **Next**\ ”;

|image19|

Click“\ **Next**\ ”again

|image20|

Then select the corresponding device and click“\ **Connect**\ ”. If no
device shows up for selection, please refer to the link:
https://makecode.microbit.org/device/usb/webusb/troubleshoot

And for updating the firmware of the Micro:bit:
https://microbit.org/guide/firmware/ .

|image21|

Click“\ **Done**\ ”to finish the pairing.

|image22|

|image23|

**Download Program:**

After pairing, click “download”to directly download the program to the
board. If it is successfully downloaded, the icon |image24| will shift
to |image25|.

|image26|

Makecode Extension Libraries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We have made a makecode extension library for this Mecanum robot car
V2.0

Add an extension library of the Mecanum robot car V2.0

Please follow the following steps to add extension files:

Open Makecode to enter a certain project → click the gear-shaped
icon(for setting) in the upper right corner →
choose“\ **Extensions**\ ”;

|image27|

Or click“\ **Extensions**\ ”, as shown below:

|image28|

Input the link
``https://github.com/keyestudio2019/mecanum_robot _v2.git`` to search;

Tap the searching result “\ **MecanumRobotV2**\ ” to download and
install it, This process may take a few seconds.

|image29|

After the installation, you can find the extension files **Mecanum
RobotV2** and **IrRemote** on the left side.

And extension file Neopixel is also installed.

|image30|

|image31|

|image32|

**Note:** The extension files added are only available for this project.
Therefore, when you create a new **MecanumRobotV2** project, you will
need to add these extension files again.

**Update or delete the MecanumRobotV2 extension files:**

Please follow the following steps to update or delete extension files:

Click "Js JavaScript" to change to textual version:

|image33|

Click the “\ **Explorer**\ ” on the left side:

|image34|

You can find these added files in the list;

Click the dustbin icon beside the file to delete the MecanumRobotV2 file
and tap the refresh icon to update it.

|image35|

Import test code
~~~~~~~~~~~~~~~~

We provide hexadecimal code files (project files) for each project. The
file contains all the contents of the project and can be imported
directly, and you can manually drag the code blocks to complete the
program.

For simple projects, dragging a block of code to complete the program is
recommended. For complex projects, it is recommended to conduct the
program by importing the provided hexadecimal code file.

Let's take the "**Heatbeat**" project as an example to show how to load
the code.

Open the Web version of Makecode or the Windows 10 App version of
Makecode then click “\ **Import**\ ”.

|image36|

Click“\ **Import File**\ ”;

|image37|

|image38|

Select
``..\Important Resources\Makecode Code\Project 1：Heartbeat\Project 1: Heart beat.hex``
, then click“\ **Go ahead**\ ”.

|image39|

|image40|

In addition to importing the provided test code file into the Makecode
compiler above, you can also drag them to the code editing area of the
Makecode compiler, as shown in the figure below:

|image41|

After a few seconds, it has done.

|image42|

**Note:** If your computer system is’t Windows 10, the pairing cannot be
done via Google Chrome. Therefore, digital or analog signals of sensors
and modules cannot be read. However, we can use the CoolTerm software to
read the serial port data. Next chapter is about how to install the
CoolTerm.

Install CoolTerm
~~~~~~~~~~~~~~~~

CoolTerm program is used to read the data on serial port.

Download CoolTerm program: https://freeware.the-meiers.org/

After downloading, we need to install CoolTerm program file, and we take
PC Window system as an example.

1) Choose “\ **win**\ ” to download the zip file of CoolTerm

2) Unzip the file and open it. (also suitable for Mac and Linux system)

|image43|

|image44|

3) Double-click\ |image45|.（Please make sure that the driver of
   Micro:bit is installed and the main board is connected to the
   computer.)

|image46|

The functions of each button on the Toolbar are listed below:

|image47|

========= ================================================
|image48| Opens up a new Terminal
|image49| Opens a saved Connection
|image50| Saves the current Connection to disk
|image51| Opens the Serial Connection
|image52| Closes the Serial Connection
|image53| Clears the Received Data
|image54| Opens the Connection Options Dialog
|image55| Displays the Terminal Data in Hexadecimal Format
|image56| Displays the Help Window
========= ================================================

Projects
--------

(**Note:** project 8.1 to 8.12 are basic courses conducted with the
built-in sensors and LED dot matrix of the Micro:bit main board V2,
while project 8.13 to 8.20 are extended courses)

Project 1：Heart beat
~~~~~~~~~~~~~~~~~~~~~

|image57|

1. **Description**

This project is easy to conduct solely with a micro:bit main board, a
micro USB cable and a computer. The micro:bit will display a “flickering
heart” pattern. This experiment serves as a starter for your to entry to
the magical world of the micro:bit.

2. **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the Web version of Makecode and Click “New Project” into the
code editing interface of Makecode.

|image58|

3. **Test Code**

|image59|

Click“JavaScript" to view the corresponding JavaScript code:

|image60|

4. **Test Result**

Download code to micro:bit and keep the USB cable connected. The LED dot
matrix will display ❤ and |image61| ceaselessly.

If the download is not success, try to disconnect the micro:bit from
your computer and then reconnect them and reopen Makecode to try again.

Project 2：Light A Single LED
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image62|

1. **Description**

The LED dot matrix consists of 25 diodes arranged in a 5 by 5 square and
placed at the intersection of row lines (X) and column lines (Y). We can
control one of the 25 LEDs by setting coordinate points. For example,
the first LED sits in the first line is (0,0）and the third LED
positioned in the first line is (2,0）and others likewise.

|image63|

2. **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the Web version of Makecode and Click “New Project” into the
code editing interface of Makecode.

|image64|

3. **Test Code**

|image65|

Click“JavaScript”to switch into corresponding JavaScript code:

|image66|

4. **Test Result**

After uploading the test code to micro:bit main board V2 and powering it
via the USB cable, the LED in (1,0) lights up for 0.5s and the one in
(3,4) shines for 0.5s and repeat this sequence.

Project 3：5 x 5 LED Dot Matrix
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image67|

1. **Description**

Dot matrix is very commonplace in daily life, which has found wide
applications in LED advertisement screens, elevator floor display, bus
stop announcement and so on.

The LED dot matrix of Micro: Bit main board contains 25 Diodes.
Previously, we have succeeded in controlling a certain LED via its
position point. Supported by the same theory, we can turn on many LEDs
at the same time to showcase patterns, digits and characters.

What’s more, we can also click”show icon“ to choose the pattern we like
to display. Last but not the least, we can design patterns by ourselves
as well.

2. **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the Web version of Makecode.

3. **Test Code**

**Test Code1：**

|image68|

Select“JavaScript”to switch into JavaScript language code:

|image69|

**Test Code 2：**

|image70|

Select“JavaScript”to switch into JavaScript language code:

|image71|

4. **Test Result**

Upload code 1 and power the board , we will see the icon\ |image72|

Upload code 2 and plug micro:bit in power, Micro: bit starts showing
number 1, 2, 3, 4, and 5, then cyclically
display\ |image73|,“Hello!”,\ |image74|,\ |image75|,\ |image76|,\ |image77|
and\ |image78|\ patterns.

Project 4：Programmable Buttons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image79|

1. **Description**

|image80|

Buttons can be used to control circuits. In an integrated circuit with a
push button, the circuit is connected when pressing the button and but
after release, it will break again. 

Both ends of the button like two mountains. There is a river in between.

The internal metal piece connect the two sides to let the current pass,
just like building a bridge to connect two mountains.

The internal structure of the button is shown as follows: before
pressing the button, 1 ,2 , 3 and 4 are turned on. However, 1, 3 or 1, 4
or 2, 3 or 2 and 4 are disconnected, which is only enabled when the
button is pressed. |image81|

Micro: Bit main board boasts three push buttons, two are programmable
buttons(marked with A and B), and the one on the other side is a reset
button. By pressing the two programmable buttons can input three
different signals. We can press button A or B alone or press them
together and the LED dot matrix shows A,B and AB respectively. Let’s get
started.

2. **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the Web version of Makecode.

3. **Test Code1**

Press buttons on micro:bit, micro:bit will display character strings.

|image82|

Select“JavaScript”to switch into JavaScript language code:

|image83|

4. **Test Result1**

After uploading test code 1 to micro:bit main board V2 and powering the
board via the USB cable, the 5*5 LED dot matrix shows A if button A is
pressed, B if button B pressed, and AB if button A and B are pressed
together.

5. **Test Code2**

|image84|

Click“JavaScript”to switch into JavaScript code:

|image85|

6. **Test Result2**

After uploading test code 2 to micro:bit main board V2 and powering the
board via the USB cable, when pressing the button A , the LEDs turning
red increase by 5 , while when pressing the button B the LEDs turning
red reduce.

Project 5：Temperature Measurement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

**Note:** the temperature sensor of Micro:bit main board is shown below:

|image86|

2. **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the Web version of Makecode.

3. **Test Code1**

Micro:bit detects temperature

|image87|

Click“JavaScript”to view the corresponding JavaScript code:

|image88|

4. **Test Result1**

Download code 1 to micro:bit board and keep USB cable connected, then
tap the button |image89|:

|image90|

Temperature data is shown below:

|image91|

Through the test, the room temperature is 35℃when touching the NFR51822
chip of micro:bit; however, the temperature rises to 37℃ when it touches
water cup.

If you're running Windows 7 or 8 instead of Windows 10, it won't be able
to match devices via Google Chrome. You'll need to use the CoolTerm
serial monitor software to read data.

You could open CoolTerm, click Options to select SerialPort. Set COM
port and 115200 baud rate(the baud rate of USB serial communication of
Micro:bit is 115200 through the test). Click“OK”and“Connect”.

The serial monitor shows the current ambient temperature value, as shown
below:

|image92|

|image93|

|image94|

|image95|

5. **Test Code2**

Micro:bit display different pictures by temperature(the temperature
value in the code could be adjusted).

|image96|

Click“JavaScript”, the corresponding JavaScript code is shown below:

|image97|

6. **Test Result2**

Upload the Code 2 and plug in power. And the 5*5 LED displays the
ambient temperature. When pressing the temperature sensor, the
temperature will grow on dot matrix. When the ambient temperature is
less than 35℃, the 5*5LED will show\ |image98|. When the temperature is
equivalent to or greater than 35℃, the pattern\ |image99| will appear.

Project 6：Geomagnetic Sensor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image100|

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
detection and compass blocks.

Then we could read the value detected by it to determine the location.
We need to calibrate the micro:bit board when the magnetic sensor works.
The correct calibration method is to rotate the micro:bit board.

In addition, the objects nearby may affect the accuracy of readings and
calibration.

2. **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the Web version of Makecode.

3. **Test Code1**

Press A on micro:bit, the value of compass is shown.

|image101|

Select“JavaScript”to switch into JavaScript language code:

|image102|

4. **Test Result1**

Upload the code 1, plug in micro:bit via an USB cable.

After uploading the test code1 to the micro:bit main board and powering
the board via an USB cable, and the LED dot matrix shows “TILT TO FILL
SCREEN”. Pressing the button A, the board asks us to calibrate the
compass. Then enter the calibration page. Rotate the board until all 25
red LEDs are on, as shown below.

|image103|

The calibration will be finished until you view the smile
pattern\ |image104|\ appear.

The serial monitor will show 0°, 90°, 180° and 270° when pressing A.

5. **Test Code2**

|image105|

This module can keep reading data to determine direction, and let arrow
point to the current magnetic North Pole.

|image106|

For the above picture, the arrow will point to the upper right when the
value ranges from 292.5 to 337.5. Because 0.5 can’t be input in the
code, the values we get are 293 and 338.

Make micro: bit board point to the north, south, east and west
horizontally , LED dot matrix displays the corresponding direction
patterns

|image107|

|image108|

|image109|

|image110|

Select“JavaScript”to switch into JavaScript language code:

|image111|

|image112|

6. **Test Result2**

Upload code 2 and plug micro:bit into power. After calibration, tilt the
micro:bit board, and the LED dot matrix displays the direction signs.

Project 7：Accelerometer
~~~~~~~~~~~~~~~~~~~~~~~~

|image113|

1. **Description**

The micro:bit board has a built-in Freescale MMA8653FC three-axis
acceleration sensor (accelerometer). Its I2C interface works on external
communication, the range can be set to ±2g, ±4g, and ±8g, and the
maximum data update rate can reach 800Hz.

When the Micro:bit is stationary or moving at a constant speed, the
accelerometer only detects the gravitational acceleration; when the
Micro:bit is slightly shaken, the acceleration detected is much smaller
than the gravitational acceleration and can be ignored. Therefore, in
the process of using Micro:bit, the main purpose is to detect the
changes of the gravitational acceleration on the x, y, and z axes when
the attitude changes.

For this project, we will introduce the detection of several special
postures by the accelerometer.

2. **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the Web version of Makecode.

3. **Test Code1**

|image114|

|image115|

Click“JavaScript", you will view the corresponding JavaScript code:

|image116|

4. **Test Result1**

After uploading the test code 1 to micro:bit main board V2 and powering
the board via the USB cable, if we shake the Micro: Bit main board V2,
no matter at any direction, the LED dot matrix displays the digit “1”.

When it is kept upright （make its logo above the LED dot matrix）, the
number 2 shows.

|image117|

When it is kept upside down( make its logo below the LED dot matrix) ,
it shows as below.

|image118|

When it is placed still on the desk, showing its front side, the number
4 appears.

When it is placed still on the desk, showing its back side, the number 5
exhibits.

When the board is tilted to the left , the LED dot matrix shows the
number 6, as shown below.

|image119|

When the board is tilted to the right , the LED dot matrix displays the
number 7, as shown below:

|image120|

When the board is knocked to the floor, this process can be considered
as a free fall and the LED dot matrix shows the number 8. (Please note
that this test is not recommended for it may damage the main board.)

**Attention:** if you’d like to try this function, you can also set the
acceleration to 3g, 6g or 8g.

5. **Test Code2**

Detect the value of acceleration speed at x, y and z axis

|image121|

Click“JavaScript" to view the corresponding JavaScript code:

|image122|

6. **Test Result2**

Download code 2 to micro:bit board, keep USB cable connected and
click\ |image123|

|image124|

After referring to the MMA8653FC data manual and the hardware schematic
diagram of the Micro: Bit main board V2, the accelerometer coordinate of
the Micro: Bit V2 motherboard are shown in the figure below:

The following interface shows the decomposition value of acceleration in
X axis, Y axis and Z axis respectively, as well as acceleration
synthesis (acceleration synthesis of gravity and other external forces).

|image125|

|image126|

If you're running Windows 7 or 8 instead of Windows 10, it won't be able
to match devices via Google Chrome. You'll need to use the CoolTerm
serial monitor software to read data.

You could open CoolTerm software, click Options, select SerialPort, set
COM port and put baud rate to 115200 (after testing, the baud rate of
USB SerialPort communication on Micro: Bit main board V2 is 115200),
click OK, and Connect. The CoolTerm serial monitor shows the data of X
axis, Y axis and Z axis , as shown in the figures below :

|image127|

Project 8：Light Detection
~~~~~~~~~~~~~~~~~~~~~~~~~~

|image128|

1. **Description**

In this project, we focus on the light detection function of the Micro:
Bit main board V2. It is achieved by the LED dot matrix since the main
board is not equipped with a photoresistor.

When the light irradiates the LED matrix, the voltage change will be
produced. Therefore, we could determine the light intensity by voltage
change.

2. **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the Web version of Makecode.

3. **Test Code**

|image129|

Click“JavaScript”to switch into the corresponding JavaScript code:

|image130|

4. **Test Result**

Download code to micro:bit board don’t plug off the USB cable and
click\ |image131|

|image132|

The intensity value is 0 when covering the LED dot matrix. And the value
varies with the light intensity. When placing micro:bit under the
sunlight, the stronger the light is, the larger the intensity value will
be. As shown below:

|image133|

If you're running Windows 7 or 8 instead of Windows 10, it won't be able
to match devices via Google Chrome. You'll need to use the CoolTerm
serial monitor software to read data.

You could open“CoolTerm”, click“Options”to select “SerialPort”, and set
“COM” port and 115200 baud rate(the baud rate of USB serial
communication of micro:bit is 115200 through the test).

Then click“OK”and“Connect”. The light intensity value is shown below:

|image134|

Project 9：Speaker
~~~~~~~~~~~~~~~~~~

|image135|

1. **Description**

Micro: Bit main board has an built-in speaker, which makes adding sound
to the programs easier. It can also be programmed to produce all kinds
of tones, like playing the song *Ode to Joy*.

2. **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the Web version of Makecode.

3. **Test Code**

|image136|

Select “JavaScript” to switch into JavaScript language code:

|image137|

4. **Test Result**

After uploading the test code to micro:bit main board V2 and powering
the board via the USB cable, the speaker utters sound and the LED dot
matrix shows the logo of music.

Project 10：Touch-sensitive Logo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image138|

1. **Description**

The Micro: Bit main board V2 is equipped with a golden touch-sensitive
logo, which can act as an input component like an button.

It contains a capacitive touch sensor that senses small changes in the
electric field when pressed (or touched), just like your phone or tablet
screen. When you press it , the program can be activated.

2. **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the Web version of Makecode.

3. **Test Code**

|image139|

Select“JavaScript" and“Python”to switch into JavaScript and Python
language code:

|image140|

|image141|

4. **Test Result**

via the USB cable, the LED dot matrix exhibits the“❤” pattern when the
touch-sensitive logo is pressed or touched and displays digit when the
logo is released.

Project 11：Microphone
~~~~~~~~~~~~~~~~~~~~~~

|image142|

|image143|

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

B. Open the Web version of Makecode.

3. **Test Code1**

|image144|

Select“JavaScript”to switch into JavaScript language code:

|image145|

4. **Test Results 1**

After uploading test code1 to micro:bit main board V2 and powering the
board via the USB cable, the LED dot matrix displays pattern“❤””when you
claps and pattern\ |image146|\ when it is quiet around.

5. **Test Code2**

|image147|

Select“JavaScript”to switch into JavaScript language code:

|image148|

6. **Test Results 2**

Upload test code 2 to micro:bit main board V2, power the board via the
USB cable and click “Show console Device”as shown below.

|image149|

When the sound is louder around, the sound value shows in the serial
port is bigger as shown below.

|image150|

What’s more, when pressing the button A, the LED dot matrix displays the
value of the biggest volume( please note that the biggest volume can be
reset via the Reset button on the other side of the board ) while when
clapping, the LED dot matrix shows the pattern of the sound.

Project 12：Bluetooth Wireless Communication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image151|

1. **Description**

The Micro: Bit main board V2 comes with a nRF52833 processor (with a
built-in BLE(Bluetooth Low Energy) device Bluetooth 5.1 ) and a 2.4GHz
antenna for Bluetooth wireless communication and 2.4GHz wireless
communication. With the help of them, the board is able to communicate
with a variety of Bluetooth devices, including smart phones and tablets.

In this project, we mainly concentrate on the Bluetooth wireless
communication functions of this main board. Linked with Bluetooth, it
can transmit code or signals. To this end, we should connect an Apple
device (a phone or an iPad) to the board.

Since setting up Android phones to achieve wireless transmission is
similar to that of Apple devices, so we don’t need to illustrate again.

2. **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. IPhone device (phone /iPad) or Android phone.

3. **Procedures**

For Apple devices, enter this link:
https://www.microbit.org/get-started/user-guide/ble-ios/ with your
computer first, and then click “Download pairing HEX file”to download
the Micro: Bit firmware to a folder or desk, and upload the downloaded
firmware to the Micro: Bit main board V2.

|image152|

|image153|

|image154|

Open\ |image155|\ to search “micro bit”in your App Store to download the
APP micro:bit then click“\ |image156|\ ”.

|image157|

Connect your Apple device with Micro: Bit main board V2:

Firstly, turn on the Bluetooth of your Apple device and open the APP
micro:bit to select item “Choose micro:bit”to start pairing Bluetooth.

Please make sure that the Micro: Bit main board V2 and your computer are
still linked via the USB cable.

|image158|

Secondly, click“Pair a new micro:bit”;

|image159|

Following the instructions to press button A and B at the same time(do
not release them until you are told to) and press Reset & Power button
for a few seconds.

Release the Reset & Power button, you will see a password pattern shows
on the LED dot matrix. Now , release buttons A and B and click Next.

|image160|

|image161|

Set the password pattern on your Apple device as the same pattern showed
on the matrix and click Next.

|image162|

Still click Next and a dialog box props up as shown below. Then click
"Pair". A few seconds later, the match is done and the LED dot matrix
displays the "√" pattern.

|image163|\ |image164|

|image165|\ |image166|

After the match with Bluetooth, write and upload code with the App.

Click “Create Code” to enter the programming page and write code.

Click\ |image167|\ and the box\ |image168|\ appears, and then select
“Create √”.

|image169|

|image170|

|image171|

|image172|

Name the code as “1 “and click\ |image173| to save it.

|image174|

Click the third item“Flash”to enter the uploading page.  The default
code program for uploading is the one saved just now and named "1" and
then click the other "Flash" to upload the code program "1".

|image175|

|image176|

|image177|

If the code is uploaded successfully a few seconds later, the App will
emerge as below and the LED dot matrix of the Micro: Bit main board V2
will exhibit a heart pattern.

|image178|

**Projects above all conduct with the built-in sensors and the LED dot
matrix of the main board while the following ones will carry out with
the help of external sensors of this turtle car.（Attention：In order to
avoid burning the the Micro:bit main board V2, please remove the USB
cable and the external power from the board before fix it with the
shield of the car; likewise, the USB cable and the external power should
be cut from the main board before disconnect the shield from the
board.)**

Project 13：Seven-Color LED
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image179|

1. **Description**

This module consists of a commonly used LED with 7colors but in white
appearance. It can automatically flash different colors to create
fantastic light effects when high level is input like a normal LED.

2. **Preparation**

- Insert the micro:bit board into the slot of keyestudio
  4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the Web version of Makecode.

3. **Test Code1**

Make the RGB light flash 7 lights alternatively.

|image180|

Click“JavaScript”to view the corresponding JavaScript code:

|image181|

4. **Test Result1**

Download code 1 to micro:bit board and dial POWER switch to ON end, 2
RGB lights of smart car emit red, green, blue, indigo, dark red, yellow
and white color cyclically.

5. **Test Code2**

|image182|

Click“JavaScript”to view the corresponding JavaScript code:

|image183|

5. **Test Result2**

Download code 2 to micro:bit board, 2 RGB lights will flash for 1 second
and then stop flashing for 1 second, cyclically.

Project 14：4 WS2812 RGB LEDs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image184|

1. **Description**

The driver shield cooperates 4 pcs WS2812 RGB LEDs, compatible with
micro:bit board and controlled by P7. In this lesson, we will make the
RGB LEDs display different colors by P7. In this lesson, 3 sets of test
code are provided to make the 4 WS2812 RGB LEDs display different
effects.

2. **Preparation**

- Insert the micro:bit board into the slot of keyestudio
  4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the Web version of Makecode.

3. **Test Code1**

|image185|

Click“JavaScript" to switch into the corresponding JavaScript code:

|image186|

4. **Test Result1**

Download code 1 to micro：bit, and dial POWER to ON end. All four
WS2812RGB LEDs light up a different color a time cyclically.

5. **Test Code2**

|image187|

|image188|

|image189|

Click“JavaScript" to switch into the corresponding JavaScript code:

|image190|

|image191|

6. **Test Result2**

Download code 2 to micro：bit, WS2812RGB LEDs display like flow light.

7. **Test Code3**

|image192|

Click“JavaScript”to switch into the corresponding JavaScript code:

|image193|

8. **Test Result3**

Download code 3 to micro：bit, every WS2812RGB light shows random color
one by one.

Project 15：Servo
~~~~~~~~~~~~~~~~~

|image194|

1. **Description**

For those DIY smart cars, they often have the function of automatic
obstacle avoidance. In the DIY process, we need to use a servo to
control the ultrasonic module to rotate left and right, and then detect
the distance between the car and the obstacle, so as to control the car
to avoid the obstacle. If other microcontrollers are used to control the
rotation of the servo, we need to set a certain frequency and a certain
width of pulse to control the servo angle.

However, if the micro:bit main board is used to control the servo angle,
we only need to set the control angle in the development environment
where the corresponding pulse will be automatically set to control the
servo rotation. In this project, you will learn how to control the servo
to rotate back and forth between 0° and 90°.

2. **Information of the Servo**

Servo motor is a position control rotary actuator. It mainly consists of
housing, circuit board, core-less motor, gear and position sensor. Its
working principle is that the servo receives the signal sent by MCU or
receiver, and produces a reference signal with a period of 20ms and
width of 1.5ms, then compares the acquired DC bias voltage to the
voltage of the potentiometer and obtains the voltage difference output.

|image195|

For the servo used in this project, the brown wire is the ground, the
red one is the positive wire, and the orange one is the signal wire.

The rotation angle of servo motor is controlled by regulating the duty
cycle of PWM (Pulse-Width Modulation) signal. The standard cycle of PWM
signal is 20ms (50Hz). Theoretically, the width is distributed
between 1ms-2ms, but in fact, it's between 0.5ms-2.5ms. The width
corresponds to the rotation angle from 0° to 180°. But note that for
different brand motor, the same signal may have different rotation
angle. 

|image196|

More details:

|image197|

3. **Parameters**

- Working voltage: DC 4.8V ~ 6V

- Operating angle range: about 180 ° (at 500 → 2500 μsec)

- Pulse width range: 500 → 2500 μsec

- No-load speed: 0.12 ± 0.01 sec / 60 (DC 4.8V) 0.1 ± 0.01 sec / 60 (DC
  6V)

- No-load current: 200 ± 20mA (DC 4.8V) 220 ± 20mA (DC 6V)

- Stopping torque: 1.3 ± 0.01kg · cm (DC 4.8V) 1.5 ± 0.1kg · cm (DC 6V)

- Stop current: ≦ 850mA (DC 4.8V) ≦ 1000mA (DC 6V)

- Standby current: 3 ± 1mA (DC 4.8V) 4 ± 1mA (DC 6V)

4. **Preparation**

- Insert the micro:bit board into the slot of keyestudio
  4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the Web version of Makecode

5. **Test Code**

|image198|

Click“JavaScript" to view the corresponding JavaScript code: ：

|image199|

6. **Test Result**

After uploading the test code and dial POWER switch to ON end, the servo
rotates from 0 degree to 180 degrees.

Project 16：Motor
~~~~~~~~~~~~~~~~~

|image200|

1. **Description**

The Keyestudio 4WD Mecanum Robot Car is equipped with 4 DC reduction
motors, also called gear reduction motor, which is developed on the
ordinary DC motor. It has a matching gear reduction box which provides a
lower speed but a larger torque. Furthermore, different reduction ratios
of the box can provide different speeds and torques.

Gear motor is the integration of gearmotor and motor, which is applied
widely in steel and machine industry

Micro:bit motor driver shield comes with a DRV8833 chip. In order to
save the IO port resource, we control the rotation direction and speed
of 4 DC gear motors with the DRV8833 chip.

|image201|

Front

|image202|

Back

|image203|

STC8G1K08 Chip circuit

|image204|

HR8833 Motor driver circuit

2. **Preparation**

- Insert the micro:bit board into the slot of keyestudio
  4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the Web version of Makecode

3. **Test Code1**

|image205|

Click“JavaScript" to view the corresponding JavaScript code: ：

|image206|

4. **Test Result1**

Download code 1 to micro:bit board, dial POWER switch to ON end. Smart
car goes forward for 2s and stops for 2s.

5. **Test Code2**

|image207|

Click“JavaScript" to view the corresponding JavaScript code: ：

|image208|

6. **Test Result2**

Download code 2 to micro:bit board, the car goes forward for 2s, turns
back for 2s, turn left for 2s, turn right for 2s and stops for 2s and
repeats this pattern.

Project 17：Line Tracking Sensor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _project-171detect-line-tracking-sensor:

Project 17.1：Detect Line Tracking Sensor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|image209|

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

After putting a white paper on the bottom of the 4WD Mecanum Robot Car,
we will rotate the potentiometers on the 3-way tracking sensor. When the
indicator light on the sensor module is on, pick up the car to make the
two wheels on the 4WD Mecanum Robot Car separate. The height of the
white paper is about 1.5cm, when the indicator light on the sensor
module is off, and then the sensitivity is adjusted.

3. **Preparation**

- Insert the micro:bit board into the slot of keyestudio
  4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the Web version of Makecode

4. **Test Code**

|image210|

Click“JavaScript" to view the corresponding JavaScript code: ：

|image211|

5. **Test Result**

Download code to micro:bit board, dial POWER switch to ON end.

Open CoolTerm, click Options to select SerialPort. Set COM port and
115200 baud rate. Click“OK”and“Connect”.

|image212|

|image213|

|image214|

|image215|

The CoolTerm serial monitor displays the digital signals read by the
line tracking sensors.

|image216|

.. _project-172tracking-smart-car:

Project 17.2：Tracking Smart Car
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|image217|

1. **Description**

In this lesson we will combine a line tracking sensor with a motor to
make a line tracking smart car.

The micro:bit board will analyze the signals and control the smart car
to show the line tracking function.

2. **Working Principle**

The smart car will make different moves according to the value received
by the 3-channel line tracking sensor.

|image218|

3. **Preparation**

- Insert the micro:bit board into the slot of keyestudio
  4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the Web version of Makecode

**Warning:** The 3-way tracking sensor should be used in environments
without infrared interference such as sunlight. Sunlight contains a lot
of invisible light, such as infrared and ultraviolet. In an environment
with strong sunlight, the 3-way tracking sensor cannot work properly.

4.\ **Flow Chart**

|image219|

5. **Test Code**

|image220|

Click“JavaScript”to view the corresponding JavaScript code:

|image221|

|image222|

5. **Test Result**

Download code to micro:bit and dial POWER to ON end, line tacking car
goes forward along black line .

**Note:** turn on the switch at the back of micro:bit car, the width of
black line should be larger than the width of line tracking sensor.

Avoid to test smart car under the strong light.

Project 18：Ultrasonic Sensor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _project-181ultrasonic-ranging:

Project 18.1：Ultrasonic Ranging
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. **Description**

The ultrasonic sensor uses sonar to determine distance to an object like
bats do. It offers excellent non-contact range detection with high
accuracy and stable readings in an easy-to-use package. It comes
complete with ultrasonic transmitter and receiver modules.

The ultrasonic sensor is being used in a wide range of electronics
projects for creating obstacle detection and distance measuring
application as well as various other applications.

|image223|

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

|image224|

2. **Working Principle**

|image225|

(1)Pull down TRIG then trigger high level signals with least 10us;

(2)After triggering, the module will automatically send eight 40KHz
ultrasonic pulses and detect whether there is a signal return;

(3)If there is a signal return, when ECHO (E) outputs a high level, then
the duration of the high level is the time from transmission to
reception of the ultrasonic waves. Then test distance = high level
duration \*340m/s*0.5. 

3. **Parameters**

- Working voltage: 3-5.5V (DC)

- Working current: 15mA

- Working frequency: 40khz

- Maximum detection distance: about 3m

- Minimum detection distance: 2-3cm

- Precision: up to 0.2cm

- Sensing angle: less than 15 degrees

- Input trigger pulse: 10us TTL level

- Output echo signal: output TTL level signal (high), proportional to
  range

4. **Preparation**

- Insert the micro:bit board into the slot of keyestudio
  4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the Web version of Makecode

5. **Test Code**

|image226|

Click“JavaScriptto view the corresponding JavaScript code: ：

|image227|

6. **Test Result**

Download code to micro:bit, keep USB cable connected, dial POWER switch
to ON end. The distance value will be displayed on monitor.

|image228|

The monitor shows the distance between the obstacle and ultrasonic
sensor(as shown below).

|image229|

Open CoolTerm, click Options to select SerialPort. Set COM port and
115200 baud rate(the baud rate of USB serial communication of Micro:bit
is 115200 through the test). Click “OK” and “Connect”.

CoolTerm serial monitor displays the distance value as follows:

|image230|

.. _project-182ultrasonic-avoidance:

Project 18.2：Ultrasonic Avoidance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|image231|

1. **Description**

In this project, we will integrate an ultrasonic sensor and a car to
make an ultrasonic avoidance car.

Its principle is to detect the distance between the car and obstacle via
the ultrasonic sensor to control the motion of smart car.

2. **Preparation**

- Insert the micro:bit board into the slot of keyestudio
  4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the Web version of Makecode

3. **Flow Chart**

|image232|

4. **Test Code**

|image233|

Click“JavaScript”to view the corresponding JavaScript code: ：

|image234|

|image235|

5. **Test Result**

Download code to micro:bit, dial to ON end, and dial POWER to ON end.
When the obstacle distance is greater than 20cm, the car goes forward ;
on the contrary, smart car turns left.

.. _project-183ultrasonic-following:

Project 18.3：Ultrasonic Following
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|image236|

1. **Description**

In previous lesson, we’ve learned the basic principle of line tracking
sensor. Next, we will combine the ultrasonic sensor with the car to make
an ultrasonic following car.

The ultrasonic sensor detects the obstacle distance and control the
motion status of car.

2. **Preparation**

- Insert the micro:bit board into the slot of keyestudio
  4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the Web version of Makecode

3. **Flow Chart**

|image237|

4. **Test Code**

|image238|

Click“JavaScript”to view the corresponding JavaScript code: ：

|image239|

5. **Test Result**

Download code to micro:bit, dial POWER switch to ON end on shield, smart
car could follow the obstacle to move.

Project 19：IR Remote Control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _project-191decode-ir-remote-control:

Project 19.1：Decode IR Remote Control
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|image240|

1. **Description**

There is no doubt that infrared remote control is ubiquitous in daily
life. It is used to control various household appliances, such as TVs,
stereos, video recorders and satellite signal receivers. Infrared remote
control is composed of infrared transmitting and infrared receiving
systems, that is, an infrared remote control, an infrared receiving
module and a single-chip microcomputer capable of decoding.

|image241|

The 38K infrared carrier signal emitted by remote controller is encoded
by the encoding chip in the remote controller. It is composed of a
section of pilot code, user code, user inverse code, data code, and data
inverse code. The time interval of the pulse is used to distinguish
whether it is a 0 or 1 signal and the encoding is made up of these 0, 1
signals.

The user code of the same remote control is unchanged. The data code can
distinguish the key.

When the remote control button is pressed, the remote control sends out
an infrared carrier signal. When the IR receiver receives the signal,
the program will decode the carrier signal and determines which key is
pressed. The MCU decodes the received 01 signal, thereby judging what
key is pressed by the remote control.

Infrared receiver we use is an infrared receiver module. Mainly composed
of an infrared receiver head, it is a device that integrates reception,
amplification, and demodulation. Its internal IC has completed
demodulation, and can achieve from infrared reception to output and be
compatible with TTL signals. Additionally, it is suitable for infrared
remote control and infrared data transmission. The infrared receiving
module made by the receiver has only three pins, signal line, VCC and
GND.

According to the picture above, the integrated port of the infrared
receiver is connected to the P9 5V G port on the motor driver board and
controlled by the the P9 of the micro:bit.

2. **Parameters:**

- Operating Voltage: 3.3-5V（DC）

- Interface: 3PIN

- Output Signal: Digital signal

- Receiving Angle: 90 degrees

- Frequency: 38khz

- Receiving Distance: about 5m

3. **Preparation**

- Insert the micro:bit board into the slot of keyestudio
  4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the Web version of Makecode

4. **Test Code**

|image242|

Click“JavaScript" to switch into the corresponding JavaScript code:

|image243|

**Code explanation:** If the buttons are not pressed, the serial monitor
constantly shows 0; when pressed, the corresponding key values are
displayed.

**Notes：**

The remote control in this kit is not inclusive of batteries. We
recommend you to purchase them online.(battery type:CR2025).

Make sure IR remote is good before test. There is a tip for you to check
it.

Open the cellphone camera , make IR remote control point at camera and
press button. The remote control is good if you see the purple flashing
light in the camera.

5. **Test Result**

Download code to micro: bit board and don’t plug off USB cable
Click\ |image244|

|image245|

Make IR remote control point at IR receiver and press the button, the
serial monitor will display the corresponding key values, as shown
below：

|image246|

Open CoolTerm, click Options to select SerialPort. Set COM port and
115200 baud rate. Click“OK”and“Connect”.

CoolTerm serial monitor shows the key value as follows:

|image247|

|image248|

The key value is displayed as for your reference:

|image249|

.. _project-192ir-remote-control:

Project 19.2：IR Remote Control
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|image250|

1. **Description**

In this project, we combine IR remote control with car shield to make an
IR remote smart car. Its principle is to control the motion of car by
sending key signals from IR remote control to IR receiving module of car
shield.

2. **Preparation**

- Insert the micro:bit board into the slot of keyestudio
  4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the Web version of Makecode

**Note:** The infrared sensor and infrared remote control should not be
used in environments with infrared interference such as sunlight for it
contains a lot of invisible lights, such as infrared and ultraviolet. In
an environment with strong sunlight, they cannot work normally.

3. **Flow Chart**

|image251|

4. **Test Code**

|image252|

Click“JavaScript" to switch into the corresponding JavaScript code:

|image253|

|image254|

5. **Test Result**

Download code to micro:bit board, and dial POWER to ON end.

Make IR remote control point at micro:bit and press the button to
control smart car to move.

|image255|\ button makes smart car move forward，\ |image256|\ stands
for turning left，\ |image257|\ implies rightward turning,
|image258|\ indicates moving backward，\ |image259| stops car.

**Note:** The distance between IR remote control and IR receiving head
of smart car are supposed less than 5m during the test.

Project 20：Bluetooth Multi-purpose Smart Car
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _project-201read-bluetooth-data:

Project 20.1：Read Bluetooth Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image260|

1. **Description**

Micro:bit main board comes with a built-in Bluetooth which can be used
to communicate with it. And the Micro:bit can also be controlled by
Bluetooth or transmit signals back to smartphone or computer via it.
This Bluetooth can communicate with the Bluetooth equipped in other
devices or with Bluetooth App to control other equipment.

It is compatible with both Android system ans IOS system. And we have
designed two Bluetooth Apps for both systems.

The connection of the Bluetooth on the board with these two Apps is
similar. In this lesson, we will introduce the functions of all keys and
patterns on the Apps and control the smart car via Bluetooth App.

2. **Preparation**

- Insert the micro:bit board into the slot of keyestudio
  4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the Web version of Makecode

**If you choose to drag the code manually, you need to add the Bluetooth
extension library first. Click the gear icon (Settings) in the upper
right corner, then click on Extensions to go to the library file
selection screen, and then click on the "Bluetooth" extension library
(if it doesn't exist, search Bluetooth to find it), as shown below:** 

|image261|

As the Bluetooth and extension radio can’t work together, therefore,
their extension libraries are not compatible.

Therefore, remove extension(s) and add Bluetooth please if you see the
following prompt box pop up.

|image262|

3. **Test Code**

|image263|

Click“JavaScript”to view the corresponding JavaScript code:

|image264|

4. **Test Result**

If you drag blocks step by step, you need to set as follows after
finishing test code.

|image265|

|image266|

|image267|

However, you could skip this step if you directly import test code.

After setting, download code to micro:bit board, don’t plug off the USB
cable.Next to download App.

**For IOS System:**

a. Open App Store;

|image268|

b. Search mecanum_robot and click“\ |image269|\ ”to download the
Bluetooth App of mecanum_robot;

c. After downloading the APP, click "OPEN" or click the application
mecanum_robot on the phone/iPad desktop to open the APP. A dialog box
appears on the APP interface, and click "OK" in the dialog box.

d. First turn on the Bluetooth of the mobile phone/iPad, and then click
the connect button (control) in the upper left corner of the APP
interface to perform a Bluetooth search. In the search results, click
"BCC micro:bit". After a few seconds, the Bluetooth is connected.

**For Android System:**

a. Use the scanning function in the browser to scan and identify the QR
code

|image270|

or enter the http://8.210.52.206/mecanum_robot.apk to download. After
the identification is successful, click "go to website" to enter the
download mecanum_robot.apk page , click "Download" to download the
mecanum_robot application.

b. Click“Allow allow”to enter Installation Diagram; click“install”to
install the App.

|image271|

c. Click "Open" or click the application mecanum_robot on the mobile
phone desktop to open the APP, and a dialog box appears. In the dialog
box, click "Allow" to turn on the Bluetooth of the mobile phone. You can
also turn on the phone's Bluetooth before opening the APP.

|image272|

|image273|

d. Click |image274| on the upper right corner to search for Bluetooth
and click“connect”; a few seconds later, the Bluetooth is paired.

|image275|

|image276|

Open CoolTerm, click Options to select SerialPort. Set COM port and
115200 baud rate. Click“OK”and“Connect”.

Point at micro:bit board and press the icons on APP, the corresponding
characters are shown on CoolTerm monitor.

|image277|

Through the test, we get the functions of every icon, as shown below:

|image278|

.. _project-202multi-purpose-smart-car:

Project 20.2：Multi-purpose Smart Car
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image279|

1. **Description**

In this lesson, we will control the smart car to perform multipurpose
functions.

2. **Preparation**

- Insert the micro:bit board into the slot of keyestudio
  4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the Web version of Makecode

**Steps：** Click the gear icon (Settings) in the upper right corner,
then click on Extensions to go to the library file selection screen, and
then click on the "Bluetooth" extension library (if it doesn't exist,
search Bluetooth to find it), as shown below: 

|image280|

As the Bluetooth and extension radio can’t work together, therefore,
their extension libraries are not compatible.

Therefore, remove extension(s) and add Bluetooth please if you see the
following prompt box pop up.

|image281|

3. **Test Code**

Since the code is quite long, it won't be displayed here. You can
directly go to the following path to find the corresponding code.

|image282|

Click“JavaScript" to view the corresponding JavaScript code: ：

|image283|

4. **Test Result**

This experiment combines the previous projects to make the car to
perform actions via Bluetooth.

Enter Makecode online editor→Projecting Settings→\ |image284|, enable
“No Pairing....”(you could skip this step if you import test code
directly)

Download code to micro:bit board, dial POWER to ON end, and connect the
Bluetooth, then you can control the car via the Bluetooth App of
mecanum_robot.

**Note:** |image285|\ is used to adjust the speed, and |image286| can
only be dragged.

Common Problems
---------------

1. **The car has no reaction**

Please check whether the batteries are sufficient

Please check whether the wirings are correct

2. **Computers can't recognize the USB ports**

Please ensure whether the microbit driver is installed

Please check whether the USB wire is in good condition.

3. **Code fails to burn and dot matrix displays expressions**

Please check whether the Mecanum Robot Car_V2.py library file i mported

.. |image1| image:: ./media/1bdf1af4b048a53ce0185bb14288ce2a.jpg
.. |image2| image:: ./media/b5a90ee5338cd7fb96e135fe71a79a61.png
.. |image3| image:: ./media/18c70cf16dcf8c9694a1af8b12530cf9.png
.. |image4| image:: ./media/a2b53f93f4c24b81fc5cdb5986fd100d.png
.. |image5| image:: ./media/fd741a4a932cf25b5165c8135b512848.png
.. |image6| image:: ./media/f76062b0607cfca5d20bc26199b2f711.png
.. |Img| image:: ./media/img-20250512104916.png
.. |image7| image:: ./media/f971b8018385c40e0cccf3e1c0c1180c.png
.. |image8| image:: ./media/920329c0eff9d8bd1fe1589f2eed3627.png
.. |image9| image:: ./media/f577dd083f8b00bc532fc4c3acc81705.png
.. |image10| image:: ./media/0bcd358ac11dd2947dd85bbceec9656e.png
.. |image11| image:: ./media/a81d4430eb152346d13bf67b2233b9db.png
.. |image12| image:: ./media/fe0f2de72ba0b38f00403f1aaef7f514.png
.. |image13| image:: ./media/b4f3602c0e192646f77b150e2acaf947.png
.. |image14| image:: ./media/672bfb4d87b938fc586a849bff0229fe.png
.. |image15| image:: ./media/d61a26d2f2367f0378974832f679efe1.png
.. |image16| image:: ./media/285f5ee70c3d95855f87a17d227b8675.png
.. |image17| image:: ./media/79dcee521d5973a83119aee10f45f90f.png
.. |image18| image:: ./media/bbb909c230e7e053577c5650a3a7e33a.png
.. |image19| image:: ./media/e843e223f125fdd0448c49d80e576d39.png
.. |image20| image:: ./media/fe5c6991e1ba8bd46f0bc6b7069b91c1.png
.. |image21| image:: ./media/4cf10fecd346658a9943e900eef2e265.png
.. |image22| image:: ./media/0b3776a491c27034738926b3f958b3f0.png
.. |image23| image:: ./media/37f01f5a75b4127a193a1099bdd142d3.png
.. |image24| image:: ./media/af296c6d48f189a98fcb96522182ffa9.png
.. |image25| image:: ./media/c55e4d43d82301258cbc0367cb3b3d49.png
.. |image26| image:: ./media/96fbd5a50eb87de8ad464cbbd09624f1.png
.. |image27| image:: ./media/139fb53627ddf8cf5b97908e4ad0be61.png
.. |image28| image:: ./media/905cacbd7ab3008d59eb2fed4b197a9f.png
.. |image29| image:: ./media/605b9b18187c770fca1c4f14b9156726.png
.. |image30| image:: ./media/0c07886b6068a4e7bb7c0dcc3f219165.png
.. |image31| image:: ./media/33a64d410046c2c07a29bb56e5fc0263.png
.. |image32| image:: ./media/c987fd1584225ae1efdb32ba13984e9f.png
.. |image33| image:: ./media/4cecc51aa1c8ce608840ae2531613fd0.png
.. |image34| image:: ./media/5eb1985341717f52ff96359a6d2b9b18.png
.. |image35| image:: ./media/dc7549c5f3758b096345215679addcf0.png
.. |image36| image:: ./media/40e8e36d4a7e9b8a726ff1a832393df5.png
.. |image37| image:: ./media/3358909f898dd9898923f72945613851.png
.. |image38| image:: ./media/ff66d0d78d170913676e361a62078faf.png
.. |image39| image:: ./media/317e1065692aa5d3b6479f6d79dff66d.png
.. |image40| image:: ./media/30668623254c10c3c27381ba6e197d23.png
.. |image41| image:: ./media/527cd02b657db82c8dbd8ccd043686a0.png
.. |image42| image:: ./media/a451132713cbd16f3f7957c5312673ba.png
.. |image43| image:: ./media/97f831d38df9ee01dcfedac244bfe281.png
.. |image44| image:: ./media/e77548d01727e523e9e8c900d2fa962d.png
.. |image45| image:: ./media/5f29eed25fc16602cfc0716f047c2da1.png
.. |image46| image:: ./media/74fd81c83f0c0a26b4e299b93ce4ede4.png
.. |image47| image:: ./media/70bebd79d7cd20336ae394c916500a28.png
.. |image48| image:: ./media/2b728375ed2b8cd288c884e553418001.png
.. |image49| image:: ./media/5f972f2eac5050ca0107416b2be067c2.png
.. |image50| image:: ./media/be6f8b560e0afc447f9c32b4474f633f.png
.. |image51| image:: ./media/52257d028694a313fc4eea4d9c2469d7.png
.. |image52| image:: ./media/6ad366842b18084553a142ab82a613cf.png
.. |image53| image:: ./media/8fa3ac342549d33b6c9aa5a9e4688bea.png
.. |image54| image:: ./media/c8d1dd8c3356b4938e143de1022e5842.png
.. |image55| image:: ./media/36e13c266fd4b9723d9db40fe30cd203.png
.. |image56| image:: ./media/b505c71c3344036730b1d67f0c62a354.png
.. |image57| image:: ./media/8c3f540a07aab97e1608ba8770837f7b.png
.. |image58| image:: ./media/b14ace883d757d0dffb2adae9a035aaa.png
.. |image59| image:: ./media/a04acf78eaaa7b404b7b9b034bcfb1cd.png
.. |image60| image:: ./media/00e2115f7e171c91af90f27889395dde.png
.. |image61| image:: ./media/04fdfc9060943954e7938bb1a741d626.png
.. |image62| image:: ./media/8c3f540a07aab97e1608ba8770837f7b.png
.. |image63| image:: ./media/41c834c1592b4ecbec3066082c25f10b.png
.. |image64| image:: ./media/b14ace883d757d0dffb2adae9a035aaa.png
.. |image65| image:: ./media/f19c365efafd84e76d058e97f7a6c50f.png
.. |image66| image:: ./media/img-20250512132427.png
.. |image67| image:: ./media/8c3f540a07aab97e1608ba8770837f7b.png
.. |image68| image:: ./media/d44a44c5708aa9ea67a70220d3afde02.png
.. |image69| image:: ./media/2456980fec90ec5086f078165471889f.png
.. |image70| image:: ./media/20fed03d66e92ef565333d6f060b1267.png
.. |image71| image:: ./media/4c537c2e073066441fb23219619ecf09.png
.. |image72| image:: ./media/d4e278da768e447ed344d581e671f57a.png
.. |image73| image:: ./media/d4e278da768e447ed344d581e671f57a.png
.. |image74| image:: ./media/66b31365d42274ef94ce9a3fcea1cd6c.png
.. |image75| image:: ./media/39fe4029acb5fb675d875c58e382d148.png
.. |image76| image:: ./media/45fcde65eb80a942d3903e400a346587.png
.. |image77| image:: ./media/9e34fdb19d72918bde242994a3c94c1f.png
.. |image78| image:: ./media/2a45fca9d836ce38674c347c70c81e02.png
.. |image79| image:: ./media/06be84fb11b1fd07cd0cbb392132b903.png
.. |image80| image:: ./media/2ff75a1d81bfe0228b83931a0b7cc860.png
.. |image81| image:: ./media/d2a204e61c768f18924150db58aee093.png
.. |image82| image:: ./media/1ad59546b238e9644160019cdb102ee4.png
.. |image83| image:: ./media/50c59105d5a2409eea809e6ce73cf740.png
.. |image84| image:: ./media/e2d7143ce59218e14780e9370d973c51.png
.. |image85| image:: ./media/21704f7ef37d6ed440545c28dbd93211.png
.. |image86| image:: ./media/206c8ec1c3f11d2de8d0f42fdf5b6b47.png
.. |image87| image:: ./media/e1e316ab2c9727c9b5a36dd82a7ab11a.png
.. |image88| image:: ./media/0cb83e9f83fa0fd0344685f38913cb43.png
.. |image89| image:: ./media/e0580d7886af95d2a4ea7cd9d40759ff.png
.. |image90| image:: ./media/0d3198e0cb5460c9820bc2f016c0d7c1.png
.. |image91| image:: ./media/6177222069a9583f2d8314d592fdb916.png
.. |image92| image:: ./media/b3a18bca1b2a7b5337470735e5a0c5aa.png
.. |image93| image:: ./media/f78128c148de3862a3fe10d86f063e22.png
.. |image94| image:: ./media/13238e98c31d620f4ffd7742dd71c78d.png
.. |image95| image:: ./media/9c88bb875124738a55e5e0fd5bf957ca.png
.. |image96| image:: ./media/75b4f8dfc29b2a45e718383972ff0dc4.png
.. |image97| image:: ./media/9424f8456bb544ca25a7c5a4ea6e852c.png
.. |image98| image:: ./media/4b1765e12b413dc5d562f2a16d32392f.png
.. |image99| image:: ./media/f2705fbc4886efcfaac96589ca255f66.png
.. |image100| image:: ./media/24c31bb0174e2ac672203e5c36c6875e.png
.. |image101| image:: ./media/3dac0d4c18fe1334cb76de8a87bf150c.png
.. |image102| image:: ./media/a3fa9018b3e83be04515297b5fd94b42.png
.. |image103| image:: ./media/acf3b8c0dee027d9e555fc708831f874.jpg
.. |image104| image:: ./media/a4faf86fb027b2f4c3dacaeee5d47d2b.png
.. |image105| image:: ./media/img-20250512113408.png
.. |image106| image:: ./media/img-20250512113350.png
.. |image107| image:: ./media/ca4bc854081faf63bb13b2db448fa284.png
.. |image108| image:: ./media/5e3330d735a144c4a6461ece221db219.png
.. |image109| image:: ./media/99ec247ce0be9850c92e8fdfc1fc5d63.png
.. |image110| image:: ./media/2ca9ab458e80a2c3ec7002c15b74235e.png
.. |image111| image:: ./media/7140a86db633ec1bb6ec7e07a109a0dc.png
.. |image112| image:: ./media/1d4fdac44bf4e1629145fac97f627c24.png
.. |image113| image:: ./media/24c31bb0174e2ac672203e5c36c6875e.png
.. |image114| image:: ./media/75e625fbae54fd3d76cf6c4967d87415.png
.. |image115| image:: ./media/3fc45754cb7a060d660212c5cb8c268f.png
.. |image116| image:: ./media/ffd55d004aee7f100e1a2608c90f1c7c.png
.. |image117| image:: ./media/1600323e3e61e331c248cbeda5ccdcfc.jpg
.. |image118| image:: ./media/3be80acf957e53117f695801ce19c449.jpg
.. |image119| image:: ./media/326095934bcff0a925b4f9a09d6cf7d2.jpg
.. |image120| image:: ./media/185b0ac204e9b2c54dd8fa93d852568c.jpg
.. |image121| image:: ./media/57fec5e7a6bda76b8ddc6c3538b58010.png
.. |image122| image:: ./media/381a6d80fa940cb21ad6963469eef351.png
.. |image123| image:: ./media/e310a9105faecbe6ed8400101a4e852d.png
.. |image124| image:: ./media/821a64a53c3a9709ff556e71b070f4dd.png
.. |image125| image:: ./media/6303a0ac122680207fe856d9be38d01c.png
.. |image126| image:: ./media/ded4e05f2b15d694e2061159628574dc.png
.. |image127| image:: ./media/b4f4201cccf6ac0dadffb952b7596895.png
.. |image128| image:: ./media/8c3f540a07aab97e1608ba8770837f7b.png
.. |image129| image:: ./media/1ae769b6a1d9f6c6a393351c69b10d32.png
.. |image130| image:: ./media/7739b4e9b0603e04cdeb1c7051b9d2f8.png
.. |image131| image:: ./media/e310a9105faecbe6ed8400101a4e852d.png
.. |image132| image:: ./media/04b472326485cf676cdb4dd61ca6ef1a.png
.. |image133| image:: ./media/d7f1751ea1e6f251376dee5390ed21fa.png
.. |image134| image:: ./media/77a6de8ab9b171353693610a09f3a83c.png
.. |image135| image:: ./media/ac515b9ae8891dc32f368a29f194a2fb.png
.. |image136| image:: ./media/ebd84db5c527208b9fa4c7bfd91c50a5.png
.. |image137| image:: ./media/984405217312d495104129a784ef76de.png
.. |image138| image:: ./media/644695850097c5ade080bb4848b4b481.png
.. |image139| image:: ./media/bb847ad951cd721972d24fe0b90631a1.png
.. |image140| image:: ./media/15d6364778e29d2a05442c6cf01cc88d.png
.. |image141| image:: ./media/f63f0917317e2f8542961a88a5e6827f.png
.. |image142| image:: ./media/3073a8af772ab91ecf264843b37d3b74.png
.. |image143| image:: ./media/7f0741158e734ff8449d5b87d5ba85f4.png
.. |image144| image:: ./media/b48689241988a3fda8de4e26ebd9a4ed.png
.. |image145| image:: ./media/e366483e9d5c574f3ec520f30e31e5cd.png
.. |image146| image:: ./media/04fdfc9060943954e7938bb1a741d626.png
.. |image147| image:: ./media/c42455108c20d4ae51546957ab4198bb.png
.. |image148| image:: ./media/4e327f5f9ed716e6cf27cccba674f1c3.png
.. |image149| image:: ./media/e22507af4953df977269bbdb2463d69e.png
.. |image150| image:: ./media/50b81518d9f7925b0c20476ab1f64185.png
.. |image151| image:: ./media/55b2424d88ba1ba8a711c49418ca8dc6.png
.. |image152| image:: ./media/cfaf7f8ae83cbe2636c39162a78adc7f.png
.. |image153| image:: ./media/9118815df7403daaf3a5dc8b9967b200.jpg
.. |image154| image:: ./media/63f1faf124af4949b31d7a84cee19a92.png
.. |image155| image:: ./media/27924fdb3d67692df7c63d8d0fb72287.png
.. |image156| image:: ./media/962a57f92b78eea1f0e3e81463497a9c.png
.. |image157| image:: ./media/66d1f34d8d4c52e2b7c0ce10e602a063.png
.. |image158| image:: ./media/34f5fbb1c0c371970d1aec6c59c5cbb5.png
.. |image159| image:: ./media/e20270a0ade9c00b61198b26fc2fd83b.png
.. |image160| image:: ./media/c00520400ecd1f20f958c1c6d1a3c907.png
.. |image161| image:: ./media/cabc60d7f8a030f5c9d86ac7de6c7bd7.png
.. |image162| image:: ./media/9411a5280e6f3b0d45306a31f80c1b38.png
.. |image163| image:: ./media/7b56c56e10415ac2881ac69448b4ad3c.png
.. |image164| image:: ./media/803cb5cf5f7d595581a11f5e6b7e61ed.png
.. |image165| image:: ./media/dc570950dd81f427edb5ea58f50b3a7e.png
.. |image166| image:: ./media/f72e83dc6276d520e82c349659106e1a.png
.. |image167| image:: ./media/f3e9cc7884f7bba807fa4633c429422b.png
.. |image168| image:: ./media/e081360be7c91b7a156b01a787e4a58c.png
.. |image169| image:: ./media/d54bf2d1c01cd3c18544009b1f9dc5a0.png
.. |image170| image:: ./media/4e7a5d06a5f9a5a209ef5fbc005e9f62.png
.. |image171| image:: ./media/5bd84e8d293bf8c0c999c7f4e756cf30.png
.. |image172| image:: ./media/bd19bb4c97ad2a5bc300412b8eb93ede.png
.. |image173| image:: ./media/a32c2d832ab38d19eb623108143c744e.png
.. |image174| image:: ./media/25cf76f891c5eac7381b8095363a2748.png
.. |image175| image:: ./media/c1661720ea2eaa521ff31a778501eb23.png
.. |image176| image:: ./media/350abcbb09d431d40427f34c3764f2eb.png
.. |image177| image:: ./media/4863bf826f119805a6a9bf9c12d5ec81.png
.. |image178| image:: ./media/ebfd31347a0553de0be4e01636652a15.png
.. |image179| image:: ./media/804e502bd0692ecb92e2f2ac16727bfc.png
.. |image180| image:: ./media/1b065b7fa2d2ddf1a6baafad8bf5c064.png
.. |image181| image:: ./media/c111933f0e49c4785c284cb34f6494aa.png
.. |image182| image:: ./media/bdce981c0ae66ebe881ff85892b06384.png
.. |image183| image:: ./media/66e648293b33dfa43f965a0a00d1decc.png
.. |image184| image:: ./media/eecf79fe278bc8107ce6827f9668f560.png
.. |image185| image:: ./media/b2cdf8ccae177a77965bb692e7f0bff1.png
.. |image186| image:: ./media/ce3ad2e98499f1b894338673ef1c6bbf.png
.. |image187| image:: ./media/669d30b5bbc4bf1f5dea711b8c11cc39.png
.. |image188| image:: ./media/fd64aca351ebaaa0d5866e8b7d96cef8.png
.. |image189| image:: ./media/f06b9905088a3d39373f78c947e64be3.png
.. |image190| image:: ./media/06ef211131608693b324de4564f211a9.png
.. |image191| image:: ./media/cc2c2fb3e0e8335d3958121a92b6e462.png
.. |image192| image:: ./media/9004a799ddf2a0d952d4174efade0410.png
.. |image193| image:: ./media/212ce3c897c73c055c793752591102dc.png
.. |image194| image:: ./media/ae51208a3f560ad6edefe370eb588c13.png
.. |image195| image:: ./media/69be958142b773acdae33eeef12afed7.png
.. |image196| image:: ./media/49467dfa70799401a5a5acc691014aee.png
.. |image197| image:: ./media/ddc74f62dc936c925d28d70a1a9c2214.png
.. |image198| image:: ./media/087e18229bba5f7a01520f80f8c8187c.png
.. |image199| image:: ./media/2354311fc81b6b5dc9819544be60e356.png
.. |image200| image:: ./media/02a16adfdabb92d6de1796019e909b44.png
.. |image201| image:: ./media/5b67b46bfb1c9d8b6bdeca1b98aa6bbf.jpg
.. |image202| image:: ./media/4919ce3b3fa299f13aa33348165ed728.png
.. |image203| image:: ./media/59c34b6eeef8ad7eb0ad8304426c207e.png
.. |image204| image:: ./media/8874ded0289da7d5d5a0141cc7b88769.png
.. |image205| image:: ./media/3a759dd8c19a12c8294cd4a56348e0b2.png
.. |image206| image:: ./media/242ba6ca775c1ba73825d0affebe8495.png
.. |image207| image:: ./media/a3a9d39aafc4162630ad4740cbc08462.png
.. |image208| image:: ./media/ee70b8466efde60855efa486fab502fa.png
.. |image209| image:: ./media/ea7f6c8c87ab8a6aa921ad35f6569523.png
.. |image210| image:: ./media/3683d83f8320256e3c74aa9a79aea314.png
.. |image211| image:: ./media/4b4406164f393a90039758cbb655cbc8.png
.. |image212| image:: ./media/ea164439c46c8641e24d04e08528f18c.png
.. |image213| image:: ./media/c9fd8c63a021e0cf1c8cf65b8baf4762.png
.. |image214| image:: ./media/9876cc606f056e134e32756e1a3b6b5d.png
.. |image215| image:: ./media/ddb290f42e5a4d96ad676222991000f1.png
.. |image216| image:: ./media/0141051aca98f66393c28ee23d34d734.png
.. |image217| image:: ./media/d7b67de2bc904ba303a88a268dfac339.jpg
.. |image218| image:: ./media/img-20250512134536.png
.. |image219| image:: ./media/img-20250512135417.png
.. |image220| image:: ./media/4b1041553ed0d547c117292490fa6dfd.png
.. |image221| image:: ./media/f5caa06aeb3bb1944a0298f1bbf7ad86.png
.. |image222| image:: ./media/8f5f07ec0d28bb334447b50e857639fe.png
.. |image223| image:: ./media/0180b169a1c3b228394b43df704fac32.png
.. |image224| image:: ./media/1174e0ec8487f223400c50ee4f765dac.png
.. |image225| image:: ./media/8ff02741199a0f03d8d814a4b72f27d7.png
.. |image226| image:: ./media/497760b1d2daeec2134c8ed8fa89d130.png
.. |image227| image:: ./media/387f32432a158fd0c34ff03a6d6bbde5.png
.. |image228| image:: ./media/2cd74c16ab3623f6752d3f5e59deea2e.png
.. |image229| image:: ./media/422adea3e04563f038f7f28cd40efb2d.png
.. |image230| image:: ./media/69b0699826728a3ac629f8869b2c644b.png
.. |image231| image:: ./media/a9f6a779aba5cc124d3ac8789ff87458.jpg
.. |image232| image:: ./media/img-20250512135516.png
.. |image233| image:: ./media/05a4740bad5faf67199577dc79e502ac.png
.. |image234| image:: ./media/c8f86a24196a5bd7569ad419207e71e4.png
.. |image235| image:: ./media/13baf1d67d2b0e5fefe9a31c6120b185.png
.. |image236| image:: ./media/6dcfae5b12fd196e2e2c567d8d159814.jpg
.. |image237| image:: ./media/img-20250512135602.png
.. |image238| image:: ./media/03b95531c329ada277242c0ce8c16b5a.png
.. |image239| image:: ./media/a93c824520e7139f7419817a8d05d5e2.png
.. |image240| image:: ./media/3a3e9860725c893c34613ee1eafb91fc.png
.. |image241| image:: ./media/9980b41f57feddc2e8a9c0346afaaea9.png
.. |image242| image:: ./media/2e20f731f34b79115eedecb2d1eefd78.png
.. |image243| image:: ./media/87e18859852d9e1f086a36edee21ffac.png
.. |image244| image:: ./media/1f02508d0c79cd976c673a6a5daba648.png
.. |image245| image:: ./media/e7bf712e0c8bedc4b0423427848fa395.png
.. |image246| image:: ./media/c7a33a4cc9d6decbf9b653d91bcb5318.png
.. |image247| image:: ./media/img-20250512140159.png
.. |image248| image:: ./media/bd951869f7f822f8420d6174122c9a35.jpg
.. |image249| image:: ./media/db524e7e2d5a77652948837ed70a1310.jpg
.. |image250| image:: ./media/058af4ba6b305a06d628d68d32788062.jpg
.. |image251| image:: ./media/img-20250512140241.png
.. |image252| image:: ./media/22d06d7487b51c0dfdd0ca30c7f4945e.png
.. |image253| image:: ./media/e68b6275a1026ed95ca88502e5bc4c49.png
.. |image254| image:: ./media/94de6552ca4ccdb232d5e9dd0466e611.png
.. |image255| image:: ./media/d55474f3fdf94e5d35de424c0135f554.png
.. |image256| image:: ./media/5c8a65498c17f35878adf79ba446a7c8.png
.. |image257| image:: ./media/41116032870ebaa49d6e78fe2445da36.png
.. |image258| image:: ./media/369433f6b13252c1df8c30b3f71028d2.png
.. |image259| image:: ./media/a8ef4b174911d528e2dc232c2f862b7d.png
.. |image260| image:: ./media/55b2424d88ba1ba8a711c49418ca8dc6.png
.. |image261| image:: ./media/4e30836054aa5b5a983cb70b3baa62b0.png
.. |image262| image:: ./media/aee56e76bad3421a20cea6018ccd5e2c.png
.. |image263| image:: ./media/ac5ffe1aee7b0f7ff335606b02cd153e.png
.. |image264| image:: ./media/24191138f7bb709f2c6de046df16edef.png
.. |image265| image:: ./media/01b256e5bbe9420226085513778f5173.png
.. |image266| image:: ./media/982334c8cdfb3ab43cd2db629090ca1b.png
.. |image267| image:: ./media/09767d5efdc8f05fdb331b5ae6d352b5.png
.. |image268| image:: ./media/27924fdb3d67692df7c63d8d0fb72287.png
.. |image269| image:: ./media/962a57f92b78eea1f0e3e81463497a9c.png
.. |image270| image:: ./media/d9acbfab8eccc3da40cde7788a3e1854.png
.. |image271| image:: ./media/638d0a4ae5f55ca39bff4f20a3bd14a6.png
.. |image272| image:: ./media/c818fd71d6872374fbe177f082207fac.png
.. |image273| image:: ./media/0c35f0dceebddef4110b47372fe299a4.png
.. |image274| image:: ./media/d3f566b98da750bf4d5799b624211516.png
.. |image275| image:: ./media/3d21cf8757f8cd7434985e60bc940418.png
.. |image276| image:: ./media/4a23b1970c9f012293aef3327a90cf7c.png
.. |image277| image:: ./media/0ed4a53ef14fbfe047929d07d5433fcb.png
.. |image278| image:: ./media/05c3d32b07c8e1393eacd805b4de77c7.jpg
.. |image279| image:: ./media/b9de6fb2ea158ce9fd59513a9e8c4833.jpg
.. |image280| image:: ./media/4e30836054aa5b5a983cb70b3baa62b0.png
.. |image281| image:: ./media/aee56e76bad3421a20cea6018ccd5e2c.png
.. |image282| image:: ./media/d9d0b14680f4131194595baaee971699.png
.. |image283| image:: ./media/a73529d60614999f05244e4fa4c31cca.png
.. |image284| image:: ./media/bef5b73422672f316f211a959bcdfa60.png
.. |image285| image:: ./media/81da4f47165508a486698671a3568af0.jpg
.. |image286| image:: ./media/adc3be608cbddaca066d63aa9bc0c435.jpg
