## Project 18：Ultrasonic Sensor

### Project 18.1：Ultrasonic Ranging

1\.  **Description**

The ultrasonic sensor uses sonar to determine distance to an object like bats do. It offers excellent non-contact range detection with high accuracy and stable readings in an easy-to-use package. It comes complete with ultrasonic transmitter and receiver modules.

The ultrasonic sensor is being used in a wide range of electronics projects for creating obstacle detection and distance measuring application as well as various other applications.

![](./media/Makecode_0180b169.png)

The ultrasonic module will emit the ultrasonic waves after trigger signals. When the ultrasonic waves encounter the object and are reflected back, the module outputs an echo signal, so it can determine the distance of object from the time difference between trigger signal (TRIG)and echo signal(ECHO).

As the picture shows, it is like two eyes. One is transmitting end, the other is receiving end.

According to the above wiring diagram, the integrated port of the ultrasonic sensor module is connected to the 5V G P15 P16 port on the micro:bit motor driver base plate. The Trig (T) pin is controlled by P15 of the micro:bit and the pin of Echo (E) the P16.

![](./media/Makecode_1174e0ec.png)

2\. **Working Principle**

![](./media/Makecode_8ff02741.png)

(1)Pull down TRIG then trigger high level signals with least 10us;

(2)After triggering, the module will automatically send eight 40KHz ultrasonic pulses and detect whether there is a signal return;

(3)If there is a signal return, when ECHO (E) outputs a high level, then the duration of the high level is the time from transmission to reception of the ultrasonic waves. Then test distance = high level duration \*340m/s\*0.5. 

3\. **Parameters**

- Working voltage: 3-5.5V (DC)

- Working current: 15mA

- Working frequency: 40khz

- Maximum detection distance: about 3m

- Minimum detection distance: 2-3cm

- Precision: up to 0.2cm

- Sensing angle: less than 15 degrees

- Input trigger pulse: 10us TTL level

- Output echo signal: output TTL level signal (high), proportional to  range

4\. **Preparation**

- Insert the micro:bit board into the slot of keyestudio 4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the Web version of Makecode


5\. **Test Code**

![](./media/Makecode_497760b1.png)

Click“JavaScriptto view the corresponding JavaScript code: 

![](./media/Makecode_387f3243.png)

6\.  **Test Result**

Download code to micro:bit, keep USB cable connected, dial POWER switch to ON end. The distance value will be displayed on monitor.

![](./media/Makecode_2cd74c16.png)

The monitor shows the distance between the obstacle and ultrasonic sensor(as shown below).

![](./media/Makecode_422adea3.png)

Open CoolTerm, click Options to select SerialPort. Set COM port and 115200 baud rate(the baud rate of USB serial communication of Micro:bit is 115200 through the test). Click “OK” and “Connect”.

CoolTerm serial monitor displays the distance value as follows:

![](./media/Makecode_69b06998.png)

### Project 18.2：Ultrasonic Avoidance

![Img](./media/Makecode_13139b46.png)

1\. **Description**

In this project, we will integrate an ultrasonic sensor and a car to make an ultrasonic avoidance car.

Its principle is to detect the distance between the car and obstacle via the ultrasonic sensor to control the motion of smart car.

2\.  **Preparation**

- Insert the micro:bit board into the slot of keyestudio   4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the Web version of Makecode

3\.  **Flow Chart**

![Img](./media/Makecode_e2adae4b.png)

4\.  **Test Code**

![](./media/Makecode_05a4740b.png)

![Img](./media/Makecode_d7879887.png)

Click“JavaScript”to view the corresponding JavaScript code: 

![](./media/Makecode_c8f86a24.png)

![](./media/Makecode_13baf1d6.png)

5\.  **Test Result**

Download code to micro:bit, dial to ON end, and dial POWER to ON end. When the obstacle distance is greater than 20cm, the car goes forward ;
on the contrary, smart car turns left.

### Project 18.3：Ultrasonic Following

![Img](./media/Makecode_d17a7889.png)

1\. **Description**

In previous lesson, we’ve learned the basic principle of line tracking sensor. Next, we will combine the ultrasonic sensor with the car to make an ultrasonic following car.

The ultrasonic sensor detects the obstacle distance and control the motion status of car.

2\. **Preparation**

- Insert the micro:bit board into the slot of keyestudio   4WD Mecanum Robot Car V2.0

- Place batteries into battery holder

- Dial power switch to ON end

- Connect the micro:bit to your computer via an USB cable

- Open the Web version of Makecode

3\. **Flow Chart**

![Img](./media/Makecode_f5026aed.png)

4\. **Test Code**

![](./media/Makecode_03b95531.png)

Click“JavaScript”to view the corresponding JavaScript code: 

![](./media/Makecode_a93c8245.png)

5\. **Test Result**

Download code to micro:bit, dial POWER switch to ON end on shield, smart car could follow the obstacle to move.
