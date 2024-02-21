# Makecode Tutorial

![](media/1bdf1af4b048a53ce0185bb14288ce2a.jpg)


## Get Started with makecode

The following instructions are applied for Windows system but can also serve as a reference if you are using a different system.

7.1 Write code and program

This chapter describes how to write program and load it to the Micro:
Bit main board V2.

Please browse the link for more details:

<https://microbit.org/guide/quick/>

Step 1: Connect the Micro: Bit

Firstly, link the Micro: Bit main board with your computer via the USB cable. Macs, PCs, Chromebooks and Linux（including Raspberry Pi）systems are all compatible with the Micro: Bit main board.

Note that if you are about to pair the board with your phone or tablet, please refer to this link:

[https:/microbit.org/get-started/user-guide/mobile/](https://microbit.org/get-started/user-guide/mobile/)

![](media/b5a90ee5338cd7fb96e135fe71a79a61.png)
![](media/18c70cf16dcf8c9694a1af8b12530cf9.png)

Secondly, if the red LED on the back of the board is on, that means the board is powered. When your computer communicates with the main board via the USB cable, the yellow LED on it will flashes. For example, it will flicker when you burn a “hex”file.

Then Micro: bit main board will display a driver named “MICROBIT(E:)”on your computer. Please note that it is not an ordinary USB disk, as shown below.

![](media/a2b53f93f4c24b81fc5cdb5986fd100d.png)

Step 2: Write programs

Access the link：<https://makecode.microbit.org/>，then click “New Project”, when the dialog box‘Create a Project’ appears, input‘heartbeat’in it and click ‘Create √’to edit.

(If you are running Windows 10 system, it is also viable to edit on the Windows 10 APP, which is exactly like editing in the website.

Link of the APP :
<https://www.microsoft.com/zh-cn/p/makecode-for-micro-bit/9pjc7sv48lcx?ocid=badgep&rtc=1&activetab=pivot:overviewtab>

![](media/fd741a4a932cf25b5165c8135b512848.png)

![](media/f76062b0607cfca5d20bc26199b2f711.png)

Write a set of micro:bit code. You can drag some
<span edit
‘</span>heartbeat’ program .

Here's a demo video(path): .../2. Makecode Tutorial\Makecode Code\Project 1：Heart beat\heartbeat.mp4

![](media/f971b8018385c40e0cccf3e1c0c1180c.png)

Click“ JS JavaScript”，then we enable to find
the corresponding program in JavaScript language, as shown below:

![](media/920329c0eff9d8bd1fe1589f2eed3627.png)

You also can click the“JS JavaScript”and slide the button to choose“Python”and you will find the corresponding
as shown below:

![](media/f577dd083f8b00bc532fc4c3acc81705.png)

Step 3: Download Code

If your computer is Windows 10, you solely need to click the ‘Download’ button to download the program to your micro: bit main board.

If you are writing program through the website, following these steps:

Click the ‘Download’ button in the editor to download a "hex" file, which can be read by the Micro: Bit main board. Once the hexadecimal file is downloaded, copy it to your board just like the process that you copy the file to the USB driver. If you are running Windows system, you can also right-click and select ‘Send to → MICROBIT(E:) ‘to copy the hex file to the Micro: Bit main board.

![](media/0bcd358ac11dd2947dd85bbceec9656e.png)

![](media/a81d4430eb152346d13bf67b2233b9db.png)

You can also directly drag the "hex" file onto the MICROBIT (E:) disk.

![](media/fe0f2de72ba0b38f00403f1aaef7f514.png)

![](media/b4f3602c0e192646f77b150e2acaf947.png)

During the process of copying the downloaded hex file to the Micro: bit main board, the yellow signal light on the back side of the board flashes. When the copy is completed, the yellow signal light will stop flashing and remain on.

Step 4: Run the program

After the program is uploaded to the Micro: bit main board, you could still power it via an USB cable or an external power. The 5 x 5 LED dot matrix on the board displays the heartbeat pattern.

![](media/672bfb4d87b938fc586a849bff0229fe.png)
![](media/d61a26d2f2367f0378974832f679efe1.png)

Power via USB cable Power via external power（3V）

Caution:

When programming, the MICROBIT
driver will automatically eject and return and your hexadecimal files will disappear. And the board can only have access to hexadecimal files (hex) and won’t save other files.

Step5：Other programming languages

Go to the link: ：<https://microbit.org/code/> for different programming languages or ：<https://microbit.org/projects/> to learn what you are interested.

7.2.Makecode

Access the link：<https://makecode.microbit.org/>，and enter the online editor of makecode or open the APP makecode for micro:bit Windows 10.

![](media/285f5ee70c3d95855f87a17d227b8675.png)

Click“New Project”, and input“heartbeat”in the dialog box, then click
“create √”to enter Makecode editor, as shown below:

![](media/79dcee521d5973a83119aee10f45f90f.png)


There are blocks“on start”and“forever”in the code editing area.

When the power is plugged or reset,“on start”means that
the code in the block only executes once, while“forever”implies that the code runs cyclically.

7.3.Quick Download

As mentioned before, if your computer is Windows 10 and you have downloaded the MakeCode APP for micro:bit, then the code can be quickly downloaded to the Micro: Bit main board by clicking‘Download’button.

While it is a little more trickier if you are using a browser to enter Makecode. However, if you use Google Chrome for Android，ChromeOS，Linux，macOS and Windows 10, the process can be quicker too.

We use the webUSB function of Chrome to access the micro USB hardware device.

You could refer to the following steps to connect and pair devices.

Device pairing:

Connect micro:bit to your computer by USB cable.

Click“...”beside to“Download”and tap“Connect device”;

![](media/bbb909c230e7e053577c5650a3a7e33a.png)

Click“Next”;

![](media/e843e223f125fdd0448c49d80e576d39.png)

Click“Next”again

![](media/fe5c6991e1ba8bd46f0bc6b7069b91c1.png)

Then select the corresponding device and click“Connect”. If no device shows up for selection, please refer to the link:
<https://makecode.microbit.org/device/usb/webusb/troubleshoot>

And for updating the firmware of the Micro:bit:
<https://microbit.org/guide/firmware/> .

If the links are too troublesome for you , then you can also turn to our
‘Troubleshooting Downloads with WebUSB.pdf”

![](media/4cf10fecd346658a9943e900eef2e265.png)

Click“Done”to finish the pairing.

![](media/0b3776a491c27034738926b3f958b3f0.png)

![](media/37f01f5a75b4127a193a1099bdd142d3.png)

Download Program

After pairing, click “download”to directly download the program to the board. If it is successfully downloaded, the icon
![](media/af296c6d48f189a98fcb96522182ffa9.png)
will shift to
![](media/c55e4d43d82301258cbc0367cb3b3d49.png).

![](media/96fbd5a50eb87de8ad464cbbd09624f1.png)

7.4.Makecode Extension Libraries

We have made a makecode extension library for this Mecanum robot car V2.0

Add an extension library of the Mecanum robot car V2.0

Please follow the following steps to add extension files:

Open Makecode to enter a certain project→click the gear-shaped icon(for setting) in the upper right corner→choose“Extensions”;

![](media/139fb53627ddf8cf5b97908e4ad0be61.png)

Or click“Extensions”, as shown below:

![](media/905cacbd7ab3008d59eb2fed4b197a9f.png)

Input the link <u><https://github.com/keyestudio2019/mecanum_robot>
\_v2.git</u> to search;

Tap the searching result“MecanumRobotV2”to download and install it, This process may take a few seconds.

![](media/605b9b18187c770fca1c4f14b9156726.png)

After the installation, you can find the extension files **Mecanum RobotV2** and **IrRemote** on the left side.

And extension file Neopixel is also installed.

![](media/0c07886b6068a4e7bb7c0dcc3f219165.png)

![](media/33a64d410046c2c07a29bb56e5fc0263.png)

![](media/c987fd1584225ae1efdb32ba13984e9f.png)

Note: The extension files added are only available for this project. Therefore, when you create a new **MecanumRobotV2** project, you will need to add these extension files again.

Update or delete the MecanumRobotV2 extension files:

Please follow the following steps to update or delete extension files:

Click "Js JavaScript" to change to textual version:

![](media/4cecc51aa1c8ce608840ae2531613fd0.png)

Click the“Explorer”on the left side:

![](media/5eb1985341717f52ff96359a6d2b9b18.png)

You can find these added files in the list;

Click the dustbin icon beside the file to delete the MecanumRobotV2 file and tap the refresh icon to update it.

![](media/dc7549c5f3758b096345215679addcf0.png)

7.5.Resources and Test Code

Download link：<https://fs.keyestudio.com/KS4034-4035>

Once downloaded and unzipped, a file named KS4034(KS4035) Keyestudio Micro bit 4WD Mecanum Robot Car Kit V2.0 will lie in sight.

Open it , as shown in the figure below:

![](media/a29de15a808596dc1d9a3f6af6d47b3f.png)

7.6.**Import test code**

We provide hexadecimal code files (project files) for each project. The file contains all the contents of the project and can be imported directly, and you can manually drag the code blocks to complete the program.

For simple projects, dragging a block of code to complete the program is recommended. For complex projects, it is recommended to conduct the program by importing the provided hexadecimal code file.

Let's take the "Heatbeat" project as an example to show how to load the code.

Open the Web version of Makecode or the Windows 10 App version of Makecode then click “Import”.

![](media/40e8e36d4a7e9b8a726ff1a832393df5.png)

Click“Import File”;

![](media/3358909f898dd9898923f72945613851.png)

![](media/ff66d0d78d170913676e361a62078faf.png)

Select“..\2. Makecode Tutorial\Makecode Code\Project 1：Heartbeat\Project 1: Heart beat.hex”, then click“Go ahead”.

![](media/317e1065692aa5d3b6479f6d79dff66d.png)

![](media/30668623254c10c3c27381ba6e197d23.png)

In addition to importing the provided test code file into the Makecode compiler above, you can also drag them to the code editing area of the Makecode compiler, as shown in the figure below:

![](media/527cd02b657db82c8dbd8ccd043686a0.png)

After a few seconds, it has done.

![](media/a451132713cbd16f3f7957c5312673ba.png)

Note: If your computer system is’t Windows 10, the pairing cannot be done via Google Chrome. Therefore, digital or analog signals of sensors and modules cannot be read. However, we can use the CoolTerm software to read the serial port data. Next chapter is about how to install the CoolTerm.

7.7.Install CoolTerm 

CoolTerm program is used to read the data on serial port.

Download CoolTerm program: <https://freeware.the-meiers.org/>

After downloading, we need to install CoolTerm program file, and we take PC Window system as an example.

1)  Choose“win”to download the zip file of CoolTerm

2)  Unzip the file and open it. (also suitable for Mac and Linux system)

![](media/97f831d38df9ee01dcfedac244bfe281.png)

![](media/e77548d01727e523e9e8c900d2fa962d.png)

\(3\) Double-click![](media/5f29eed25fc16602cfc0716f047c2da1.png).（Please make sure that the driver of Micro:bit is installed and the main board is connected to the computer.)

![](media/74fd81c83f0c0a26b4e299b93ce4ede4.png)

The functions of each button on the Toolbar are listed below:

![](media/70bebd79d7cd20336ae394c916500a28.png)


|                                                                      |                                                  |
|----------------------------------------------------------------------|--------------------------------------------------|
|![](media/2b728375ed2b8cd288c884e553418001.png)|Opens up a new Terminal|
|![](media/5f972f2eac5050ca0107416b2be067c2.png)|Opens a saved Connection|
|![](media/be6f8b560e0afc447f9c32b4474f633f.png)|Saves the current Connection to disk|
|![](media/52257d028694a313fc4eea4d9c2469d7.png)|Opens the Serial Connection|
|![](media/6ad366842b18084553a142ab82a613cf.png)|Closes the Serial Connection|
|![](media/8fa3ac342549d33b6c9aa5a9e4688bea.png)|Clears the Received Data|
|![](media/c8d1dd8c3356b4938e143de1022e5842.png)|Opens the Connection Options Dialog|
|![](media/36e13c266fd4b9723d9db40fe30cd203.png)|Displays the Terminal Data in Hexadecimal Format|
|![](media/b505c71c3344036730b1d67f0c62a354.png)|Displays the Help Window|




## Projects

(Note: project 8.1 to 8.12 are basic courses conducted with the built-in sensors and LED dot matrix of the Micro:bit main board V2, while project 8.13 to 8.20 are extended courses)

### Project 1：Heart beat

![](media/8c3f540a07aab97e1608ba8770837f7b.png)

1.  **Description**

This project is easy to conduct solely with a micro:bit main board, a micro USB cable and a computer. The micro:bit will display a “flickering heart” pattern. This experiment serves as a starter for your to entry to the magical world of the micro:bit.

2.  **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the Web version of Makecode.

