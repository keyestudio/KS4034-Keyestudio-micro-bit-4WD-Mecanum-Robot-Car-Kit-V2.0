# Assemble Mecanum Robot  

It is a programmable car based on BBC micro:bit. It integrates a motor driver, a line tracking sensor and an IR receiver into the base plate, which also contains an ultrasonic sensor, a servo, 2 seven-color lights as well as 4 WS2812 RGB lights. The wiring is not complicated and it has Lego jacks to facilitate connection with other peripheral devices. Abundant hardware resources will enable you to master more knowledge and skills to create more technological inventions.

## Sensors and control pins of the 4WD Mecanum Robot Car V2.0

This car can help you to better learn how to use the Micro:bit and make electronic knowledge accessible to you.

**Functions**

|        |                   |                       |       |                   |                      |             |                  |              |
| ------ | ----------------- | --------------------- | ----- | ----------------- | -------------------- | ----------- | ---------------- | ------------ |
| Sensor | Seven-color light | Decelerating DC motor | Servo | Ultrasonic sensor | Line Tracking Sensor | IR Receiver | WS2812 RGB light | Power switch |
| QTY    | 2                 | 4                     | 1     | 1                 | 3                    | 1           | 4                | 1            |

**Note: the line tracking sensor, WS2812 RGB lights, IR receiver and moto river are integrated in the base plate.**

**Pins：**

![Img](./media/Assemble_Mecanum_Robot_97b760ef.png)

**Power supply and Battery**

The keyestudio 4WD Mecanum Robot Car is powered by two 18650 batteries. The battery holder of the car is compatible with any type of 18650 lithium battery (rechargeable). You can use a universal battery charger to charge the 18650 lithium battery.

**Note:** This product does not contain batteries.

## The Installation of Keyestudio 4WD Mecanum Robot Car V2.0 

Step 1

**Components Needed:**

![](./media/Assemble_Mecanum_Robot_f3d856b4.png)

**Installation Diagram:**

![](./media/Assemble_Mecanum_Robot_3d1dbf07.png)

**Prototype:**

![](./media/Assemble_Mecanum_Robot_f5d38786.png)

Step 2

**Components Needed:**

![](./media/Assemble_Mecanum_Robot_a2ee8074.png)

**Installation Diagram:**

![](./media/Assemble_Mecanum_Robot_6fdf9d4d.png)

**Prototype:**

![](./media/Assemble_Mecanum_Robot_3fec7c19.png)

Step 3

**Components Needed:**

![](./media/Assemble_Mecanum_Robot_d4f24cc5.png)

**Installation Diagram:**

![](./media/Assemble_Mecanum_Robot_e1d7b425.png)

**Prototype:**

![](./media/Assemble_Mecanum_Robot_cc96b9d6.png)

Step 4

（adjust the angle of the servo first）

**Adjust the angle of the servo to 90 degrees.**

**Method 1：MakeCode code**

⚠️**Special note:** Before you write the code and upload it, you must Understand the MakeCode IDE and add library files, please go to the the link: [Get Started with makecode](./Code1.7z)

![](./media/Assemble_Mecanum_Robot_a9ff633c.png)

The MakeCode code above is provided in the materials. Open the adjustment code of the servo and burn it into the microbit motherboard of the 4WD Mecanum Robot Car V2.0, and **power on via micro USB cable or external power supply(turn the DIP switch to ON)**. That's it. The code is at the following position as shown in the figure:

![Img](./media/Assemble_Mecanum_Robot_21db9fa2.png)

**Method 2：Python code**

⚠️**Special note:** Before you write the code and upload it, you must install the Mu IDE and add library files, please go to the the link: [Get Started with Python](./Code2.7z)

```Python
# import microbit related libraries
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


Servo(pin14).write_angle(90)
sleep(1000)
```

**Components Needed:**

![](./media/Assemble_Mecanum_Robot_1e3fd9e2.png)

