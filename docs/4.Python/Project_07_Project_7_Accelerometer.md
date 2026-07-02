### Project 7：Accelerometer

![](./media/Python_26d107ae.png)

1\.  **Beschreibung**

Das micro: bit main board V2 verfügt über einen integrierten LSM303AGR-Gravitationsbeschleunigungssensor, auch Beschleunigungssensor (Accelerometer) genannt, mit einer Auflösung von 8/10/12 Bit. Im Codeabschnitt kann der Bereich auf 1g, 2g, 4g und 8g eingestellt werden.

Wir verwenden Beschleunigungssensoren häufig, um den Zustand von Geräten zu erkennen.

In diesem Projekt zeigen wir, wie die Lage des Boards mit dem Beschleunigungssensor gemessen wird. Anschließend betrachten wir die rohen Dreiachsenausgaben des Beschleunigungssensors.

2\.  **Vorbereitung**

A. Verbinden Sie das micro:bit main board per USB-Kabel mit Ihrem Computer.

B. Öffnen Sie die Offline-Version von Mu.

3\.  **Testcode1**

Starten Sie die Mu-Software und öffnen Sie die Datei “Three-axis acceleration sensor -1\.py“, um den Code zu importieren. Sie können den Code auch selbst im Editor eingeben.

(**Hinweis: Alle Wörter und Zeichen müssen in Englisch geschrieben werden.**)

![](./media/Python_f20f5b58.png)

```python
from microbit import *

while True:
    gesture = accelerometer.current_gesture()

    if gesture == "shake":
        display.show("1")
    if gesture == "up":
        display.show("2")
    if gesture == "down":
        display.show("3")
    if gesture == "face up":
        display.show("4")
    if gesture == "face down":
        display.show("5")
    if gesture == "left":
        display.show("6")
    if gesture == "right":
        display.show("7")
    if gesture == "freefall":
        display.show("8")
```

Klicken Sie auf “Check”, um den Code auf Fehler zu prüfen. Das Programm ist fehlerhaft, wenn Unterstreichungen und Cursor angezeigt werden. 

![](./media/Python_07e4b578.png)

Wenn der Code korrekt ist, verbinden Sie das micro:bit mit Ihrem Computer und klicken Sie auf “Flash”, um den Code auf das micro:bit-Board zu übertragen.

![](./media/Python_eb56750b.png)

4\.  **Testergebnis1**

Nachdem der Code erfolgreich auf das Board geladen wurde, **schalten Sie die Stromversorgung über das Micro-USB-Kabel oder eine externe Stromquelle ein (DIP-Schalter auf ON stellen)** und drücken Sie die Reset-Taste am micro:bit.

![Img](./media/Python_bb3e1312.png)

Wenn wir das micro: bit main board schütteln, zeigt die LED-Matrix unabhängig von der Richtung die Ziffer “1” an.

Wenn es aufrecht gehalten wird (das Logo oberhalb der LED-Matrix), erscheint die Zahl 2.

![](./media/Python_b91421df.jpg)

Wenn es umgedreht gehalten wird (das Logo unterhalb der LED-Matrix), wird wie unten gezeigt angezeigt.

![](./media/Python_69e81587.jpg)

Wenn es ruhig auf dem Tisch liegt und die Vorderseite zeigt, erscheint die Zahl 4.

![](./media/Python_9e08cb69.jpg)

Wenn es ruhig auf dem Tisch liegt und die Rückseite zeigt, erscheint die Zahl 5.

Wenn das Board nach links geneigt wird, zeigt die LED-Matrix die Zahl 6, wie unten dargestellt:

![](./media/Python_81fa2ce1.jpg)

Wenn das Board nach rechts geneigt wird, zeigt die LED-Matrix die Zahl 7, wie unten dargestellt：

![](./media/Python_fc13912b.jpg)

Wenn das Board auf den Boden geschlagen wird, kann dieser Vorgang als freier Fall betrachtet werden und die LED-Matrix zeigt die Zahl 8. (Bitte beachten Sie, dass dieser Test nicht empfohlen wird, da das Mainboard beschädigt werden kann.)

**Achtung: Wenn Sie diese Funktion ausprobieren möchten, können Sie die Beschleunigung auch auf 3g, 6g oder 8g einstellen.**

5\.  **Testcode2**

Starten Sie die Mu-Software und öffnen Sie die Datei “Three-axis acceleration sensor -2\.py“, um den Code zu importieren. Sie können den Code auch selbst im Editor eingeben.

(**Hinweis: Alle Wörter und Zeichen müssen in Englisch geschrieben werden.**)

![](./media/Python_0f7ccf57.png)

```python
from microbit import *

while True:

    x = accelerometer.get_x()

    y = accelerometer.get_y()

    z = accelerometer.get_z()

    print("x, y, z:", x, y, z)

    sleep(100)
```
Klicken Sie auf “Check”, um den Code auf Fehler zu prüfen. Das Programm ist fehlerhaft, wenn Unterstreichungen und Cursor angezeigt werden. 

![](./media/Python_0ed2221e.png)

Wenn der Code korrekt ist, verbinden Sie das micro:bit mit Ihrem Computer und klicken Sie auf “Flash”, um den Code auf das micro:bit-Board zu übertragen.

![](./media/Python_35c4c76b.png)

6\.  **Testergebnis2**

Nachdem der Code erfolgreich auf das Board geladen wurde, **schalten Sie die Stromversorgung über das Micro-USB-Kabel oder eine externe Stromquelle ein (DIP-Schalter auf ON stellen)**. Klicken Sie auf “REPL” und drücken Sie die Reset-Taste am micro:bit.

![Img](./media/Python_bb3e1312.png)

Dann zeigt das REPL-Fenster die Werte der Beschleunigung entlang der X-Achse, Y-Achse und Z-Achse, wie unten dargestellt:

![](./media/Python_940cfcf7.png)

Nach Bezugnahme auf das Datenhandbuch des MMA8653FC und das Hardware-Schaltbild des micro: bit main board sind die Beschleunigungskoordinaten des micro: bit in der folgenden Abbildung dargestellt:

![](./media/Python_ebd0d44d.png)

7\.  **Codeerklärung**

![Img](./media/Python_d533d72c.png)

![Img](./media/Python_89d95342.png)

---