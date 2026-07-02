### Projekt 17：Linienverfolgungs-Sensor

#### Projekt 17.1：Erkennung des Linienverfolgungssensors

![](./media/Python_ea7f6c8c.png)

1\. **Beschreibung**

Das Motortreiber-Board des Keyestudio 4WD Mecanum Robot Car verfügt über einen 3-Kanal-Linienverfolgungssensor, der TCRT5000-IR-Bauelemente und 3 Potentiometer verwendet.

Das TCRT5000-IR-Bauelement enthält eine IR-Sendediode und eine IR-Empfängerdiode. Wenn die von der Sendediode ausgesandten Infrarot-Signale über Reflexion von der empfangenden Diode detektiert werden, ändert sich der Widerstand der Empfangsdiode, was sich üblicherweise in einer Spannungsänderung im Schaltkreis widerspiegelt.

Der Widerstand variiert abhängig von der Intensität der von der Empfangsdiode empfangenen Infrarot-Signale, was häufig von der Farbe der reflektierenden Fläche und dem Abstand zwischen reflektierender Fläche und Empfangsdiode abhängt. Bei der Erkennung gilt: Schwarz ist auf High-Pegel aktiv, Weiß ist auf Low-Pegel aktiv.

2\.  **Funktionsprinzip**

Fährt das Fahrzeug über eine weiße Fahrbahn, sendet die unter dem Fahrzeug angebrachte IR-Sendediode Infrarot-Signale aus, die von der Empfangsdiode reflektiert und zurückgegeben werden. Dann gibt der Ausgang Low-Pegel (0) aus; beim Erkennen schwarzer Linien wird High-Pegel (1) ausgegeben.

Der integrierte 3-Kanal-Tracking-Sensor-Anschluss auf dem 4WD Mecanum Robot Car ist mit den Anschlüssen G, 5V, P10, P4 und P3 auf dem micro:bit-Erweiterungsboard verbunden und wird vom micro:bit über P10, P4 und P3 gesteuert. Das linke TCRT5000-Infrarotpaar auf dem Sensor wird von P3 gesteuert, das mittlere von P4 und das rechte von P10.

Nachdem Sie ein weißes Blatt Papier unter das 4WD Mecanum Robot Car gelegt haben, drehen Sie die Potentiometer des 3-Kanal-Tracking-Sensors. Leuchtet die Kontroll-LED auf dem Sensormodul, heben Sie das Fahrzeug an, sodass die beiden Räder des 4WD Mecanum Robot Car vom Untergrund abheben. Der Abstand zwischen Papier und Sensor sollte etwa 1,5 cm betragen. Erlischt die Kontroll-LED des Sensormoduls, ist die Empfindlichkeit passend eingestellt.

**Beachten Sie, dass die 5x5-Punktmatrix die Pins P3, P4, P6, P7, P10 verwendet — die Punktmatrixfunktion muss daher deaktiviert werden, wenn der Linienverfolgungssensor verwendet wird.**

3\.  **Vorbereitung**

- Stecken Sie das micro:bit-Board in den Steckplatz des keyestudio 4WD Mecanum Robot Car V2.0
- Legen Sie Batterien in den Batteriehalter ein
- Schalten Sie den Powerschalter auf ON
- Verbinden Sie das micro:bit per USB-Kabel mit dem Computer
- Öffnen Sie die Offline-Version von Mu.

4\.  **Testcode**

Öffnen Sie die Mu-Software und laden Sie die Datei “Line tracking detection\.py”, um den Code zu importieren. Sie können den Code auch selbst in das Bearbeitungsfenster eingeben.

(**Hinweis: Alle englischen Wörter und Symbole müssen auf Englisch geschrieben sein**.)

Klicken Sie auf “Check”, um den Code auf Fehler zu prüfen. Sind Unterstreichungen oder Cursor sichtbar, ist das Programm fehlerhaft.

Ist der Code korrekt, verbinden Sie das micro:bit mit Ihrem Computer und klicken auf “Flash”, um den Code auf das micro:bit-Board zu übertragen.

![](./media/Python_2c7b1c21.png)

```python
from microbit import *
display.off()

val_L = 0
val_C = 0
val_R = 0
while True:
    val_L = pin3.read_digital()
    val_C = pin4.read_digital()
    val_R = pin10.read_digital()
    print("digital signal:", end = ' ')
    print(val_L, end = ' ')
    print(val_C, end = ' ')
    print(val_R)
    sleep(200)
```

5\.  **Testergebnis**

Nachdem der Code erfolgreich auf das Board geladen wurde und das USB-Kabel nicht getrennt wurde: Klicken Sie auf “REPL” und drücken Sie dann die Reset-Taste.

![Img](./media/Python_bb3e1312.png)

Die vom linken TCRT5000-IR-Sensor erfassten Werte werden im Monitor angezeigt.

Wenn der linke TCRT5000-IR-Sensor ein weißes Objekt erkennt, wird 0 angezeigt und die linke Kontroll-LED leuchtet; wenn nur ein schwarzes Objekt erkannt wird, wird 1 angezeigt und die LED ist aus, wie unten gezeigt:

![](./media/Python_6a25b450.png)

6\.  **Code-Erklärung**

![Img](./media/Python_5dad345e.png)


