### Project 9: Speaker

![](./media/Python_ac515b9a.png)

1\.  **Beschrijving**

Het micro:bit-hoofdboard heeft een ingebouwde speaker, waardoor het toevoegen van geluid aan programma's gemakkelijker wordt. Het kan ook geprogrammeerd worden om allerlei tonen te produceren, zoals het spelen van het lied *Ode to Joy*.

2\.  **Voorbereiding**

A. Sluit het micro:bit-hoofdboard met de USB-kabel aan op uw computer

B. Open de offline versie van Mu.

3\.  **Testcode**

Start de Mu-software en open het bestand “Speaker\.py” om de code te importeren. U kunt de code ook zelf in het bewerkingsvenster invoeren.

(**Opmerking: Alle woorden en symbolen moeten in het Engels geschreven zijn**.)

![](./media/Python_eec7f643.png)

```python
from microbit import *

import audio

display.show(Image.MUSIC_QUAVER)

while True:
    audio.play(Sound.GIGGLE)
    sleep(1000)
    audio.play(Sound.HAPPY)
    sleep(1000)
    audio.play(Sound.HELLO)
    sleep(1000)
    audio.play(Sound.YAWN)
    sleep(1000)
```

Klik op “Check” om fouten in de code te controleren. Het programma is fout als er onderstrepingen en cursors worden weergegeven.

![](./media/Python_f8852abf.png)

Als de code correct is, sluit u de micro:bit aan op uw computer en klikt u op “Flash” om de code naar het micro:bit-board te downloaden.

![](./media/Python_3fd94e43.png)

4\.  **Testresultaat**

Nadat de code succesvol naar het board is gedownload, **zet u de voeding aan via de micro USB-kabel of een externe voedingsbron (zet de DIP-schakelaar op ON)** en druk op de resetknop van de micro:bit.

![Img](./media/Python_bb3e1312.png)

 De speaker geeft geluid en de LED-puntmatrix toont het muzieksymbool.

5\.  **Codeuitleg**

![Img](./media/Python_18c047bd.png)

---