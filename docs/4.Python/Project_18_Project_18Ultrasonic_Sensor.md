### Progetto 18：Sensore a ultrasuoni

#### Progetto 18.1：Rilevamento della distanza ad ultrasuoni

1\. **Descrizione**

![](./media/Python_9810ae67.jpg)

Il sensore a ultrasuoni usa il sonar per determinare la distanza di un oggetto, come fanno i pipistrelli. Offre un eccellente rilevamento della distanza senza contatto con alta precisione e letture stabili in un pacchetto facile da usare. Include moduli trasmettitore e ricevitore ultrasonico.

Il sensore a ultrasuoni viene utilizzato in una vasta gamma di progetti elettronici per creare applicazioni di rilevamento ostacoli e misurazione della distanza, oltre a varie altre applicazioni.

![](./media/Python_0180b169.png)

Il modulo ultrasonico emetterà le onde ultrasoniche dopo il segnale di trigger. Quando le onde ultrasoniche incontrano un oggetto e vengono riflesse, il modulo emette un segnale echo, quindi può determinare la distanza dell'oggetto dal tempo trascorso tra il segnale di trigger (TRIG) e il segnale di echo (ECHO).

Come mostra l'immagine, è come due occhi. Uno è l'estremità di trasmissione, l'altro è l'estremità di ricezione.

Secondo il diagramma di collegamento sopra, la porta integrata del modulo sensore a ultrasuoni è collegata alla porta 5V G P15 P16 sulla basetta driver motore micro:bit. Il pin Trig (T) è controllato da P15 del micro:bit e il pin Echo (E) da P16.

![](./media/Python_19b45a23.jpg)

2\. **Principio di funzionamento**

![](./media/Python_8ff02741.png)

(1) Mettere a livello basso TRIG poi inviare un segnale di trigger a livello alto per almeno 10us;

(2) Dopo il trigger, il modulo invierà automaticamente otto impulsi ultrasonici a 40KHz e verificherà se c'è un segnale di ritorno;

(3) Se c'è un segnale di ritorno, quando ECHO (E) passa a livello alto, la durata del livello alto è il tempo dalla trasmissione alla ricezione delle onde ultrasoniche. Quindi distanza misurata = durata del livello alto * 340 m/s * 0.5.

3\.  **Parametri**

- Tensione di lavoro: 3-5.5V (DC)

- Corrente di lavoro: 15mA

- Frequenza di lavoro: 40kHz

- Distanza massima di rilevamento: circa 3m

- Distanza minima di rilevamento: 2-3cm

- Precisione: fino a 0.2cm

- Angolo di rilevamento: inferiore a 15 gradi

- Impulso di trigger in ingresso: 10us livello TTL

- Segnale echo in uscita: segnale di livello TTL in uscita (alto), proporzionale alla distanza

4\.  **Preparazione**

- Inserire la scheda micro:bit nello slot del keyestudio 4WD Mecanum Robot Car V2.0

- Inserire le batterie nel portabatterie

- Portare l'interruttore di alimentazione su ON

- Collegare il micro:bit al computer tramite un cavo USB

- Aprire la versione offline di Mu.

5\.  **Codice di prova**

Aprire il software Mu e aprire il file “Ultrasonic Ranging\.py” per importare il codice. È anche possibile inserire il codice direttamente nella finestra di modifica.

(**Nota: Tutte le parole e i simboli in inglese devono essere scritti in inglese**.)

Cliccare “Files” per importare il file di libreria “keyes_mecanum_Car_V2.py” nel micro:bit.

Cliccare “Check” per verificare errori nel codice. Il programma è errato se appaiono sottolineature o cursori.

Se il codice è corretto, collegare il micro:bit al computer e cliccare “Flash” per scaricare il codice sulla scheda micro:bit.

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

6\.  **Risultato del test**

Dopo aver scaricato correttamente il codice sulla scheda, non scollegare il cavo USB. Cliccare “REPL” e poi premere il pulsante di reset.

![Img](./media/Python_bb3e1312.png)

Il valore della distanza dell'ostacolo verrà visualizzato, come mostrato sotto.

Quando la distanza è inferiore a 10cm, il buzzer passivo dello smart car emetterà un suono.

![](./media/Python_4dc8054e.png)

