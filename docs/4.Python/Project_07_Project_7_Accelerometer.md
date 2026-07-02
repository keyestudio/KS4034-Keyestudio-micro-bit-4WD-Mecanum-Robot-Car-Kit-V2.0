### Project 7：Accelerometer

![](./media/Python_26d107ae.png)

1\.  **Beschrijving**

De micro: bit main board V2 heeft een ingebouwde LSM303AGR zwaartekrachtversnellingssensor, ook wel accelerometer genoemd, met een resolutie van 8/10/12 bits. In het codegedeelte kan het bereik worden ingesteld op 1g, 2g, 4g en 8g.

We gebruiken een accelerometer vaak om de toestand van machines te detecteren.

In dit project leggen we uit hoe de positie van de board met de accelerometer kan worden gemeten. Vervolgens bekijken we de ruwe driedimensionale uitvoer van de accelerometer.

2\.  **Voorbereiding**

A. Sluit de micro:bit main board aan op uw computer via de USB-kabel.

B. Open de offline versie van Mu.

3\.  **Testcode1**

Start de Mu-software en open het bestand “Three-axis acceleration sensor -1\.py“ om de code te importeren. U kunt de code ook zelf in het bewerkingsvenster invoeren.

(**Opmerking: Alle woorden en symbolen moeten in het Engels worden geschreven.**)

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

Klik op “Check” om fouten in de code te controleren. Het programma is fout als onderstrepingen en cursors worden weergegeven. 

![](./media/Python_07e4b578.png)

Als de code correct is, verbind dan de micro:bit met uw computer en klik op “Flash” om de code naar het micro:bit-board te downloaden.

![](./media/Python_eb56750b.png)

4\.  **Testresultaat1**

Nadat de code succesvol naar het board is gedownload, **zet de voeding aan via de micro USB-kabel of een externe voeding (zet de DIP-schakelaar op ON)** en druk op de resetknop op de micro:bit.

![Img](./media/Python_bb3e1312.png)

Wanneer we het micro: bit main board schudden, geeft de LED-dotmatrix ongeacht de richting het cijfer “1” weer.

Wanneer het rechtop wordt gehouden (met het logo boven de LED-dotmatrix), verschijnt het cijfer 2.

![](./media/Python_b91421df.jpg)

Wanneer het ondersteboven wordt gehouden (met het logo onder de LED-dotmatrix), wordt het als hieronder weergegeven.

![](./media/Python_69e81587.jpg)

Wanneer het stil op het bureau ligt met de voorkant omhoog, verschijnt het cijfer 4.

![](./media/Python_9e08cb69.jpg)

Wanneer het stil op het bureau ligt met de achterkant omhoog, verschijnt het cijfer 5.

Wanneer de board naar links gekanteld is, toont de LED-dotmatrix het cijfer 6, zoals hieronder weergegeven:

![](./media/Python_81fa2ce1.jpg)

Wanneer de board naar rechts gekanteld is, toont de LED-dotmatrix het cijfer 7, zoals hieronder weergegeven：

![](./media/Python_fc13912b.jpg)

Wanneer de board op de grond wordt geslagen, kan dit proces worden beschouwd als vrije val en toont de LED-dotmatrix het cijfer 8. (Let op: deze test wordt niet aanbevolen omdat het de main board kan beschadigen.)

**Let op: Als u deze functie wilt proberen, kunt u de versnelling ook instellen op 3g, 6g of 8g.**

5\.  **Testcode2**

Start de Mu-software en open het bestand “Three-axis acceleration sensor -2\.py“ om de code te importeren. U kunt de code ook zelf in het bewerkingsvenster invoeren.

(**Opmerking: Alle woorden en symbolen moeten in het Engels worden geschreven.**)

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
Klik op “Check” om fouten in de code te controleren. Het programma is fout als onderstrepingen en cursors worden weergegeven. 

![](./media/Python_0ed2221e.png)

Als de code correct is, verbind dan de micro:bit met uw computer en klik op “Flash” om de code naar het micro:bit-board te downloaden.

![](./media/Python_35c4c76b.png)

6\.  **Testresultaat2**

Nadat de code succesvol naar het board is gedownload, **zet de voeding aan via de micro USB-kabel of een externe voeding (zet de DIP-schakelaar op ON)**. Klik op “REPL” en druk op de resetknop op de micro:bit.

![Img](./media/Python_bb3e1312.png)

Vervolgens toont het REPL-venster de waarden van de versnelling op de X-as, Y-as en Z-as zoals hieronder weergegeven:

![](./media/Python_940cfcf7.png)

Na raadpleging van de MMA8653FC datasheet en het hardware-schema van het micro: bit main board, worden de accelerometercoördinaten van het micro: bit weergegeven in de onderstaande afbeelding:

![](./media/Python_ebd0d44d.png)

7\.  **Code-uitleg**

![Img](./media/Python_d533d72c.png)

![Img](./media/Python_89d95342.png)

---