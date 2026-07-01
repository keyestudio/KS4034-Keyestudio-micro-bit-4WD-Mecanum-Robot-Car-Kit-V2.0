## Project 7: Accelerometer

![](./media/Makecode_66670811.jpg)

[Click to download the code 1 for this lesson](./Code/Accelerometer.hex)

[Click to download the code 2 for this lesson](./Code/Accelerometer2.hex)

### (1)Project Description:

The Micro: Bit main board V2 has a built- in LSM303AGR gravity acceleration sensor, also known as accelerometer, with a resolution of 8/10/12 bits. The code section sets the range to 1g, 2g, 4g, and 8g.

We often use accelerometer to detect the status of machines. In this project, we will introduce how to measure the position of the board with the accelerometer. And then have a look at the original three- axis data output by the accelerometer.

### (2)Components Needed:

Micro:bit main board V2 

Micro USB cable

### (3)Test Code 1 :

Link computer with micro:bit board by micro USB cable, and program in MakeCode editor,

![](./media/Makecode_2cd48603.gif)

Complete Program :

![](./media/Makecode_ba28162b.png)

### (4)Test Results 1:

After uploading Test Code 1 to the micro:bit V2 board, changing the board's orientation will cause the 5x5 dot matrix to display different numbers.

![](./media/Makecode_2e6708e6.gif)

if we shake the Micro: Bit main board V2. no matter at any direction, the LED dot matrix displays the digit "1".

When it is kept upright ( make its logo above the LED dot matrix), the number 2 shows.

![](./media/Makecode_67247ae1.jpg)

When it is kept upside down( make its logo below the LED dot matrix), it shows as below.

![](./media/Makecode_1668a9d0.jpg)

When it is placed still on the desk, showing its front side, the number 4 appears.

![](./media/Makecode_0dd33fa1.jpg)

When it is placed still on the desk, showing its back side, the number 5 exhibits.

When the board is tilted to the left, the LED dot matrix shows the number 6 as shown below.

![](./media/Makecode_ce2b3501.jpg)

When the board is tilted to the right, the LED dot matrix displays the number 7 as shown below

![](./media/Makecode_d098ff98.jpg)

When the board is knocked to the floor, this process can be considered as a free fall and the LED dot matrix shows the number 8. (please note that this test is not recommended for it may damage the main board.)

Attention: if you'd like to try this function, you can also set the acceleration to 3g, 6g or 8g. But still, we do not recommend.

### (5)Test Code 2 :

![](./media/Makecode_99083bf6.gif)

Complete Program :

![](./media/Makecode_42654b0e.png)

### (6) Test Results 2

Upload test code to micro:bit main board V2, power the main board via the USB cable, and click "Show console Device".

The following interface shows the decomposition value of acceleration in X axis, Y axis and Z axis respectively, as well as acceleration synthesis (acceleration synthesis of gravity and other external forces).

![](./media/Makecode_c17f5477.gif)

After referring to the MMA8653FC data manual and the hardware schematic diagram of the Micro: Bit main board V2, the accelerometer coordinate of the Micro: Bit V2 motherboard are shown in the figure below:

![](./media/Makecode_79d90885.jpg)

If you're running Windows 7 or 8 instead of Windows 10, via Google Chrome won't be able to match devices. You'll need to use the CoolTerm serial monitor software to read data.You could open CoolTerm software, click Options, select SerialPort, set COM port and put baud rate to 115200 (after testing, the baud rate of USB SerialPort communication on Micro: Bit main board V2 is 115200), click OK, and Connect. The CoolTerm serial monitor shows the data of X axis, Y axis and Z axis, as shown in the figures below:

![](./media/Makecode_2a63fc72.gif)
