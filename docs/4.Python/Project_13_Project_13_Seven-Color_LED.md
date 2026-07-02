### Progetto 13: LED a sette colori

![](./media/Python_804e502b.png)

1\.  **Descrizione**

Questo modulo è costituito da un LED comunemente usato a 7 colori ma con aspetto bianco. Può lampeggiare automaticamente diversi colori per creare effetti luminosi fantastici quando viene applicato un livello alto, come con un LED normale.

2\.  **Preparazione**

- Inserire la scheda micro:bit nello slot del keyestudio 4WD Mecanum Robot Car V2.0

- Inserire le batterie nel vano portabatterie

- Portare l'interruttore di alimentazione in posizione ON

- Collegare il micro:bit al computer tramite un cavo USB

- Aprire la versione offline di Mu.

3\.  **Codice di test**

Aprire il software Mu e aprire il file“Colorful lights\.py”per importare il codice. È inoltre possibile inserire il codice nella finestra di modifica manualmente.

(**Nota: Tutte le parole e i simboli devono essere scritti in inglese**.)

![](./media/Python_010a8a12.png)

```python
from microbit import *
from keyes_mecanum_Car_V2 import *

mecanumCar = Mecanum_Car_Driver_V2()

while True:
    mecanumCar.left_led(1)
    mecanumCar.right_led(1)
    sleep(3000)
    mecanumCar.left_led(0)
    mecanumCar.right_led(0)
    sleep(3000)
```

**Avviso importante:** Se il file di libreria 'keyes_mecanum_Car_V2.py' non è ancora stato importato nella scheda micro:bit, è essenziale importare prima il file di libreria nella scheda micro:bit. Il metodo per importare la libreria può essere trovato cliccando sul link: [How to Import Library to Micro:bit](https://docs.keyestudio.com/projects/KS4034/en/latest/docs/Python/Python.html#how-mu-import-library-to-micro-bit) e seguendo le istruzioni fornite; altrimenti il codice non verrà eseguito.

Dopo che il file di libreria è stato importato con successo, è inoltre necessario fare clic sul pulsante "Check" per controllare il codice. Se appare un cursore o un sottolineamento su una determinata riga, significa che sono presenti errori nel programma.

![](./media/Python_ce67f468.png)

Tuttavia, durante questo processo apparirà il seguente avviso anche se non ci sono errori nel codice. Questi avvisi sono solo messaggi di warning e non errori del codice.

![](./media/Python_863bb61b.png)

![](./media/Python_ccfbfa56.png)

Se il codice è corretto, collegare il micro:bit al computer e cliccare su“Flash”per scaricare il codice sulla scheda micro:bit.

![](./media/Python_39512a13.png)

Se dopo aver cliccato sul pulsante "Flash" compaiono errori, verificare se è stato importato il file di libreria fornito "keyes_mecanum_Car_V2.py".

**Nota:** Prima di programmare con Micropython, è necessario importare il file di libreria "keyes_mecanum_Car_V2.py" nel micro:bit. Se si programma con un micro:bit diverso, il file di libreria "keyes_mecanum_Car_V2.py" deve essere importato nuovamente sul nuovo micro:bit.

4\. **Risultato del test**

Dopo aver scaricato correttamente il codice sulla scheda, **alimentazione esterna (portare l'interruttore DIP su ON)** e premere il pulsante di reset sul micro:bit.

![Img](./media/Python_bb3e1312.png)

Il LED a sette colori lampeggerà per 3s poi si fermerà per 3s e ripeterà questo schema.

5\. **Spiegazione del codice**

![Img](./media/Python_a4a670c0.png)