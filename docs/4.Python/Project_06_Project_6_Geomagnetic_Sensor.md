### Project 6：Geomagnetic Sensor

![](./media/Python_26d107ae.png)

1\.  **Beschrijving**

Dit project introduceert voornamelijk het gebruik van de geomagnetische sensor van de micro:bit. Naast het detecteren van de sterkte van het magnetische veld, kan deze ook worden gebruikt om de richting te bepalen, wat een belangrijk onderdeel is van het heading- en attitude-referentiesysteem (AHRS).

Het gebruikt de FreescaleMAG3110 driewasige magnetometer. De I2C-interface communiceert extern, het bereik is ±1000µT en de maximale gegevensverversingssnelheid is 80Hz. In combinatie met een versnellingsmeter kan het de positie berekenen. Daarnaast wordt het toegepast voor magnetische detectie en kompasblokken.

Vervolgens kunnen we de door het apparaat gedetecteerde waarde uitlezen om de oriëntatie te bepalen. De micro:bit-board moet worden gekalibreerd wanneer de magneetsensor werkt. De juiste kalibratiemethode is het draaien van de micro:bit-board.

Bovendien kunnen objecten in de buurt de nauwkeurigheid van de metingen en de kalibratie beïnvloeden.

2\.  **Voorbereiding**

A. Sluit de micro:bit hoofdbord met de USB-kabel aan op uw computer

B. Open de offline versie van Mu.

3\.  **Test Code1**

Start de Mu-software en open het bestand “Magnetic sensor -1\.py” om de code te importeren. U kunt de code ook zelf in het bewerkingsvenster invoeren.

(**Opmerking: Alle woorden en symbolen moeten in het Engels worden geschreven**.)

![](./media/Python_1366c5ed.png)

```python
from microbit import *

compass.calibrate()

while True:

    if button_a.is_pressed():
        display.scroll(compass.heading())
```
Klik op “Check” om fouten in de code te controleren. Het programma is fout als er onderstrepingen en cursors worden weergegeven. 

![](./media/Python_5bfe40c4.png)

Als de code correct is, verbind de micro:bit met de computer en klik op “Flash” om de code naar het micro:bit-bord te downloaden.

![](./media/Python_695d8f29.png)

4\.  **Testresultaat1**

Nadat de code met succes naar het bord is gedownload, **zet de voeding aan via de micro USB-kabel of externe voeding (zet de DIP-schakelaar op ON)** en druk op de resetknop op de micro:bit.

![Img](./media/Python_bb3e1312.png)

 De LED-puntenmatrix toont “TILT TO FILL SCREEN”. Als u op knop A drukt, vraagt het bord om de kompas te kalibreren. Ga vervolgens naar de kalibratiepagina. Draai het bord totdat alle 25 rode LED’s branden, zoals hieronder weergegeven.

![](./media/Python_c8fd6670.jpg)

Daarna verschijnt een smile-patroon ![](./media/Python_a3b91e3e.png), wat betekent dat de kalibratie is voltooid. Wanneer het kalibratieproces is voltooid, zal het indrukken van knop A de magnetometerlezing rechtstreeks op het scherm tonen. De richtingen noord, oost, zuid en west komen overeen met respectievelijk 0°, 90°, 180° en 270°.

5\.  **Test Code2**

Voor de onderstaande afbeelding zal de pijl naar rechtsboven wijzen wanneer de waarde in het bereik van 292,5 tot 337,5 ligt. Omdat 0,5 niet in de code kan worden ingevoerd, gebruiken we de waarden 293 en 338.

Voeg vervolgens andere instructies toe om een volledige code te maken.

![](./media/Python_d1a4e9f6.png)

Start de Mu-software en open het bestand “Magnetic sensor -2\.py” om de code te importeren. U kunt de code ook zelf in het bewerkingsvenster invoeren.

(**Opmerking: Alle woorden en symbolen moeten in het Engels worden geschreven.**)

![](./media/Python_5b0d8e26.png)

```python
from microbit import *
compass.calibrate()
x = 0
while True:
    x = compass.heading()
    if x >= 293 and x < 338:
        display.show(Image("00999:""00099:""00909:""09000:""90000"))
    elif x >= 23 and x < 68:
        display.show(Image("99900:""99000:""90900:""00090:""00009"))
    elif x >= 68 and x < 113:
        display.show(Image("00900:""09000:""99999:""09000:""00900"))
    elif x >= 113 and x < 158:
        display.show(Image("00009:""00090:""90900:""99000:""99900"))
    elif x >= 158 and x < 203:
        display.show(Image("00900:""00900:""90909:""09990:""00900"))
    elif x >= 203 and x < 248:
        display.show(Image("90000:""09000:""00909:""00099:""00999"))
    elif x >= 248 and x < 293:
        display.show(Image("00900:""00090:""99999:""00090:""00900"))
    else:
        display.show(Image("00900:""09990:""90909:""00900:""00900"))

```

Klik op “Check” om fouten in de code te controleren. Het programma is fout als er onderstrepingen en cursors worden weergegeven. 

![](./media/Python_42389bcf.png)

Als de code correct is, verbind de micro:bit met uw computer en klik op “Flash” om de code naar het micro:bit-bord te downloaden.

![](./media/Python_bedc607a.png)

6\.  **Testresultaat**

Nadat de code met succes naar het bord is gedownload, **zet de voeding aan via de micro USB-kabel of externe voeding (zet de DIP-schakelaar op ON)** en druk op de resetknop op de micro:bit.

![Img](./media/Python_bb3e1312.png)

Na de kalibratie draait u het micro:bit-bord, waarna de LED-puntenmatrix de richtingssymbolen weergeeft. 

7\.  **Code-uitleg**

![Img](./media/Python_76f66bb0.png)

---