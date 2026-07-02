### Progetto 14: 4 LED RGB WS2812

![](./media/Python_eecf79fe.png)

1\.  **Descrizione**

La shield driver gestisce 4 pezzi di LED RGB WS2812, è compatibile con la scheda micro:bit e viene controllata da P7. In questa lezione faremo visualizzare alle LED RGB colori diversi tramite P7. In questa lezione sono forniti 3 set di codice di prova per far visualizzare ai 4 LED WS2812 RGB effetti differenti.

![Img](./media/Python_0be70eda.png)

2\.  **Preparazione**

- Inserire la scheda micro:bit nello slot del keyestudio 4WD Mecanum Robot Car V2.0

- Inserire le batterie nel portabatterie

- Ruotare l'interruttore di alimentazione sulla posizione ON

- Collegare il micro:bit al computer tramite un cavo USB

- Aprire la versione offline di Mu.

3\.  **Test Code1**

Avviare il software Mu e aprire il file“4 WS2812 RGB LEDs-1\.py”per importare il codice\ È inoltre possibile inserire il codice manualmente nella finestra di modifica.

(**Nota: Tutte le parole e i simboli in inglese devono essere scritti in inglese.**)

Cliccare su“Check”per verificare errori nel codice. Il programma è considerato errato se sono mostrati sottolineature e cursori. 

![](./media/Python_5b5266e2.png)

```python
from microbit import *
import neopixel
np = neopixel.NeoPixel(pin7, 4)
while True:
    for pixel_id1 in range(0, len(np)):
        np[pixel_id1] = (255, 0, 0)
        np.show()
    sleep(1000)
    for pixel_id2 in range(0, len(np)):
        np[pixel_id2] = (255, 165, 0)
        np.show()
    sleep(1000)
    for pixel_id3 in range(0, len(np)):
        np[pixel_id3] = (255, 255, 0)
        np.show()
    sleep(1000)
    for pixel_id4 in range(0, len(np)):
        np[pixel_id4] = (0, 255, 0)
        np.show()
    sleep(1000)
    for pixel_id5 in range(0, len(np)):
        np[pixel_id5] = (0, 0, 255)
        np.show()
    sleep(1000)
    for pixel_id6 in range(0, len(np)):
        np[pixel_id6] = (75, 0, 130)
        np.show()
    sleep(1000)
    for pixel_id7 in range(0, len(np)):
        np[pixel_id7] = (238, 130, 238)
        np.show()
    sleep(1000)
    for pixel_id8 in range(0, len(np)):
        np[pixel_id8] = (160, 32, 240)
        np.show()
    sleep(1000)
    for pixel_id9 in range(0, len(np)):
        np[pixel_id9] = (255, 255, 255)
    sleep(1000)
```

Se il codice è corretto, collegare il micro:bit al computer e cliccare su“Flash”per scaricare il codice sulla scheda micro:bit.

![](./media/Python_56a9ab63.png)

4\.  **Risultato del Test1**

Dopo aver scaricato con successo il codice sulla scheda, **alimentazione esterna (portare l'interruttore DIP su ON)** e premere il pulsante di reset sul micro:bit.

![Img](./media/Python_bb3e1312.png)

Le 4 WS2812RGB LED si accendono a ciclo mostrando ciascuna un colore diverso.

5\.  **Test Code2**

Avviare il software Mu e aprire il file“4 WS2812 RGB LEDs-2\.py”per importare il codice. È inoltre possibile inserire il codice manualmente nella finestra di modifica.

(**Nota: Tutte le parole e i simboli in inglese devono essere scritti in inglese**.)

Cliccare su“Check”per verificare errori nel codice. Il programma è considerato errato se sono mostrati sottolineature e cursori. 

Se il codice è corretto, collegare il micro:bit al computer e cliccare su“Flash”per scaricare il codice sulla scheda micro:bit.

![](./media/Python_8cb1dd7c.png)

```python
from microbit import *
import neopixel
np = neopixel.NeoPixel(pin7, 4)
while True:
    for index in range(0, 4):
        np.clear()
        np[index] = (255, 0, 0)
        np.show()
        sleep(100)
    for index1 in range(0, 4):
        np.clear()
        np[index1] = (255, 165, 0)
        np.show()
        sleep(100)
    for index2 in range(0, 4):
        np.clear()
        np[index2] = (255, 255, 0)
        np.show()
        sleep(100)
    for index3 in range(0, 4):
        np.clear()
        np[index3] = (0, 255, 0)
        np.show()
        sleep(100)
    for index4 in range(0, 4):
        np.clear()
        np[index4] = (0, 0, 255)
        np.show()
        sleep(100)
    for index5 in range(0, 4):
        np.clear()
        np[index5] = (75, 0, 130)
        np.show()
        sleep(100)
    for index6 in range(0, 4):
        np.clear()
        np[index6] = (238, 130, 238)
        np.show()
        sleep(100)
    for index7 in range(0, 4):
        np.clear()
        np[index7] = (160, 32, 240)
        np.show()
        sleep(100)
    for index8 in range(0, 4):
        np.clear()
        np[index8] = (255, 255, 255)
        np.show()
        sleep(100)
```

6\.  **Risultato del Test2**

Dopo aver scaricato con successo il codice sulla scheda, **alimentazione esterna (portare l'interruttore DIP su ON)** e premere il pulsante di reset sul micro:bit.

![Img](./media/Python_bb3e1312.png)

Le WS2812RGB LED mostrano un effetto di luce scorrente.

7\.  **Test Code3**

Avviare il software Mu e aprire il file“4 WS2812 RGB LEDs-3\.py”per importare il codice. È inoltre possibile inserire il codice manualmente nella finestra di modifica.

(**Nota: Tutte le parole e i simboli in inglese devono essere scritti in inglese.**)

Cliccare su“Check”per verificare errori nel codice. Il programma è considerato errato se sono mostrati sottolineature e cursori. 

Se il codice è corretto, collegare il micro:bit al computer e cliccare su“Flash”per scaricare il codice sulla scheda micro:bit.

![](./media/Python_b248f1c5.png)

```python
from microbit import *
import neopixel
np = neopixel.NeoPixel(pin7, 4)
from random import randint
R = 0
G = 0
B = 0
while True:
   for index in range(0, 4):
        R = randint(10, 255)
        G = randint(10, 255)
        B = randint(10, 255)
        np.clear()
        np[index] = (R, G, B)
        np.show()
        sleep(500)
```

8\.  **Risultato del Test3**

Dopo aver scaricato con successo il codice sulla scheda, **alimentazione esterna (portare l'interruttore DIP su ON)** e premere il pulsante di reset sul micro:bit.

![Img](./media/Python_bb3e1312.png)

Ogni LED WS2812RGB mostra una colore casuale, uno dopo l'altro.

5\.  **Spiegazione del codice**

![Img](./media/Python_d1e3977b.png)

---