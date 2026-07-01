### Project 10: Touch-sensitive Logo

![](./media/Python_64469585.png)

1\.  **Description**

The Micro: Bit main board V2 is equipped with a golden touch-sensitive logo, which can act as an input component like an button.

It contains a capacitive touch sensor that senses small changes in the electric field when pressed (or touched), just like your phone or tablet screen. When you press it , the program can be activated.

2\.  **Preparation**

A. Attach the micro:bit main board to your computer via the USB cable

B. Open the offline version of Mu.

3\.  **Test Code**

Enter Mu software and open the file“Touch-sensitive Logo\.py”to import code.You can also input code in the edit window yourself.

(**Note: All English words and symbols must be written in English**.)

![](./media/Python_0c54cbe5.png)

```python
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
```

**How Micro:bit works?**

A\. The runtime is recorded in milliseconds(ms) .

B\. When you press button A, a variable named start will be set to the current running time.

C\. When you press button B, the start time will be subtracted from the new running time to calculate the passed time since you started the stopwatch. This difference is added to the total time, which is stored in a variable named time.

D\. If you press the golden logo, the program will display the total elapsed time on the LED display. It converts time from milliseconds (thousandths of a second) to seconds by dividing by 1000. It uses the integer division operator to give an integer (integer) result.

E\. The program is also controlled by a Boolean variable named running. Boolean variable only has two values: true or false. If "running" is "true", it means that the stopwatch has started. If "running" is false, it means that the stopwatch has not started or has stopped.

F\. If "running" is true, the beating heart pattern will be displayed on the LED dot matrix screen.

G\. (7) If the stopwatch has stopped and the "running" is false, when you press the golden logo, it will only display the time.

H\. If the stopwatch has been started and"running" is true, it only need to ensure that the time variable will change when button B is pressed, and the code can also prevent false readings.

Click“Check”to examine errors in the code. The program proves wrong if underlines and cursors are shown.

![](./media/Python_1766a28c.png)

If the code is correct, connect the micro:bit to your computer and click“Flash”to download code to the micro:bit board.

![](./media/Python_a3d6e994.png)

4\.  **Test Result**

After downloading the code to the board successfully, **power on via micro USB cable or external power supply(turn the DIP switch to ON)**,and press the reset button on micro:bit.

![Img](./media/Python_bb3e1312.png)

Press button A to start the stopwatch. When timing, the beating heart pattern will be displayed on the LED dot matrix screen. Press button B to stop it and you can start and stop it at any time. 

It will keep recording time, just like a real stopwatch. Press the golden logo in the front of the micro:bit to display the measured time in seconds. And the time can be reset to zero by pressing the reset button on the back of it.
