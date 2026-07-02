### Project 1：Heart Beat

![](./media/Python_b855274f.png)

1\.  **Beschreibung**

Dieses Projekt lässt sich ausschließlich mit einem micro:bit Hauptboard und einem micro USB-Kabel leicht durchführen. Dieses Experiment dient als Einstieg, um in die faszinierende Programmierwelt des micro:bit einzutreten.

2\.  **Vorbereitung**

A. Schließen Sie das micro:bit Hauptboard über das USB-Kabel an Ihren Computer an.

B. Öffnen Sie die Offline-Version von Mu.

3\.  **Testcode**

Öffnen Sie die Mu-Software, tippen Sie „Load“, wählen Sie die Datei „“microbit-Heartbeat\.py“ und klicken Sie auf „open“:

![](./media/Python_1ec17d44.png)

![](./media/Python_4bda2b61.png)

Es gibt eine andere Möglichkeit, Code zu importieren. Öffnen Sie die Mu-Software und ziehen Sie die Datei „microbit-Heartbeat\.py“ hinein.

![](./media/Python_c5b7322b.png)

Sie können den Code auch direkt im Bearbeitungsfenster eingeben.

(**Hinweis: Alle englischen Wörter und Symbole müssen auf Englisch geschrieben sein.**)

![](./media/Python_80af4cb3.png)

```python
from microbit import *

while True:
    display.show(Image.HEART)
    sleep(500)
    display.show(Image.HEART_SMALL)
    sleep(500)
```
Nachfolgend eine Liste der eingebauten Bilder:

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

Verbinden Sie das micro:bit Board mit dem Computer über ein USB-Kabel und klicken Sie auf „Flash“, um den Code auf das Board herunterzuladen.

![](./media/Python_93e18731.png)


![](./media/Python_48e78948.png)


![](./media/Python_cc33f1a9.png)

Der Code kann, selbst wenn er fehlerhaft ist, erfolgreich auf das micro:bit Board heruntergeladen werden, jedoch nicht auf dem micro:bit ausgeführt werden.

Klicken Sie auf „Flash“, um den Code auf das micro:bit zu laden.

![](./media/Python_8982d0b0.png)

Klicken Sie auf „REPL“ und drücken Sie die Reset-Taste auf dem micro:bit; die Fehlermeldungen werden im REPL-Fenster angezeigt, wie unten dargestellt:

![](./media/Python_0c2abf18.png)

Klicken Sie erneut auf „REPL“, um den REPL-Modus zu beenden, dann können Sie neuen Code aktualisieren.

Um sicherzustellen, dass der Code korrekt ist, tippen Sie einfach auf „Check“. Die Fehler werden im Fenster angezeigt.

![](./media/Python_b994c0d3.png)

Ändern Sie den Code entsprechend den Hinweisen und klicken Sie auf „Check“.

![](./media/Python_bc5cbed3.png)

 Bitte besuchen Sie die Website für weitere Tutorials: [https://codewith.mu/en/tutorials/](https://codewith.mu/en/tutorials/)

4\.  **Testergebnis**

Klicken Sie auf “<span style="color: rgb(255, 76, 65);">**Flash**</span>”, um den Code auf das micro:bit Board zu laden.

![Img](./media/Python_ed83ac25.png)

Nachdem der Code erfolgreich auf das Board heruntergeladen wurde, **schalten Sie die Stromversorgung über das micro USB-Kabel oder eine externe Stromquelle ein (DIP-Schalter auf ON stellen)** und drücken Sie die Reset-Taste auf dem Board.

![Img](./media/Python_bb3e1312.png)

Die LED-Punktmatrix zeigt abwechselnd das Muster „❤“ und dann „![](./media/Python_04fdfc90.png)“.

5\.  **Code-Erklärung**

|from microbit import*|Importieren der Bibliothek des micro:bit|
|-|-|
|while True:|Dies ist eine Endlosschleife, die den micro:bit dazu bringt, den Code in dieser Schleife dauerhaft auszuführen.|
|display.show(Image.HEART)|micro:bit zeigt „❤“ an|
|sleep(500)|Verzögerung von 500 ms|
|display.show(Image.HEART_SMALL)|Die LED-Punktmatrix zeigt „![](./media/Python_04fdfc90.png)“ an|

---