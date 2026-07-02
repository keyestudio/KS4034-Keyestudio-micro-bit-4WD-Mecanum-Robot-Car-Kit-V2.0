## Project 17：Line Tracking Sensor

### Project 17.1：Detect Line Tracking Sensor

![](./media/Makecode_ea7f6c8c.png)

1\. **Beschreibung**

Die Motorsteuerplatine des Keyestudio 4WD Mecanum Robot Car ist mit einem 3-Kanal-Linienverfolgungssensor ausgestattet, der TCRT5000-IR-Module und 3 Potentiometer verwendet.

Das TCRT5000-IR-Modul enthält eine IR-Sende- und eine IR-Empfängerröhre. Wenn die von der Senderröhre ausgesendeten Infrarotsignale nach Reflexion von der Empfangsröhre empfangen werden, ändert sich der Widerstand der Empfangsröhre, was sich gewöhnlich in einer Spannungsänderung in der Schaltung widerspiegelt.  

Der Widerstand variiert in Abhängigkeit von der Intensität der von der Empfangsröhre empfangenen Infrarotsignale, was oft von der Farbe der reflektierenden Oberfläche und dem Abstand zwischen der reflektierenden Oberfläche und der Empfangsröhre abhängt. Bei der Erkennung gilt Schwarz als aktiver hoher Pegel (High) und Weiß als niedriger Pegel (Low).

2\.  **Funktionsprinzip**

Fährt das Fahrzeug über eine weiße Strecke, sendet die unter dem Fahrzeug angebrachte IR-Senderröhre Infrarotsignale zur Streckenerkennung und die Empfangsröhre empfängt die Signale zurück. Dann gibt der Ausgang einen niedrigen Pegel (0) aus; wenn schwarze Linien erkannt werden, gibt er einen hohen Pegel (1) aus.

Nachdem Sie ein weißes Blatt Papier unter das 4WD Mecanum Robot Car gelegt haben, drehen Sie die Potentiometer am 3-Wege-Tracking-Sensor. Leuchtet die Kontroll-LED am Sensormodul, heben Sie das Fahrzeug an, sodass sich die beiden Räder des 4WD Mecanum Robot Car frei drehen können. Der Abstand des weißen Papiers beträgt etwa 1,5 cm. Erlischt die Kontroll-LED am Sensormodul, ist die Empfindlichkeit eingestellt.

3\.  **Vorbereitung**

- Stecken Sie das micro:bit-Board in den Steckplatz des keyestudio 4WD Mecanum Robot Car V2.0

- Legen Sie Batterien in den Batteriehalter ein

- Schalten Sie den Netzschalter auf ON

- Verbinden Sie das micro:bit über ein USB-Kabel mit Ihrem Computer

- Öffnen Sie die Webversion von Makecode

4\.  **Testcode**

![](./media/Makecode_3683d83f.png)

Klicken Sie auf “JavaScript”, um den entsprechenden JavaScript-Code anzusehen: 

![](./media/Makecode_4b440616.png)

5\.  **Testergebnis**

Laden Sie den Code auf das micro:bit-Board und stellen Sie den POWER-Schalter auf ON.

Öffnen Sie CoolTerm, klicken Sie auf Options und wählen Sie SerialPort. Stellen Sie COM-Port und Baudrate auf 115200 ein. Klicken Sie auf “OK” und “Connect”.

![](./media/Makecode_ea164439.png)

![](./media/Makecode_b3a18bca.png)

![](./media/Makecode_f78128c1.png)

![](./media/Makecode_13238e98.png)

Der CoolTerm-Seriellmonitor zeigt die digitalen Signale an, die von den Linienverfolgungssensoren gelesen werden.

![](./media/Makecode_0141051a.png)

### Project 17.2：Tracking Smart Car

![Img](./media/Makecode_547634e4.png)

1\. **Beschreibung**

In dieser Lektion kombinieren wir einen Linienverfolgungssensor mit einem Motor, um ein Linienverfolgungs-Smartcar zu erstellen.

Das micro:bit-Board wertet die Signale aus und steuert das Smartcar, um die Linienverfolgungsfunktion zu demonstrieren.

2\. **Funktionsprinzip**

Das Smartcar führt je nach den von dem 3-Kanal-Linienverfolgungssensor empfangenen Werten unterschiedliche Bewegungen aus.

![Img](./media/Makecode_bbccdb34.png)

3\. **Vorbereitung**

- Stecken Sie das micro:bit-Board in den Steckplatz des keyestudio 4WD Mecanum Robot Car V2.0

- Legen Sie Batterien in den Batteriehalter ein

- Schalten Sie den Netzschalter auf ON

- Verbinden Sie das micro:bit über ein USB-Kabel mit Ihrem Computer

- Öffnen Sie die Webversion von Makecode

**Warnung:** Der 3-Wege-Tracking-Sensor sollte in Umgebungen ohne Infrarotstörungen wie direkte Sonneneinstrahlung verwendet werden. Sonnenlicht enthält viel unsichtbares Licht, z. B. Infrarot und Ultraviolett. In Umgebungen mit starker Sonneneinstrahlung kann der 3-Wege-Tracking-Sensor nicht ordnungsgemäß arbeiten.

4\.**Flussdiagramm**

![Img](./media/Makecode_70f1fd80.png)


5\.  **Testcode**

![](./media/Makecode_4b104155.png)

![Img](./media/Makecode_d36220cf.png)

![Img](./media/Makecode_4fff0a27.png)

![Img](./media/Makecode_ca91a31f.png)


Klicken Sie auf “JavaScript”, um den entsprechenden JavaScript-Code anzuzeigen:

![](./media/Makecode_f5caa06a.png)

![](./media/Makecode_8f5f07ec.png)

5\. **Testergebnis**

Laden Sie den Code auf das micro:bit und stellen Sie den POWER-Schalter auf ON; das Linienverfolgungsfahrzeug fährt entlang der schwarzen Linie vorwärts.

**Hinweis:** Schalten Sie den Schalter an der Rückseite des micro:bit-Fahrzeugs ein. Die Breite der schwarzen Linie sollte größer sein als die Breite des Linienverfolgungssensors.

Vermeiden Sie Tests des Smartcars bei starkem Licht.