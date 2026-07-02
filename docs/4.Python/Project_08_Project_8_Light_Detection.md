### Project 8：Lichtdetectie

![](./media/Python_b855274f.png)

1\.  **Beschrijving**

In dit project richten we ons op de lichtdetectiefunctie van de Micro: Bit main board. Dit wordt gerealiseerd door de LED dot matrix omdat het main board niet is uitgerust met een fotoweerstand.

2\.  **Voorbereiding**

A. Sluit het micro:bit main board via de USB-kabel aan op uw computer

B. Open de offline versie van Mu.

3\.  **Testcode**

Start de Mu-software en open het bestand “Detect Light Intensity by Microbit\.py” om de code te importeren. U kunt de code ook zelf in het bewerkingsvenster invoeren.

(**Opmerking: Alle Engelse woorden en symbolen moeten in het Engels worden geschreven.**)

![](./media/Python_b4f06503.png)

```python
from microbit import *

while True:

    Lightintensity = display.read_light_level()

    print("Light intensity:", Lightintensity)

    sleep(100)
```
Klik op “Check” om fouten in de code te controleren. Het programma is onjuist als er onderstrepingen en cursors worden weergegeven.

![](./media/Python_b41eeb0f.png)

Als de code correct is, sluit u de micro:bit op uw computer aan en klikt u op “Flash” om de code naar het micro:bit board te downloaden.

![](./media/Python_7baa2190.png)

4\.  **Testresultaat**

Na het succesvol downloaden van de code naar het board, **zet u de voeding aan via de micro USB-kabel of een externe voeding (turn the DIP switch to ON)**. Klik op “REPL” en druk op de resetknop op de micro:bit.

![Img](./media/Python_bb3e1312.png)

Vervolgens zal het REPL-venster de waarde van de lichtintensiteit weergeven, zoals hieronder getoond.

Wanneer de LED dot matrix met de hand wordt afgedekt, is de getoonde lichtintensiteit ongeveer 0; wanneer de LED dot matrix aan licht wordt blootgesteld, wordt de weergegeven lichtintensiteit sterker naarmate het licht toeneemt.

![](./media/Python_778d89d6.png)

5\.  **Code-uitleg**

![Img](./media/Python_dcdc4536.png)