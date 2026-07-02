### Project 2：Een enkele LED laten oplichten

![](./media/Python_b855274f.png)

1\.  **Beschrijving**

De LED-pixelmatrix bestaat uit 25 diodes, gerangschikt in een 5×5 vierkant en geplaatst op de kruising van rijlijnen (X) en kolomlijnen (Y). We kunnen één van de 25 LEDs aansturen door coördinaatpunten in te stellen. Bijvoorbeeld: de eerste LED in de eerste rij bevindt zich op (0,0) en de derde LED in de eerste rij bevindt zich op (2,0), enzovoort.

![](./media/Python_094d5908.png)

2\.  **Voorbereiding**

A. Sluit de micro:bit hoofdbord aan op uw computer via de USB-kabel

B. Open de offlineversie van Mu.

3\.  **Testcode**

Start de Mu-software en open het bestand “Single LED display\.py.” om de code te importeren. U kunt de code ook zelf in het bewerkingsvenster invoeren.

(**Opmerking: Alle Engelse woorden en symbolen moeten in het Engels worden geschreven**)

![](./media/Python_9545233e.png)

```python
from microbit import *

val1 = Image("09000:""00000:""00000:""00000:""00000:")
val2 = Image("00000:""00000:""00000:""00000:""00090:")
val3 = Image("00000:""00000:""00000:""00000:""00000:")

while True:
    display.show(val1)
    sleep(500)
    display.show(val3)
    sleep(500)
    display.show(val2)
    sleep(500)
    display.show(val3)
    sleep(500)

```

Klik op “Check” om fouten in de code te controleren. Het programma is fout als er onderstrepingen en cursors worden weergegeven.

![](./media/Python_d205be08.png)

Als de code correct is, verbind dan de micro:bit met uw computer en klik op “Flash” om de code naar het micro:bit-bord te downloaden.

![](./media/Python_86dd6eea.png)

4\.  **Testresultaat**

Nadat de code succesvol naar het bord is gedownload, **schakel de voeding in via de micro-USB-kabel of een externe voeding (zet de DIP-schakelaar op ON)** en druk op de resetknop op het bord.

![Img](./media/Python_bb3e1312.png)

De LED op (1,0) zal 0,5 s aan- en uitgaan en de LED op (3,4) zal 0,5 s aan- en uitgaan, en deze volgorde zal zich blijven herhalen.

5\.  **Codeverklaring**

![Img](./media/Python_c79b7922.png)

6\.  **Referentie**

sleep(ms) : wachttijd

Voor meer details over de vertraging, zie de link: [https://microbit-micropython.readthedocs.io/en/latest/utime.html](https://microbit-micropython.readthedocs.io/en/latest/utime.html)