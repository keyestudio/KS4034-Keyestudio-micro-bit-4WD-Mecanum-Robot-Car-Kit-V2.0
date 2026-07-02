## Project 18：Ultraschallsensor

### Project 18.1：Ultraschall-Entfernungsmessung

1\.  **Beschreibung**

Der Ultraschallsensor verwendet Sonar, um wie Fledermäuse die Entfernung zu einem Objekt zu bestimmen. Er bietet eine hervorragende berührungslose Abstandserkennung mit hoher Genauigkeit und stabilen Messwerten in einem leicht zu handhabenden Modul. Das Modul enthält sowohl den Ultraschall-Sender als auch den Empfänger.

Der Ultraschallsensor wird in einer Vielzahl von Elektronikprojekten zur Hinderniserkennung, Entfernungsbestimmung und für weitere Anwendungen eingesetzt.

![](./media/Makecode_0180b169.png)

Das Ultraschallmodul sendet Ultraschallwellen nach einem Trigger-Signal aus. Trifft das Ultraschallsignal auf ein Objekt und wird reflektiert, so gibt das Modul ein Echo-Signal aus. Aus der Zeitdifferenz zwischen Trigger-Signal (TRIG) und Echo-Signal (ECHO) kann die Entfernung zum Objekt berechnet werden.

Wie im Bild zu sehen ist, ähnelt es zwei Augen. Eines ist der Sender, das andere der Empfänger.

Laut dem obigen Anschlussdiagramm ist der integrierte Anschluss des Ultraschallmoduls mit dem 5V G P15 P16-Anschluss auf der micro:bit Motorsteuerungsplatine verbunden. Der Trig (T)-Pin wird von P15 des micro:bit gesteuert und der Echo (E)-Pin an P16 angeschlossen.

![](./media/Makecode_1174e0ec.png)

2\. **Funktionsprinzip**

![](./media/Makecode_8ff02741.png)

(1) TRIG auf LOW ziehen, dann einen HIGH-Impuls mit mindestens 10µs auslösen;

(2) Nach dem Trigger sendet das Modul automatisch acht 40 kHz Ultraschallimpulse und prüft, ob ein Echo zurückkehrt;

(3) Wenn ein Echo zurückkommt, gibt ECHO (E) ein HIGH aus. Die Dauer dieses HIGH ist die Zeit vom Senden bis zum Empfang der Ultraschallwellen. Dann Testdistanz = HIGH-Dauer \*340m/s\*0.5. 

3\. **Parameter**

- Betriebsspannung: 3-5.5V (DC)

- Betriebsstrom: 15mA

- Arbeitsfrequenz: 40 kHz

- Maximale Erkennungsdistanz: etwa 3 m

- Minimale Erkennungsdistanz: 2-3 cm

- Genauigkeit: bis zu 0,2 cm

- Erfassungswinkel: weniger als 15 Grad

- Eingangstriggerimpuls: 10µs TTL-Pegel

- Ausgangs-Echo-Signal: TTL-Pegelausgang (HIGH), proportional zur Entfernung

4\. **Vorbereitung**

- Setzen Sie das micro:bit Board in den Steckplatz des keyestudio 4WD Mecanum Robot Car V2.0 ein

- Legen Sie die Batterien in den Batteriefach ein

- Schalten Sie den POWER-Schalter auf ON

- Verbinden Sie das micro:bit über ein USB-Kabel mit Ihrem Computer

- Öffnen Sie die Web-Version von Makecode


5\. **Test-Code**

![](./media/Makecode_497760b1.png)

Klicken Sie auf “JavaScript”, um den entsprechenden JavaScript-Code anzuzeigen:

![](./media/Makecode_387f3243.png)

6\.  **Testergebnis**

Laden Sie den Code auf das micro:bit, lassen Sie das USB-Kabel angeschlossen und schalten Sie den POWER-Schalter ein. Der Entfernungswert wird auf dem Monitor angezeigt.

![](./media/Makecode_2cd74c16.png)

Der Monitor zeigt die Entfernung zwischen dem Hindernis und dem Ultraschallsensor (siehe unten).

![](./media/Makecode_422adea3.png)

Öffnen Sie CoolTerm, klicken Sie auf Options, um SerialPort auszuwählen. Stellen Sie den COM-Port und die Baudrate auf 115200 ein (die Baudrate der USB-Seriellkommunikation des micro:bit beträgt im Test 115200). Klicken Sie auf “OK” und “Connect”.

Der CoolTerm-Seriellmonitor zeigt den Entfernungswert wie folgt an:

![](./media/Makecode_69b06998.png)

### Project 18.2：Ultraschall-Ausweichverhalten

![Img](./media/Makecode_13139b46.png)

1\. **Beschreibung**

In diesem Projekt integrieren wir einen Ultraschallsensor und ein Fahrzeug, um ein Ultraschall-Ausweichfahrzeug zu bauen.

Das Prinzip besteht darin, die Entfernung zwischen Fahrzeug und Hindernis über den Ultraschallsensor zu erfassen und dadurch die Bewegung des Fahrzeugs zu steuern.

2\.  **Vorbereitung**

- Setzen Sie das micro:bit Board in den Steckplatz des keyestudio 4WD Mecanum Robot Car V2.0 ein

- Legen Sie die Batterien in den Batteriefach ein

- Schalten Sie den POWER-Schalter auf ON

- Verbinden Sie das micro:bit über ein USB-Kabel mit Ihrem Computer

- Öffnen Sie die Web-Version von Makecode

3\.  **Flussdiagramm**

![Img](./media/Makecode_e2adae4b.png)

4\.  **Test-Code**

![](./media/Makecode_05a4740b.png)

![Img](./media/Makecode_d7879887.png)

Klicken Sie auf “JavaScript”, um den entsprechenden JavaScript-Code anzuzeigen:

![](./media/Makecode_c8f86a24.png)

![](./media/Makecode_13baf1d6.png)

5\.  **Testergebnis**

Laden Sie den Code auf das micro:bit, schalten Sie das Gerät und den POWER-Schalter ein. Wenn der Hindernisabstand größer als 20 cm ist, fährt das Fahrzeug vorwärts; andernfalls dreht das Fahrzeug nach links.

### Project 18.3：Ultraschall-Folgefunktion

![Img](./media/Makecode_d17a7889.png)

1\. **Beschreibung**

Im vorherigen Kapitel haben wir das Grundprinzip des Linienverfolgungssensors kennengelernt. Nun kombinieren wir den Ultraschallsensor mit dem Fahrzeug, um ein Ultraschall-Folgefahrzeug zu bauen.

Der Ultraschallsensor ermittelt die Hindernisentfernung und steuert den Fahrzustand des Fahrzeugs.

2\. **Vorbereitung**

- Setzen Sie das micro:bit Board in den Steckplatz des keyestudio 4WD Mecanum Robot Car V2.0 ein

- Legen Sie die Batterien in den Batteriefach ein

- Schalten Sie den POWER-Schalter auf ON

- Verbinden Sie das micro:bit über ein USB-Kabel mit Ihrem Computer

- Öffnen Sie die Web-Version von Makecode

3\. **Flussdiagramm**

![Img](./media/Makecode_f5026aed.png)

4\. **Test-Code**

![](./media/Makecode_03b95531.png)

Klicken Sie auf “JavaScript”, um den entsprechenden JavaScript-Code anzuzeigen:

![](./media/Makecode_a93c8245.png)

5\. **Testergebnis**

Laden Sie den Code auf das micro:bit, schalten Sie den POWER-Schalter auf ON auf dem Shield, das Fahrzeug kann dem Hindernis folgen und sich bewegen.