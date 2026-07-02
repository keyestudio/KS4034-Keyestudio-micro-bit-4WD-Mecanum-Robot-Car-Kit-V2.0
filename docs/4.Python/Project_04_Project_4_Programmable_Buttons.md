### Project 4：Programmeerbare knoppen

![](./media/Python_06be84fb.png)

1\.  **Beschrijving**

![](./media/Python_b6d60ae2.png)

Knoppen kunnen worden gebruikt om schakelingen te bedienen. In een schakeling met een drukknop wordt het circuit gesloten wanneer de knop wordt ingedrukt en bij loslaten weer onderbroken.

Beide uiteinden van de knop lijken op twee bergen. Er loopt een rivier tussenin.  
Het interne metalen deel verbindt de twee zijden zodat de stroom kan doorlopen, net zoals een brug die twee bergen verbindt.

De interne structuur van de knop wordt als volgt weergegeven: vóór het indrukken zijn 1, 2, 3 en 4 ingeschakeld. Echter, 1 en 3 of 1 en 4 of 2 en 3 of 2 en 4 zijn niet verbonden; deze verbindingen worden pas geactiveerd wanneer de knop wordt ingedrukt. ![](./media/Python_d2a204e6.png)

De micro:bit-hoofdplaat heeft drie drukknoppen: twee zijn programmeerbare knoppen (aangeduid met A en B), en die aan de andere kant is een resetknop. Door op de twee programmeerbare knoppen te drukken kunnen drie verschillende signalen worden ingevoerd. We kunnen knop A of B afzonderlijk indrukken of ze samen indrukken; de LED-dotmatrix toont respectievelijk A, B en AB. Laten we beginnen.

2\.  **Voorbereiding**

A. Sluit de micro:bit-hoofdplaat via de USB-kabel aan op uw computer.

B. Open de offlineversie van Mu.

3\.  **Test Code1**

Start de Mu-software en open het bestand “Programmable Buttons-1\.py” om de code te laden. U kunt de code ook zelf in het bewerkingsvenster invoeren.

(**Opmerking: Alle woorden en symbolen moeten in het Engels worden geschreven.**)

![](./media/Python_2637f524.png)

```python
from microbit import *

while True:
    if button_a.is_pressed():
        display.show("A")
    elif button_a.is_pressed() and button_b.is_pressed():
        display.scroll("AB")
    elif button_b.is_pressed():
        display.show("B")
```
Klik op “Check” om fouten in de code te controleren. Het programma is fout als er onderstrepingen en cursors worden weergegeven.

![](./media/Python_a0f284f3.png)

Als de code correct is, verbindt u de micro:bit met uw computer en klikt u op “Flash” om de code naar de micro:bit-ontwikkelbord te downloaden.

![](./media/Python_5694d3ce.png)

4\.  **Testresultaat1**

Nadat de code met succes naar het bord is gedownload, **zet de voeding aan via de micro-USB-kabel of een externe voeding (zet de DIP-schakelaar op ON)** en druk op de resetknop op het bord.

![Img](./media/Python_bb3e1312.png)

De 5*5 LED-dotmatrix toont “A” als knop A wordt ingedrukt, vervolgens “B” als knop B wordt ingedrukt, en “AB” als A en B samen worden ingedrukt.

5\.  **Test Code2**

Start de Mu-software en open het bestand “Programmable Buttons-2\.py” om de code te laden. U kunt de code ook zelf in het bewerkingsvenster invoeren.

(**Opmerking: Alle woorden en symbolen moeten in het Engels worden geschreven.**)

![](./media/Python_1a1126f6.png)

![](./media/Python_94849305.png)

```python
from microbit import *
a = 0
b = 0
val1 = Image("00000:""00000:""00000:""00000:""00900")
val2 = Image("00000:""00000:""00000:""00900:""99999")
val3 = Image("00000:""00000:""00900:""99999:""99999")
val4 = Image("00000:""00900:""99999:""99999:""99999")
val5 = Image("00900:""99999:""99999:""99999:""99999")
val6 = Image("99999:""99999:""99999:""99999:""99999")
display.show(val1)

while True:
    while button_a.is_pressed() == True:
        sleep(10)
        if button_a.is_pressed() == False:
            a = a + 1
            if(a >= 5):
                a = 5
            break
    while button_b.is_pressed() == True:
        sleep(10)
        if button_b.is_pressed() == False:
            a = a - 1
            if(a <= 0):
                a = 0
            break
    if a == 0:
        display.show(val1)
    if a == 1:
        display.show(val2)
    if a == 2:
        display.show(val3)
    if a == 3:
        display.show(val4)
    if a == 4:
        display.show(val5)
    if a == 5:
        display.show(val6)
```
Klik op “Check” om fouten in de code te controleren. Het programma is fout als er onderstrepingen en cursors worden weergegeven.

![](./media/Python_21771d90.png)

![Img](./media/Python_8d257384.png)

Als de code correct is, verbindt u de micro:bit met uw computer en klikt u op “Flash” om de code naar de micro:bit-ontwikkelbord te downloaden.

![](./media/Python_84ba8cde.png)

![Img](./media/Python_8d257384.png)

6\.  **Testresultaat2**

Nadat de code met succes naar het bord is gedownload, **zet de voeding aan via de micro-USB-kabel of een externe voeding (zet de DIP-schakelaar op ON)** en druk op de resetknop op het bord.

![Img](./media/Python_bb3e1312.png)

Als knop A wordt ingedrukt, neemt het aantal rood oplichtende LED's toe; als knop B wordt ingedrukt, neemt het aantal rood oplichtende LED's af.

7\.  **Uitleg van de code**

![Img](./media/Python_b33858dc.png)

![Img](./media/Python_32bd1cca.png)

---