7\.  **Spiegazione del codice**

![Img](./media/Python_ebde06e9.png)

#### Progetto 18.2：Evitamento Ultrasonico

![](./media/Python_aee41f6f.jpg)

1\. **Descrizione**

In questo progetto integreremo un sensore a ultrasuoni e un'auto per realizzare un'auto ad evitamento ultrasonico.

Il principio è rilevare la distanza tra l'auto e l'ostacolo tramite il sensore a ultrasuoni per controllare il movimento dello smart car.

2\. **Preparazione**

- Inserire la scheda micro:bit nello slot del keyestudio 4WD Mecanum Robot Car V2.0

- Inserire le batterie nel portabatterie

- Portare l'interruttore di alimentazione su ON

- Collegare il micro:bit al computer tramite un cavo USB

- Aprire la versione offline di Mu.

3\.  **Diagramma di flusso**

![Img](./media/Python_a4efee72.png)

4\.  **Codice di prova**

Aprire il software Mu e aprire il file “Ultrasonic Avoid Smart Car\.py” per importare il codice. È anche possibile inserire il codice direttamente nella finestra di modifica.

(**Nota: Tutte le parole e i simboli in inglese devono essere scritti in inglese**.)

Cliccare “Files” per importare il file di libreria “keyes_mecanum_Car_V2.py” nel micro:bit.

Cliccare “Check” per verificare errori nel codice. Il programma è errato se appaiono sottolineature o cursori.

Se il codice è corretto, collegare il micro:bit al computer e cliccare “Flash” per scaricare il codice sulla scheda micro:bit.

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

5\.  **Risultato del test**

Dopo aver scaricato correttamente il codice sulla scheda, **alimentazione esterna (portare l'interruttore DIP su ON)**, e premere il pulsante di reset sul micro:bit.

![Img](./media/Python_bb3e1312.png)

Quando la distanza dall'ostacolo è maggiore di 20cm, l'auto procede in avanti; al contrario, lo smart car svolta a sinistra.

6\.  **Spiegazione del codice**

![Img](./media/Python_9e28cce7.png)

![Img](./media/Python_c33a22a8.png)

#### Progetto 18.3：Inseguimento Ultrasonico

![](./media/Python_28806167.jpg)

1\. **Descrizione**

Nella lezione precedente abbiamo imparato il principio base del sensore per il tracciamento della linea. Successivamente, combineremo il sensore a ultrasuoni con l'auto per realizzare un'auto ad inseguimento ultrasonico.

Il sensore a ultrasuoni rileva la distanza dall'ostacolo e controlla lo stato di movimento dell'auto.

2\. **Preparazione**

- Inserire la scheda micro:bit nello slot del keyestudio 4WD Mecanum Robot Car V2.0

- Inserire le batterie nel portabatterie

- Portare l'interruttore di alimentazione su ON

- Collegare il micro:bit al computer tramite un cavo USB

- Aprire la versione offline di Mu.

2\.  **Diagramma di flusso**

![Img](./media/Python_53a30906.png)

3\.  **Codice di prova**

Aprire il software Mu e aprire il file “Ultrasonic Follow Smart Car\.py” per importare il codice. È anche possibile inserire il codice direttamente nella finestra di modifica.

(**Nota: Tutte le parole e i simboli in inglese devono essere scritti in inglese**.)

Cliccare “Files” per importare il file di libreria “keyes_mecanum_Car_V2.py” nel micro:bit.

Cliccare “Check” per verificare errori nel codice. Il programma è errato se appaiono sottolineature o cursori.

Se il codice è corretto, collegare il micro:bit al computer e cliccare “Flash” per scaricare il codice sulla scheda micro:bit.

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

4\.  **Risultato del test**

Dopo aver scaricato correttamente il codice sulla scheda, **alimentazione esterna (portare l'interruttore DIP su ON)**, e premere il pulsante di reset sul micro:bit.

![Img](./media/Python_bb3e1312.png)

Lo smart car potrà seguire l'ostacolo nel movimento e le 4 luci RGB WS2812 mostreranno colori diversi.

**Nota:** l'ostacolo può muoversi solo davanti allo smart car.

5\.  **Spiegazione del codice**

![Img](./media/Python_930a04fa.png)

![Img](./media/Python_26371a4d.png)