### Project 14: 4 WS2812 RGB LEDs

![](./media/Python_eecf79fe.png)

1\.  **Beschrijving**

De driver shield werkt met 4 stuks WS2812 RGB LEDs, is compatibel met de micro:bit-board en wordt aangestuurd via P7. In deze les laten we de RGB-LEDs verschillende kleuren weergeven via P7. In deze les worden 3 sets testcode geleverd om de 4 WS2812 RGB LEDs verschillende effecten te laten tonen.

![Img](./media/Python_0be70eda.png)

2\.  **Voorbereiding**

- Plaats het micro:bit-board in de sleuf van de keyestudio 4WD Mecanum Robot Car V2.0

- Plaats batterijen in de batterijhouder

- Zet de aan/uit-schakelaar in de ON-stand

- Verbind de micro:bit met uw computer via een USB-kabel

- Open de offline versie van Mu.

3\.  **Test Code1**

Start de Mu-software en open het bestand“4 WS2812 RGB LEDs-1\.py”om de code te importeren\ U kunt de code ook zelf in het bewerkingsvenster invoeren.

(**Opmerking: Alle Engelse woorden en symbolen moeten in het Engels worden geschreven.**)

Klik op“Check”om fouten in de code te controleren. Het programma is fout als er onderstrepingen en cursors worden weergegeven. 

![](./media/Python_5b5266e2.png)

```python
from microbit import *
import neopixel
np = neopixel.NeoPixel(pin7, 4)
while True:
    for pixel_id1 in range(0, len(np)):
        np[pixel_id1] = (255, 0, 0)
        np.show()
    sleep(1000)
    for pixel_id2 in range(0, len(np)):
        np[pixel_id2] = (255, 165, 0)
        np.show()
    sleep(1000)
    for pixel_id3 in range(0, len(np)):
        np[pixel_id3] = (255, 255, 0)
        np.show()
    sleep(1000)
    for pixel_id4 in range(0, len(np)):
        np[pixel_id4] = (0, 255, 0)
        np.show()
    sleep(1000)
    for pixel_id5 in range(0, len(np)):
        np[pixel_id5] = (0, 0, 255)
        np.show()
    sleep(1000)
    for pixel_id6 in range(0, len(np)):
        np[pixel_id6] = (75, 0, 130)
        np.show()
    sleep(1000)
    for pixel_id7 in range(0, len(np)):
        np[pixel_id7] = (238, 130, 238)
        np.show()
    sleep(1000)
    for pixel_id8 in range(0, len(np)):
        np[pixel_id8] = (160, 32, 240)
        np.show()
    sleep(1000)
    for pixel_id9 in range(0, len(np)):
        np[pixel_id9] = (255, 255, 255)
    sleep(1000)
```

Als de code correct is, verbind dan de micro:bit met uw computer en klik op“Flash”om de code naar de micro:bit-board te downloaden.

![](./media/Python_56a9ab63.png)

4\.  **Testresultaat1**

Nadat de code succesvol naar het board is gedownload, **externe voeding (zet de DIP-schakelaar op ON)**, en druk op de resetknop van de micro:bit.

![Img](./media/Python_bb3e1312.png)

De 4 WS2812RGB LEDs lichten om de beurt cyclisch in verschillende kleuren op.

5\.  **Test Code2**

Start de Mu-software en open het bestand“4 WS2812 RGB LEDs-2\.py”om de code te importeren. U kunt de code ook zelf in het bewerkingsvenster invoeren.

(**Opmerking: Alle Engelse woorden en symbolen moeten in het Engels worden geschreven**.)

Klik op“Check”om fouten in de code te controleren. Het programma is fout als er onderstrepingen en cursors worden weergegeven. 

Als de code correct is, verbind dan de micro:bit met uw computer en klik op“Flash”om de code naar de micro:bit-board te downloaden.

![](./media/Python_8cb1dd7c.png)

```python
from microbit import *
import neopixel
np = neopixel.NeoPixel(pin7, 4)
while True:
    for index in range(0, 4):
        np.clear()
        np[index] = (255, 0, 0)
        np.show()
        sleep(100)
    for index1 in range(0, 4):
        np.clear()
        np[index1] = (255, 165, 0)
        np.show()
        sleep(100)
    for index2 in range(0, 4):
        np.clear()
        np[index2] = (255, 255, 0)
        np.show()
        sleep(100)
    for index3 in range(0, 4):
        np.clear()
        np[index3] = (0, 255, 0)
        np.show()
        sleep(100)
    for index4 in range(0, 4):
        np.clear()
        np[index4] = (0, 0, 255)
        np.show()
        sleep(100)
    for index5 in range(0, 4):
        np.clear()
        np[index5] = (75, 0, 130)
        np.show()
        sleep(100)
    for index6 in range(0, 4):
        np.clear()
        np[index6] = (238, 130, 238)
        np.show()
        sleep(100)
    for index7 in range(0, 4):
        np.clear()
        np[index7] = (160, 32, 240)
        np.show()
        sleep(100)
    for index8 in range(0, 4):
        np.clear()
        np[index8] = (255, 255, 255)
        np.show()
        sleep(100)
```

6\.  **Testresultaat2**

Nadat de code succesvol naar het board is gedownload, **externe voeding (zet de DIP-schakelaar op ON)**, en druk op de resetknop van de micro:bit.

![Img](./media/Python_bb3e1312.png)

De WS2812RGB LEDs tonen een lopend-licht (flow light) effect.

7\.  **Test Code3**

Start de Mu-software en open het bestand“4 WS2812 RGB LEDs-3\.py”om de code te importeren. U kunt de code ook zelf in het bewerkingsvenster invoeren.

(**Opmerking: Alle Engelse woorden en symbolen moeten in het Engels worden geschreven.**)

Klik op“Check”om fouten in de code te controleren. Het programma is fout als er onderstrepingen en cursors worden weergegeven. 

Als de code correct is, verbind dan de micro:bit met uw computer en klik op“Flash”om de code naar de micro:bit-board te downloaden.

![](./media/Python_b248f1c5.png)

```python
from microbit import *
import neopixel
np = neopixel.NeoPixel(pin7, 4)
from random import randint
R = 0
G = 0
B = 0
while True:
   for index in range(0, 4):
        R = randint(10, 255)
        G = randint(10, 255)
        B = randint(10, 255)
        np.clear()
        np[index] = (R, G, B)
        np.show()
        sleep(500)
```

8\.  **Testresultaat3**

Nadat de code succesvol naar het board is gedownload, **externe voeding (zet de DIP-schakelaar op ON)**, en druk op de resetknop van de micro:bit.

![Img](./media/Python_bb3e1312.png)

Elke WS2812RGB LED toont om de beurt een willekeurige kleur.

5\.  **Code Uitleg**

![Img](./media/Python_d1e3977b.png)

---