#### Projekt 17.2：Linienverfolgungs-Smartcar

![](./media/Python_f0b62e0f.jpg)

1\. Beschreibung

In dieser Lektion kombinieren wir einen Linienverfolgungssensor mit einem Motor, um ein Linienverfolgungs-Smartcar zu bauen.

Das micro:bit-Board wertet die Signale aus und steuert das Smartcar, sodass die Linienverfolgungsfunktion ausgeführt wird.

2\.  **Funktionsprinzip**

Das Smartcar führt je nach den Werten des 3-Kanal-Linienverfolgungssensors unterschiedliche Bewegungen aus.

![Img](./media/Python_e672c637.png)

3\.  **Vorbereitung**

- Stecken Sie das micro:bit-Board in den Steckplatz des keyestudio 4WD Mecanum Robot Car V2.0
- Legen Sie Batterien in den Batteriehalter ein
- Schalten Sie den Powerschalter auf ON
- Verbinden Sie das micro:bit per USB-Kabel mit dem Computer
- Öffnen Sie die Offline-Version von Mu.

**Warnung:** Der 3-Kanal-Tracking-Sensor sollte in einer Umgebung ohne IR-Störungen wie direkte Sonneneinstrahlung verwendet werden. Sonnenlicht enthält viel unsichtbares Licht, z. B. Infrarot und Ultraviolett. In einer Umgebung mit starker Sonneneinstrahlung kann der 3-Kanal-Tracking-Sensor nicht richtig arbeiten.

4\.  **Ablaufdiagramm**

![Img](./media/Python_47856ed2.png)

5\.  **Testcode**

Öffnen Sie die Mu-Software und laden Sie die Datei “Line tracking car\.py”, um den Code zu importieren. Sie können den Code auch selbst in das Bearbeitungsfenster eingeben.

(**Hinweis: Alle englischen Wörter und Symbole müssen auf Englisch geschrieben sein**.)

Klicken Sie auf “Files”, um die Bibliotheksdatei “keyes_mecanum_Car.py” auf das micro:bit zu importieren.

Klicken Sie auf “Check”, um den Code auf Fehler zu prüfen. Sind Unterstreichungen oder Cursor sichtbar, ist das Programm fehlerhaft.

Ist der Code korrekt, verbinden Sie das micro:bit mit Ihrem Computer und klicken auf “Flash”, um den Code auf das micro:bit-Board zu übertragen.

![](./media/Python_bd395cbe.png)

```python
from microbit import *
from keyes_mecanum_Car_V2 import *
mecanumCar = Mecanum_Car_Driver_V2()
display.off()

val_L = 0
val_C = 0
val_R = 0
while True:
    val_L = pin3.read_digital()
    val_C = pin4.read_digital()
    val_R = pin10.read_digital()
    if val_C == 0:
        if val_L == 0 and val_R == 1:
            mecanumCar.Motor_Upper_L(1, 80)
            mecanumCar.Motor_Lower_L(1, 80)
            mecanumCar.Motor_Upper_R(0, 80)
            mecanumCar.Motor_Lower_R(0, 80)
        elif val_L == 1 and val_R == 0:
            mecanumCar.Motor_Upper_L(0, 80)
            mecanumCar.Motor_Lower_L(0, 80)
            mecanumCar.Motor_Upper_R(1, 80)
            mecanumCar.Motor_Lower_R(1, 80)
        else:
            mecanumCar.Motor_Upper_L(0, 0)
            mecanumCar.Motor_Lower_L(0, 0)
            mecanumCar.Motor_Upper_R(0, 0)
            mecanumCar.Motor_Lower_R(0, 0)
    else :
        if val_L == 0 and val_R == 1:
            mecanumCar.Motor_Upper_L(1, 80)
            mecanumCar.Motor_Lower_L(1, 80)
            mecanumCar.Motor_Upper_R(0, 80)
            mecanumCar.Motor_Lower_R(0, 80)
        elif val_L == 1 and val_R == 0:
            mecanumCar.Motor_Upper_L(0, 80)
            mecanumCar.Motor_Lower_L(0, 80)
            mecanumCar.Motor_Upper_R(1, 80)
            mecanumCar.Motor_Lower_R(1, 80)
        else:
            mecanumCar.Motor_Upper_L(1, 80)
            mecanumCar.Motor_Lower_L(1, 80)
            mecanumCar.Motor_Upper_R(1, 80)
            mecanumCar.Motor_Lower_R(1, 80)
```

6\.  **Testergebnis**

Nachdem der Code erfolgreich auf das Board geladen wurde: Externe Stromversorgung sicherstellen (DIP-Schalter auf ON stellen) und die Reset-Taste auf dem micro:bit drücken.

![Img](./media/Python_bb3e1312.png)

Das Linienverfolgungsfahrzeug fährt entlang der schwarzen Linie vorwärts.

**Hinweis:** (1) Die Breite der schwarzen Linie sollte beim Tracking gleich oder größer als die Breite des Linienverfolgungssensors sein.

(2) Vermeiden Sie Tests des Smartcars bei starker Beleuchtung.

7\.  **Code-Erklärung**

![Img](./media/Python_b16f9d7b.png)

![Img](./media/Python_35f35a4c.png)

---