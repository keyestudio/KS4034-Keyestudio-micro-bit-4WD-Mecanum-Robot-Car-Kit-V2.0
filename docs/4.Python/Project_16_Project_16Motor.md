### Projekt 16：Motor

![](./media/Python_32655f47.png)

1\.  **Beschreibung**

Das Keyestudio 4WD Mecanum Robot Car ist mit 4 DC‑Untersetzungsgetriebemotoren (auch Getriebemotor genannt) ausgestattet, die auf gewöhnlichen DC‑Motoren basieren. Sie verfügen über ein passendes Untersetzungsgetriebe, das eine geringere Drehzahl, aber ein höheres Drehmoment liefert. Verschiedene Übersetzungsverhältnisse des Getriebes ermöglichen unterschiedliche Geschwindigkeiten und Drehmomente.

Der Getriebemotor ist die Kombination aus Getriebe und Motor und wird häufig in der Stahl‑ und Maschinenbauindustrie eingesetzt.

Das micro:bit Motor Driver Shield verwendet einen STC8G‑ und einen HR8833‑Chip. Um IO‑Port‑Ressourcen zu sparen, steuern wir die Drehrichtung und Geschwindigkeit der 4 DC‑Getriebemotoren mit dem HR8833‑Chip.

**Details zu den Chips:**

![](./media/Python_d7132b53.jpg)

Vorderseite

![](./media/Python_4919ce3b.png)

Rückseite

![](./media/Python_fbfa17f7.png)

Schaltplan des STC8G1K08‑Chips

![](./media/Python_47cdde6b.png)

Schaltplan des HR8833‑Motor­treibers

2\. **Vorbereitung**

- Stecken Sie das micro:bit‑Board in den Steckplatz des Keyestudio 4WD Mecanum Robot Car V2.0

- Legen Sie die Batterien in den Batteriehalter ein

- Stellen Sie den Netzschalter auf die ON‑Position

- Verbinden Sie das micro:bit über ein USB‑Kabel mit dem Computer

- Öffnen Sie die Offline‑Version von Mu.

3\. **Test Code1**

Öffnen Sie die Mu‑Software und laden Sie die Datei “microbit-Motor Driving-1\.py”, um den Code zu importieren. Sie können den Code auch selbst in das Editor‑Fenster eingeben.

(**Hinweis: Alle englischen Wörter und Symbole müssen in Englisch geschrieben werden**.)

Klicken Sie “Files”, um die Bibliotheksdatei “keyes_mecanum_Car.py” auf das micro:bit zu importieren. 

Klicken Sie “Check”, um den Code auf Fehler zu überprüfen. Das Programm ist fehlerhaft, wenn Unterstreichungen und Cursor angezeigt werden. 

Wenn der Code korrekt ist, verbinden Sie das micro:bit mit Ihrem Computer und klicken Sie “Flash”, um den Code auf das micro:bit‑Board zu laden.

![](./media/Python_71476377.png)

```python
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
```

4\. **Testergebnis1**

Nachdem der Code erfolgreich auf das Board geladen wurde, **externe Stromversorgung (DIP‑Schalter auf ON)**, und drücken Sie den Reset‑Knopf am micro:bit.

![Img](./media/Python_bb3e1312.png)

Dann fährt das Auto 1 s vorwärts, 1 s rückwärts, 1 s nach links, 1 s nach rechts, 1 s gegen den Uhrzeigersinn, 1 s im Uhrzeigersinn und hält 1 s an. Die Matrix zeigt ebenfalls die Muster an.

5\. **Test Code2**

Öffnen Sie die Mu‑Software und laden Sie die Datei “microbit-Motor Driving-2\.py”, um den Code zu importieren. Sie können den Code auch selbst in das Editor‑Fenster eingeben.

(**Hinweis: Alle englischen Wörter und Symbole müssen in Englisch geschrieben werden**.)

Klicken Sie “Files”, um die Bibliotheksdatei “keyes_mecanum_Car.py“ auf das micro:bit zu importieren. 

Klicken Sie “Check”, um den Code auf Fehler zu überprüfen. Das Programm ist fehlerhaft, wenn Unterstreichungen und Cursor angezeigt werden. 

Wenn der Code korrekt ist, verbinden Sie das micro:bit mit Ihrem Computer und klicken Sie “Flash”, um den Code auf das micro:bit‑Board zu laden.

![](./media/Python_96230faf.png)

```python
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
```

6\. **Testergebnis2**

Nachdem der Code erfolgreich auf das Board geladen wurde, **externe Stromversorgung (DIP‑Schalter auf ON)**, und drücken Sie den Reset‑Knopf am micro:bit.

![Img](./media/Python_bb3e1312.png)

Wenn die Tasten A und B zunächst gedrückt werden, zeigt das micro:bit ein „L“ an; die Fahrroute des Autos ist „L“. Wenn sie erneut gedrückt werden, wird auf dem micro:bit „口“ angezeigt und die Fahrroute des Autos ist „口“. Das Auto wiederholt dieses Muster.

7\.  **Code‑Erklärung**

![Img](./media/Python_70b4e70f.png)

![Img](./media/Python_e3250a8a.png)