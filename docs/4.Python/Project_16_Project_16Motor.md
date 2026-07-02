### Progetto 16: Motore

![](./media/Python_32655f47.png)

1\.  **Descrizione**

Il Keyestudio 4WD Mecanum Robot Car è dotato di 4 motori DC a riduzione, detti anche motori con riduttore, sviluppati a partire dal normale motore DC. Presentano una scatola di riduzione corrispondente che fornisce una velocità più bassa ma una coppia maggiore. Inoltre, diversi rapporti di riduzione della scatola possono fornire velocità e coppie diverse.

Il motore con riduttore è l'integrazione di riduttore e motore ed è ampiamente impiegato nell'industria siderurgica e meccanica.

Lo shield driver motore per micro:bit è dotato dei chip STC8G e HR8833. Per risparmiare le risorse delle porte I/O, controlliamo la direzione di rotazione e la velocità dei 4 motori DC con riduttore tramite il chip HR8833.

**Dettagli sui chip:**

![](./media/Python_d7132b53.jpg)

Fronte

![](./media/Python_4919ce3b.png)

Retro

![](./media/Python_fbfa17f7.png)

Circuito del chip STC8G1K08

![](./media/Python_47cdde6b.png)

Circuito driver motori HR8833

2\. **Preparazione**

- Inserire la scheda micro:bit nello slot del keyestudio 4WD Mecanum Robot CarV2.0

- Inserire le batterie nel vano portapile

- Portare l'interruttore di alimentazione su ON

- Collegare il micro:bit al computer tramite un cavo USB

- Aprire la versione offline di Mu.

3\. **Codice di test1**

Avviare il software Mu e aprire il file “microbit-Motor Driving-1.py” per importare il codice. È anche possibile inserire il codice manualmente nella finestra di modifica.

(**Nota: tutte le parole e i simboli in inglese devono essere scritti in inglese**.)

Fare clic su “Files” per importare il file di libreria “keyes_mecanum_Car.py” nel micro:bit. 

Fare clic su “Check” per controllare eventuali errori nel codice. Il programma contiene errori se compaiono sottolineature e cursori. 

Se il codice è corretto, collegare il micro:bit al computer e fare clic su “Flash” per caricare il codice sulla scheda micro:bit.

![](./media/Python_71476377.png)

```python
from microbit import *
from keyes_mecanum_Car_V2 import *
mecanumCar = Mecanum_Car_Driver_V2()
while True:
    display.show(Image.ARROW_S)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    display.show(Image.ARROW_N)
    mecanumCar.Motor_Upper_L(0, 100)
    mecanumCar.Motor_Lower_L(0, 100)
    mecanumCar.Motor_Upper_R(0, 100)
    mecanumCar.Motor_Lower_R(0, 100)
    sleep(1000)
    display.show(Image.ARROW_E)
    mecanumCar.Motor_Upper_L(0, 100)
    mecanumCar.Motor_Lower_L(0, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    display.show(Image.ARROW_W)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(0, 100)
    mecanumCar.Motor_Lower_R(0, 100)
    sleep(1000)
    display.show(Image("00900:""09990:""99999:""99999:""09090"))
    mecanumCar.Motor_Upper_L(0, 0)
    mecanumCar.Motor_Lower_L(0, 0)
    mecanumCar.Motor_Upper_R(0, 0)
    mecanumCar.Motor_Lower_R(0, 0)
    sleep(1000)
```

4\. **Risultato del test1**

Dopo aver scaricato correttamente il codice sulla scheda, **alimentare dall'esterno (portare l'interruttore DIP su ON)** e premere il pulsante di reset sul micro:bit.

![Img](./media/Python_bb3e1312.png)

Quindi il veicolo avanzerà per 1s, indietreggerà per 1s, sterzerà a sinistra per 1s, a destra per 1s, ruoterà in senso antiorario per 1s, in senso orario per 1s e si fermerà per 1s. La matrice LED mostra anche i relativi simboli.

5\. **Codice di test2**

Avviare il software Mu e aprire il file “microbit-Motor Driving-2.py” per importare il codice. È anche possibile inserire il codice manualmente nella finestra di modifica.

(**Nota: tutte le parole e i simboli in inglese devono essere scritti in inglese**.)

Fare clic su “Files” per importare il file di libreria “keyes_mecanum_Car.py” nel micro:bit. 

Fare clic su “Check” per controllare eventuali errori nel codice. Il programma contiene errori se compaiono sottolineature e cursori. 

Se il codice è corretto, collegare il micro:bit al computer e fare clic su “Flash” per caricare il codice sulla scheda micro:bit.

![](./media/Python_96230faf.png)

```python
from microbit import button_a, button_b, display, Image, sleep
from keyes_mecanum_Car_V2 import *
mecanumCar = Mecanum_Car_Driver_V2()

show_L = Image("90000:""90000:""90000:""90000:""99999")
show_O = Image("09990:""90009:""90009:""90009:""09990")
a = 0
b = 0
def run_L():
    global b
    sleep(1000)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    mecanumCar.Motor_Upper_L(0, 100)
    mecanumCar.Motor_Lower_L(0, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(650)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    mecanumCar.Motor_Upper_L(0, 0)
    mecanumCar.Motor_Lower_L(0, 0)
    mecanumCar.Motor_Upper_R(0, 0)
    mecanumCar.Motor_Lower_R(0, 0)
    b = 0
def run_O():
    global b
    sleep(1000)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    mecanumCar.Motor_Upper_L(0, 100)
    mecanumCar.Motor_Lower_L(0, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(620)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    mecanumCar.Motor_Upper_L(0, 100)
    mecanumCar.Motor_Lower_L(0, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(620)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    mecanumCar.Motor_Upper_L(0, 100)
    mecanumCar.Motor_Lower_L(0, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(620)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    mecanumCar.Motor_Upper_L(0, 0)
    mecanumCar.Motor_Lower_L(0, 0)
    mecanumCar.Motor_Upper_R(0, 0)
    mecanumCar.Motor_Lower_R(0, 0)
    b = 0
while True:
    if button_a.was_pressed():
        a = a + 1
        if a >= 3:
            a = 0
    if button_b.was_pressed():
        b = 1
    if (a == 1):
        display.show(show_L)
        if b == 1:
            run_L()
    elif a == 2:
        display.show(show_O)
        if b == 1:
            run_O()
```

6\. **Risultato del test2**

Dopo aver scaricato correttamente il codice sulla scheda, **alimentare dall'esterno (portare l'interruttore DIP su ON)** e premere il pulsante di reset sul micro:bit.

![Img](./media/Python_bb3e1312.png)

Quando i pulsanti A e B vengono premuti la prima volta, il micro:bit mostrerà “L”, la traiettoria dell'auto sarà a forma di “L”. Quando vengono premuti di nuovo, sul micro:bit appare “口” e la traiettoria dell'auto sarà a forma di “口”. L'auto ripeterà questo schema.

7\.  **Spiegazione del codice**

![Img](./media/Python_70b4e70f.png)

![Img](./media/Python_e3250a8a.png)