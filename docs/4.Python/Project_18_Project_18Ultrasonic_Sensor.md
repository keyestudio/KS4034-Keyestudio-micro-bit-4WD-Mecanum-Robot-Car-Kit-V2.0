### Project 18：Ultrasone Sensor

#### Project 18.1：Ultrasone Afstandsbepaling

1\. **Beschrijving**

![](./media/Python_9810ae67.jpg)

De ultrasone sensor gebruikt sonar om, zoals vleermuizen, de afstand tot een object te bepalen. Hij biedt uitstekende contactloze afstandsdetectie met hoge nauwkeurigheid en stabiele metingen in een gebruiksvriendelijk pakket. De module bevat zowel een ultrasone zender- als ontvangermodule.

De ultrasone sensor wordt in veel elektronica-projecten gebruikt voor het maken van obstakeldetectie- en afstandsmeettoepassingen, evenals verschillende andere toepassingen. 

![](./media/Python_0180b169.png)

De ultrasone module zal de ultrasone golven uitsturen nadat de trigger-signalen zijn gegeven. Wanneer de ultrasone golven het object tegenkomen en teruggekaatst worden, geeft de module een echo-signaal uit, zodat hij de afstand tot het object kan bepalen uit het tijdsverschil tussen het trigger-signaal (TRIG) en het echo-signaal (ECHO).

Zoals de afbeelding toont, is het alsof het twee ogen heeft. De ene is het zendende uiteinde, de andere het ontvangende uiteinde.

Volgens het bovenstaande bedrading schema is de geïntegreerde poort van de ultrasone sensormodule verbonden met de 5V G P15 P16-poort op de micro:bit motor driver basisplaat. De Trig (T) pin wordt aangestuurd door P15 van de micro:bit en de Echo (E) pin door P16.

![](./media/Python_19b45a23.jpg)

2\. **Werking**

![](./media/Python_8ff02741.png)

(1) Trek TRIG laag en geef daarna een trigger-hoogsignaal van minimaal 10µs;

(2) Na triggeren stuurt de module automatisch acht pulsen van 40kHz uit en detecteert of er een signaal terugkeert;

(3) Als er een signaal terugkeert: wanneer ECHO (E) een hoge toestand uitstuurt, is de duur van die hoge toestand de tijd van verzending tot ontvangst van de ultrasone golven. Dan testafstand = hoge duur * 340 m/s * 0,5.

3\.  **Parameters**

- Werkspanning: 3-5.5V (DC)

- Werkstroom: 15mA

- Werkfrequentie: 40kHz

- Maximale detectieafstand: ongeveer 3m

- Minimale detectieafstand: 2-3cm

- Nauwkeurigheid: tot 0,2cm

- Detectiehoek: minder dan 15 graden

- Ingang triggerpuls: 10µs TTL-niveau

- Uitgang echo-signaal: TTL-niveau signaal (hoog), proportioneel aan bereik

4\.  **Voorbereiding**

- Steek de micro:bit in de sleuf van de keyestudio 4WD Mecanum Robot Car V2.0

- Plaats batterijen in het batterijhouder

- Zet de stroomschakelaar op ON

- Verbind de micro:bit met de computer via een USB-kabel

- Open de offline versie van Mu.

5\.  **Testcode**

Open Mu-software en open het bestand “Ultrasonic Ranging\.py” om de code te importeren. Je kunt de code ook zelf in het bewerkingsvenster invoeren.

(**Opmerking: alle Engelse woorden en symbolen moeten in het Engels worden geschreven**.)

Klik op “Files” om het bibliotheekbestand “keyes_mecanum_Car_V2.py” naar de micro:bit te importeren.

Klik op “Check” om fouten in de code te controleren. Het programma is fout als er onderstrepingen en cursors worden getoond.

Als de code correct is, verbind de micro:bit met je computer en klik op “Flash” om de code naar de micro:bit te downloaden.

![](./media/Python_5a29bde9.png)

```python
from microbit import *
from keyes_mecanum_Car_V2 import *
mecanumCar = Mecanum_Car_Driver_V2()
import music
tune = ["C4:4"]
distance_val = 0

while True:
    i = 0
    distance_val = mecanumCar.get_distance()
    print("distance:", distance_val)
    if distance_val < 10:
        while i < 1:
            music.play(tune)
            sleep(200)
            music.play(tune)
            sleep(200)
            i += 1

```

6\.  **Testresultaat**

Nadat de code succesvol naar het bord is gedownload en je de USB-kabel niet loskoppelt, klik op “REPL” en druk daarna op de resetknop.

![Img](./media/Python_bb3e1312.png)

De afstandswaarde van het obstakel wordt weergegeven, zoals hieronder.

