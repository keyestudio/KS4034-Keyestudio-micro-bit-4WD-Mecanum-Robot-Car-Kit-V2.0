### Progetto 1：Heart Beat

![](./media/Python_b855274f.png)

1\.  **Descrizione**

Questo progetto è facile da eseguire utilizzando soltanto una scheda micro:bit e un cavo micro USB. Questo esperimento funge da introduzione per farti entrare nel magico mondo della programmazione del micro:bit.

2\.  **Preparazione**

A. Collega la scheda micro:bit al tuo computer tramite il cavo USB.

B. Apri la versione offline di Mu.

3\.  **Codice di test**

Apri il software Mu, tocca “Load”, seleziona il file ““microbit-Heartbeat\.py“” e clicca “open”:

![](./media/Python_1ec17d44.png)

![](./media/Python_4bda2b61.png)

C'è un altro modo per importare il codice. Apri Mu e trascina il file “microbit-Heartbeat\.py” al suo interno.

![](./media/Python_c5b7322b.png)

Puoi anche inserire il codice direttamente nella finestra di modifica.

(**Nota: Tutte le parole e i simboli in inglese devono essere scritti in inglese.**)

![](./media/Python_80af4cb3.png)

```python
from microbit import *

while True:
    display.show(Image.HEART)
    sleep(500)
    display.show(Image.HEART_SMALL)
    sleep(500)
```
Di seguito è riportato un elenco delle immagini integrate:

• Image.HEART

• Image.HEART_SMALL

• Image.HAPPY

• Image.SMILE

• Image.SAD

• Image.CONFUSED

• Image.ANGRY

• Image.ASLEEP

• Image.SURPRISED

• Image.SILLY

• Image.FABULOUS

• Image.MEH

• Image.YES

• Image.NO

• Image.CLOCK12, Image.CLOCK11, Image.CLOCK10, Image.CLOCK9, Image.CLOCK8, Image.CLOCK7, Image.CLOCK6, Image.CLOCK5,

Image.CLOCK4, Image.CLOCK3, Image.CLOCK2, Image.CLOCK1

• Image.ARROW_N, Image.ARROW_NE, Image.ARROW_E, Image.ARROW_SE, Image.ARROW_S, Image.ARROW_SW, Image.ARROW_W, Image.ARROW_NW

• Image.TRIANGLE

• Image.TRIANGLE_LEFT

• Image.CHESSBOARD

• Image.DIAMOND

• Image.DIAMOND_SMALL

• Image.SQUARE

• Image.SQUARE_SMALL

• Image.RABBIT

• Image.COW

• Image.MUSIC_CROTCHET

• Image.MUSIC_QUAVER

• Image.MUSIC_QUAVERS

• Image.PITCHFORK

• Image.PACMAN

• Image.TARGET

• Image.TSHIRT

• Image.ROLLERSKATE

• Image.DUCK

• Image.HOUSE

• Image.TORTOISE

• Image.BUTTERFLY

• Image.STICKFIGURE

• Image.GHOST

• Image.SWORD

• Image.GIRAFFE

• Image.SKULL

• Image.UMBRELLA

• Image.SNAKE，Image.ALL_CLOCKS，Image.ALL_ARROWS

Collega la scheda micro:bit al computer tramite un cavo USB, fai clic su “Flash” per scaricare il codice sulla scheda.

![](./media/Python_93e18731.png)


![](./media/Python_48e78948.png)


![](./media/Python_cc33f1a9.png)

Il codice, anche se errato, può essere scaricato correttamente sulla scheda micro:bit, ma non funzionerà sul micro:bit.

Clicca “Flash” per scaricare il codice sul micro:bit.

![](./media/Python_8982d0b0.png)

Clicca “REPL” e premi il pulsante di reset sul micro:bit: le informazioni di errore verranno visualizzate nella finestra REPL, come mostrato sotto:

![](./media/Python_0c2abf18.png)

Clicca di nuovo “REPL” per disattivare la modalità REPL, quindi potrai aggiornare il nuovo codice.

Per assicurarti che il codice sia corretto, basta toccare “Check”. Gli errori saranno mostrati nella finestra.

![](./media/Python_b994c0d3.png)

Modifica il codice secondo le indicazioni e clicca “Check”.

![](./media/Python_bc5cbed3.png)

 Per altri tutorial visita il sito: [https://codewith.mu/en/tutorials/](https://codewith.mu/en/tutorials/)

4\.  **Risultato del test**

Clicca su “<span style="color: rgb(255, 76, 65);">**Flash**</span>” per caricare il codice sulla scheda micro:bit.

![Img](./media/Python_ed83ac25.png)

Dopo aver scaricato correttamente il codice sulla scheda, **alimenta tramite il cavo micro USB o una fonte di alimentazione esterna (imposta l'interruttore DIP su ON)** e premi il pulsante di reset sulla scheda.

![Img](./media/Python_bb3e1312.png)

La matrice di LED mostra alternativamente il motivo “❤” e poi “![](./media/Python_04fdfc90.png)”.

5\.  **Spiegazione del codice**

|from microbit import*|Importa il file della libreria del micro:bit|
|-|-|
|while True:|Questo è un ciclo permanente che fa sì che il micro:bit esegua il codice in questo ciclo per sempre.|
|display.show(Image.HEART)|micro:bit mostra “❤”|
|sleep(500)|Ritardo di 500 ms|
|display.show(Image.HEART_SMALL)|La matrice LED visualizza “![](./media/Python_04fdfc90.png)”|

---