How to Update the Firmware
==========================

**What is micro:bit firmware?**

Firmware is a special piece of software that makes a device work
properly. The Micro: Bit has two chips on the back, one runs your code,
while the other runs the firmware to enable you to program the device. 

Micro: Bit can be used with the accompanying firmware, thereby if you
don't need to update it, please come back to our micro: bit
function guide. 

Sometimes you may need to update your firmware to test new software
features. If this is the case, this page will show you how to do it. 

**Checking your firmware version**

To find out what version of the firmware you have on your micro:bit,
**Plug it in via USB**, open up the **DETAILS.TXT** file from the
**MICROBIT** driver and look for the number on the line that begins
'Interface Version'.

::

   \# DAPLink Firmware - see https://mbed.com/daplink

   Unique ID: 9904360249624e45004a601400000027000000009796990b

   HIC ID: 9796990b

   Auto Reset: 1

   Automation allowed: 0

   Overflow detection: 0

   Incompatible image detection: 1

   Page erasing: 0

   # DAPLink Firmware - see https://mbed.com/daplink
   Unique ID: 9904360249624e45004a601400000027000000009796990b
   HIC ID: 9796990b
   Auto Reset: 1
   Automation allowed: 0
   Overflow detection: 0
   Incompatible image detection: 1
   Page erasing: 0
   Daplink Mode: Interface
   Interface Version: 0254
   Bootloader Version: 0254
   Git SHA: ec3fec91e815b1fe27cefb8bc4ffa85ca3317502
   Local Mods: 0
   USB Interfaces: MSD, CDC, HID, WebUSB
   Bootloader CRC: 0xdb256cca
   Interface CRC: 0xd0f0bacf
   Remount count: 0
   URL: https://microbit.org/device/?id=9904&v=0254

**How to update the firmware**

1. Download the hexadecimal file to your computer from this page.

Link for the latest Micro: Bit firmware -0255:
https://www.microbit.org/get-started/user-guide/firmware/

(**Note:** You can download the latest firmware -025 exadecimal file by
clicking the link above;  If you don't download it here is also the
latest firmware -0255 hex file in the correspondin older.) 

2. With the battery pack removed and the Micro USB cable connected to
the computer, press and hold the reset button on the back of the Micro:
Bit and insert the Micro USB cable into the device. 

You empower to see a driver named MAINTENANCE in the file manager. 

|image1|

3. Drag and drop the new firmware .HEX file you have downloaded from
this page onto the micro:bit and wait for the yellow LED on the back of
the device to stop flashing. When the upgrade is completed, the
micro:bit will reset, ejecting itself from the computer and re-appear in
normal **MICROBIT** drive mode.

4. Finally, check the DETAILS.TXT file that is on the **MICROBIT**
driver and make sure that it has the same version number as the .HEX
firmware that you just downloaded and flashed to the interface chip.

.. |image1| image:: media/microbit-1.png