Installation Diagram: (mind the installation direction)

![](./media/Assemble_Mecanum_Robot_9ca5d2c8.png)

**Prototype:**

![](./media/Assemble_Mecanum_Robot_9b8bccaa.png)

Step 5

**Components Needed:**

![](./media/Assemble_Mecanum_Robot_8d138501.png)

**Installation Diagram:**

![](./media/Assemble_Mecanum_Robot_bda8fbc4.png)

**Prototype:**

![](./media/Assemble_Mecanum_Robot_9f244272.png)

Step 6

**Components Needed:**

![](./media/Assemble_Mecanum_Robot_36259594.png)

**Installation Diagram:**

![](./media/Assemble_Mecanum_Robot_6d3e3ad9.png)

**Prototype:**

![](./media/Assemble_Mecanum_Robot_3c33f63b.png)

Step 7

**Components Needed:**

![](./media/Assemble_Mecanum_Robot_817e834e.png)

**Installation Diagram:** (mind the direction of the motor)

![](./media/Assemble_Mecanum_Robot_09a61aa6.png)

**Prototype:**

![](./media/Assemble_Mecanum_Robot_8c97de28.png)

Step 8

**Components Needed:**

![](./media/Assemble_Mecanum_Robot_43bac346.png)

**Installation Diagram:** (Pay attention to the installation direction of the mecanum wheel)

![](./media/Assemble_Mecanum_Robot_d92dee68.png)

**Prototype:**

![](./media/Assemble_Mecanum_Robot_64467ed0.png)

Step 9

**Components Needed:**

![](./media/Assemble_Mecanum_Robot_5c38573f.png)

**Installation Diagram:**

![](./media/Assemble_Mecanum_Robot_a72469e3.png)

**Prototype:**

![](./media/Assemble_Mecanum_Robot_243aa35b.png)

Step 10

**Components Needed:**

![](./media/Assemble_Mecanum_Robot_b60b9f16.png)

**Installation Diagram:**

![](./media/Assemble_Mecanum_Robot_55f2db60.png)

**Prototype:**

![](./media/Assemble_Mecanum_Robot_456df8a0.png)

Wiring Diagram

**The wiring of the servo:**

![Img](./media/Assemble_Mecanum_Robot_c82a9395.png)

![](./media/Assemble_Mecanum_Robot_859cd41e.jpg)

![](./media/Assemble_Mecanum_Robot_b3bcce9d.png)

**The wiring of the ultrasonic sensor:**

![Img](./media/Assemble_Mecanum_Robot_c9f3da75.png)

![](./media/Assemble_Mecanum_Robot_5747ad7c.jpg)

![](./media/Assemble_Mecanum_Robot_a8f0e176.png)

**The wiring of the IR receiver module:**

![Img](./media/Assemble_Mecanum_Robot_61d53b21.png)

![](./media/Assemble_Mecanum_Robot_1e081a3a.png)

**The wiring of the RGB:**

![Img](./media/Assemble_Mecanum_Robot_c5b8a804.png)

![](./media/Assemble_Mecanum_Robot_01848b2e.jpg)

**The wiring of controlling the motor and seven-color light :**

![Img](./media/Assemble_Mecanum_Robot_0c4635c5.png)

![](./media/Assemble_Mecanum_Robot_1689f2c9.jpg)

**The wiring of controlling the 3-channel line-tracking sensor:**

![Img](./media/Assemble_Mecanum_Robot_542d1798.png)

![](./media/Assemble_Mecanum_Robot_08eb8d7e.jpg)

**The wiring of the power supply:**

![](./media/Assemble_Mecanum_Robot_cdcec4ba.jpg)

**The corresponding interface of the motor:**

![](./media/Assemble_Mecanum_Robot_ffcceef1.jpg)

**The installation of the battery:**

![](./media/Assemble_Mecanum_Robot_fe8ce786.png)



