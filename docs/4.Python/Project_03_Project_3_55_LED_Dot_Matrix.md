### Projekt 3：5*5 LED-Punktmatrix

![](./media/Python_b855274f.png)

1\.  **Beschreibung**

Punktmatrizen sind im Alltag sehr verbreitet und finden breite Anwendung in LED-Werbetafeln, Etagenanzeigen von Aufzügen, Haltestellenanzeigen usw.
Die LED-Punktmatrix des Micro:bit-Hauptboards besteht aus 25 Dioden. Zuvor ist es uns gelungen, eine einzelne LED über ihren Positionspunkt zu steuern. Auf derselben Theorie basierend können wir mehrere LEDs gleichzeitig einschalten, um Muster, Ziffern und Zeichen darzustellen.

Außerdem können wir auf „show icon“ klicken, um ein gewünschtes Muster auszuwählen. Schließlich können wir auch eigene Muster entwerfen.

2\.  **Vorbereitung**

A. Verbinden Sie das micro:bit-Hauptboard mithilfe des USB-Kabels mit Ihrem Computer

B. Öffnen Sie die Offline-Version von Mu.

3\.  **Testcode1**

Sie können die Datei „5×5 LED Dot Matrix-1\.py“ öffnen, um den Code zu importieren. Sie können den Code auch selbst im Bearbeitungsfenster eingeben.

(**Hinweis: Alle Wörter und Symbole müssen auf Englisch geschrieben werden.**)

![](./media/Python_00f15f0a.png)

```python
from microbit import *

val = Image("00900:""00900:""90909:""09990:""00900")

display.show(val)
```

Klicken Sie auf „Check“, um Fehler im Code zu überprüfen. Das Programm ist fehlerhaft, wenn Unterstreichungen und Cursor angezeigt werden. 

![](./media/Python_a1197f5e.png)

Wenn der Code korrekt ist, verbinden Sie den micro:bit mit dem Computer und klicken Sie auf „Flash“, um den Code auf das micro:bit-Board zu übertragen.

![](./media/Python_1fd78e31.png)

4\.  **Testergebnis1**

Nachdem der Code erfolgreich auf das Board heruntergeladen wurde, **schalten Sie die Stromversorgung über das Micro-USB-Kabel oder eine externe Stromquelle ein (DIP-Schalter auf ON stellen)** und drücken Sie die Reset-Taste auf dem Board.

![Img](./media/Python_bb3e1312.png)

Sie werden sehen, dass die 5×5-Punktmatrix einen nach unten zeigenden Pfeil anzeigt ![](./media/Python_26c7d8c0.png).

5\.  **Testcode2**

Sie können die Datei „5×5 LED Dot Matrix-2\.py“ öffnen, um den Code zu importieren. Sie können den Code auch selbst im Bearbeitungsfenster eingeben.

(**Hinweis: Alle Wörter und Symbole müssen auf Englisch geschrieben werden.**)

![](./media/Python_dc6eea45.png)

```python
from microbit import *
val = Image("00900:""00900:""90909:""09990:""00900")
display.show('1')
sleep(500)
display.show('2')
sleep(500)
display.show('3')
sleep(500)
display.show('4')
sleep(500)
display.show('5')
sleep(500)
display.show(val)
sleep(500)
display.scroll("hello!")
sleep(200)
display.show(Image.HEART)
sleep(500)
display.show(Image.ARROW_NE)
sleep(500)
display.show(Image.ARROW_SE)
sleep(500)
display.show(Image.ARROW_SW)
sleep(500)
display.show(Image.ARROW_NW)
sleep(500)
display.clear()
```

Klicken Sie auf „Check“, um Fehler im Code zu überprüfen. Das Programm ist fehlerhaft, wenn Unterstreichungen und Cursor angezeigt werden. 

![](./media/Python_14bb490a.png)

Wenn der Code korrekt ist, verbinden Sie den micro:bit mit dem Computer und klicken Sie auf „Flash“, um den Code auf das micro:bit-Board zu übertragen.

![](./media/Python_a05c33d2.png)

6\.  **Testergebnis2**

Nachdem der Code erfolgreich auf das Board heruntergeladen wurde, **schalten Sie die Stromversorgung über das Micro-USB-Kabel oder eine externe Stromquelle ein (DIP-Schalter auf ON stellen)** und drücken Sie die Reset-Taste auf dem Board.

![Img](./media/Python_bb3e1312.png)

Sie werden feststellen, dass die 5×5-Punktmatrix nacheinander die Zahlen 1, 2, 3, 4 und 5 anzeigt und anschließend abwechselnd einen nach unten zeigenden Pfeil ![](./media/Python_26c7d8c0.png), „Hello“, ein Herzmuster ![](./media/Python_9b18b2b8.png), einen nach Nordosten zeigenden Pfeil ![](./media/Python_364f2e35.png), dann nach Südosten
![](./media/Python_fb3ba009.png), dann nach Südwesten ![](./media/Python_7ec21961.png) und schließlich nach Nordwesten ![](./media/Python_ced0bb41.png) an.

7\.  **Code-Erklärung**

![Img](./media/Python_ef42956d.png)


6.  **Referenz**

display.scroll() ：

Die Anzeige scrollt, um die Werte anzuzeigen. Wenn es sich um einen Integer oder Float handelt, verwenden wir str(), um ihn in Zeichenketten umzuwandeln.

Weitere Details finden Sie unter: [https://microbit-micropython.readthedocs.io/en/latest/utime.html](https://microbit-micropython.readthedocs.io/en/latest/utime.html)