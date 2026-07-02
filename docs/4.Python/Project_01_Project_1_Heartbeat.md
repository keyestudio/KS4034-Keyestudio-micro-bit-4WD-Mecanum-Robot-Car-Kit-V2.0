### Project 1：Heart Beat

![](./media/Python_b855274f.png)

1\.  **Beschrijving**

Dit project is eenvoudig uit te voeren met alleen een micro:bit hoofdplaat en een micro USB-kabel. Dit experiment dient als een starter om de magische programmeerwereld van de micro:bit te betreden.

2\.  **Voorbereiding**

A. Sluit de micro:bit hoofdplaat via de USB-kabel aan op uw computer.

B. Open de offline versie van Mu.

3\.  **Testcode**

Open de Mu-software, tik op “Load”, selecteer het bestand ““microbit-Heartbeat\.py“” en klik op “open”:

![](./media/Python_1ec17d44.png)

![](./media/Python_4bda2b61.png)

Er is een andere manier om code te importeren. Open Mu en sleep het bestand „microbit-Heartbeat\.py“ erin.

![](./media/Python_c5b7322b.png)

U kunt ook zelf code invoeren in het bewerkingsvenster.

(**Opmerking: Alle Engelse woorden en symbolen moeten in het Engels worden geschreven.**)

![](./media/Python_80af4cb3.png)

```python
from microbit import *

while True:
    display.show(Image.HEART)
    sleep(500)
    display.show(Image.HEART_SMALL)
    sleep(500)
```
Hieronder staat een lijst van ingebouwde afbeeldingen:

• Image.HEART

• Image.HEART_SMALL

• Image.HAPPY

• Image.SMILE

• Image.SAD

• Image.CONFUSED

• Image.ANGRY

• Image.ASLEEP

• Image.SURPRISED

• Image.SILLY

• Image.FABULOUS

• Image.MEH

• Image.YES

• Image.NO

• Image.CLOCK12, Image.CLOCK11, Image.CLOCK10, Image.CLOCK9, Image.CLOCK8, Image.CLOCK7, Image.CLOCK6, Image.CLOCK5,

Image.CLOCK4, Image.CLOCK3, Image.CLOCK2, Image.CLOCK1

• Image.ARROW_N, Image.ARROW_NE, Image.ARROW_E, Image.ARROW_SE, Image.ARROW_S, Image.ARROW_SW, Image.ARROW_W, Image.ARROW_NW

• Image.TRIANGLE

• Image.TRIANGLE_LEFT

• Image.CHESSBOARD

• Image.DIAMOND

• Image.DIAMOND_SMALL

• Image.SQUARE

• Image.SQUARE_SMALL

• Image.RABBIT

• Image.COW

• Image.MUSIC_CROTCHET

• Image.MUSIC_QUAVER

• Image.MUSIC_QUAVERS

• Image.PITCHFORK

• Image.PACMAN

• Image.TARGET

• Image.TSHIRT

• Image.ROLLERSKATE

• Image.DUCK

• Image.HOUSE

• Image.TORTOISE

• Image.BUTTERFLY

• Image.STICKFIGURE

• Image.GHOST

• Image.SWORD

• Image.GIRAFFE

• Image.SKULL

• Image.UMBRELLA

• Image.SNAKE，Image.ALL_CLOCKS，Image.ALL_ARROWS

Verbind de micro:bit kaart met de computer via een USB-kabel en klik op “Flash” om de code naar de kaart te downloaden.

![](./media/Python_93e18731.png)


![](./media/Python_48e78948.png)


![](./media/Python_cc33f1a9.png)

De code kan, ook al is deze onjuist, succesvol naar de micro:bit kaart gedownload worden, maar zal niet op de micro:bit zelf werken.

Klik op “Flash” om de code naar de micro:bit te downloaden.

![](./media/Python_8982d0b0.png)

Klik op “REPL” en druk op de resetknop van de micro:bit; de foutmeldingen worden weergegeven in het REPL-venster, zoals hieronder te zien is:

![](./media/Python_0c2abf18.png)

Klik nogmaals op “REPL” om de REPL-modus uit te schakelen, waarna je nieuwe code kunt verversen.

Om te controleren of de code correct is, hoef je alleen maar op “Check” te tikken. De fouten worden in het venster weergegeven.

![](./media/Python_b994c0d3.png)

Wijzig de code volgens de aanwijzingen en klik op “Check”.

![](./media/Python_bc5cbed3.png)

 Raadpleeg de website voor meer tutorials: [https://codewith.mu/en/tutorials/](https://codewith.mu/en/tutorials/)

4\.  **Testresultaat**

Klik op “<span style="color: rgb(255, 76, 65);">**Flash**</span>” om de code naar de micro:bit kaart te laden.

![Img](./media/Python_ed83ac25.png)

Nadat de code succesvol naar de kaart is gedownload, **schakel stroom in via de micro USB-kabel of een externe voeding (zet de DIP-schakelaar op ON)** en druk op de resetknop op de kaart.

![Img](./media/Python_bb3e1312.png)

De LED-dots matrix toont afwisselend het patroon “❤” en vervolgens “![](./media/Python_04fdfc90.png)”.

5\.  **Code-uitleg**

|from microbit import*|Importeer het bibliotheekbestand van de micro:bit|
|-|-|
|while True:|Dit is een permanente lus die ervoor zorgt dat de micro:bit de code in deze lus voor altijd uitvoert.|
|display.show(Image.HEART)|micro:bit toont “❤”|
|sleep(500)|Vertraging van 500 ms|
|display.show(Image.HEART_SMALL)|De LED-dots matrix toont “![](./media/Python_04fdfc90.png)”|

---