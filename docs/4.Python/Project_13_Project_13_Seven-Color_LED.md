### Project 13: Zevenkleurige LED

![](./media/Python_804e502b.png)

1\.  **Beschrijving**

Deze module bestaat uit een veelgebruikte LED met 7 kleuren maar met een witte uitstraling. Het kan automatisch verschillende kleuren knipperen om fantastische lichteffecten te creëren wanneer een hoog niveau wordt ingevoerd, zoals bij een normale LED.

2\.  **Voorbereiding**

- Plaats de micro:bit-board in de sleuf van de keyestudio 4WD Mecanum Robot Car V2.0

- Plaats batterijen in de batterijhouder

- Draai de aan/uit-schakelaar naar de ON-stand

- Sluit de micro:bit aan op uw computer via een USB-kabel

- Open de offline versie van Mu.

3\.  **Testcode**

Open de Mu-software en open het bestand“Colorful lights\.py”om de code te importeren. U kunt de code ook zelf in het bewerkingsvenster invoeren.

(**Opmerking: Alle woorden en symbolen moeten in het Engels worden geschreven**.)

![](./media/Python_010a8a12.png)

```python
from microbit import *
from keyes_mecanum_Car_V2 import *

mecanumCar = Mecanum_Car_Driver_V2()

while True:
    mecanumCar.left_led(1)
    mecanumCar.right_led(1)
    sleep(3000)
    mecanumCar.left_led(0)
    mecanumCar.right_led(0)
    sleep(3000)
```

**Belangrijke mededeling:** Als het bibliotheekbestand 'keyes_mecanum_Car_V2.py' nog niet op het micro:bit-board is geïmporteerd, is het essentieel om eerst het bibliotheekbestand op het micro:bit-board te importeren. De methode om de bibliotheek te importeren vindt u door op de volgende link te klikken: [How to Import Library to Micro:bit](https://docs.keyestudio.com/projects/KS4034/en/latest/docs/Python/Python.html#how-mu-import-library-to-micro-bit) en de gegeven instructies te volgen; anders zal de code niet worden uitgevoerd.

Nadat het bibliotheekbestand succesvol is geïmporteerd, moet u ook op de knop "Check" klikken om de code te controleren. Als er een cursor of een onderstreping op een bepaalde regel verschijnt, zijn er fouten in het programma.

![](./media/Python_ce67f468.png)

Tijdens dit proces kan echter de volgende melding verschijnen, zelfs als er geen fout in de code is. Deze meldingen zijn slechts waarschuwingen en geen foutmeldingen van de code.

![](./media/Python_863bb61b.png)

![](./media/Python_ccfbfa56.png)

Als de code correct is, sluit u de micro:bit aan op uw computer en klikt u op“Flash”om de code naar het micro:bit-board te downloaden.

![](./media/Python_39512a13.png)

Als er fouten verschijnen nadat u op de knop "Flash" hebt geklikt, controleer dan of u het meegeleverde bibliotheekbestand "keyes_mecanum_Car_V2.py" hebt geïmporteerd.

**Opmerking:** Voordat u met Micropython programmeert, moet u het bibliotheekbestand "keyes_mecanum_Car_V2.py" op de micro:bit importeren. Als u met een andere micro:bit programmeert, moet het bibliotheekbestand "keyes_mecanum_Car_V2.py" opnieuw op de nieuwe micro:bit worden geïmporteerd.

4\. **Testresultaat**

Nadat de code succesvol naar het board is gedownload, **externe voeding (zet de DIP-schakelaar op ON)**, en druk op de resetknop op de micro:bit.

![Img](./media/Python_bb3e1312.png)

De zevenkleurige LED knippert 3s en stopt dan 3s en herhaalt dit patroon.

5\. **Codeuitleg**

![Img](./media/Python_a4a670c0.png)