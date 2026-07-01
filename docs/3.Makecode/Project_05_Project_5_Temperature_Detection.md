## Project 5: Temperature Detection

![](./media/Makecode_22c6434f.jpg)

[Click to download the code 1 for this lesson](./Code/Temperature-Detection.hex)

[Click to download the code 2 for this lesson](./Code/Temperature-Detection2.hex)

### (1)Project Description:

The Micro:bit main board V2 is not equipped with a temperature sensor, but uses the temperature sensor built into NFR52833 chip for temperature detection. Therefore, the detected temperature is more closer to the temperature of the chip, and there maybe deviation from the ambient temperature.

### (2)Components Needed:

Micro:bit main board V2

Micro USB cable

### (3)Test Code 1 :

![](./media/Makecode_e6674fe9.gif)

### (4)Test Results 1:

After uploading test code 1 to micro:bit main board V2, powering the main board via the USB cable, and clicking "Show console Device", the data of temperature shows in the serial monitor page as shown below.

![](./media/Makecode_898eded8.gif)

If you're running Windows 7 or 8 instead of Windows 10, via

Google Chrome won't be able to match devices. You'll need to use the CoolTerm serial monitor software to read data.You could open CoolTerm software, click Options, select SerialPort, set COM port and put baud rate to 115200 (after testing, the baud rate of USB SerialPort communication on Micro: Bit main board V2 is 115200), click OK, and Connect. The CoolTerm serial monitor shows the change of temperature in the current environment, as shown in the figures below :

![](./media/Makecode_268159a1.gif)

### (5)Test Code 2 :

Link computer with micro:bit board by micro USB cable, and program in MakeCode editor,

![](./media/Makecode_4057bdd7.gif)

Complete Program :

![](./media/Makecode_ec457959.png)

### (6)Test Results 2:

After uploading the code 2, when the ambient temperature is  less than 35℃, the 5*5 LED dot matrix shows ![](./media/Makecode_350d26c6.png). When the temperature is equivalent to or greater than 35℃, the pattern ![](./media/Makecode_ef8d7c88.png)appears.