Wanneer de afstand minder is dan 10cm, zal de passieve zoemer van de smart geluid geven.

![](./media/Python_4dc8054e.png)

7\.  **Code Uitleg**

![Img](./media/Python_ebde06e9.png)

#### Project 18.2：Ultrasone Ontwijking

![](./media/Python_aee41f6f.jpg)

1\. **Beschrijving**

In dit project integreren we een ultrasone sensor met een auto om een ultrasone ontwijkingsauto te maken.

Het principe is om de afstand tussen de auto en een obstakel te detecteren via de ultrasone sensor om zo de beweging van de smart car te sturen.

2\. **Voorbereiding**

- Steek de micro:bit in de sleuf van de keyestudio 4WD Mecanum Robot Car V2.0

- Plaats batterijen in het batterijhouder

- Zet de stroomschakelaar op ON

- Verbind de micro:bit met de computer via een USB-kabel

- Open de offline versie van Mu.

3\.  **Stroomschema**

![Img](./media/Python_a4efee72.png)

4\.  **Testcode**

Open Mu-software en open het bestand “Ultrasonic Avoid Smart Car\.py” om de code te importeren. Je kunt de code ook zelf in het bewerkingsvenster invoeren.

(**Opmerking: alle Engelse woorden en symbolen moeten in het Engels worden geschreven**.)

Klik op “Files” om het bibliotheekbestand “keyes_mecanum_Car_V2.py” naar de micro:bit te importeren.

Klik op “Check” om fouten in de code te controleren. Het programma is fout als er onderstrepingen en cursors worden getoond.

Als de code correct is, verbind de micro:bit met je computer en klik op “Flash” om de code naar de micro:bit te downloaden.

![](./media/Python_38f3510c.png)

```python
from microbit import *
from keyes_mecanum_Car_V2 import *
mecanumCar = Mecanum_Car_Driver_V2()
distance_val = 0
distance_l = 0
distance_r = 0
class Servo:
    def __init__(self, pin, freq=50, min_us=600, max_us=2400, angle=180):
        self.min_us = min_us
        self.max_us = max_us
        self.us = 0
        self.freq = freq
        self.angle = angle
        self.analog_period = 0
        self.pin = pin
        analog_period = round((1/self.freq) * 1000)  # hertz to miliseconds
        self.pin.set_analog_period(analog_period)

    def write_us(self, us):
        us = min(self.max_us, max(self.min_us, us))
        duty = round(us * 1024 * self.freq // 1000000)
        self.pin.write_analog(duty)
        sleep(100)
        self.pin.write_analog(0)

    def write_angle(self, degrees=None):
        if degrees is None:
            degrees = math.degrees(radians)
        degrees = degrees % 360
        total_range = self.max_us - self.min_us
        us = self.min_us + total_range * degrees // self.angle
        self.write_us(us)

Servo(pin14).write_angle(90)

while True:

    distance_val = mecanumCar.get_distance()

    if distance_val < 20:
        mecanumCar.Motor_Upper_L(0, 0)
        mecanumCar.Motor_Lower_L(0, 0)
        mecanumCar.Motor_Upper_R(0, 0)
        mecanumCar.Motor_Lower_R(0, 0)
        sleep(500)
        Servo(pin14).write_angle(180)
        sleep(500)
        distance_l = mecanumCar.get_distance()
        sleep(500)

        Servo(pin14).write_angle(0)
        sleep(500)
        distance_r = mecanumCar.get_distance()
        sleep(500)

        if distance_l > distance_r:
            mecanumCar.Motor_Upper_L(0, 100)
            mecanumCar.Motor_Lower_L(0, 100)
            mecanumCar.Motor_Upper_R(1, 100)
            mecanumCar.Motor_Lower_R(1, 100)
            Servo(pin14).write_angle(90)
            sleep(300)
        else:
            mecanumCar.Motor_Upper_L(1, 100)
            mecanumCar.Motor_Lower_L(1, 100)
            mecanumCar.Motor_Upper_R(0, 100)
            mecanumCar.Motor_Lower_R(0, 100)
            Servo(pin14).write_angle(90)
            sleep(300)

    else:
        mecanumCar.Motor_Upper_L(1, 100)
        mecanumCar.Motor_Lower_L(1, 100)
        mecanumCar.Motor_Upper_R(1, 100)
        mecanumCar.Motor_Lower_R(1, 100)
```

5\.  **Testresultaat**

Nadat de code succesvol naar het bord is gedownload, **externe voeding inschakelen (zet de DIP-schakelaar op ON)** en druk op de resetknop van de micro:bit.

![Img](./media/Python_bb3e1312.png)