Import Hex profile [(How to import?)](#import-test-code)

Click“New Project”to drag blocks step by step

![](media/b14ace883d757d0dffb2adae9a035aaa.png)

3.  **Test Code**

Route to get test code（[How to load?](#import-test-code)）


|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code\Project 1：Heartbeat|Project 1：Heartbeat.hex|




Or you could edit code in the editing area.

Go to“Basic”→“show icon”.

Copy it again and place it into“forever”block.

Click“❤”to select“![](media/04fdfc9060943954e7938bb1a741d626.png)”.

![](media/7b7e9577c6993f443060015e141f9189.png)

Complete Program：|<p>

![](media/a04acf78eaaa7b404b7b9b034bcfb1cd.png)

</p>
<p>“on start”: command block runs once to start program.</p>
<p>The program under the block“forever”runs cyclically.</p>
<p>LED dot matrix displays“❤”</p>
<p>LED dot matrix shows“![](media/04fdfc9060943954e7938bb1a741d626.png)”</p>|




Click“JavaScript" to view the corresponding JavaScript code:

![](media/00e2115f7e171c91af90f27889395dde.png)

4.  **Test Result**

Download code to micro:bit and keep the USB cable connected. The LED dot matrix will display ❤ and
![](media/04fdfc9060943954e7938bb1a741d626.png)
ceaselessly.

([How to download?](#A11) [How to quick download?](#quick-download))

If the download is not success, try to disconnect the micro:bit from your computer and then reconnect them and reopen Makecode to try again.

### Project 2：Light A Single LED

![](media/8c3f540a07aab97e1608ba8770837f7b.png)

1.  **Description**

The LED dot matrix consists of 25 diodes arranged in a 5 by 5 square and placed at the intersection of row lines (X) and column lines (Y). We can control one of the 25 LEDs by setting coordinate points. For example, the first LED sits in the first line is (0,0）and the third LED positioned in the first line is (2,0）and others likewise.

![](media/41c834c1592b4ecbec3066082c25f10b.png)

2.  **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the Web version of Makecode.

Import Hex profile [(How to import?)](#import-test-code)

Click“New Project”to drag blocks step by step

3.  **Test Code**

Route to get test code（[How to load?](#import-test-code)）

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 2：Light A Single LED.hex|




Or you could edit code in the editing area.

A. Click“Led”→“more”→“led enable false”

B. Put it into the“on start”block, and click the drop-down triangle button to select“true”.![](media/435799818ee58f1d628e2b489a9d627e.png)

C. Enter“Led”→“toggle x 0 y 0”block, and drag it into“forever”，then alter“x 0”into“x 1”.

![](media/2a74b354ec30c63263a23ae2d5f326c8.png)

4.  Enter“Basic”→“pause (ms) 100”from“ , then move it to     the![](media/2a74b354ec30c63263a23ae2d5f326c8.png)block,     and set to delay     500ms.![](media/b3b41cd5bd85c0f9e87f387db59f0180.png)

5.  Duplicate code     string![](media/d3b6a973504ec50c1b631ed8eea42ff3.png)once     and place it     into“forever”block.![](media/c184abd0cd80bf6d97b2a2db5a06d6cc.png)

6.  Enter“Led”, and drag“plot x 0 y 0”into“forever”block，then alter“x 0     y 0”into“x 3 y 4”.

![](media/581bb86e609771d6bc64bd20911a435a.png)

7.  Replicate“pause (ms) 500”once and place it into“forever”block.

![](media/178ce1bef3b8b7112362fb61e7803ad7.png)

8.  Click“Led”→“unplot x 0 y 0”and set to“unplot x3 y 4”then copy“pause     (ms) 500”block once, and place it into“forever”block.

![](media/56b1ee20b10053ada305a20ec3a3c7b2.png)

Complete Program：

![](media/f19c365efafd84e76d058e97f7a6c50f.png)

“on start”: command block only runs once to start program.

Turn on LED dot matrix.

The program under the block “forever” runs cyclically.

Toggle the LED brightness at coordinate point “x 1 y 0”.

Toggle the LED brightness at coordinate point “x 1 y 0”.

Turn on the LED at coordinate point “x3，y4”.

Delay in 500ms

Turn off the LED at coordinate point “x3 y4”.

Click“JavaScript”to switch into corresponding JavaScript code:

![](media/472b93b10b3d00bef040ae15892f9c5d.png)

4.  **Test Result**

0.5s and the one in (3,4) shines for 0.5s and repeat this sequence.

([How to download?](#A11) [How to quick download?](#quick-download))

### Project 3：5 x 5 LED Dot Matrix

![](media/8c3f540a07aab97e1608ba8770837f7b.png)

1.  **Description**

Dot matrix is very commonplace in daily life, which has found wide applications in LED advertisement screens, elevator floor display, bus stop announcement and so on.

The LED dot matrix of Micro: Bit main board contains 25 Diodes. Previously, we have succeeded in controlling a certain LED via its position point. Supported by the same theory, we can turn on many LEDs at the same time to showcase patterns, digits and characters.

What’s more, we can also click”show icon“ to choose the pattern we like to display. Last but not the least, we can design patterns by ourselves as well.

2.  **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the Web version of Makecode.

3.  **Test Code**

Test Code1：

The route to get test code（[How to load?](#import-test-code)）

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 3：LED Dot Matrix-1.hex|




Or you could edit code step by step in the editing area.

Enter“Led”→“more”→“led enable false”n and place it into “on start” block

Click the drop-down triangle button to select“true”
![](media/976aaaf61e578c48e2f00f6d2a3fccc0.png)

Click“Led”, and move“plot x 0 y 0”into“forever”，then replicate“plot x 0 y 0”for 8 times, respectively set to“x 2”y 0”,“x 2”y 1”,“x 2”y 2”,“x 2”y 3”,“x 2”y 4”,“x 1”y 3”“x 0”y 2”,“x 3”y 3”,“x 4”y 2”.

![](media/81df51e221db7392c533cf8b1759c832.png)

Complete Program：|<p>

![](media/d44a44c5708aa9ea67a70220d3afde02.png)

</p>
<p>“on start”: command block only runs once to start program.</p>
<p>Turn on LED dot matrix.</p>
<p>The program under the block “forever” runs cyclically.</p>
<p>Toggle the LED brightness at coordinate point “x 2，y 0”, “x 2，y 1”,
“x 2，y 2”, “x 2，y 3”, “x 2，y 4”, “x 1，y 3”, “x 0，y 2”, “x 3，y 3”and“x 4，y 2”</p>|




Select“JavaScript" and“Python”to switch into JavaScript and Python language code:

![](media/2456980fec90ec5086f078165471889f.png)

Code 2：

The route to get test code（[How to load?](#import-test-code)）

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 3：LED Dot Matrix-2.hex|




Or you could edit code step by step in the editing area.

Enter“Basic”→“show number 0”block,

Duplicate it for 4 times, then separately set to“show number 1”,“show number 2”,“show number 3”,“show number 4”,“show number 5”.

![](media/80c1aea0724a89a4da5f565bf800ef90.png)

Click“Basic”→“show leds”, then put it into“forever”block，tick blue boxes to light LED and generate“↓”pattern.

![](media/dbbf7bb73084873f4aaa616a424647ee.png)

Move out the block“show string” from“Basic”block, and leave it beneath the“show leds” block

![](media/8fc9948d8a5e03e04ba647bafa4bbf72.png)

Choose“show icon”from“Basic”block, and leave it in the “forever “block

![](media/2a458d5d954be27aa61c9e4ec3840d65.png)

Enter“Basic”→“show arrow North”and leave it into“forever”block，then replicate“show arrow North”for 3 times，respectively set to“North East”,“South East”, “South West”,“North West”.

![](media/098ce1f29443c1e3161eb50579f69272.png)

Click“Basic”and drag the block“clear screen”into “forever”

![](media/f2eee7559182e26ed10ec4fd89f5bbf7.png)

Drag“pause (ms) 100”block from“Basic”block and set the delay to 500ms, then place it in “forever”below“ block.

![](media/037524a44342d33050fe9822b0ac6f45.png)

Complete Program:|<p>

![](media/20fed03d66e92ef565333d6f060b1267.png)

</p>
<p>“on start”: command block only runs once to start program.</p>
<p>LED dot matrix displays 1,2,3,4,5</p>
<p>Under the block “forever”，program runs cyclically.</p>
<p>Dot matrix shows the“↓” pattern</p>
<p>Dot matrix scrolls to show “Hello!”</p>
<p>“❤”is shown on dot matrix</p>
<p>LED dot matrix displays“North East”arrow.</p>
<p>The“South East”arrow shows up on LED dot matrix</p>
<p>The“South West”arrow appears up on LED dot matrix</p>
<p>The“North West”arrow is displayed on LED dot matrix</p>
<p>Clear the screen</p>
<p>Delay in 500ms</p>|




Select“JavaScript" and“Python”to switch into JavaScript and Python language code:

![](media/4c537c2e073066441fb23219619ecf09.png)

4.  **Test Result**

Upload code 1 and power the board , we will see the icon![](media/d4e278da768e447ed344d581e671f57a.png)

Upload code 2 and plug micro:bit in power, Micro: bit starts showing number 1, 2, 3, 4, and 5, then cyclically display![](media/d4e278da768e447ed344d581e671f57a.png),“Hello!”,
![](media/66b31365d42274ef94ce9a3fcea1cd6c.png),
![](media/39fe4029acb5fb675d875c58e382d148.png),
![](media/45fcde65eb80a942d3903e400a346587.png),
![](media/9e34fdb19d72918bde242994a3c94c1f.png) and
![](media/2a45fca9d836ce38674c347c70c81e02.png)patterns.

([How to download?](#A11) [How to quick download?](#quick-download))

### Project 4：Programmable Buttons

![](media/06be84fb11b1fd07cd0cbb392132b903.png)

1.  **Description**

![](media/2ff75a1d81bfe0228b83931a0b7cc860.png)Buttons can be used to control circuits. In an integrated circuit with a push button, the circuit is connected when pressing the button and but after release, it will break again. 

Both ends of the button like two mountains. There is a river in between.

The internal metal piece connect the two sides to let the current pass, just like building a bridge to connect two mountains.

The internal structure of the button is shown as follows: before pressing the button, 1 ,2 , 3 and 4 are turned on. However, 1, 3 or 1, 4 or 2, 3 or 2 and 4 are disconnected, which is only enabled when the button is pressed. ![](media/d2a204e61c768f18924150db58aee093.png)

Micro: Bit main board boasts three push buttons, two are programmable buttons(marked with A and B), and the one on the other side is a reset button. By pressing the two programmable buttons can input three different signals. We can press button A or B alone or press them together and the LED dot matrix shows A,B and AB respectively. Let’s get started.

2.  **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the Web version of Makecode.

3.  **Test Code**

Test Code 1：

Press buttons on micro:bit, micro:bit will display character strings.

The route to get test code（[How to load?](#import-test-code)）

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 4：Programmable Buttons-1.hex|




Or you could edit code step by step in the editing area.

Delete“on start”and“forever”firstly，then click“Input”→“on button A pressed”

A. Click“Basic”→“show string”;

B. Then place it into“on button A pressed”block, change
“Hello!”into“A”.![](media/aebeefcca33e544db91944881f0a9a68.png)

Copy code string![](media/aebeefcca33e544db91944881f0a9a68.png)once, tap the drop-down button“A”to select“B”and modify character“A”into“B”.![](media/6c6bcb6bbeaf8ed55b985e44fc734d61.png)

Copy![](media/aebeefcca33e544db91944881f0a9a68.png)once，and pull down the triangle button to select“A+B”and“show string “AB”

![](media/3e8bde170db9e02e9cee36b3ede184b7.png)

Complete Code:|<p>

![](media/1ad59546b238e9644160019cdb102ee4.png)

</p>
<p>Press button A on Micro: bit main board</p>
<p>Show the character “A”</p>
<p>Press button B on Micro: bit main board</p>
<p>Show the character “B”</p>
<p>Press button A and B at same time</p>
<p>Display the character “AB”</p>|




Select“JavaScript" and“Python”to switch into JavaScript and Python language code:

![](media/50c59105d5a2409eea809e6ce73cf740.png)

Code 2：

The route to get test code（[How to load?](#import-test-code)）

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 4：Programmable Buttons-2.hex|




Or you could edit code step by step in the editing area.

A. Click“Led”→“more”→“led enable false”,

B. Put it into the block“on start”，click drop-down triangle button to select“true”
![](media/976aaaf61e578c48e2f00f6d2a3fccc0.png).

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

A. Tap“Variables”→“Make a Variable...”→“New variable name：”

B. Enter“item”in the dialog box and click“OK”，then variable“item”is produced. And move“set item to 0”into“on start”block.

![](media/f3b557425067334957b8154c19cd1946.png)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

A. Click“Input”→“on button A pressed”.

B. Go to“Variables”→“ change item by 1 ”

C. Place it into“on button A pressed”and 1 is modified into 5.![](media/81ec128a3a4bb86fed7d2f78bab20447.png)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Duplicate![](media/81ec128a3a4bb86fed7d2f78bab20447.png)code string once，click the drop-down button to select“B”，then set 5 to
-5.![](media/a53f0e6deb299ba15c494547dec19259.png)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

A. Enter“Led”→“plot bar graph of 0 up to 0”

B. Keep it into“forever”block

C. Go to“Variables”to move“item”into 0 box，change 0 into 25.

![](media/3232608700bf086dd0474de156a9116d.png)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

A. Go to“Logic”to move out “if...true...then...”and “=”blocks，

B. Keep“=”into“true”box and set to “\>”

C. Select“item”in the“Variables”and lay it down at left box of
“\>”，change 0 into 25；

D. Enter“Variables”to drag“set item to 0”block into“if...true..then...”, alter 0 into 25.

![](media/e084eebe07357f95e892e7626ed3618a.png)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\(7\) A. Replicate code string![](media/e0de4c7488b48605b292df5d3dd798dc.png)once

B.“\>”is modified into“\<”and 25 is changed into 0,

C. Leave it beneath
![](media/e0de4c7488b48605b292df5d3dd798dc.png)code string.

![](media/7435b5faf1f74a4a533fb1d83626c674.png)

Complete Program：|<p>

![](media/e2d7143ce59218e14780e9370d973c51.png)

</p>
<p>“on start”: command block runs once</p>
<p>to start program.</p>
<p>Turn on LED dot matrix</p>
<p>Set the initial value of item to 0</p>
<p>Press button A on Micro:bit board</p>
<p>Change item by 5</p>
<p>Press button B on Micro:bit board</p>
<p>Change item by -5</p>
<p>The program under the block “forever” runs cyclically.Light on LED in dot matric to draw bar graph, light up up to 25 LEDs</p>
<p>If item is greater than 25</p>
<p>Then set item to 25</p>
<p>If item is less than 0</p>
<p>Then set item to 0</p>|




Click“JavaScript" to switch into JavaScript code:

![](media/21704f7ef37d6ed440545c28dbd93211.png)

4.  **Test Result**

After uploading test code 1 to micro:bit main board V2 and powering the board via the USB cable, the 5\*5 LED dot matrix shows A if button A is pressed, B if button B pressed, and AB if button A and B are pressed together.

After uploading test code 2 to micro:bit main board V2 and powering the board via the USB cable, when pressing the button A , the LEDs turning red increase by 5 while when pressing the button B the LEDs turning red reduce.

([How to download?](#A11) [How to quick download?](#quick-download))

### Project 5：Temperature Measurement

1.  **Description**

The Micro:bit main board is not equipped with a temperature sensor, but uses the built-in temperature sensor in NFR52833 chip for temperature detection. Therefore, the detected temperature is more closer to the temperature of the chip, and there maybe deviation from the ambient temperature.

In this project, we will seek to use the sensor to test the temperature in the current environment, and display the test results in the display data (device). And then control the LED dot matrix to display different patterns by setting the temperature range detected by the sensor.

Note: the temperature sensor of Micro:bit main board is shown below:

![](media/206c8ec1c3f11d2de8d0f42fdf5b6b47.png)

2.  **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the Web version of Makecode.

3.  **Test Code**

Test Code 1：

Micro:bit detects temperature

The route to get test code（[How to load?](#import-test-code)）

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 5：Temperature Measurement-1.hex|




Or you could edit code step by step in the editing area.

Go to“Advanced” →“Serial” →“serial redirect to USB”

Place it into “on start”

![](media/07637ee0425802f6a59eb6f6dd62ea5c.png)

Click“Serial”to drag out“serial write value x=0”

Move it into“forever”block

![](media/0e709be8f6acc9521f1f76a0fc32c792.png)

Go to“Input” →“temperature(℃)”

Place it into 0 box

Change x into Temperature

![](media/2143a993b073f763a2e770a7eea628d6.png)

Move“pause (ms) 100”from“Basic”block and place it in the“forever”block, and set the delay to 500ms.
![](media/0c03bc986e186751ac33b92e5052b26f.png)

Complete Program：|<p>

![](media/e1e316ab2c9727c9b5a36dd82a7ab11a.png)

</p>
<p>“on start”: command block runs once to start program.</p>
<p>Serial redirect to USB</p>
<p>The program under the block “forever” runs cyclically.</p>
<p>Serial writes Temperature</p>
<p>Delay in 500ms</p>|




Click“JavaScript" to view the corresponding JavaScript code:

![](media/0cb83e9f83fa0fd0344685f38913cb43.png)

Download code 1 to micro:bit board and keep USB cable connected, then tap the button
![](media/e0580d7886af95d2a4ea7cd9d40759ff.png):

( [How to quick download?](#quick-download))

![](media/0d3198e0cb5460c9820bc2f016c0d7c1.png)

Temperature data is shown below:

![](media/6177222069a9583f2d8314d592fdb916.png)

Through the test, the room temperature is 35℃when touching the NFR51822 chip of micro:bit; however, the temperature rises to 37℃ when it touches water cup.

Open CoolTerm, click Options to select SerialPort. Set COM port and 115200 baud rate(the baud rate of USB serial communication of Micro:bit is 115200 through the test). Click“OK”and“Connect”.

The serial monitor shows the current ambient temperature value, as shown below:

![](media/b3a18bca1b2a7b5337470735e5a0c5aa.png)

![](media/f78128c148de3862a3fe10d86f063e22.png)

![](media/13238e98c31d620f4ffd7742dd71c78d.png)



![](media/9c88bb875124738a55e5e0fd5bf957ca.png)

<

Code 2：

Micro:bit display different pictures by temperature(the temperature value in the code could be adjusted).

The route to get test code（[How to load?](#import-test-code)）

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 5：Temperature Measurement-2.hex|




Or you could edit code step by step in the editing area.

You could set temperature based on real situation.

Click“Led”→“more”→“led enable false”into“on start”，click drop-down triangle button to select“true”
![](media/976aaaf61e578c48e2f00f6d2a3fccc0.png)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

A. Go to“Logic”→“if..true...then...else”and “=” block;

B. Move“if..true...then...else” into“forever”block，then place“=”into“true”box.

![](media/28c4cf38fbacb05ca0e457146767757d.png)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

A. Change“=”into“≥”

B. Go to“Input”→“temperature(℃)”

C. Change 0 into 35.

![](media/2b0e3775540415849bf36f7d118a8599.png)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Tap“Basic”→“show icon”，copy it once and lay down them under the“if ...then” and else blocks, then click the drop-down triangle button to select“![](media/9fa58029eb504582ee5a915f591ea583.png)”.

![](media/43df31dacdcc06623c6e2289f1623461.png)

Complete Program：|<p>

![](media/75b4f8dfc29b2a45e718383972ff0dc4.png)

</p>
<p>“on start”: command block runs once to start program.</p>
<p>Turn on LED dot matrix</p>
<p>Under the block“forever”，program runs cyclically.</p>
<p>If the detected temperature≥35°，the next program will be executed.</p>
<p>Dot matrix shows“![](media/9fa58029eb504582ee5a915f591ea583.png)”</p>
<p>Otherwise, the another program will be executed under the else block</p>
<p>LED dot matrix displays “![](media/9fa58029eb504582ee5a915f591ea583.png)”</p>|




Click“JavaScript", the corresponding JavaScript code is shown below:

![](media/9424f8456bb544ca25a7c5a4ea6e852c.png)

4.  **Test Result**

Upload the Code 1 and plug in power. And the 5\*5 LED displays the ambient temperature. When pressing the temperature sensor, the temperature will grow on dot matrix. When the ambient temperature is less than 35℃, the 5\*5LED will show![](media/4b1765e12b413dc5d562f2a16d32392f.png). When the temperature is equivalent to or greater than 35℃, the pattern![](media/f2705fbc4886efcfaac96589ca255f66.png)
will appear.

([How to download?](#A11) [How to quick download?](#quick-download))

### Project 6：Geomagnetic Sensor

![](media/24c31bb0174e2ac672203e5c36c6875e.png)

1.  **Description**

This project mainly introduces the use of the micro:bit’s geomagnetic sensor. In addition to detecting the strength of the magnetic field, it can also be used to determine the direction, which is an important part of the heading and attitude reference system (AHRS) as well.

It uses FreescaleMAG3110 three-axis magnetometer. Its I2C interface communicates with the outside, and the range is ±1000µT, the maximum data update rate is 80Hz. Combined with an accelerometer, it can calculate the position. Additionally, it is applied to magnetic detection and compass blocks.

Then we could read the value detected by it to determine the location. We need to calibrate the micro:bit board when the magnetic sensor works. The correct calibration method is to rotate the micro:bit board.

In addition, the objects nearby may affect the accuracy of readings and calibration.

2.  **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the Web version of Makecode.

3.  **Test Code**

Test Code 1：

Press A on micro:bit, the value of compass is shown.

The route to get test code（[How to load?](#import-test-code)）

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 6：Geomagnetic Sensor-1.hex|




Or you could edit code step by step in the editing area.

A. Click“Input”→“more”→“calibrate compass”

B. Lay down it into block“on start”.

![](media/f0973c3116eb4faf2d4ca138bd057d45.png)

A. Go to“Input”→“on button A pressed”.

B. Enter“Basic”→“show number”, put it into“on button A pressed”block;

C. Tap“Input”→“compass heading(℃)”， and place it into“show number”

![](media/0d9b5a65740d9406848d9a360635982b.png)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

![](media/3dac0d4c18fe1334cb76de8a87bf150c.png)Complete Program：|<p>

![](media/3dac0d4c18fe1334cb76de8a87bf150c.png)

</p>
<p>①“on start”: command block only runs once to start program.</p>
<p>②Calibrate compass</p>
<p>③Press button A on Micro:bit main board</p>
<p>④Dot matrix shows the direction of compass heading</p>|




Select“JavaScript" and“Python”to switch into JavaScript and Python language code:

![](media/a3fa9018b3e83be04515297b5fd94b42.png)

Code Description：

Upload the code 1, plug in micro:bit via an USB cable.

As the button A is pressed, LED dot matrix indicates the“TILT TO FILL SCREEN”then enter the calibration interface. The calibration method:
rotate the micro:bit to make the LED dot matrix draw a square (25 LEDs are on), as shown in the following figure:

([How to download?](#A01) [How to quick download?](#quick-download))

![](media/acf3b8c0dee027d9e555fc708831f874.jpg)

The calibration will be finished until you view the smile pattern![](media/a4faf86fb027b2f4c3dacaeee5d47d2b.png)appear.

The serial monitor will show 0°, 90°, 180° and 270° when pressing A.

Code 2：

Make micro: bit board point to the north, south, east and west horizontally , LED dot matrix displays the corresponding direction patterns

The route to get test code（[How to load?](#import-test-code)）

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 6：Geomagnetic Sensor-2.hex|




![](media/66c4482e3bcd71e712a54f4d73044104.png)

This module can keep reading data to determine direction, and let arrow point to the current magnetic North Pole.

![](media/d1a4e9f62bdf690ba809ae35c347b233.png)

For the above picture, the arrow will point to the upper right when the value ranges from 292.5 to 337.5. Because 0.5 can’t be input in the code, the values we get are 293 and 338.

Link computer with micro:bit board by a micro USB cable, and program in MakeCode editor:

Enter“Input”→ “more”→“calibrate compass”

Move“calibrate compass”into“on start”

![](media/f0973c3116eb4faf2d4ca138bd057d45.png)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

A. Click“Variables”→“Make a Variable...”→“New variable name：”

B. Input“x”in the blank box and click“OK”, and the variable “x” is generated.

C. Drag out“set x to”into“forever”block

![](media/0ecd067449d3d52ce3ba751632129b54.png)

A. Go to“Input”→“compass heading(℃)”, and keep it into“0”box

![](media/a97f7ff675fc62533a9053b6c415652b.png)

Tap“Logic”→“if...then...else”, and place it into “forever”block, then click![](media/bf972b006ad6d05686352c4785e54994.png)icon for 6 times.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

A. Place“and”into“true”block

B. Then move“=”block to the left box of “and”

C. Click“Variables”to drag“x”to the left “0”box, change 0 into 293 and set to “≥”;

D. Then copy“x≥293”once and leave it to the right “0”box and set to“x\<338”

![](media/5ae5c284c0466f093c97b0e2ee44d5d6.png)

A. Go to“Basic”→“show leds”

B. Lay it down beneath
![](media/6dbd99f5a6e4abe8ffd450d19b8a857b.png)block, then click“show leds”and the pattern
![](media/eab025b80ef24f1d5351bd3e06221bad.png)appears.

![](media/fe40fd39ae6abce0721d19cf86ef136d.png)

A. Duplicate
![](media/6dbd99f5a6e4abe8ffd450d19b8a857b.png)for 6 times.

B. Separately leave them into the blank boxes behind “else if”.

C. Set to“x≥23 and x\<68”,“x≥68 and x\<113 ”,“x≥113 and x\<158 ”,“x≥158 and x\<203 ”,“x≥203 and x\<248 ”,“x≥248 and x\<293 ”respectively.

D. Then copy “show leds”for 7 times and keep them below the “else if.......then” block respectively.

E. Click the blue boxes to form the pattern“![](media/4c73992fa4dfc6a2735b49ea8f000ed6.png)”,
“![](media/0771b8fd797a3e945a01ec1525ba4a9d.png)”,
“![](media/41eb716a282d52483e8467704613d034.png)”,
“![](media/2cae18294b329c10ecdefd768d6954e0.png)”,
“![](media/14b893d1a7157d72209b975d0df8d890.png)”,
“![](media/c362406f55115926523a0f60e16828b6.png)”and
“![](media/3977e13fdec2bfbc7fc55f5dce4969a9.png)”.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Complete Program：








<td colspan="2"><p>

![](media/ca4bc854081faf63bb13b2db448fa284.png)![](media/5e3330d735a144c4a6461ece221db219.png)

</p>
<p>“on start”: command block only runs once to start program.</p>
<p>Calibrate compass</p>
<p>The program under the block “forever” runs cyclically.</p>
<p>Store the angle of the compass heading into the variable x</p>
<p>When 293≤x&lt;338，the next program will be executed</p>
<p>

![](media/eab025b80ef24f1d5351bd3e06221bad.png)

<
appears on the dot matrix</p>
<p>When 23≤x&lt;68，the next program will be executed</p>
<p>

![](media/4c73992fa4dfc6a2735b49ea8f000ed6.png)

<is displayed on dot matrix</p>
<p>When 68≤x&lt;113, the next program will be executed</p>
<p>

![](media/0771b8fd797a3e945a01ec1525ba4a9d.png)

<
is shown on dot matrix</p>
<p>When 113≤x&lt;158，the next program will be executed</p>
<p>

![](media/41eb716a282d52483e8467704613d034.png)

<pattern appears</p>|
|<p>

![](media/2ca9ab458e80a2c3ec7002c15b74235e.png)![](media/99ec247ce0be9850c92e8fdfc1fc5d63.png)

</p>
<p>When 158≤x&lt;203, the next program will be executed.</p>
<p>Dot matrix shows ![](media/2cae18294b329c10ecdefd768d6954e0.png)</p>
<p>When 203≤x&lt;248, the next program will be executed.</p>
<p>Dot matrix displays ![](media/14b893d1a7157d72209b975d0df8d890.png)</p>
<p>When 248≤x&lt;293, the next program will be executed.</p>
<p>Dot matrix shows ![](media/c362406f55115926523a0f60e16828b6.png)</p>
<p>When x is not among the above rang, the next program will be executed under else block</p>||




Select“JavaScript" and“Python”to switch into JavaScript and Python language code:

![](media/7140a86db633ec1bb6ec7e07a109a0dc.png)

![](media/1d4fdac44bf4e1629145fac97f627c24.png)

4.  **Test Result**

Upload code 2 and plug micro:bit into power. After calibration, tilt the micro:bit board, and the LED dot matrix displays the direction signs.

([How to download?](#A11) [How to quick download?](#quick-download))

### Project 7：Accelerometer 

![](media/24c31bb0174e2ac672203e5c36c6875e.png)

1.  **Description**

The micro:bit board has a built-in Freescale MMA8653FC three-axis acceleration sensor (accelerometer). Its I2C interface works on external communication, the range can be set to ±2g, ±4g, and ±8g, and the maximum data update rate can reach 800Hz.

When the Micro:bit is stationary or moving at a constant speed, the accelerometer only detects the gravitational acceleration; when the Micro:bit is slightly shaken, the acceleration detected is much smaller than the gravitational acceleration and can be ignored. Therefore, in the process of using Micro:bit, the main purpose is to detect the changes of the gravitational acceleration on the x, y, and z axes when the attitude changes.

For this project, we will introduce the detection of several special postures by the accelerometer.

2.  **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the Web version of Makecode.

3.  **Test Code**

Test Code 1：

The route to get test code（[How to load?](#import-test-code)）

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 7：Accelerometer-1.hex|




Or you could edit code step by step in the editing area.

\(1\) A. Enter“Input”→“on shake”，

B. Click“Basic”→“show number”, place it into“on shake”block, then change 0 into 1.![](media/b86b68744e64e4e9907ccb1fa0cb2af7.png)

\(2\) A. Copy code string
![](media/b86b68744e64e4e9907ccb1fa0cb2af7.png)for 7 times, and separately click the triangle button to select“logo up”,“logo down”,“screen up”,“screen down”,“tilt left”,“tilt right”and“free fall”, then respectively change 1 into 2, 3, 4, 5, 6, 7, 8.

Complete Program：








<td colspan="2"><p>

![](media/75e625fbae54fd3d76cf6c4967d87415.png)

</p>
<p>Shake the Micro:bit board</p>
<p>LED dot matrix displays 1</p>
<p>The log is up</p>
<p>LED dot matrix displays 2</p>
<p>The logo is down</p>
<p>LED dot matrix displays 3</p>
<p>The screen is up</p>
<p>LED dot matrix displays 4</p>|
|<p>

![](media/3fc45754cb7a060d660212c5cb8c268f.png)

</p>
<p>The screen is down</p>
<p>Number 5 is shown</p>
<p>The Micro:bit board is tilt to the left</p>
<p>Number 6 is displayed</p>
<p>The Micro:bit board is tilt to the right</p>
<p>Number7 is displayed</p>
<p>When the Micro:bit board is free fall</p>
<p>LED dot matrix shows 8</p>||




Click“JavaScript", you will view the corresponding JavaScript code:

![](media/ffd55d004aee7f100e1a2608c90f1c7c.png)

Code 2：

Detect the value of acceleration speed at x, y and z axis

The route to get test code（[How to load?](#import-test-code)）

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 7：Accelerometer-2.hex|




Or you could edit code step by step in the editing area.

A. Go to“Advanced”→“Serial”→“serial redirect to USB”

B. Drag it into“on start”

![](media/8c0cfdd76322ebf7febafa519e98b76f.png)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

A. Enter“Serial”→“serial write value x =0”

B. Leave it into“forever”block

![](media/1dcff6f8c61c0c7ac220ded584bcf988.png)

A. Click“Input”→“acceleration(mg) x”；

B. Keep it into“0”box and capitalize the“x”

![](media/3f132064ad2081eabf6269eb4c0e698b.png)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Go to“Basic”and place“pause (ms) 100”into “forever”, then set the delay to 100ms.

![](media/98c688ae175b0c5eca6bed1d95f7b301.png)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Replicate code string![](media/c013533f2e3a02f26116f176ba6f975b.png)

for 2 times and keep them into“forever”block，separately set the whole code string as follows:

![](media/e11b467aef3999050e8a3b5cd175dce9.png)

Complete Program：

![](media/57fec5e7a6bda76b8ddc6c3538b58010.png)

“on start”: command block runs once to start program.

Serial redirects to USB

The program under the block “forever” runs cyclically.

Serial write value “X”=acceleration value on x axis

Serial write value “Y”=acceleration value on y axis

Serial write value “Z”=acceleration value on z axis

Click“JavaScript" to view the corresponding JavaScript code:

![](media/381a6d80fa940cb21ad6963469eef351.png)

Download code 1 to micro:bit board, keep USB cable connected and click![](media/e310a9105faecbe6ed8400101a4e852d.png)

([How to quick download?](#quick-download))

![](media/821a64a53c3a9709ff556e71b070f4dd.png)

After referring to the MMA8653FC data manual and the hardware schematic diagram of the Micro: Bit main board V2, the accelerometer coordinate of the Micro: Bit V2 motherboard are shown in the figure below:

The following interface shows the decomposition value of acceleration in X axis, Y axis and Z axis respectively, as well as acceleration synthesis (acceleration synthesis of gravity and other external forces).

![](media/6303a0ac122680207fe856d9be38d01c.png)

![](media/ded4e05f2b15d694e2061159628574dc.png)

If you're running Windows 7 or 8 instead of Windows 10, it won't be able to match devices via Google Chrome. You'll need to use the CoolTerm serial monitor software to read data.

You could open CoolTerm software, click Options, select SerialPort, set COM port and put baud rate to 115200 (after testing, the baud rate of USB SerialPort communication on Micro: Bit main board V2 is 115200), click OK, and Connect. The CoolTerm serial monitor shows the data of X axis, Y axis and Z axis , as shown in the figures below :

![](media/b4f4201cccf6ac0dadffb952b7596895.png)

4.  **Test Result**

After uploading the test code 1 to micro:bit main board V2 and powering the board via the USB cable, if we shake the Micro: Bit main board V2, no matter at any direction, the LED dot matrix displays the digit “1”.

([How to download?](#A01) [How to quick download?](#quick-download))

When it is kept upright （make its logo above the LED dot matrix）, the number 2 shows.

![](media/1600323e3e61e331c248cbeda5ccdcfc.jpg)

When it is kept upside down( make its logo below the LED dot matrix) , it shows as below.

![](media/3be80acf957e53117f695801ce19c449.jpg)

When it is placed still on the desk, showing its front side, the number 4 appears.

When it is placed still on the desk, showing its back side, the number 5 exhibits.

When the board is tilted to the left , the LED dot matrix shows the number 6, as shown below.

![](media/326095934bcff0a925b4f9a09d6cf7d2.jpg)

When the board is tilted to the right , the LED dot matrix displays the number 7, as shown below:

![](media/185b0ac204e9b2c54dd8fa93d852568c.jpg)

When the board is knocked to the floor, this process can be considered as a free fall and the LED dot matrix shows the number 8. (Please note that this test is not recommended for it may damage the main board.)

Attention: if you’d like to try this function, you can also set the acceleration to 3g, 6g or 8g.

### Project 8：Light Detection

![](media/8c3f540a07aab97e1608ba8770837f7b.png)

1.  **Description**

In this project, we focus on the light detection function of the Micro:
Bit main board V2. It is achieved by the LED dot matrix since the main board is not equipped with a photoresistor.

When the light irradiates the LED matrix, the voltage change will be produced. Therefore, we could determine the light intensity by voltage change.

2.  **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the Web version of Makecode.

Import Hex profile [(How to import?)](#import-test-code)

Or click“New Project”and drag blocks step by step

3.  **Test Code**

The route to get test code（[How to load?](#import-test-code)）

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 8：Light Detection.hex|




Or you could edit code step by step in the editing area.

(1)A. Enter“Advanced”→“Serial”→“serial redirect to USB”;

B. Drag it into“on start”block.![](media/8c0cfdd76322ebf7febafa519e98b76f.png)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\(2\) A. Go to“Serial”→“serial write value x =0”;

B. Move it into“forever”![](media/1dcff6f8c61c0c7ac220ded584bcf988.png)

A. Click“Input”→“acceleration(mg) x”

B. Put“acceleration(mg) x”in the“0”box and change “x”into“Light intensity”.

![](media/222517cdc77eb80d0a844a8de7c72d17.png)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

A. Click“Basic”→“pause (ms) 100”;

B. Lay it down into“forever”and set the delay to 100ms.

![](media/9ba8558c0d520cc80b01080e437ddff5.png)

Complete Program：|<p>

![](media/1ae769b6a1d9f6c6a393351c69b10d32.png)

</p>
<p>“on start”: command block runs once to start program.</p>
<p>Serial redirects to USB</p>
<p>The program under the block“forever”runs cyclically.</p>
<p>Serial write value “Light intensity”</p>
<p>= light level</p>
<p>Delay in 100ms</p>|




Click“JavaScript" to switch into the corresponding JavaScript code:

![](media/7739b4e9b0603e04cdeb1c7051b9d2f8.png)

4.  **Test Result**

Download code to micro:bit board don’t plug off the USB cable and click![](media/e310a9105faecbe6ed8400101a4e852d.png)

([How to quick download?](#quick-download))

![](media/04b472326485cf676cdb4dd61ca6ef1a.png)

The intensity value is 0 when covering the LED dot matrix. And the value varies with the light intensity. When placing micro:bit under the sunlight, the stronger the light is, the larger the intensity value will be. As shown below:

![](media/d7f1751ea1e6f251376dee5390ed21fa.png)

Open“CoolTerm”, click“Options”to select “SerialPort”, and set “COM” port and 115200 baud rate(the baud rate of USB serial communication of micro:bit is 115200 through the test).

Then click“OK”and“Connect”.

The light intensity value is shown below:

![](media/77a6de8ab9b171353693610a09f3a83c.png)

### Project 9：Speaker

![](media/ac515b9ae8891dc32f368a29f194a2fb.png)

1.  **Description**

Micro: Bit main board has an built-in speaker, which makes adding sound to the programs easier. It can also be programmed to produce all kinds of tones, like playing the song *Ode to Joy.*

2.  **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the Web version of Makecode.

Import Hex profile [(How to import?)](#import-test-code)

Or click“New Project”and drag blocks step by step

3.  **Test Code**

The route to get test code（[How to load?](#import-test-code)）

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 9：Speaker.hex|




Or you could edit code step by step in the editing area.

Enter“Basic”module to find “show icon”and drag it into“on start”block;

Click the little triangle to find
“![](media/7f7aa904c35f83b61c7c560ad1e40d2a.png)”

![](media/fed4c4f6e66e6d53fa2d8e10f01268fd.png)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\(2\) Enter“Music”module to find and drug“play sound giggle until done”
into “forever”block;

Enter“Basic”module to find and drug“pause(ms) 100” into “forever” block
;

Change 100 into 1000;

![](media/2a264656778216144131c75fabbbabf2.png)

( 3 ) Copy
![](media/39f8b940e6a1a3e8dbfa8eae70aa10c3.png)
three times and place it into “forever” block ;

Click the little triangle to select “happy”,”hello”,”yawn”;



![](media/a8cee1c98866343f817d29e2ed97c584.png)

<

Complete Program：

![](media/ebd84db5c527208b9fa4c7bfd91c50a5.png)

①““on start”: command block runs once to start program.

②LED displays“![](media/7f7aa904c35f83b61c7c560ad1e40d2a.png)”

③The program under the block“forever”runs cyclically.

④The buzzer will sound“giggle”

⑤Delay in 1000ms

⑥The buzzer will sound“happy”

⑦Delay in 1000ms

⑧The buzzer will sound“hello”

⑨Delay in 1000ms

⑩The buzzer will sound“yawn”

⑪Delay in 1000ms

Select “JavaScript" and “Python” to switch into JavaScript and Python language code:

![](media/984405217312d495104129a784ef76de.png)

4.  **Test Result**

After uploading the test code to micro:bit main board V2 and powering the board via the USB cable, the speaker utters sound and the LED dot matrix shows the logo of music.

([How to download?](#A11) [How to quick download?](#A12))

([How to download?](#A11) [How to quick download?](#A12))

### Project 10：Touch-sensitive Logo

![](media/644695850097c5ade080bb4848b4b481.png)

1.  **Description**

The Micro: Bit main board V2 is equipped with a golden touch-sensitive logo, which can act as an input component like an button.

It contains a capacitive touch sensor that senses small changes in the electric field when pressed (or touched), just like your phone or tablet screen. When you press it , the program can be activated.

2.  **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the Web version of Makecode.

Import Hex profile [(How to import?)](#import-test-code)

Or click“New Project”and drag blocks step by step

3.  **Test Code**

The route to get test code（[How to load?](#import-test-code)）

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 10：Touch-sensitive Logo.hex|




Or you could edit code step by step in the editing area.

( 1 ) Delete block“on start”and“forever”;

( 2 )Enter“Input”module to find and drag“on logo pressed” ;

Click the little triangle to find“touched”;

![](media/b228ddd2c400e6cc11be3a87636c27be.png)

( 3 ) Enter module“Variables”→choose“Make a Variable”→input“start”→click“OK”

The variable“start”is established;

Enter“Variables”module to find and drag “set start to 0” into “on logo touched”block;

![](media/f425f9f9545f2d8300fbb0c8946b9ea3.png)

( 4 )Enter“Input”module →click “more”→ find and drag“running time(ms)”into the“0”of“set start to 0”block;

![](media/7af1f7fa05580ed5d588daf80351182c.png)

( 5 )Enter“Basic”module to find and drag“show icon❤”into “on logo touched”block;

![](media/931663a2485eca2baa411b43484e5cc3.png)

( 6 )Enter“Input”module to find and drag“on logo pressed”→choose
“released”→ establish variable “time”;

Enter“Variables”module to find and drag “set time to 0”into “on logo pressed”block;

Enter“Math”module to find and drag “0-0”into the “0”of“set start to 0”block;

![](media/f2b9c02043be64c98da2e0ded2181082.png)

( 7 )Enter“Input”module→ “more” → find and drag “running time(ms)” into
“0”on the left side of “0-0”;

Enter“Variables”module to find and drag“start” into “0”on the right side of “0-0”;

![](media/09e205a5774658821e5a988b63b39203.png)

( 8 )Enter“Basic”module to find and drag“show number” into “on logo released”block;

Enter“Math”module to find and drag“square root 0” into“0”; Click the little triangle to find”integer÷”;

![](media/5056fe4add2914acf570df6706ce0bb7.png)

( 9 ) Enter“Variables”module to find and drag“time”into“0”on the left side of“0-0”and change the“0”on the right side to”1000”;
![](media/a2247b14f9957f856485a927cfa7186e.png)

Complete Program：

![](media/bb847ad951cd721972d24fe0b90631a1.png)

①Touch the logo on the Microbit mainboard 

- ②Assign the running time value to the variable   start

③LED display“❤”pattern

③Release the logo by hand

-  ④Assign the value of running time- variable start   to variable time

- 

<!-- -->

- ⑤LED dot matrix display variable time divided by   1000 rounded

- 

Select“JavaScript" and“Python”to switch into JavaScript and Python language code:

![](media/15d6364778e29d2a05442c6cf01cc88d.png)

![](media/f63f0917317e2f8542961a88a5e6827f.png)

4.  **Test Result**

via the USB cable, the LED dot matrix exhibits the“❤” pattern when the touch-sensitive logo is pressed or touched and displays digit when the logo is released.

([How to download?](#A11) [How to quick download?](#A12))

### Project 11：Microphone

![](media/3073a8af772ab91ecf264843b37d3b74.png)![](media/7f0741158e734ff8449d5b87d5ba85f4.png)

1.  **Description**

The Micro: Bit main board has a built-in microphone, which can test the volume of ambient environment. When you clap, the microphone LED indicator turns on. Furthermore, it can measure the intensity of sound, thereby you can make a noise scale or disco lighting changing with music.

The microphone is placed on the opposite side of the microphone LED indicator and in proximity with holes that lets sound pass. When the board detects the sound, the LED indicator lights up.

2.  **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the Web version of Makecode.

Import Hex profile [(How to import?)](#import-test-code)

Or click“New Project”and drag blocks step by step

3.  **Test Code**

The route to get test code（[How to load?](#import-test-code)）

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 11：Microphone-1.hex|




Or you could edit code step by step in the editing area.

(1 ) Delete block“on start”and“forever”;

( 2 ) Enter“Input”module to find and drag“on loud sound”;

Enter“Basic”module to find and drag “show number”into “on loud sound”block ;

![](media/4fc47e876fa715d7e18b42f81aaf2f75.png)

( 3 )Copy
![](media/c7e2c46845a453f1de63b5e6f16af7fc.png)
once;

Click the little triangle of “lond” to choose”quiet”;

Click the little triangle of “❤” to choose”![](media/9a40d2f51ed0a372a82e559cdb2ca0dd.png)”;

![](media/2aa3293670d895afc772871026303399.png)

Complete Program：

![](media/b48689241988a3fda8de4e26ebd9a4ed.png)

①The microphone detects sound

②LED dot matrix display“❤”

③The microphone detects sound

④LED dot matrix display
“![](media/04fdfc9060943954e7938bb1a741d626.png)”

Select“JavaScript" and“Python”to switch into JavaScript and Python language code:

![](media/e366483e9d5c574f3ec520f30e31e5cd.png)

4.  **Test Results 1**

“❤””when you claps and pattern
![](media/04fdfc9060943954e7938bb1a741d626.png)
when it is quiet around.

([How to download?](#A11) [How to quick download?](#A12))

Code 2:

The route to get test code（[How to load?](#import-test-code)）

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 11：Microphone-2.hex|




Or you could edit code step by step in the editing area.

Enter“Advanced”module→ choose“Serial”to find and drag“serial redirect to USB”into “on start”block ;

![](media/8c0cfdd76322ebf7febafa519e98b76f.png)

<span Variable”→
input “maxSound”→click “OK”,variable ”maxSound”is established;</span>

Enter“Variables”module to find and drag“set maxSound to 0”into “on start”block ;

![](media/39347e31badf7d15710fc12f581ce7e1.png)

Enter“Logic”module to find and drag“if true then...else”into “forever” block ;

Enter“Input”module to find and drag “button A is pressed”into “then” ;

![](media/643d739679dd8891a240feda70868302.png)

<span number”into
“then” ;</span>

<span drag“maxSound”into
“0” ;</span>



![](media/eff0b22497be40e1826bccef95ceb0a4.png)

<

Establish variable“soundLevel”;

Enter“Variables”module to find and drag“set soundLevel to 0”into “else”;

<span into
“0”;</span>

![](media/c84fcdd7bfc4b545e420fa2d6a975bfe.png)

Enter“Led”module to find and drag“plot bar graph of 0 up to 0”into “else”;

Enter“Variables”module to find and drag“soundLevel”into the“0”behind “of”;

Change the “0”behind “up” to “255”;



![](media/adc684949503c334c505157743fdbc7b.png)

<

<span then”into
“else”block ;</span>

<span 0”into
“then” ;</span>

Enter“Variables”module to find and drag“soundLevel”into “0”on the left side of “0-0” ;

<span drag“maxSound”
into “0” on the right side;</span>



![](media/928f828756c965def348b56ef5299749.png)

<

Enter“Variables”module to find and drag“set maxSound to 0”into the second “then” ;

Enter“Variables”module to find and drag“soundLevel”into the “0” ;

![](media/d62369e61dcc9dba69b80c93b1c7c7e8.png)

Complete Program：

![](media/c42455108c20d4ae51546957ab4198bb.png)

Select“JavaScript" and“Python”to switch into JavaScript and Python language code:

![](media/4e327f5f9ed716e6cf27cccba674f1c3.png)

5.  **Test Results 2**

Upload test code 2 to micro:bit main board V2, power the board via the USB cable and click “Show console Device”as shown below.

( [How to quick download?](#A12))

![](media/e22507af4953df977269bbdb2463d69e.png)

When the sound is louder around, the sound value shows in the serial port is bigger as shown below.

![](media/50b81518d9f7925b0c20476ab1f64185.png)

What’s more, when pressing the button A, the LED dot matrix displays the value of the biggest volume( please note that the biggest volume can be reset via the Reset button on the other side of the board ) while when clapping, the LED dot matrix shows the pattern of the sound.

### Project 12：Bluetooth Wireless Communication

![](media/55b2424d88ba1ba8a711c49418ca8dc6.png)

1.  **Description**

The Micro: Bit main board V2 comes with a nRF52833 processor (with a built-in BLE(Bluetooth Low Energy) device Bluetooth 5.1 ) and a 2.4GHz antenna for Bluetooth wireless communication and 2.4GHz wireless communication. With the help of them, the board is able to communicate with a variety of Bluetooth devices, including smart phones and tablets.

In this project, we mainly concentrate on the Bluetooth wireless communication functions of this main board. Linked with Bluetooth, it can transmit code or signals. To this end, we should connect an Apple device (a phone or an iPad) to the board.

Since setting up Android phones to achieve wireless transmission is similar to that of Apple devices, so we don’t need to illustrate again.

2.  **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. IPhone device (phone /iPad) or Android phone.

3.  **Procedures**

For Apple devices, enter this link:
<https://www.microbit.org/get-started/user-guide/ble-ios/> with your computer first, and then click “Download pairing HEX file”to download the Micro: Bit firmware to a folder or desk, and
upload the downloaded firmware to the Micro:
Bit main board V2.



![](media/cfaf7f8ae83cbe2636c39162a78adc7f.png)

<

![](media/9118815df7403daaf3a5dc8b9967b200.jpg)

![](media/63f1faf124af4949b31d7a84cee19a92.png)

Open
![](media/27924fdb3d67692df7c63d8d0fb72287.png)to search “micro bit”in your App Store to download the APP micro:bit then click
“

![](media/962a57f92b78eea1f0e3e81463497a9c.png)

”.



![](media/66d1f34d8d4c52e2b7c0ce10e602a063.png)

<

Connect your Apple device with Micro: Bit main board V2:

Firstly, turn on the Bluetooth of your Apple device and open the APP micro:bit to select item “Choose micro:bit”to start pairing Bluetooth.

Please make sure that the Micro: Bit main board V2 and your computer are still linked via the USB cable.

![](media/34f5fbb1c0c371970d1aec6c59c5cbb5.png)

Secondly, click“Pair a new micro:bit”;

![](media/e20270a0ade9c00b61198b26fc2fd83b.png)

Following the instructions to press button A and B at the same time(do not release them until you are told to) and press Reset & Power button for a few seconds.

Release the Reset & Power button, you will see a password pattern shows on the LED dot matrix. Now , release buttons A and B and click Next.

![](media/c00520400ecd1f20f958c1c6d1a3c907.png)

![](media/cabc60d7f8a030f5c9d86ac7de6c7bd7.png)

Set the password pattern on your Apple device as the same pattern showed on the matrix and click Next.

![](media/9411a5280e6f3b0d45306a31f80c1b38.png)

Still click Next and a dialog box props up as shown below. Then click "Pair". A few seconds later, the match is done and the LED dot matrix displays the "√" pattern.

![](media/7b56c56e10415ac2881ac69448b4ad3c.png)![](media/803cb5cf5f7d595581a11f5e6b7e61ed.png)


![](media/dc570950dd81f427edb5ea58f50b3a7e.png)![](media/f72e83dc6276d520e82c349659106e1a.png)

<

After the match with Bluetooth, write and upload code with the App.

Click “Create Code” to enter the programming page and write code.

Click
![](media/f3e9cc7884f7bba807fa4633c429422b.png)
and the box
![](media/e081360be7c91b7a156b01a787e4a58c.png)
appears, and then select “Create √”.

![](media/d54bf2d1c01cd3c18544009b1f9dc5a0.png)

![](media/4e7a5d06a5f9a5a209ef5fbc005e9f62.png)

![](media/5bd84e8d293bf8c0c999c7f4e756cf30.png)

![](media/bd19bb4c97ad2a5bc300412b8eb93ede.png)

Name the code as “1 “and click
![](media/a32c2d832ab38d19eb623108143c744e.png) to save it.

![](media/25cf76f891c5eac7381b8095363a2748.png)

Click the third item“Flash”to enter the uploading page.  The default code program for uploading is the one saved just now and named "1" and then click the other "Flash" to upload the code program "1".

![](media/c1661720ea2eaa521ff31a778501eb23.png)

![](media/350abcbb09d431d40427f34c3764f2eb.png)

![](media/4863bf826f119805a6a9bf9c12d5ec81.png)

If the code is uploaded successfully a few seconds later, the App will emerge as below and the LED dot matrix of the Micro: Bit main board V2 will exhibit a heart pattern.

![](media/ebfd31347a0553de0be4e01636652a15.png)

Projects above all conduct with the built-in sensors and the LED dot matrix of the main board while the following ones will carry out with the help of external sensors of this turtle car.**（Attention：In order to avoid burning the the Micro:bit main board V2, please remove the USB cable and the external power from the board before fix it with the shield of the car; likewise, the USB cable and the external power should be cut from the main board before disconnect the shield from the board.)**

### Project 13：Seven-Color LED

![](media/804e502bd0692ecb92e2f2ac16727bfc.png)

1.  **Description**

This module consists of a commonly used LED with 7colors but in white appearance. It can automatically flash different colors to create fantastic light effects when high level is input like a normal LED.

2.  **Preparation**

- Insert the micro:bit board into the slot of keyestudio   4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the Web version of Makecode.

Import Hex profile [(How to import?)](#import-test-code) , or click“New Project”and drag blocks step by step(add MecanumRobot extension library first)

[**(How to add Mecanum_Robot extension?)**](#M11)

3.  **Test Code**

Code1:

Make the RGB light flash 7 lights alternatively.

Code path:

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 13：Colorful Lights-1.hex|




Or you could edit code step by step in the editing area.

1)  Click“MecanumRobotV2”→find and     drag![](media/1b7d690949953b411f6c2e623b51f0a9.png)to“on     start”;

Copy
![](media/1b7d690949953b411f6c2e623b51f0a9.png)
once;

Click the little triangle behind “Left”to choose“Right”：![](media/1b065b7fa2d2ddf1a6baafad8bf5c064.png)

Compete Program:

![](media/1b065b7fa2d2ddf1a6baafad8bf5c064.png)

①run“on start”once to start the program

②open the colorful light on the left of the car

③open the colorful light on the right of the car

Click“JavaScript" to view the corresponding JavaScript code: ：

![](media/c111933f0e49c4785c284cb34f6494aa.png)

Code2:

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 13：Colorful Lights-2.hex|




Or you could edit code step by step in the editing area.

1)  click“MecanumRobotV2” to find and     drag![](media/1b7d690949953b411f6c2e623b51f0a9.png)to“forever”;

Copy
![](media/1b7d690949953b411f6c2e623b51f0a9.png)
once;

Click the little triangle behind “Left”to choose“Right”：![](media/0baf5f83bcc2439212eba4d85eaa8a5d.png)

2)  Click“Basic”to find and     drag![](media/4acf410cb1c252408cf02c249890051e.png)
    and tap the little triangle to choose “1     second”![](media/c97a860956311188998d075dcc6871c9.png);

Copy
![](media/d0ce7b23b6f4546cfd8b146a4f1153dd.png)once and choose OFF
![](media/7d8a250effe60388a24f8b07a663e06d.png)and put them in forever.

Complete Program:

![](media/bdce981c0ae66ebe881ff85892b06384.png)

① In the "forever" instruction block, the program runs cyclically.

②Turn on the 2 colorful lights of the car.

③Wait for 1 second

④Turn off the 2 colorful lights of the car.

⑤Wait for 1 second

![](media/66e648293b33dfa43f965a0a00d1decc.png)

4.  **Test Result**

Download code 1 to micro:bit board and dial POWER switch to ON end, 2 RGB lights of smart car emit red, green, blue, indigo, dark red, yellow and white color cyclically.

Download code 2 to micro:bit board, 2 RGB lights will flash for 1 second and then stop flashing for 1 second, cyclically.

([How to download?](#A01) [How to quick download?](#quick-download))

### Project 14：4 WS2812 RGB LEDs

![](media/eecf79fe278bc8107ce6827f9668f560.png)

1.  **Description**

The driver shield cooperates 4 pcs WS2812 RGB LEDs, compatible with micro:bit board and controlled by P7. In this lesson, we will make the RGB LEDs display different colors by P7. In this lesson, 3 sets of test code are provided to make the 4 WS2812 RGB LEDs display different effects.

2.  **Preparation**

- Insert the micro:bit board into the slot of keyestudio   4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the Web version of Makecode.

Import Hex profile [(How to import?)](#import-test-code) , or click“New Project”and drag blocks step by step(add MecanumRobot extension library first)

[**(How to add Mecanum_Robot extension?)**](#M11)

3.  **Test Code**

Code 1：

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 14：WS2812 RGB LEDs-1.hex|




Or you could edit code step by step in the editing area.

a\. Enter“Neopixel” →“set strip to Neopixel at pin P0 with 24 leds as RGB (GRB format)”

b\. Place it into“on start”block，

c\. Signal end P7 of WS2812 RGB is controlled by P7 of micro:bit . So we set to P7.

d\. Smart car has 4 pcs WS2812 RGB lights, so set to 4 leads

![](media/253b37d2d45744f944fc3521af50855c.png)

Click“Neopixel”to move block“strip clear”into“on start”block.

![](media/9287db5ccffb51dd82e5d2a15d2fd2fc.png)

Click“Led” →“more” →“led enable(false)”and place it into“on start”block，

![](media/040bbee9d3d72767aa966da34e960edf.png)

Enter“Neopixel”to move block“strip show color red” into “forever” block

![](media/88de3d44c971c2369711430a893d7821.png)

Click“Basic”to move“pause (ms) 100”block into“forever”block

Then set the delay to 1000ms

![](media/ba93a1de285dc713513a788b420e3ce6.png)

Copy code string
![](media/e553a68f56eba016892b29528e711907.png)for eight times, and click red to respectively set to orange, yellow, green, blue, indigo, violet, purple and white.

Tap the triangle icon to select orange, yellow, green, blue, indigo, violet, purple and white.

![](media/156cd64dce0b25f741f7d2f9a08f8e5d.png)

Complete Code:|<p>

![](media/b2cdf8ccae177a77965bb692e7f0bff1.png)

</p>
<p>.“on start”: command block runs once to start program.</p>
<p>Set strip to Neopixel at pin P7 with 4 leads as RGB</p>
<p>Turn off 4pcs WS2812 RGB lights</p>
<p>The program under the block“forever”runs cyclically.</p>
<p>All RGB lights show red color</p>
<p>Delay in 1000ms</p>
<p>All RGB lights show orange color</p>
<p>Delay in 1000ms</p>
<p>All RGB lights show yellow color</p>
<p>Delay in 1000ms</p>
<p>All RGB lights show green color</p>
<p>Delay in 1000ms</p>
<p>All RGB lights show blue color</p>
<p>Delay in 1000ms</p>
<p>All RGB lights show indigo color</p>
<p>Delay in 1000ms</p>
<p>All RGB lights show violet color</p>
<p>Delay in 1000ms</p>
<p>All RGB lights show purple color</p>
<p>Delay in 1000ms</p>
<p>All RGB lights show white color</p>
<p>Delay in 1000ms</p>|




Click“JavaScript" to switch into the corresponding JavaScript code:

![](media/ce3ad2e98499f1b894338673ef1c6bbf.png)

Code 2：

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 14：WS2812 RGB LEDs-2.hex|




a\. Enter“Neopixel” →“set strip to Neopixel at pin P0 with 24 leds as RGB (GRB format)”

b\. Place it into“on start”block，

c\. Signal end P7 of WS2812 RGB is controlled by P7 of micro:bit . So we set to P7.

d\. Smart car has 4 pcs WS2812 RGB lights, so set to 4 leads

![](media/1b10418150f245ba56a4208755729094.png)

Click“Led” →“more” →“led enable(false)”and place it into“on start”block，

![](media/b25da8c6746a006656adcab30f6c9cec.png)

Click“Loops”to drag“for index from 0 to 4...do”into“forever”block

Change 4 into 3

![](media/9c42b551fc532d473414871e64c8a5ee.png)

Click“Neopixel”to move block“strip clear”into block“for index from 0 to 3...do”

![](media/aa478b7456e1860d1665cab16014fc13.png)

Tap“Neopixel”→“more”→“strip set pixel color at 0 to red”

Place it into“for index from 0 to 3...do”block

Click“Variables”to move“index”into 0 box

![](media/360081c03f2f475441c442a601334ce2.png)

Click“Neopixel”to move“strip show”into“for index from 0 to 3...do” block

![](media/51d0ac03e131f1c42b67f4fd2631a7a0.png)

Tap“Basic”to move “pause (ms) 100”block into“index from 0 to 3...do”and set the delay to 100ms.

![](media/eda2a23160cf34a76c1f4ab73118151d.png)

Replicate code string![](media/b8590766809462fa433eb907d60e8908.png)for eight times and place them into“forever”block.

Click red to respectively choose orange, yellow, green, blue, indigo, violet, purple and white.

Complete Code：|<p>

![](media/669d30b5bbc4bf1f5dea711b8c11cc39.png)

</p>
<p>“on start”: command block runs once to start program.</p>
<p>Set strip to Neopixel at pin p7 with 4 leads as RGB</p>
<p>The program under the block“forever”runs cyclically.</p>
<p>For index from 0 to 3, execute the program under do block</p>
<p>Turn off 4 pcs WS2812 RGB lights</p>
<p>Set index of WS2812 RGB lights to red color</p>
<p>Strip shows</p>
<p>Delay in 100ms</p>
<p>For index from 0 to 3, execute the program under do block</p>
<p>Turn off 4 pcs WS2812 RGB lights</p>
<p>Set index of WS2812 RGB lights to orange color</p>
<p>Strip shows</p>
<p>Delay in 100ms</p>
<p>For index from 0 to 3, execute the program under do block</p>
<p>Turn off 4 pcs WS2812 RGB lights</p>
<p>Set index of WS2812 RGB lights to yellow color</p>
<p>Strip shows</p>
<p>Delay in 100ms</p>
<p>

![](media/fd64aca351ebaaa0d5866e8b7d96cef8.png)

</p>
<p>.For index from 0 to 3, execute the program under do block</p>
<p>Turn off 4 pcs WS2812 RGB lights</p>
<p>Set the index of WS2812 RGB lights to green color</p>
<p>Strip shows</p>
<p>Delay in 100ms</p>
<p>For index from 0 to 3, execute the program under do block</p>
<p>Turn off 4 pcs WS2812 RGB lights</p>
<p>Set the index of WS2812 RGB lights to blue color</p>
<p>strip shows</p>
<p>Delay in 100ms</p>
<p>For index from 0 to 3, execute the program under do block</p>
<p>Turn off 4 pcs WS2812 RGB lights</p>
<p>Set the index of WS2812 RGB lights to indigo color</p>
<p>Strip shows</p>
<p>Delay in 100ms</p>
<p>For index from 0 to 17, execute the program under do block</p>
<p>Turn off all RGB on strip</p>
<p>Set the index of WS2812 RGB lights to violet color</p>
<p>Set all RGB lights to show violet color</p>
<p>Strip displays all changes</p>
<p>Delay in 100ms</p>
<p>For index from 0 to 17, execute the program under do block</p>
<p>Turn off all RGB on strip</p>
<p>Set the index of WS2812 RGB lights to purple color</p>
<p>Strip displays all changes</p>
<p>Delay in 100ms</p>
<p>For index from 0 to 17, execute the program under do block</p>
<p>Turn off all RGB on strip</p>
<p>Set the index of WS2812 RGB lights to white color</p>
<p>Strip displays all changes</p>
<p>Delay in 100ms</p>
<p>

![](media/f06b9905088a3d39373f78c947e64be3.png)

</p>
<p>For index from 0 to 3, execute the program under do block</p>
<p>Turn off 4 pcs WS2812 RGB lights</p>
<p>Set the index of WS2812 RGB lights to violet color</p>
<p>Strip shows</p>
<p>Delay in 100ms</p>
<p>For index from 0 to 3, execute the program under do block</p>
<p>Turn off 4 pcs WS2812 RGB lights</p>
<p>Set the index of WS2812 RGB lights to purple color</p>
<p>Strip shows</p>
<p>Delay in 100ms</p>
<p>For index from 0 to 3, execute the program under do block</p>
<p>Turn off 4 pcs WS2812 RGB lights</p>
<p>Set the index of WS2812 RGB lights to white color</p>
<p>Strip shows</p>
<p>Delay in 100ms</p>|




Click“JavaScript" to switch into the corresponding JavaScript code:

![](media/06ef211131608693b324de4564f211a9.png)

![](media/cc2c2fb3e0e8335d3958121a92b6e462.png)

Code 3：

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 14：WS2812 RGB LEDs-3.hex|




Or you could edit code step by step in the editing area.

a\. Enter“Neopixel” →“set strip to Neopixel at pin P0 with 24 leds as RGB (GRB format)”

b\. Place it into“on start”block，

c\. Signal end P7 of WS2812 RGB is controlled by P7 of micro:bit . So we set to P7.

d\. Smart car has 4 pcs WS2812 RGB lights, set to 4 leads



![](media/9301a19bcac1a66dd86d35282a6adb1c.png)

<


Click“Led” →“more” →“led enable(false)”and place it into“on start”block，

![](media/b25da8c6746a006656adcab30f6c9cec.png)

Click“Variables”→“Make a Variable...”

Input R to build up variable R

We create variable“G”and“B”in same way

Drag“set B to 0”into“on start”block

Copy“set B to 0”twice and click triangle button to choose G and B

![](media/ec1bcce927c0c29517f842427e055738.png)

Click“Loops”to get block“for index from 0 to 4...do”

Leave it into “forever”and change 4 into 3

![](media/00751ac422252c11b90e88d1dd5e5e1b.png)

Move block“set B to 0”into“for index from 0 to 3...do”block,

Click B to choose R

Go to“Math”to drag block“pick random 0 to 10”into 0 box

Change 0 into 10, 10 into 255

![](media/808240f2784ec6bf5cd696813178ad51.png)

Replicate block
![](media/141700e2baf4f6ec06126a7eabdd15c3.png)twice and place them into“for index from 0 to 3...do”block.

Click R to select G and B

![](media/18c0be6843e83bf51f99c240d0faa45c.png)

Tap“Neopixel”and move“strip clear”into“for index from 0 to 3...do”
block.

![](media/cbc6b59e73365b0038a11a465b775f18.png)

Go to“Neopixel”→“more”→“strip set pixel color at 0 to red”

Leave it in the block“for index from 0 to 3...do”block

Drag block“red 255 green 255 blue 255”into“red”box

Tap“Variables”to move“index”block into 0 box

Separately drag R , G and B into 255 box, as shown below:

![](media/965b62ff435a6c5b35ef77745474b976.png)

Click“Basic”to drag“pause (ms) 100” under block “strip.....B”

Set the delay to 500ms.

![](media/ef0a30f6ea2627dbee666c6a7139c404.png)

Click“Neopixel”to move“strip show”block under “pause(as) 500”

![](media/7d0ee3ddfa68a63b292c77709dc20e89.png)

Complete Code:|<p>

![](media/9004a799ddf2a0d952d4174efade0410.png)

</p>
<p>“on start”: command block runs once to start program.</p>
<p>Set strip to Neopixel at pin p7 with 4 leads as RGB(GRB format)</p>
<p>Set variable R to 0</p>
<p>Set variable G to 0</p>
<p>Set variable B to 0</p>
<p>The program under the block“forever”runs cyclically.</p>
<p>When the value of index is in 0-3, execute the program under do block</p>
<p>Set variable R to random number in 10-255</p>
<p>Set variable G to random number in 10-255</p>
<p>Set variable B to random number in 10-255</p>
<p>Turn off all RGB on strip</p>
<p>Set index of 4 pcs WS2812 RGB lights to RGB(red, green, blue)</p>
<p>Delay in 500ms</p>
<p>Strip shows</p>|




Click“JavaScript" to switch into the corresponding JavaScript code:

![](media/212ce3c897c73c055c793752591102dc.png)

4.  **Test Result**

Download code 1 to micro：bit, and dial POWER to ON end. All four WS2812RGB LEDs light up a different color a time cyclically.

Download code 2 to micro：bit, WS2812RGB LEDs display like flow light.

Download code 3 to micro：bit, every WS2812RGB light shows random color one by one.

([How to download?](#A01) [How to quick download?](#quick-download))

### Project 15：Servo

![](media/ae51208a3f560ad6edefe370eb588c13.png)

1.  **Description**

For those DIY smart cars, they often have the function of automatic obstacle avoidance. In the DIY process, we need to use a servo to control the ultrasonic module to rotate left and right, and then detect the distance between the car and the obstacle, so as to control the car to avoid the obstacle. If other microcontrollers are used to control the rotation of the servo, we need to set a certain frequency and a certain width of pulse to control the servo angle.

However, if the micro:bit main board is used to control the servo angle, we only need to set the control angle in the development environment where the corresponding pulse will be automatically set to control the servo rotation. In this project, you will learn how to control the servo to rotate back and forth between 0° and 90°.

2.  **Information of the Servo**

Servo motor is a position control rotary actuator. It mainly consists of housing, circuit board, core-less motor, gear and position sensor. Its working principle is that the servo receives the signal sent by MCU or receiver, and produces a reference signal with a period of 20ms and width of 1.5ms, then compares the acquired DC bias voltage to the voltage of the potentiometer and obtains the voltage difference output.

![](media/69be958142b773acdae33eeef12afed7.png)For the servo used in this project, the brown wire is the ground, the red one is the positive wire, and the orange one is the signal wire.

The rotation angle of servo motor is controlled by regulating the duty cycle of PWM (Pulse-Width Modulation) signal. The standard cycle of PWM signal is 20ms (50Hz). Theoretically, the width is distributed between 1ms-2ms, but in fact, it's between 0.5ms-2.5ms. The width corresponds to the rotation angle from 0° to 180°. But note that for different brand motor, the same signal may have different rotation angle. 

![](media/49467dfa70799401a5a5acc691014aee.png)

More details:

![](media/ddc74f62dc936c925d28d70a1a9c2214.png)

3.  **Parameters**

- Working voltage: DC 4.8V ~ 6V

- Operating angle range: about 180 ° (at 500 → 2500 μsec)

- Pulse width range: 500 → 2500 μsec

- No-load speed: 0.12 ± 0.01 sec / 60 (DC 4.8V) 0.1 ± 0.01 sec / 60 (DC   6V)

- No-load current: 200 ± 20mA (DC 4.8V) 220 ± 20mA (DC 6V)

- Stopping torque: 1.3 ± 0.01kg · cm (DC 4.8V) 1.5 ± 0.1kg · cm (DC 6V)

- Stop current: ≦ 850mA (DC 4.8V) ≦ 1000mA (DC 6V)

- Standby current: 3 ± 1mA (DC 4.8V) 4 ± 1mA (DC 6V)

4.  **　Preparation**

- Insert the micro:bit board into the slot of keyestudio   4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the Web version of Makecode

Import Hex profile [**(How to import?)**](#import-test-code) , or click“New Project”and drag blocks step by step(add MecanumRobot extension library first)

[**(How to add Mecanum_Robot extension?)**](#M11)

5.  **Test Code**

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 15：Servo.hex|




Or you could edit code step by step in the editing area.

1)  Click“Variables”; motor“Make a Variable name” create a variable     named“angle”; set the value to     0：![](media/6f5afff91a08cadd05caa1dbfda3a566.png);
    and then put it into“on     start”![](media/84aa43c617547629c6ab018cdc5dedf6.png);

(2)Click“Loops”to find and drag![](media/931d144427e762093f77c1ccf0f25422.png)to“forever”and change the number to“180”; click“MecanumRobotV2”to find and drag![](media/44064d42ba3784766ed2b3bd7f9a5bde.png)and put variable“angle”into
![](media/620f22e6a5c51998bac55eb189e93641.png);
put into![](media/931d144427e762093f77c1ccf0f25422.png)
and change the digit 0 to 180![](media/0746e3def9d7062499d34f5dfe16be04.png);

Click![](media/bc874b1942f1a9471481445e610d665b.png)
of “Variable” and
![](media/e6064b33ba089a52a096df76f0ac5673.png) of
“Math”; put variable”angle” on the left and change the umber on the right to 1:![](media/ba828b1c44af9db7c09d7a3da822eb52.png);put it into![](media/bc874b1942f1a9471481445e610d665b.png)：;Put
![](media/2e15452c0b7780dce74438e03575f989.png)behind![](media/620f22e6a5c51998bac55eb189e93641.png)and add delay in 10ms![](media/ab7ef2718c3ba5241c90eb2bfd1247dc.png);

Copy
![](media/ab7ef2718c3ba5241c90eb2bfd1247dc.png)once and change the “+”of
![](media/ba828b1c44af9db7c09d7a3da822eb52.png) to
“-”：![](media/2945c3f78c0a9eb3cc5e552361fd1039.png).

Complete Program:

![](media/087e18229bba5f7a01520f80f8c8187c.png)

① The "on start" command block runs only once to start the program.

②Set the initial value of the angle variable to 0.

③In the "forever" command box, the program runs cyclically

④Cycle 180 times

⑤Rotate the servo to angle

⑥ Angle variable increases 1

⑦ Delay in 10ms

⑧ Cycle 180 times

⑨The servo rotates to angle

⑩Angle angle variable minus 1

⑪ Delay in 10ms

Click“JavaScript" to view the corresponding JavaScript code: ：

![](media/2354311fc81b6b5dc9819544be60e356.png)

6.  **Test Result**

After uploading the test code and dial POWER switch to ON end, the servo rotates from 0 degree to 180 degrees.

([How to download?](#A01) [How to quick download?](#quick-download))

### Project 16：Motor

![](media/02a16adfdabb92d6de1796019e909b44.png)

1.  **Description**

The Keyestudio 4WD Mecanum Robot Car is equipped with 4 DC reduction motors, also called gear reduction motor, which is developed on the ordinary DC motor. It has a matching gear reduction box which provides a lower speed but a larger torque. Furthermore, different reduction ratios of the box can provide different speeds and torques.

Gear motor is the integration of gearmotor and motor, which is applied widely in steel and machine industry

Micro:bit motor driver shield comes with a DRV8833 chip. In order to save the IO port resource, we control the rotation direction and speed of 4 DC gear motors with the DRV8833 chip.

![](media/5b67b46bfb1c9d8b6bdeca1b98aa6bbf.jpg)

Front

![](media/4919ce3b3fa299f13aa33348165ed728.png)

Back

![](media/59c34b6eeef8ad7eb0ad8304426c207e.png)

![](media/8874ded0289da7d5d5a0141cc7b88769.png)

2.  **　Preparation**

- Insert the micro:bit board into the slot of keyestudio   4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the Web version of Makecode

Import Hex profile [**(How to import?)**](#import-test-code) , or click“New Project”and drag blocks step by step(add MecanumRobot extension library first)

[**(How to add Mecanum_Robot extension?)**](#M11)

3.  **Test Code**

Code 1：

|  |  |  |
|--|--|--|
|File Type|Route|File Name|
|Python file|..\2. Makecode Tutorial\Makecode Code|Project 16：Motor-1.hex|




Or you could edit code step by step in the editing area.

(1)Click“ MecanumRobotV2”to find and drag![](media/3017a4c47b2a4799211969fc4ce21431.png)
into“forever”;click the number behind speed to choose 75![](media/985053c970402019e2b0afe192bc75e0.png);

(2)Copy![](media/985053c970402019e2b0afe192bc75e0.png)four times; click the little triangle behind “Motor”to choose Lower_left，Upper_right，Lower_right respectively; and put them all in forever![](media/4840d3f08ec9f7c0275fd434508c912a.png);

(3)Click“Basic”to find and drag“pause (ms) 100”to“forever”;set delay in 2000ms![](media/a25e088e3c77ee16fe1b0935d9edf225.png);

(4)Click“MecanumRobot”to find and drag![](media/150c1bfa02df1e644c84ba32fb889fee.png)
to
![](media/a25e088e3c77ee16fe1b0935d9edf225.png);
copy
![](media/a25e088e3c77ee16fe1b0935d9edf225.png)
once and put it behind![](media/150c1bfa02df1e644c84ba32fb889fee.png).

Complete Program:

![](media/3a759dd8c19a12c8294cd4a56348e0b2.png)

① In the "forever" instruction block, the program runs cyclically.

②Set the left front motor speed to 75, and rotate clockwise.

③Set the speed of the left rear motor to 75 and the direction to rotate clockwise.

④Set the right front motor speed to 75 and the direction to rotate clockwise.

⑤Set the right rear motor speed to 75 and the direction to rotate clockwise

⑥The delay time is 2000 milliseconds

⑦4 motors stop rotating

⑧ Delay time 2000 milliseconds

⑦4 motors stop rotating

⑧ Delay time 2000 milliseconds

Click“JavaScript" to view the corresponding JavaScript code: ：

![](media/242ba6ca775c1ba73825d0affebe8495.png)

Code2：

Code path:

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 16：Motor-2.hex|




Or you could edit code step by step in the editing area.

Drag and copy![](media/e91c5fef0c025bd9de44a28cf59d3aa2.png)three times; click the little triangle behind”run”to choose as shown![](media/cf2444064b87720b5b46594f5ed6a1c2.png)，
![](media/b5270c6c0e52b74e77cf4cd9e139f076.png)， ，
![](media/d69b7c823cc3d2f2dfae31c4bec643a4.png)And then put they all in forever and add
![](media/44b76cae1d08f206e202e53e84191baf.png).

Complete Program:

![](media/a3a9d39aafc4162630ad4740cbc08462.png)

① In the "forever" instruction block, the program runs cyclically.

②Set the left front motor speed to 75 and the direction to rotate forward.

③Set the speed of the rear left rear motor to 75 and the direction to rotate forward.

④Set the right front motor speed to 75 and the direction to rotate forward.

⑤Set the right rear motor speed to 75 and the direction to rotate forward.

⑥Wait for 2 seconds

⑦Set the left front motor speed to 75, and the direction is reversed.

⑧ Set the motor speed at the left rear to 75, and the direction is reversed.

⑨Set the right front motor speed to 75, and the direction is reversed.

⑩Set the right rear motor speed to 75, and the direction is reversed.

⑪Wait for 2 seconds

⑫Set the left front motor speed to 75, and the direction is reversed.

⑬Set the motor speed at the left rear to 75, and the direction is reversed.

⑭ Set the right front motor speed to 75 and the direction to rotate forward.

⑮ Set the right rear motor speed to 75, the direction is forward.

⑯Wait for 2 seconds

⑰ Set the left front motor speed to 75 and the direction to rotate forward.

⑱ Set the speed of the rear left motor to 75 and the direction to rotate forward.

⑲Set the front right motor speed to 75, and the direction is reversed.

⑳Set the right rear motor speed to 75, and the direction is reversed.

㉑Wait for 2 seconds

㉒The car stops

㉓Wait for 2 seconds

Click“JavaScript" to view the corresponding JavaScript code: ：

![](media/ee70b8466efde60855efa486fab502fa.png)

4.  **Test Result**

Download code 1 to micro:bit board, dial POWER switch to ON end. Smart car goes forward for 2s and stops for 2s.

Download code 2 to micro:bit board, the car goes forward for 2s, turns back for 2s, turn left for 2s, turn right for 2s and stops for 2s and repeats this pattern.

([How to download?](#A01) [How to quick download?](#quick-download))

### Project 17：Line Tracking Sensor

#### Project 17.1：Detect Line Tracking Sensor

![](media/ea7f6c8c87ab8a6aa921ad35f6569523.png)

1. Description

The motor driver board of the Keyestudio 4WD Mecanum Robot Car comes with a 3-channel line tracking sensor, which adopts TCRT5000 IR tubes and 3 potentiometers.

The TCRT5000 IR tube contains an IR emitting tube and an IR receiving tube. When the infrared signals of the emitting tube is received by the receiving tube through reflection, the resistance of the receiving tube will change, which is generally reflected in the voltage change on the circuit.  

The resistance varies depending on the intensity of the infrared signals received by the receiving tube, which is often in the color of the reflecting surface and the distance of the reflecting surface receiving tube.  At the time of detection, black is high level active and white is low level active. 

2.  **Working Principle**

When the car runs above a white road, the IR emitting tube installed under the car emits infrared signals to detect the road and the receiving tube will receive signals sending back. Then the output end outputs low level(0); when it detects black lines, it outputs high level(1).

After putting a white paper on the bottom of the 4WD Mecanum Robot Car, we will rotate the potentiometers on the 3-way tracking sensor. When the indicator light on the sensor module is on, pick up the car to make the two wheels on the 4WD Mecanum Robot Car separate. The height of the white paper is about 1.5cm, when the indicator light on the sensor module is off, and then the sensitivity is adjusted.

3.  **　Preparation**

- Insert the micro:bit board into the slot of keyestudio   4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the Web version of Makecode

Import Hex profile [**(How to import?)**](#import-test-code) , or click“New Project”and drag blocks step by step(add MecanumRobot extension library first)

[**(How to add Mecanum_Robot extension?)**](#M11)

4.  **Test Code**

Code 1：

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 17.1：Detect Line Tracking Sensor-1.hex|




Or you could edit code step by step in the editing area.

Click“Advanced”→“Serial”→“serial redirect to USB”

Place it into“on start”

![](media/73b63660eb8f378dea4930f354d04de6.png)

Click“Led”→“more”→“led enable(false)”and place it into“on start”block.

![](media/725e62a860bae23e61a8189d58ab17af.png)

Enter“Advanced”→“Serial”→![](media/9eb34e5ce5a67b9327096c00fb9036bc.png)

Leave it into“forever”block.

Input “left”and drag out block
![](media/c1dd7f8bc9f7c6eadc69c7e14651e815.png)

Click“MecanumRobotV2”, and drag out block
![](media/49b8d87a5ea9bea061c76df982013622.png)and place it behind the
![](media/f563baf7a888a937afb40dc40031b795.png).

Copy

![](media/e8983c9a50c5adce42954a3e59e3b259.png)once, and change Left to Center![](media/952605509cefdb4eb63e2f414bb5eab7.png)

.

Copy

![](media/f563baf7a888a937afb40dc40031b795.png)and change Left to Center![](media/952605509cefdb4eb63e2f414bb5eab7.png)

.

Copy

![](media/e8983c9a50c5adce42954a3e59e3b259.png)

<span right:
”</span>

![](media/8a3c060c3e3ec68e03b5dce19942b7e1.png)，and drag out block![](media/e16ec6add35ef78b91f5da5266b2ef86.png)

.

Find and drag out
![](media/49b8d87a5ea9bea061c76df982013622.png)<span>from“MecanumRobotV2”
and place it into</span>

![](media/e16ec6add35ef78b91f5da5266b2ef86.png)

，and then change Left to Right.

<span>
</span>

![](media/41bba2164e715dd5031a6e7c58c58f19.png)

<


Click“Basic”to find and drag“pause (ms) 100”to“forever”and set the delay to 200ms

<span>
</span>

![](media/765b1804f46b1b6369456ecdce8cf1c7.png)

<


Complete Program:

![](media/3683d83f8320256e3c74aa9a79aea314.png)

① The "on start" command block runs only once to start the program.

②Serial redirection USB.

③In the "forever" instruction block, the program runs cyclically.

④Write string "left:" serially

⑤Serially write the output value of the tracking sensor on the left

Serial write string "center"

Serially write the output value of the middle tracking sensor

⑥Serial write string "right:"

⑦Serially write the output value of the tracking sensor on the right

⑧Writing in line break

⑨ Delay time 200 milliseconds

Click“JavaScript" to view the corresponding JavaScript code: ：



![](media/4b4406164f393a90039758cbb655cbc8.png)

<

Open CoolTerm, click Options to select SerialPort. Set COM port and 115200 baud rate. Click“OK”and“Connect”.

The CoolTerm serial monitor displays the digital signals read by the line tracking sensors.

![](media/0141051aca98f66393c28ee23d34d734.png)

#### Project 17.2：Tracking Smart Car

![](media/d7b67de2bc904ba303a88a268dfac339.jpg)

1. Description

In this lesson we will combine a line tracking sensor with a motor to make a line tracking smart car.

The micro:bit board will analyze the signals and control the smart car to show the line tracking function.

2. Working Principle

The smart car will make different moves according to the value received by the 3-channel line tracking sensor.|Left line tracking sensor|Middle line tracking sensor|Right line tracking sensor|Binary values|Decimal value|Microbit 4WD Mecanum Robot Car V2.0的行动|
|LOW（0)|LOW（0|LOW（0|000|0|Stop|
|LOW（0)|LOW（0)|HIGH（1）|001|1|Turn Right|
|LOW（0)|HIGH（1）|LOW（0|010|2|Go forward|
|LOW（0)|HIGH（1）|HIGH（1）|011|3|Turn Right|
|HIGH（1）|LOW（0)|LOW（0|100|4|Turn Left|
|HIGH（1）|LOW（0)|HIGH（1）|101|5|Go forward|
|HIGH（1）|HIGH（1）|LOW（0|110|6|Turn Left|
|HIGH（1）|HIGH（1）|HIGH（1）|111|7|Stop|




3. Preparation

- Insert the micro:bit board into the slot of keyestudio   4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the Web version of Makecode

Import Hex profile [**(How to import?)**](#import-test-code) , or click“New Project”and drag blocks step by step(add MecanumRobot extension library first)

[**(How to add Mecanum_Robot extension?)**](#M11)

Warning: The 3-way tracking sensor should be used in environments without infrared interference such as sunlight. Sunlight contains a lot of invisible light, such as infrared and ultraviolet. In an environment with strong sunlight, the 3-way tracking sensor cannot work properly.

4. Flow Chart

![](media/73116cf35ab724e4f2abe63c40f5ca7d.emf)

5.  **Test Code**

Code path:

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|..\2. Makecode Tutorial\Makecode Code|




Or you could edit code step by step in the editing area.

Click“Variables”→“Make a Variable...”→“New variable name：”.

Input LL →“OK”，then the variable "LL" is established, and variable“CC”and“RR”are likewise.

Drag out“set RR to 0”and place into“on start”block, copy“set RR to 0”2 times and place into“on start”block.

Click the drop-down triangle button after RR to select LL and CC.

![](media/5f8355a3c9f96d54f91ed86b72321b22.png)

Click“led enable(false)”and place into“on start”block.



![](media/21df847083c4dd9474adc5eae2879b6c.png)

<

Click“Variables”, find and drag out “set RR to 0”into“forever”block.

Click the drop-down triangle button after RR to select LL and click“MecanumRobotV2”.

Find and drag out![](media/e8127d7dca199be6ab37125b77eceba3.png)and put it at the number 0 after to.

[Duplicate](C:\\Users\\NINGMEI\\AppData\\Local\\youdao\\dict\\Application\\9.0.1.1\\resultui\\html\\index.html#\\javascript:;)![](media/1e7830f494273fa198395ae1fe17560e.png)2times and place into“forever”block.

Change the second LL to CC，”Left”to”Center”and the third LL to RR，”Left”to ”Right”.



![](media/ef90823cb1df0b6659df1bd289ab4f80.png)

<

Click“Logic”, find and drag out“if true then...else”into“forever”block.

Click“

![](media/7498c9151101cb7e9756a8b0a5485f90.png)”7times to add else if, then click else![](media/1d83144e76d5b7d27d83fddff27ccb9f.png)

once to cancel else.

Find and drag out 2“and”block into
and block.



![](media/d79d4bbbed6b1f655e61355e58ab51e1.png)

<


<span is
[invariant](C:\\Users\\NINGMEI\\AppData\\Local\\youdao\\dict\\Application\\9.0.1.1\\resultui\\html\\index.html#\\javascript:;).</span>

[Duplicate](C:\\Users\\NINGMEI\\AppData\\Local\\youdao\\dict\\Application\\9.0.1.1\\resultui\\html\\index.html#\\javascript:;)“LL”2times and place it into and block.

Click the drop-down triangle button after to select CC and
<span is
[invariant](C:\\Users\\NINGMEI\\AppData\\Local\\youdao\\dict\\Application\\9.0.1.1\\resultui\\html\\index.html#\\javascript:;)</span>.



![](media/5bd34267befdc4a09590892b2fc2976f.png)

<


[Duplicate](C:\\Users\\NINGMEI\\AppData\\Local\\youdao\\dict\\Application\\9.0.1.1\\resultui\\html\\index.html#\\javascript:;)![](media/a4a84f3c536b14824e06379bfe790a23.png)7 times，and change o according to the below:



![](media/bb998512031314430075ab883bef60ec.png)

<

Click “Functions”of ”Advance”and click![](media/7bff09ac7145d2ee7d4e32e08fdb4f10.png).

<span>Change“doSomething”to
“car_forward”，“car_back”，“car_left”，“car_right”respectively.</span>



![](media/c581cb11a9bb05e397f8852e723195c8.png)

<

Click “Functions”of ”Advance”to find and drag
![](media/460d5b4f97487f6163fbdc629bc8c849.png) 2 times to the first and third else if.

Click “Functions”of ”Advance”to find and drag
![](media/ae70f5e341da2beb5bccb6f3188a6c9c.png) 2 times to the the fourth and the sixth else if and find and drag out
![](media/6f8a414e870e55bf08884a70d8368ed5.png) 2 times and put in the second one .

In the fifth and seventh Else if，click“MecanumRobotV2”,

if and drag![](media/ae70f5e341da2beb5bccb6f3188a6c9c.png)
to the first else if, find and drag![](media/b33aa5fba3096eabc60bff5f62e36d65.png)once, and place it into the first if.



![](media/8371a52f094cbf40df18eb70682b8201.png)

<



Complete Program:

![](media/4b1041553ed0d547c117292490fa6dfd.png)

。

Close the LED dot matrix

Set the variable LL to 0

Set variable
CCto 0

Set variable RR to 0

In the "forever" instruction block, the program runs cyclically.

The left tracking sensor reads the high and low levels and assigns the variable LL

The middle tracking sensor reads the high and low levels and assigns the variable
CC

The right tracking sensor reads the high and low levels and assigns the variable
RR

...................The left , middle and right tracking sensor all read 0

The car stop

.The left and middle tracking sensor all read 0

and the right tracking sensor reads 1

Turn right function

the middle
tracking sensor reads 1

...................Advance.function

...................The middle
.and right tracking sensor all read 1 and
the left tracking sensor reads 0

Turn right function

.The middle
.and right tracking sensor all read 0 and
the left tracking sensor reads 1

Turn left function

the middle
tracking sensor reads 0

Advance.function

The left and middle tracking sensor all read 1

and the right tracking sensor reads 0

Turn left function

...................The left, middle
.and right tracking sensor all read 1

...................Advance.function

![](media/a37b5961aac14dc526e6b06a0029e600.png)

![](media/3f8c9ca155ee96f39b06d853502d4840.png)

①forward function

②The left front motor rotates forward at a speed of 40

③The motor at the left rear rotates forward at a speed of 40

④The right front motor rotates forward at a speed of 40

⑤The right rear motor rotates forward at a speed of 40

⑥Backward function

⑦The left front motor reverses, the speed is 40

⑧The left rear motor reverses, the speed is 40

⑨The right front motor reverses, the speed is 40

⑩The right rear motor reverses, the speed is 40

⑪Left turn function

⑫The left front motor reverses, the speed is 60

⑬The left rear motor reverses at a speed of 60

⑭The right front motor rotates forward, the speed is 85

⑮　The right rear motor rotates forward, the speed is 85

⑯ right turn function

⑰ The left front motor rotates forward, the speed is 85

⑱ The left rear motor rotates forward, the speed is 85

⑲The right front motor reverses, the speed is 60

⑳ The right rear motor reverses, the speed is 60

Click“JavaScript"to view the corresponding JavaScript code:

![](media/f5caa06aeb3bb1944a0298f1bbf7ad86.png)



![](media/8f5f07ec0d28bb334447b50e857639fe.png)

<

5. Test Result

Download code to micro:bit and dial POWER to ON end, line tacking car goes forward along black line .

Note: turn on the switch at the back of micro:bit car.

the width of black line should be larger than the width of line tracking sensor.

Avoid to test smart car under the strong light.

### Project 18.：Ultrasonic Sensor

#### Project 18..1：Ultrasonic Ranging

1.  **Description**

The ultrasonic sensor uses sonar to determine distance to an object like bats do. It offers excellent non-contact range detection with high accuracy and stable readings in an easy-to-use package. It comes complete with ultrasonic transmitter and receiver modules.

The ultrasonic sensor is being used in a wide range of electronics projects for creating obstacle detection and distance measuring application as well as various other applications.

![](media/0180b169a1c3b228394b43df704fac32.png)

The ultrasonic module will emit the ultrasonic waves after trigger signals. When the ultrasonic waves encounter the object and are reflected back, the module outputs an echo signal, so it can determine the distance of object from the time difference between trigger signal (TRIG)and echo signal(ECHO).

As the picture shows, it is like two eyes. One is transmitting end, the other is receiving end.

According to the above wiring diagram, the integrated port of the ultrasonic sensor module is connected to the 5V G P15 P16 port on the micro:bit motor driver base plate. The Trig (T) pin is controlled by P15 of the micro:bit and the pin of Echo (E) the P16.



![](media/1174e0ec8487f223400c50ee4f765dac.png)

<

2. Working Principle

![](media/8ff02741199a0f03d8d814a4b72f27d7.png)

(1)Pull down TRIG then trigger high level signals with least 10us;

(2)After triggering, the module will automatically send eight 40KHz ultrasonic pulses and detect whether there is a signal return;

(3)If there is a signal return, when ECHO (E) outputs a high level, then the duration of the high level is the time from transmission to reception of the ultrasonic waves. Then test distance = high level duration \*340m/s\*0.5. 

3. Parameters

- Working voltage: 3-5.5V (DC)

- Working current: 15mA

- Working frequency: 40khz

- Maximum detection distance: about 3m

- Minimum detection distance: 2-3cm

- Precision: up to 0.2cm

- Sensing angle: less than 15 degrees

- Input trigger pulse: 10us TTL level

- Output echo signal: output TTL level signal (high), proportional to   range

4. Preparation

- Insert the micro:bit board into the slot of keyestudio   4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the Web version of Makecode

Import Hex profile [**(How to import?)**](#import-test-code) , or click“New Project”and drag blocks step by step(add MecanumRobot extension library first)

[**(How to add Mecanum_Robot extension?)**](#M11)

5. Test Code

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 18.1： Ultrasonic Ranging.hex|




Or you could edit code step by step in the editing area.

(1)Tap“Advanced”→“Serial” →“serial redirect to USB”

Combine it with“on start”block

![](media/73b63660eb8f378dea4930f354d04de6.png)

(2)Click“Advanced”→“Serial” to find and drag“serial write value x=0”into“forever”; Click“MecanumRobot”to find and drag“Ultrasonic”to the 0 on the right side of“serial write value x=0”and change the x on the left side of “=”to distance:

![](media/390b1b8e952e923bbeb561c0fc9a0520.png)

\(3\) find and drag![](media/0788feefa06aeed58a3f7ff4a85f3848.png)of
“Basic”,and change 100 to 200and place it behind![](media/039569dc23c7ff4a5577eea1a890eca4.png)

Complete Program:

![](media/497760b1d2daeec2134c8ed8fa89d130.png)

① The "on start" command block runs only once to start the program.

②Serial redirection USB

③In the "forever" instruction block, the program runs cyclically.

④Serial write value distance=Ultrasonic

⑤ Delay time 200 ms

Click“JavaScript" to view the corresponding JavaScript code: ：

![](media/387f32432a158fd0c34ff03a6d6bbde5.png)

6.  **Test Result**

Download code to micro:bit, keep USB cable connected, dial POWER switch to ON end. The distance value will be displayed on monitor.

([How to quick download?](#quick-download))

![](media/2cd74c16ab3623f6752d3f5e59deea2e.png)

The monitor shows the distance between the obstacle and ultrasonic sensor(as shown below).

![](media/422adea3e04563f038f7f28cd40efb2d.png)

Open CoolTerm, click Options to select SerialPort. Set COM port and 115200 baud rate(the baud rate of USB serial communication of Micro:bit is 115200 through the test). Click “OK” and “Connect”.

CoolTerm serial monitor displays the distance value as follows:

![](media/69b0699826728a3ac629f8869b2c644b.png)

#### Project 18..2：Ultrasonic Avoidance

![](media/a9f6a779aba5cc124d3ac8789ff87458.jpg)

1. Description

In this project, we will integrate an ultrasonic sensor and a car to make an ultrasonic avoidance car.

Its principle is to detect the distance between the car and obstacle via the ultrasonic sensor to control the motion of smart car.

2.  **Preparation**

- Insert the micro:bit board into the slot of keyestudio   4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the Web version of Makecode

Import Hex profile [**(How to import?)**](#import-test-code) , or click“New Project”and drag blocks step by step(add MecanumRobot extension library first)

[**(How to add Mecanum_Robot extension?)**](#M11)

3.  **Flow Chart**

![](media/d5e079ed292661bbe757f58971323fd1.emf)

4.  **Test Code**

Code path:

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 18.2： Ultrasonic Avoidance Car.hex|




Or you could edit code step by step in the editing area.

(1)Enter“Basic” →“show icon ♥”

Place it into“on start”and click the triangle button to select“![](media/b9b97ec13c745120243516b57a2f2fbc.png)”
pattern

![](media/4e8ed8afa7457e273982b6f884567de7.png)

Click “Functions”of ”Advance”and click![](media/7bff09ac7145d2ee7d4e32e08fdb4f10.png).

<span>Change“doSomething”to
“car_forward”，“car_back”，“car_left”，“car_right”respectively.</span>

<span>
</span>

![](media/bd1e14bde5915a2684edd8d8e8083a83.png)

<


Click“Variables” and then click“Make a Variable..., dialog box“New variable name：”pops up;

Fill it with “distance”;

Click“OK”to establish variable“distance;

Set the functions of servo:

Click“Variables”, drag out “set distance to 0”and place it into“forever”.

Click“MecanumRobotV2”to find and drag“Ultrasonic”to the 0 behind the”to”:



![](media/b45bf0e3b9f2f27746d8aa30403ff0ab.png)

<


Click“Logic”to find and drag“if true then...else”to“forever”;

Find and drag“=”to “true”;

Click“Variables”to find and drag“distance”on the left of“=”;

Click the little triangle behind“=”to choose“\<”;

Change the 0 behind “\>”to 20:

![](media/609b775c588c55bcb0cfe44d208909d6.png)

Click Funtionsto of “Advance”to find and drag![](media/dd9060aa29c60f92e8ce8f1abc7b5f91.png);

Click“MecanumRobot”to find and drag![](media/0ea445fb8307fca1a1454e1e12a59307.png)
to then;

Click“Basic”to find
![](media/659ed579016deb377b781697b2552aee.png)
and change the 100 to 500:

![](media/6a5855db5a6855b177b8c615c717bd46.png)

Click“MecanumRobot”to find and drag![](media/c9154a5acacec35bf9bb2d0538e3dc07.png)
and change the 0 to 180;

Copy
![](media/44d25af0ef67de4c735f87d5ceb245d6.png)
once;

Click“Variables”to find and drag“set distance_l to 0”;

Click“MecanumRobotV2”to find and drag“Ultrasonic”to 0 behind
“to”![](media/41552f84a7e07ba0dafd9d316c318c24.png);

Copy
![](media/44d25af0ef67de4c735f87d5ceb245d6.png)once;

![](media/62db53e547c6e8fc436677e055082ddf.png)

Copy
![](media/47ac979910f0378c537471eb0e205861.png)
once;

Change the 180 to 0, distance_l to distance_r and others remain unchanged:

![](media/526ffe9431e408d67128243fcbc5819f.png)

Click“Logic”to find and drag“if true then...else”;

Find and drag“=”to true;

Click“Variables”to find and drag“distance_l to the left of “=”; Click the little triangle behind“=”to choose“\>”;

Change the 0 behind “\>”to “distance_r”:

![](media/101b300f4b7db0e23ee3a7b7ca29dd6f.png)

Click Funtions of “Advance”to find and drag![](media/7e3dd5d92e3b83921b164b4f72908184.png);

Click“MecanumRobotV2”to find and drag![](media/752a8d81f9c62d904159b1405b703f53.png);

Change the 0 to 90;

Click“Basic”to find and drag
![](media/659ed579016deb377b781697b2552aee.png)
and change the 100 to 300:

![](media/5412afb79dec7e6e47c85f14151de4df.png)

Change
![](media/6ee297904b560c8c8370fc650d8ee532.png) to
![](media/7fa87915a652f69f25c4fb6325c05124.png)
and place it in the first “else”：

![](media/a860cf40263fb2c685996ce8a0e44a21.png)

Click “Funtions” of “Advance”to find and drag![](media/f87ab638cdb2e89fcef5dea3ed2c2355.png)，and place it to the second “else”：

![](media/78793a8b16332f40f3ba0188f98d9170.png)

Complete Program:

![](media/05a4740bad5faf67199577dc79e502ac.png)

“The "on start" command block runs only once to start the program.

LED dot matrix display“![](media/b9b97ec13c745120243516b57a2f2fbc.png)”

In the "forever" instruction block, the program runs cyclically.

Set variable distance to store the distance measured by ultrasonic

If the distance is less than 20cm

The car moves back

The car stop

Delay in 500ms

...................Servo rotates left

Delay in 500ms

Set variable distance_l to store the distance measured by ultrasonic

.Delay in 500ms

Servo rotates right

.Delay in500ms

Set variable distance_r to store the distance measured by ultrasonic

Delay in 500ms。

![](media/74e73b03b4ca9682a2b08ead655f6264.png)

.If the left distance is bigger than right

The car turns left

.Servo rotates to 90 degrees

..................Delay in 300ms

.If the left distance is equal to or less than right

.The car turns right

Servo rotates to 90 degrees

...................Delay in 300ms

If the front distance is equal to or bigger than 20cm

The car advance

Click“JavaScript" to view the corresponding JavaScript code: ：



![](media/c8f86a24196a5bd7569ad419207e71e4.png)

<

<span>
</span>

![](media/13baf1d67d2b0e5fefe9a31c6120b185.png)

<


5.  **Test Result**

Download code to micro:bit, dial to ON end, and dial POWER to ON end. When the obstacle distance is greater than 20cm, the car goes forward ;
on the contrary, smart car turns left.

([How to download?](#A01) [How to quick download?](#quick-download))

#### Project 18..3：Ultrasonic Following

![](media/6dcfae5b12fd196e2e2c567d8d159814.jpg)

1. Description

In previous lesson, we’ve learned the basic principle of line tracking sensor. Next, we will combine the ultrasonic sensor with the car to make an ultrasonic following car.

The ultrasonic sensor detects the obstacle distance and control the motion status of car.

2. Preparation

- Insert the micro:bit board into the slot of keyestudio   4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the Web version of Makecode

Import Hex profile [**(How to import?)**](#import-test-code) , or click“New Project”and drag blocks step by step(add MecanumRobot extension library first)

[**(How to add Mecanum_Robot extension?)**](#M11)

3. Flow Chart

![](media/f27ee773b81f14997bc1c196e1b29074.emf)

4. Test Code

Code path:

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 18.3：Ultrasonic Follow Smart Car.hex|




Or you could edit code step by step in the editing area.

(1)Enter“Basic” →“show icon ♥”

Place it into“on start”and click the triangle button to select“![](media/b9b97ec13c745120243516b57a2f2fbc.png)”
pattern。

![](media/4e8ed8afa7457e273982b6f884567de7.png)

(2)Click“ MecanumRobotV2”to find and drag![](media/1eff07a69c5638b58b55d10dae4471d9.png)to“on start”and change the angle 0 to 90:

![](media/295d9af41bb520c0df8ed0d6bb17a01f.png)

Click “Functions”of ”Advance”and click“Make a Function”, then
![](media/7bff09ac7145d2ee7d4e32e08fdb4f10.png)will appear.

<span>Change“doSomething”to
“car_forward”，“car_back”，“car_left”，“car_right”respectively.</span>

<span>
</span>

![](media/bd1e14bde5915a2684edd8d8e8083a83.png)

<


Click“Variables” and then click“Make a Variable...”, the dialog box“New variable name：”pops up; fill it with “distance”;

Click“OK”to establish variable“distance”;

Drag“set distance to 0” to “forever”;

Click“ MecanumRobotV2”to find and drag![](media/510609eb2d083a5893b81c83ec790d0d.png)to the “0” of“set distance to 0”:

![](media/1adf6ff794c9cb8304cd1669bc57edf7.png)

Click“Logic”to find and drag“if true then...else”to“forever”;

Find and drag“=”to true;

Click“Variables”to find and drag“distance”to the left side of “=”;

Click the little triangle behind“=”to choose“\<”;

Change the 0 behind “” to 10:

![](media/2dd8554239ca3eafc07e2093de962311.png)

Click “Functions” of“ Advance”to find and drag![](media/27404bb7a7aa9733a5d9a9b390ee5958.png)to“then”:

![](media/e8a12e1e353502ceb550a204a0b1f121.png)

Change the 10 to 20, car_back to car stop:

![](media/9f7cfcaee4fad430c97dbea06434a302.png)

Change the 20 to 40，car stop to car forward; Place car stop to the last”else”:

![](media/e8629032a5e8fc91d159c79d9c76a8bb.png)

Complete Program:

![](media/03b95531c329ada277242c0ce8c16b5a.png)

“The "on start" command block runs only once to start the program.

.LED dot matrix display“![](media/b9b97ec13c745120243516b57a2f2fbc.png)”

Servo rotates to 90 degrees

In the "forever" instruction block, the program runs cyclically.

Set variable distance to the value read by ultrasonic

.If the distance is less than 10cm

The car moves back

.If the distance is less than 20cm

The car stop

.If the distance is less than 40cm

The car advance

Otherwise, none of the above conditions holds

The car stop

Click“JavaScript" to view the corresponding JavaScript code: ：

![](media/a93c824520e7139f7419817a8d05d5e2.png)

5. Test Result

Download code to micro:bit, dial POWER switch to ON end on shield, smart car could follow the obstacle to move.

([How to download?](#A01) [How to quick download?](#quick-download))

### Project 19：IR Remote Control

#### Project 19.1：Decode IR Remote Control

![](media/3a3e9860725c893c34613ee1eafb91fc.png)

1. Description

There is no doubt that infrared remote control is ubiquitous in daily life. It is used to control various household appliances, such as TVs, stereos, video recorders and satellite signal receivers. Infrared remote control is composed of infrared transmitting and infrared receiving systems, that is, an infrared remote control, an infrared receiving module and a single-chip microcomputer capable of decoding.

![](media/9980b41f57feddc2e8a9c0346afaaea9.png)

The 38K infrared carrier signal emitted by remote controller is encoded by the encoding chip in the remote controller. It is composed of a section of pilot code, user code, user inverse code, data code, and data inverse code. The time interval of the pulse is used to distinguish whether it is a 0 or 1 signal and the encoding is made up of these 0, 1 signals.

The user code of the same remote control is unchanged. The data code can distinguish the key.

When the remote control button is pressed, the remote control sends out an infrared carrier signal. When the IR receiver receives the signal, the program will decode the carrier signal and determines which key is pressed. The MCU decodes the received 01 signal, thereby judging what key is pressed by the remote control.

Infrared receiver we use is an infrared receiver module. Mainly composed of an infrared receiver head, it is a device that integrates reception, amplification, and demodulation. Its internal IC has completed demodulation, and can achieve from infrared reception to output and be compatible with TTL signals. Additionally, it is suitable for infrared remote control and infrared data transmission. The infrared receiving module made by the receiver has only three pins, signal line, VCC and GND.

According to the picture above, the integrated port of the infrared receiver is connected to the P9 5V G port on the motor driver board and controlled by the the P9 of the micro:bit.

2. Parameters:

- Operating Voltage: 3.3-5V（DC）

- Interface: 3PIN

- Output Signal: Digital signal

- Receiving Angle: 90 degrees

- Frequency: 38khz

- Receiving Distance: about 5m

3. Preparation

- Insert the micro:bit board into the slot of keyestudio   4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the Web version of Makecode

Import Hex profile [**(How to import?)**](#import-test-code) , or click“New Project”and drag blocks step by step(add MecanumRobot extension library first)

[**(How to add Mecanum_Robot extension?)**](#M11)

4. Test Code

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 19.1：Decode IR Remote Control.hex|




Click“Advanced”→“Serial”→“serial redirect to USB”

Place it into“on start”block.

Enter“IrRemote”→“connect IR receiver at P0”

Put it into“on start”block

IR receiving module is controlled by P0 of micro:bit board

![](media/e96a8740cff9a9f788bfc982e37455c9.png)

Click“Led”→“more”→“led enable(false)”, and place it into “on start”.

![](media/add7fe2c5753e7c7cc583cfdb7731b47.png)

Go to“Variables”→“Make a Variable...”→ “New variable name：” dialog box，

Enter“val”and click“OK”to create variable“val”

Then drag out“set val to 0”block into“forever”block.

![](media/ca51f70bf8729f83310f70471bf1b64a.png)

Go to“Ir Remote”→“IR button”

Place it into 0 box

![](media/85bff59d45d6defe248bd5c82c4b7078.png)

Click“Advanced”→“Serial”→“serial write value“x”=0”

Put it into“forever”block

Change“x”into“IR”

Enter“Variables”to move block“val”into 0 box behind“=”

![](media/736e85fd87be88896e185cc61373f69e.png)

Drag out block“pause (ms) 100”from“Basic”and delay in 1000ms

Leave it into“forever”block

![](media/407dccc26a2a9e0e07d0436591cd99bd.png)

Complete Program：

![](media/2e20f731f34b79115eedecb2d1eefd78.png)

“on start”: command block runs once to start program.

Serial redirect to USB

Connect IR receiver to P0

The program under the block “forever” runs cyclically.

Set val to IR button

Serial port prints IR=val

Delay in 1000ms

Click“JavaScript" to switch into the corresponding JavaScript code:

![](media/87e18859852d9e1f086a36edee21ffac.png)

Code explanation: If the buttons are not pressed, the serial monitor constantly shows 0; when pressed, the corresponding key values are displayed.

Notes：

The remote control in this kit is not inclusive of batteries. We recommend you to purchase them online.(battery type:CR2025).

Make sure IR remote is good before test. There is a tip for you to check it.

Open the cellphone camera , make IR remote control point at camera and press button. The remote control is good if you see the purple flashing light in the camera.

Download code to micro: bit board and don’t plug off USB cable Click![](media/1f02508d0c79cd976c673a6a5daba648.png)

([How to quick download?](#quick-download))

![](media/e7bf712e0c8bedc4b0423427848fa395.png)

Make IR remote control point at IR receiver and press the button, the serial monitor will display the corresponding key values, as shown below：

![](media/c7a33a4cc9d6decbf9b653d91bcb5318.png)

Open CoolTerm, click Options to select SerialPort. Set COM port and 115200 baud rate. Click“OK”and“Connect”.

CoolTerm serial monitor shows the key value as follows:

![](media/bd951869f7f822f8420d6174122c9a35.jpg)

The key value is displayed as for your reference:

![](media/db524e7e2d5a77652948837ed70a1310.jpg)

#### Project 19.2：IR Remote Control 

![](media/058af4ba6b305a06d628d68d32788062.jpg)

1. Description

In this project, we combine IR remote control with car shield to make an IR remote smart car. Its principle is to control the motion of car by sending key signals from IR remote control to IR receiving module of car shield.

2. Preparation

- Insert the micro:bit board into the slot of keyestudio   4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the Web version of Makecode

Import Hex profile [**(How to import?)**](#import-test-code) , or click“New Project”and drag blocks step by step(add MecanumRobot extension library first)

[**(How to add Mecanum_Robot extension?)**](#M11)

Note: The infrared sensor and infrared remote control should not be used in environments with infrared interference such as sunlight for it contains a lot of invisible lights, such as infrared and ultraviolet. In an environment with strong sunlight, they cannot work normally.

3. Flow Chart

![](media/05bed3da2ec90a721efd1ebc14e0b89e.emf)

4. Test Code

Code path:

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 19.2：IR Remote Control .hex|




Or you could edit code step by step in the editing area.

(1)Create four functions to control the car to move forward and back and turn left and right:



![](media/bd1e14bde5915a2684edd8d8e8083a83.png)

<


(2)Click“Ir Remote”to find and drag“connect IR receiver at P0”into“on start”; Click the little triangle behind P0 to choose P0;

<span>
</span>

![](media/6f129336f7d0a1c353cfa752f8b57842.png)

<


(3)Click“Variables”then click“Make a Variable...”, the dialog box“New variable name：”pops up; fill it with“val” and click“OK”to create variable“val”;

Create variable“val2”with the same method; find and drag“set val2 to 0”to“on start”and copy it once to put into“on start”too;

Click the little triangle behind the first val2 to choose “val”;

![](media/14565505dde0260f0251b10b4ec32e0b.png)

（4)Click “Led”→“more”→“led enable(false)”and place it into“on start”.

![](media/af5233ad0eaf8c04248cd0153cc2e2e5.png)

(5)Click “Variables”, find and drag“set val2 to 0”into“forever”.

Click the little triangle behind the val2 to choose “val”.

Click“IrRemote”→“IR button”and place it into 0 behind the to.

![](media/cb2d715c478a5e5a45c5bd290d934bb0.png)

(6)Click“Logic”to find and drag“if true then”into“forever”; find and drag “=”into“true”;

Click“Variables”to find and drag“val”to the left side of “=; the 0 on the right side of “=”remain unchanged; click the little triangle behind “=”to choose“≠”;

![](media/bd0c5a825a3ec489771cd94f66bf4eeb.png)

(7)Click“Variables”to find and drag“set val2 to 0”into “then”;find and drag “val”into the o behind “to” of“set val2 to 0”;

![](media/c7113c934b0ab15ada6402db27fd2a12.png)

(8)Click“Logic”to find and drag“if...then...else”to then;

Click“![](media/a7c5c78217692a965e679b2439ab2f3a.png)”of”
if...then...else”four times;

Click“![](media/0fcc5d6332012fed7361a075bd60751f.png)”behind
“else”once to delete else;

Find and drag “=” to “true”;

![](media/472e74c957d8646cf1d8d0f691f00f24.png)

(9)Click“Variables”to find and drag“val2”to the left side of“=”and change the 0 on the right of“=”to 70:

![](media/b56abcb30b725bdd5d9d638d6af51dad.png)

(10)Click“Functions” of“Advance”to find and drag![](media/d3cf8340044d82c5d2d50246d9e6965e.png)to the second “then”:

![](media/482a152434aeb6f4c85f3fdac0ae84cd.png)

(11)Copy “val2=70”once and place it behind the first “if”;change the 70 behind “=”to 68.

![](media/d5f6fef293f69b8f8d882c7649102e7f.png)

(12)Click“Functions” of“Advance”to find and drag![](media/4deed9368819d1dbfea4610d4f67a9d1.png)
to the second “then” .

![](media/e6fb5164cb395fdfda9633cdd0e26cc3.png)

(13)Copy“val2=68”once and place it behind the second “else if “; change the 68 behind “=”to 67； place it in the forth “then”;
Click“Functions”of“Advance”to find and drag![](media/47d91ca3ea8d1dc80a1ecb2bfb72627a.png)to the forth “then”:

![](media/40f5ed1de0d11c11e8fe8e9b6b1dd9b9.png)

(14)Copy“val2=67”once and put it behind “=” of the third “else if ;
change the number 67 to 21; click “Functions” of “Advance”to find and drag![](media/cad0b2d52818bfc2bdd2c65a2663ebac.png)
to the fifth “then”:

![](media/923c2766615153dcebba2524d127fc12.png)

(15)Copy “val2=21”once and place it behind the fourth “else if “; change the the number 21 behind“=”to 64；Click“MecanumRobotV2”to find and drag
![](media/94cc49c46a54dfc4e06e604e359fa1c9.png) to the sixth “then”:

![](media/383a620fd554d765d71d628e2a37a3dc.png)

Complete Program:

![](media/22d06d7487b51c0dfdd0ca30c7f4945e.png)

① The "on start" command block runs only once to start the program.

②Connect the IR receiver to P0

③Set the variable val to 0

④Set the variable val2 to 0

⑤In the "forever" instruction box, the program runs cyclically

⑥Set val to IR button

⑦When the variable val≠0 is established, execute the program under then

⑧Set variable val2 to val

⑨When val2=70 is established, execute the program under then

⑩The car goes forward

⑪When val2=68 is established, execute the program under then

⑫Turn left

⑬When val2=67 is established, execute the program under then

⑭Car turn right

⑮When val2=21 is established, execute the program under then

⑯The car goes back

⑰When val2=64 is established, execute the program under then

⑱The car stops

Click“JavaScript" to switch into the corresponding JavaScript code:

![](media/e68b6275a1026ed95ca88502e5bc4c49.png)

![](media/94de6552ca4ccdb232d5e9dd0466e611.png)

5. Test Result

Download code to micro:bit board, and dial POWER to ON end.

Make IR remote control point at micro:bit and press the button to control smart car to move.

![](media/d55474f3fdf94e5d35de424c0135f554.png)button makes smart car move forward，![](media/5c8a65498c17f35878adf79ba446a7c8.png)stands for turning left，![](media/41116032870ebaa49d6e78fe2445da36.png)implies rightward turning,
![](media/369433f6b13252c1df8c30b3f71028d2.png)indicates moving backward，![](media/a8ef4b174911d528e2dc232c2f862b7d.png)
stops car.

([How to download?](#A01) [How to quick download?](#quick-download))

Note: The distance between IR remote control and IR receiving head of smart car are supposed less than 5m during the test.

### Project 20：Bluetooth Multi-purpose Smart Car

### Project 20.1：Read Bluetooth Data

![](media/55b2424d88ba1ba8a711c49418ca8dc6.png)

1. Description

Micro:bit main board comes with a built-in Bluetooth which can be used to communicate with it. And the Micro:bit can also be controlled by Bluetooth or transmit signals back to smartphone or computer via it. This Bluetooth can communicate with the Bluetooth equipped in other devices or with Bluetooth App to control other equipment.

It is compatible with both Android system ans IOS system. And we have designed two Bluetooth Apps for both systems.

The connection of the Bluetooth on the board with these two Apps is similar. In this lesson, we will introduce the functions of all keys and patterns on the Apps and control the smart car via Bluetooth App.

2. Preparation

- Insert the micro:bit board into the slot of keyestudio   4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the Web version of Makecode

Import Hex profile [**(How to import?)**](#import-test-code) , or click“New Project”and drag blocks step by step(add MecanumRobot extension library first)

[**(How to add Mecanum_Robot extension?)**](#M11)

If you choose to drag the code manually, you need to add the Bluetooth extension library first. Click the gear icon (Settings) in the upper right corner, then click on Extensions to go to the library file selection screen, and then click on the "Bluetooth" extension library (if it doesn't exist, search Bluetooth to find it), as shown below: 

![](media/4e30836054aa5b5a983cb70b3baa62b0.png)

As the Bluetooth and extension radio can’t work together, therefore, their extension libraries are not compatible.

Therefore, remove extension(s) and add Bluetooth please if you see the following prompt box pop up.

![](media/aee56e76bad3421a20cea6018ccd5e2c.png)

3. Test Code

Code Path:

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 20.1：Read Bluetooth Data.hex|




Or you could edit code step by step in the editing area.

Enter“Advanced” →“Serial” → “serial redirect to USB”

Place it into“on start”

![](media/73b63660eb8f378dea4930f354d04de6.png)

Click“Bluetooth”→“on bluetooth connected”

Go to“Basic”to move“show icon”block into“on bluetooth connected” block.

![](media/501b8068bafd00adcf138a2b828835d9.png)

Click“Variables”→“Make a Variable...”→“New variable name：”dialog box.

Input“connected”and click“OK”to create variable“connected”.

Drag“set connected to 0”under block “show icon” and change 0 into 1.

![](media/bc9514b04f4aae40dc295eeac3fb21ce.png)

Go to“Loops”to move block“while true do...”into“on bluetooth connected”block.

Enter“Logic”to drag out “=”block.

Click“Variables” to drag “connected” into left box of “=” block and change 0 into 1.

![](media/665a62b4895ca45f82d3ebc88e885bce.png)

Then we generate variable“rec_data”in same way.

Then drag out“set rec_data to 0”and place it into block“while connected=1 do...”block.

Click“Bluetooth”→“more”→“bluetooth uart read until new line( )”

Keep it into 0 box and click triangle button to select \#.

![](media/e993122756294214c561f660c3df07ea.png)

Go to“Advanced”→“Serial”→“serial write string”

Move it below“set rec_data...until#”block

And combine variable“rec_data”with“serial write string”block.

![](media/6effc725f7d85e4a72afbcee102cc478.png)

Click“Advanced” →“Serial” →“serial write line” and place it into “while connected=1 do...”.

![](media/5d66f2053f858d7a3f2e0af55bcc0f0f.png)

Click“Bluetooth”to drag out“on bluetooth disconnected”.

Click “Basic”, copy“show icon”block and keep it into block“on bluetooth disconnected”

Click triangle button to select“![](media/25e0341e063286ff7828c15f09ae0ade.png)”pattern.

![](media/689000dc16e8fb32f0d9918445aae4c1.png)

Complete Program|<p>

![](media/ac5ffe1aee7b0f7ff335606b02cd153e.png)

</p>
<p>“on start”: command block runs once to start program.</p>
<p>Serial redirect to USB</p>
<p>Connect Bluetooth</p>
<p>LED dot matrix shows“❤”pattern</p>
<p>Set variable connected to 1</p>
<p>When connected=1, the code under do block will be executed.</p>
<p>Set rec_data to bluetooth uart read until #</p>
<p>Serial port prints rec_data</p>
<p>Print a blank space</p>
<p>Disconnect Bluetooth</p>
<p>LED dot matrix displays“![](media/25e0341e063286ff7828c15f09ae0ade.png)”pattern.</p>|




Click“JavaScript" to view the corresponding JavaScript code:

![](media/24191138f7bb709f2c6de046df16edef.png)

4.Test Result

If you drag blocks step by step, you need to set as follows after finishing test code.

![](media/01b256e5bbe9420226085513778f5173.png)
![](media/982334c8cdfb3ab43cd2db629090ca1b.png)
![](media/09767d5efdc8f05fdb331b5ae6d352b5.png)

However, you could skip this step if you directly import test code.

After setting, download code to micro:bit board, don’t plug off the USB cable([How to download?](#A01) [How to quick download?](#quick-download))

Next to download App.

For IOS System:

a.Open App Store;

![](media/27924fdb3d67692df7c63d8d0fb72287.png)

b.Search mecanum_robot and click“![](media/962a57f92b78eea1f0e3e81463497a9c.png)”to download the Bluetooth App of mecanum_robot;

c\. After downloading the APP, click "OPEN" or click the application mecanum_robot on the phone/iPad desktop to open the APP. A dialog box appears on the APP interface, and click "OK" in the dialog box.

d\. First turn on the Bluetooth of the mobile phone/iPad, and then click the connect button (control) in the upper left corner of the APP interface to perform a Bluetooth search. In the search results, click "BCC micro:bit". After a few seconds, the Bluetooth is connected.

For Android System:

a\. Use the scanning function in the browser to scan and identify the QR code or enter the <http://8.210.52.206/mecanum_robot.apk> to download. After the identification is successful, click "go to website" to enter the download mecanum_robot.apk page , click "Download" to download the mecanum_robot application.

![](media/d9acbfab8eccc3da40cde7788a3e1854.png)

b.Click“Allow allow”to enter Installation Diagram; click“install”to install the App.

![](media/638d0a4ae5f55ca39bff4f20a3bd14a6.png)

c.Click "Open" or click the application mecanum_robot on the mobile phone desktop to open the APP, and a dialog box appears. In the dialog box, click "Allow" to turn on the Bluetooth of the mobile phone. You can also turn on the phone's Bluetooth before opening the APP.

![](media/c818fd71d6872374fbe177f082207fac.png)
![](media/0c35f0dceebddef4110b47372fe299a4.png)

d.Click
![](media/d3f566b98da750bf4d5799b624211516.png) on the upper right corner to search for Bluetooth and click“connect”; a few seconds later, the Bluetooth is paired.

![](media/3d21cf8757f8cd7434985e60bc940418.png)
![](media/4a23b1970c9f012293aef3327a90cf7c.png)

Open CoolTerm, click Options to select SerialPort. Set COM port and 115200 baud rate. Click“OK”and“Connect”.

Point at micro:bit board and press the icons on APP, the corresponding characters are shown on CoolTerm monitor.

![](media/0ed4a53ef14fbfe047929d07d5433fcb.png)

Through the test, we get the functions of every icon, as shown below:

![](media/05c3d32b07c8e1393eacd805b4de77c7.jpg)

### Project 20.2：Multi-purpose Smart Car

![](media/b9de6fb2ea158ce9fd59513a9e8c4833.jpg)

1. Description

In this lesson, we will control the smart car to perform multipurpose functions.

2. Preparation

- Insert the micro:bit board into the slot of keyestudio   4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the Web version of Makecode

Import Hex profile [**(How to import?)**](#import-test-code) , or click“New Project”and drag blocks step by step(add MecanumRobot extension library first)

[**(How to add Mecanum_Robot extension?)**](#M11)

Steps：Click the gear icon (Settings) in the upper right corner, then click on Extensions to go to the library file selection screen, and then click on the "Bluetooth" extension library (if it doesn't exist, search Bluetooth to find it), as shown below: 

![](media/4e30836054aa5b5a983cb70b3baa62b0.png)

As the Bluetooth and extension radio can’t work together, therefore, their extension libraries are not compatible.

Therefore, remove extension(s) and add Bluetooth please if you see the following prompt box pop up.

![](media/aee56e76bad3421a20cea6018ccd5e2c.png)

3. Test Code

Code path:

|  |  |  |
|--|--|--|
|File Type|Path|File Name|
|Hex file|..\2. Makecode Tutorial\Makecode Code|Project 20.2：Multi-purpose Smart Car.hex|




Complete Code:

![](media/d9d0b14680f4131194595baaee971699.png)

Click“JavaScript" to view the corresponding JavaScript code: ：

![](media/a73529d60614999f05244e4fa4c31cca.png)

4. Test Result

This experiment combines the previous projects to make the car to perform actions via Bluetooth.

Enter Makecode online editor→Projecting Settings→![](media/bef5b73422672f316f211a959bcdfa60.png), enable “No Pairing....”(you could skip this step if you import test code directly)

Download code to micro:bit board, dial POWER to ON end, and connect the Bluetooth, then you can control the car via the Bluetooth App of mecanum_robot.

([How to download?](#A01) [How to quick download?](#quick-download))

Note:![](media/81da4f47165508a486698671a3568af0.jpg)is used to adjust the speed, and
![](media/adc3be608cbddaca066d63aa9bc0c435.jpg)
can only be dragged.


## Common Problems

1.  **The car has no reaction**

Please check whether the batteries are sufficient

Please check whether the wirings are correct

2.  **Computers can't recognize the USB ports**

Please ensure whether the microbit driver is installed

Please check whether the USB wire is in good condition.

3.  **Code fails to burn and dot matrix displays expressions**

Please check whether the Mecanum Robot Car_V2.py library file i mported

## Resources

https://fs.keyestudio.com/KS4034-4035






