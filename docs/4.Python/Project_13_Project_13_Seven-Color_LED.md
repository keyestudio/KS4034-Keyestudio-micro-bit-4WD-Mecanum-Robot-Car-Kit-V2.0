### Project 13: Siebenfarbige LED

![](./media/Python_804e502b.png)

1\.  **Beschreibung**

Dieses Modul besteht aus einer häufig verwendeten LED mit 7 Farben, jedoch mit weißem Erscheinungsbild. Es kann automatisch verschiedene Farben blinken, um fantastische Lichteffekte zu erzeugen, wenn ein High-Pegel wie bei einer normalen LED anliegt.

2\.  **Vorbereitung**

- Setzen Sie das micro:bit-Board in den Steckplatz des keyestudio 4WD Mecanum Robot Car V2.0 ein

- Legen Sie die Batterien in den Batteriehalter ein

- Schalten Sie den Netzschalter auf die ON-Stellung

- Verbinden Sie das micro:bit mit Ihrem Computer über ein USB-Kabel

- Öffnen Sie die Offline-Version von Mu.

3\.  **Testcode**

Starten Sie die Mu-Software und öffnen Sie die Datei“Colorful lights\.py”, um den Code zu importieren. Sie können den Code auch selbst im Bearbeitungsfenster eingeben.

(**Hinweis: Alle Wörter und Symbole müssen in Englisch geschrieben sein**.)

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

**Wichtiger Hinweis:** Falls die Bibliotheksdatei 'keyes_mecanum_Car_V2.py' noch nicht auf das micro:bit-Board importiert wurde, ist es unbedingt erforderlich, zuerst die Bibliotheksdatei auf das micro:bit-Board zu importieren. Die Methode zum Importieren der Bibliothek finden Sie über den Link: [How to Import Library to Micro:bit](https://docs.keyestudio.com/projects/KS4034/en/latest/docs/Python/Python.html#how-mu-import-library-to-micro-bit) und befolgen Sie die dortigen Anweisungen; andernfalls wird der Code nicht ausgeführt.

Nachdem die Bibliotheksdatei erfolgreich importiert wurde, müssen Sie außerdem auf die Schaltfläche "Check" klicken, um den Code zu prüfen. Wenn ein Cursor oder eine Unterstreichung auf einer bestimmten Zeile erscheint, sind im Programm Fehler vorhanden.

![](./media/Python_ce67f468.png)

Während dieses Vorgangs erscheint jedoch die folgende Meldung, selbst wenn kein Fehler im Code vorhanden ist. Diese Meldungen sind nur Warnungen und keine Fehlermeldungen des Codes.

![](./media/Python_863bb61b.png)

![](./media/Python_ccfbfa56.png)

Wenn der Code korrekt ist, verbinden Sie das micro:bit mit Ihrem Computer und klicken Sie auf“Flash”, um den Code auf das micro:bit-Board herunterzuladen.

![](./media/Python_39512a13.png)

Falls nach dem Klicken auf die Schaltfläche "Flash" Fehler auftreten, bestätigen Sie bitte, ob Sie die bereitgestellte Bibliotheksdatei "keyes_mecanum_Car_V2.py" importiert haben.

**Hinweis:** Bevor Sie mit Micropython programmieren, müssen Sie die Bibliotheksdatei "keyes_mecanum_Car_V2.py" auf das micro:bit importieren. Wenn Sie mit einem anderen micro:bit programmieren, muss die Bibliotheksdatei "keyes_mecanum_Car_V2.py" erneut auf das neue micro:bit importiert werden.

4\. **Testergebnis**

Nachdem der Code erfolgreich auf das Board heruntergeladen wurde, **externes Netzteil (DIP-Schalter auf ON stellen)** und drücken Sie die Reset-Taste am micro:bit.

![Img](./media/Python_bb3e1312.png)

Die siebenfarbige LED blinkt 3s lang, stoppt dann für 3s und wiederholt dieses Muster.

5\. **Codeerklärung**

![Img](./media/Python_a4a670c0.png)