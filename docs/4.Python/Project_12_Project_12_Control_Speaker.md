### Project 12: Luidspreker bedienen

1\.  **Beschrijving**

In de vorige projecten hebben we respectievelijk het aanrakinggevoelige logo en de luidspreker behandeld. In dit project combineren we deze twee componenten om muziek af te spelen.

2\.  **Benodigde componenten**

|![](./media/Python_021507bd.png)|![](./media/Python_84cdea05.jpg)|
|-|-|
|Micro:bit main board \*1|USB cable\*1|


3\.  **Bedradingsschema**

Sluit het Micro:bit main board met de USB-kabel aan op uw computer.

![](./media/Python_611b2c4e.png)

4\.  **Testcode**

Start de Mu-software en open het bestand “Touch the Logo to control the speaker\.py” om de code te importeren. U kunt de code ook zelf invoeren in het bewerkingsvenster.

(**Opmerking: Alle woorden en symbolen moeten in het Engels worden geschreven**.)

![](./media/Python_600c8fa6.png)

```python
from microbit import *

import music

display.show(Image.MUSIC_QUAVER)

while True:

    if pin_logo.is_touched():
        music.play(music.BIRTHDAY)
```

Klik op “Check” om fouten in de code te controleren. Het programma is onjuist als onderstrepingen en cursors worden weergegeven.

![](./media/Python_dcc17127.png)

Als de code correct is, sluit u de micro:bit aan op uw computer en klikt u op “Flash” om de code naar de micro:bit-board te downloaden.

![](./media/Python_be3d4ee9.png)

5\.  **Testresultaat**

Nadat de code succesvol naar de board is gedownload, **zet u de voeding aan via de micro USB-kabel of externe voeding (zet de DIP-schakelaar op ON)** en druk op de resetknop van de micro:bit.

![Img](./media/Python_bb3e1312.png)

De luidspreker speelt het lied “*Happy Birthday to You*” wanneer het logo wordt aangeraakt.

6\.  **Code-uitleg**

![Img](./media/Python_852be78f.png)

**Bluetooth draadloze communicatie**

De micro:bit heeft een energiezuinig Bluetooth-module voor communicatie, maar beschikt over 16 KB RAM. De BLE-heap/stack neemt echter 12 KB RAM in beslag, waardoor er niet genoeg ruimte is om microPython uit te voeren.

Op dit moment ondersteunt microPython de Bluetooth-service niet.

[https://microbit-micropython.readthedocs.io/en/latest/ble.html](https://microbit-micropython.readthedocs.io/en/latest/ble.html)

De voorgaande projecten zijn een inleiding tot sensoren en modules. De verdere lessen zijn uitdagender voor beginners.

(**Opmerking: Om te voorkomen dat de micro:bit-board beschadigd raakt, haalt u voordat u deze op de car expansion board monteert de micro USB-kabel los en schakelt u de voeding van de micro:bit motor driver base plate uit en zet u de POWER-schakelaar op OFF. Evenzo, voordat u de main board van de car expansion board verwijdert, haalt u de micro USB-kabel los en schakelt u de voeding van de micro:bit motor driver base plate uit.**)