### Progetto 11: Microfono

![](./media/Python_3073a8af.png)

![](./media/Python_7f074115.png)

1\.  **Descrizione**

La scheda principale Micro: Bit ha un microfono integrato, che può rilevare il volume dell'ambiente circostante. Quando batte le mani, si accende l'indicatore LED del microfono. Inoltre, può misurare l'intensità del suono, permettendoti di creare una scala di rumore o luci da discoteca che cambiano con la musica.

Il microfono è posto sul lato opposto rispetto all'indicatore LED del microfono e vicino a fori che lasciano passare il suono. Quando la scheda rileva il suono, l'indicatore LED si accende.

2\.  **Preparazione**

A. Collega la scheda principale micro:bit al computer tramite il cavo USB

B. Apri la versione offline di Mu.

3\.  **Codice di test1**

Apri il software Mu e apri il file “Microphone-1\.py” per importare il codice. Puoi anche inserire il codice nella finestra di modifica manualmente.

(**Nota: Tutte le parole e i simboli devono essere scritti in inglese**.)

![](./media/Python_19b38832.png)

```python
from microbit import *

while True:
    if microphone.current_event() == SoundEvent.LOUD:
        display.show(Image.HEART)
        sleep(200)
    if microphone.current_event() == SoundEvent.QUIET:
        display.show(Image.HEART_SMALL)
```

Clicca su “Check” per verificare errori nel codice. Il programma è errato se vengono mostrati sottolineature e cursori. 

![](./media/Python_36a669c7.png)

Se il codice è corretto, collega il micro:bit al computer e clicca su “Flash” per scaricare il codice sulla scheda micro:bit.

![](./media/Python_0515bf32.png)

4\.  **Risultato del test1**

Dopo aver scaricato con successo il codice sulla scheda, **accendi l'alimentazione tramite cavo micro USB o alimentazione esterna (impostare l'interruttore DIP su ON)** e premi il pulsante di reset sul micro:bit.

![Img](./media/Python_bb3e1312.png)

La matrice a punti LED mostra il motivo “❤” quando batte le mani e il motivo ![](./media/04fdfc9060943954e7938bb1a741d626.png) quando l'ambiente è silenzioso.

5\.  **Codice di test2**

Apri il software Mu e apri il file “Microphone-2\.py” per importare il codice. Puoi anche inserire il codice nella finestra di modifica manualmente.

(**Nota: Tutte le parole e i simboli devono essere scritti in inglese.**)

![](./media/Python_f0e5a346.png)

```python
from microbit import *
maxSound = 0
lights = Image("11111:"
              "11111:"
              "11111:"
              "11111:"
              "11111")
# ignore first sound level reading
soundLevel = microphone.sound_level()
sleep(200)

while True:
    if button_a.is_pressed():
        display.scroll(maxSound)
    else:
        soundLevel = microphone.sound_level()
        display.show(lights * soundLevel)
        if soundLevel > maxSound:
            maxSound = soundLevel
```

Clicca su “Check” per verificare errori nel codice. Il programma è errato se vengono mostrati sottolineature e cursori. 

![](./media/Python_d0c79871.png)

Se il codice è corretto, collega il micro:bit al computer e clicca su “Flash” per scaricare il codice sulla scheda micro:bit.

![](./media/Python_d828b9ee.png)

6\.  **Risultato del test2**

Dopo aver scaricato con successo il codice sulla scheda, **accendi l'alimentazione tramite cavo micro USB o alimentazione esterna (impostare l'interruttore DIP su ON)** e premi il pulsante di reset sul micro:bit.

![Img](./media/Python_bb3e1312.png)

Quando viene premuto il pulsante A, la matrice a punti LED mostra il valore del volume massimo ( **nota che il volume massimo può essere azzerato tramite il pulsante Reset sull'altro lato della scheda** ). Quando si applaude, più il suono testato è forte, più luminose appaiono le 25 LED della matrice.

7\.  **Spiegazione del codice**

![Img](./media/Python_980f62b3.png)