Wanneer de obstakelafstand groter is dan 20cm, rijdt de auto vooruit; anders draait de smart car naar links.

6\.  **Code Uitleg**

![Img](./media/Python_9e28cce7.png)

![Img](./media/Python_c33a22a8.png)

#### Project 18.3：Ultrasoon Volgen

![](./media/Python_28806167.jpg)

1\. **Beschrijving**

In de vorige les hebben we het basisprincipe van de lijnvolgsensor geleerd. Nu combineren we de ultrasone sensor met de auto om een ultrasoon volgende auto te maken.

De ultrasone sensor detecteert de afstand tot een obstakel en bestuurt daarmee de bewegingsstatus van de auto.

2\. **Voorbereiding**

- Steek de micro:bit in de sleuf van de keyestudio 4WD Mecanum Robot Car V2.0

- Plaats batterijen in het batterijhouder

- Zet de stroomschakelaar op ON

- Verbind de micro:bit met de computer via een USB-kabel

- Open de offline versie van Mu.

2\.  **Stroomschema**

![Img](./media/Python_53a30906.png)

3\.  **Testcode**

Open Mu-software en open het bestand “Ultrasonic Follow Smart Car\.py” om de code te importeren. Je kunt de code ook zelf in het bewerkingsvenster invoeren.

(**Opmerking: alle Engelse woorden en symbolen moeten in het Engels worden geschreven**.)

Klik op “Files” om het bibliotheekbestand “keyes_mecanum_Car_V2.py” naar de micro:bit te importeren.

Klik op “Check” om fouten in de code te controleren. Het programma is fout als er onderstrepingen en cursors worden getoond.

Als de code correct is, verbind de micro:bit met je computer en klik op “Flash” om de code naar de micro:bit te downloaden.

![](./media/Python_f586f3f7.png)

```python
from microbit import *
from keyes_mecanum_Car_V2 import *
import neopixel
display.off()

mecanumCar = Mecanum_Car_Driver_V2()
np = neopixel.NeoPixel(pin7, 4)

class Servo:
    def __init__(self, pin, freq=50, min_us=600, max_us=2400, angle=180):
        self.min_us = min_us
        self.max_us = max_us
        self.us = 0
        self.freq = freq
        self.angle = angle
        self.analog_period = 0
        self.pin = pin
        analog_period = round((1/self.freq) * 1000)  # hertz to miliseconds
        self.pin.set_analog_period(analog_period)

    def write_us(self, us):
        us = min(self.max_us, max(self.min_us, us))
        duty = round(us * 1024 * self.freq // 1000000)
        self.pin.write_analog(duty)
        sleep(100)
        self.pin.write_analog(0)

    def write_angle(self, degrees=None):
        if degrees is None:
            degrees = math.degrees(radians)
        degrees = degrees % 360
        total_range = self.max_us - self.min_us
        us = self.min_us + total_range * degrees // self.angle
        self.write_us(us)

Servo(pin14).write_angle(90)

while True:
    distance_val = 0
    distance_val = mecanumCar.get_distance()
    if distance_val >= 20 and distance_val <= 40:
        mecanumCar.Motor_Upper_L(1, 80)
        mecanumCar.Motor_Lower_L(1, 80)
        mecanumCar.Motor_Upper_R(1, 80)
        mecanumCar.Motor_Lower_R(1, 80)
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (255, 0, 0)
            np.show()
    if distance_val <= 10:
        mecanumCar.Motor_Upper_L(0, 80)
        mecanumCar.Motor_Lower_L(0, 80)
        mecanumCar.Motor_Upper_R(0, 80)
        mecanumCar.Motor_Lower_R(0, 80)
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (255, 255, 0)
            np.show()
    if distance_val > 10 and distance_val < 20 or distance_val > 40:
        mecanumCar.Motor_Upper_L(0, 0)
        mecanumCar.Motor_Lower_L(0, 0)
        mecanumCar.Motor_Upper_R(0, 0)
        mecanumCar.Motor_Lower_R(0, 0)
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (255, 255, 255)
            np.show()
```

4\.  **Testresultaat**

Nadat de code succesvol naar het bord is gedownload, **externe voeding inschakelen (zet de DIP-schakelaar op ON)**, en druk op de resetknop van de micro:bit.

![Img](./media/Python_bb3e1312.png)

De smart car kan het obstakel volgen en bewegen en de 4 WS2812 RGB-LEDs zullen verschillende kleuren tonen.

**Opmerking:** het obstakel kan alleen vóór de smart car bewegen.

5\.  **Code Uitleg**

![Img](./media/Python_930a04fa.png)

![Img](./media/Python_26371a4d.png)