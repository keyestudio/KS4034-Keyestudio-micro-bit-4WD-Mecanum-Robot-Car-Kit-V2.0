## Project 8: Light Detection

![](./media/Makecode_14063ef9.jpg)

[Click to download the code for this lesson](./Code/Light-Detection.hex)

### (1) Project Description:

In this project, we focus on the light detection function of the Micro: Bit main board V2. It is achieved by the LED dot matrix since the main board is not equipped with a photoresistor.

### (2)Components Needed:

Micro:bit main board V2

Micro USB cable

### (3)Test Code:

Link computer with micro:bit board by micro USB cable, and program in MakeCode editor,

![](./media/Makecode_38ffa3b8.gif)

Complete Program :

![](./media/Makecode_5b9a2acf.png)

### (4)Test Results:

Upload the test code to micro:bit main board V2, power the board via the USB cable and click "Show console Device".

When the LED dot matrix is covered by hand, the light intensity showed is approximately 0; when the LED dot matrix is exposed to light, the light intensity displayed gets stronger with the light as shown below.

![](./media/Makecode_11dd3c0b.gif)

If you're running Windows 7 or 8 instead of Windows 10, via Google Chrome won't be able to match devices. You'll need to use the CoolTerm serial monitor software to read data.

You could open CoolTerm software, click Options, select SerialPort, set COM port and put baud rate to 115200 (after testing, the baud rate of USB SerialPort communication on Micro: Bit main board V2 is 115200), click OK, and Connect. The CoolTerm serial monitor shows the value of light intensity, as shown in the figures below :

![](./media/Makecode_3c6eae52.gif)
