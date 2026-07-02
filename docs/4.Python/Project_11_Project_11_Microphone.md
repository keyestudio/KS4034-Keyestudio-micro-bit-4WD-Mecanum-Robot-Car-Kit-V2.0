### Project 11: Microfoon

![](./media/Python_3073a8af.png)

![](./media/Python_7f074115.png)

1\.  **Beschrijving**

De Micro: Bit-hoofdplaat heeft een ingebouwde microfoon, die het volume van de omgeving kan meten. Wanneer je klapt, gaat de microfoon-LED-indicator aan. Bovendien kan hij de geluidsintensiteit meten, zodat je een geluidsmeter of discobelichting kunt maken die meebeweegt met de muziek.

De microfoon bevindt zich aan de tegenovergestelde kant van de microfoon-LED-indicator en in de buurt van gaatjes waardoor geluid kan passeren. Wanneer de boord geluid detecteert, gaat de LED-indicator aan.

2\.  **Voorbereiding**

A. Sluit de micro:bit-hoofdplaat aan op je computer via de USB-kabel

B. Open de offline versie van Mu.

3\.  **Testcode1**

Start de Mu-software en open het bestand “Microphone-1\.py” om de code te importeren. Je kunt de code ook zelf invoeren in het bewerkingsvenster.

(**Opmerking: Alle woorden en symbolen moeten in het Engels worden geschreven**.)

![](./media/Python_19b38832.png)

```python
from microbit import *

while True:
    if microphone.current_event() == SoundEvent.LOUD:
        display.show(Image.HEART)
        sleep(200)
    if microphone.current_event() == SoundEvent.QUIET:
        display.show(Image.HEART_SMALL)
```

Klik op “Check” om fouten in de code te controleren. Het programma is fout als er onderstrepingen en cursors worden weergegeven. 

![](./media/Python_36a669c7.png)

Als de code correct is, verbind je de micro:bit met je computer en klik je op “Flash” om de code naar de micro:bit-plaat te downloaden.

![](./media/Python_0515bf32.png)

4\.  **Testresultaat1**

Nadat de code met succes naar de plaat is gedownload, **zet je de voeding aan via de micro USB-kabel of een externe voeding (zet de DIP-schakelaar op ON)** en druk je op de resetknop op de micro:bit.

![Img](./media/Python_bb3e1312.png)

De LED-dotmatrix toont het patroon “❤” wanneer je klapt en het patroon ![](./media/04fdfc9060943954e7938bb1a741d626.png) wanneer het stil is in de omgeving.

5\.  **Testcode2**

Start de Mu-software en open het bestand “Microphone-2\.py” om de code te importeren. Je kunt de code ook zelf invoeren in het bewerkingsvenster.

(**Opmerking: Alle woorden en symbolen moeten in het Engels worden geschreven.**)

![](./media/Python_f0e5a346.png)

```python
from microbit import *
maxSound = 0
lights = Image("11111:"
              "11111:"
              "11111:"
              "11111:"
              "11111")
# ignore first sound level reading
soundLevel = microphone.sound_level()
sleep(200)

while True:
    if button_a.is_pressed():
        display.scroll(maxSound)
    else:
        soundLevel = microphone.sound_level()
        display.show(lights * soundLevel)
        if soundLevel > maxSound:
            maxSound = soundLevel
```

Klik op “Check” om fouten in de code te controleren. Het programma is fout als er onderstrepingen en cursors worden weergegeven. 

![](./media/Python_d0c79871.png)

Als de code correct is, verbind je de micro:bit met je computer en klik je op “Flash” om de code naar de micro:bit-plaat te downloaden.

![](./media/Python_d828b9ee.png)

6\.  **Testresultaat2**

Nadat de code met succes naar de plaat is gedownload, **zet je de voeding aan via de micro USB-kabel of een externe voeding (zet de DIP-schakelaar op ON)** en druk je op de resetknop op de micro:bit.

![Img](./media/Python_bb3e1312.png)

 Wanneer de knop A wordt ingedrukt, toont de LED-dotmatrix de waarde van het grootste volume ( **let op: het grootste volume kan worden gereset via de Reset-knop aan de andere kant van de plaat** ). Wanneer je klapt, geldt: hoe luider het geteste geluid, hoe feller de 25 LED's op het LED-dotmatrixscherm oplichten.

7\.  **Uitleg van de code**

![Img](./media/Python_980f62b3.png)