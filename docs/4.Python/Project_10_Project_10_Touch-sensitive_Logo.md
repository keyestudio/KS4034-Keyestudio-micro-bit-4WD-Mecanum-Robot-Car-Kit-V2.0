### Progetto 10: Logo sensibile al tatto

![](./media/Python_64469585.png)

1\.  **Descrizione**

La scheda principale micro:bit V2 è dotata di un logo dorato sensibile al tocco, che può fungere da componente di input come un pulsante.

Contiene un sensore capacitivo di tocco che rileva piccole variazioni del campo elettrico quando viene premuto (o toccato), proprio come lo schermo del tuo telefono o tablet. Quando lo premi, il programma può essere attivato.

2\.  **Preparazione**

A. Collega la scheda principale micro:bit al computer tramite il cavo USB.

B. Apri la versione offline di Mu.

3\.  **Codice di test**

Avvia il software Mu e apri il file “Touch-sensitive Logo\.py” per importare il codice. Puoi anche inserire il codice direttamente nella finestra di modifica.

(**Nota: Tutte le parole e i simboli in inglese devono essere scritti in inglese**.)

![](./media/Python_0c54cbe5.png)

```python
from microbit import *
time = 0
start = 0
running = False

while True:

    if button_a.was_pressed():
        running = True
        start = running_time()
    if button_b.was_pressed():
        if running:
            time += running_time() - start
        running = False
    if pin_logo.is_touched():
        if not running:
            display.scroll(int(time/1000))

    if running:
        display.show(Image.HEART)
        sleep(300)
        display.show(Image.HEART_SMALL)
        sleep(300)
    else:
        display.show(Image.ASLEEP)
```

**Come funziona il Micro:bit?**

A\. Il tempo di esecuzione è registrato in millisecondi (ms).

B\. Quando premi il pulsante A, una variabile chiamata start viene impostata sul tempo di esecuzione corrente.

C\. Quando premi il pulsante B, il tempo di start viene sottratto dal nuovo tempo di esecuzione per calcolare il tempo trascorso dall'avvio del cronometro. Questa differenza viene aggiunta al tempo totale, che è memorizzato in una variabile chiamata time.

D\. Se premi il logo dorato, il programma visualizzerà il tempo totale trascorso sul display LED. Converte il tempo da millisecondi (millesimi di secondo) a secondi dividendo per 1000. Usa l'operatore di divisione intera per restituire un risultato intero.

E\. Il programma è anche controllato da una variabile booleana chiamata running. Una variabile booleana ha solo due valori: true o false. Se "running" è "true", significa che il cronometro è avviato. Se "running" è false, significa che il cronometro non è avviato o è fermo.

F\. Se "running" è true, il motivo del cuore che batte sarà visualizzato sulla matrice di LED.

G\. (7) Se il cronometro è stato fermato e "running" è false, quando premi il logo dorato, verrà mostrato solo il tempo.

H\. Se il cronometro è stato avviato e "running" è true, è sufficiente assicurarsi che la variabile time cambi quando viene premuto il pulsante B, e il codice può anche prevenire letture errate.

Clicca su “Check” per controllare gli errori nel codice. Il programma risulta errato se vengono mostrati sottolineature e cursori.

![](./media/Python_1766a28c.png)

Se il codice è corretto, collega il micro:bit al computer e fai clic su “Flash” per scaricare il codice sulla scheda micro:bit.

![](./media/Python_a3d6e994.png)

4\.  **Risultato del test**

Dopo aver scaricato correttamente il codice sulla scheda, **alimenta tramite il cavo micro USB o un'alimentazione esterna (imposta l'interruttore DIP su ON)** e premi il pulsante di reset sul micro:bit.

![Img](./media/Python_bb3e1312.png)

Premi il pulsante A per avviare il cronometro. Durante la misurazione, il motivo del cuore che batte sarà visualizzato sulla matrice di LED. Premi il pulsante B per fermarlo; puoi avviarlo e fermarlo in qualsiasi momento.

Continuerà a registrare il tempo, proprio come un vero cronometro. Premi il logo dorato sulla parte anteriore del micro:bit per visualizzare il tempo misurato in secondi. Il tempo può essere azzerato premendo il pulsante di reset sul retro.

---