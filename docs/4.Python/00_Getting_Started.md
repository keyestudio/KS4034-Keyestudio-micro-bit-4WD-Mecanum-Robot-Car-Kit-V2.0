## Resource Download

Per aiutarti a ottenere rapidamente i codici correlati, le librerie e altri file di supporto per questo prodotto, fai clic sui link seguenti per scaricarli:

- [Python Code and library downloads](./PythonCode.7z)

## Iniziare con Python

Questo tutorial è scritto per il linguaggio Python. Se desideri utilizzare la programmazione grafica, fai riferimento al manuale "Makecode Tutorial". Nella directory principale della risorsa scaricata è presente una cartella denominata "Python tutorial", che contiene tutto il codice Python per il Micro:bit 4WD Mecanum Robot Car V2.0. Il file di codice Python è un file che termina con ".py".

### Che cos'è MicroPython?

Python è un linguaggio basato su testo, ampiamente utilizzato nell'istruzione e anche impiegato da programmatori professionisti in campi come data science e machine learning.

Micro: bit può essere programmato in Python; trattandosi di un microcontrollore, le differenze hardware impediscono al micro: bit di supportare Python nella sua interezza. MicroPython è dedicato al micro：bit ed è un'implementazione efficiente del linguaggio di programmazione Python3. Contiene una piccola parte della libreria standard di Python ed è ottimizzato per l'esecuzione sui microcontrollori micro:bit.

La versione di Python utilizzata dal BBC micro: bit è chiamata MicroPython. MicroPython è perfetto per chi desidera apprendere di più sulla programmazione; ti aiuta a programmare con una serie di frammenti di codice, oltre a varie grafiche e musiche predefinite.

Link per BBC microbit MicroPyth: [BBC micro:bit MicroPython ](https://microbit-micropython.readthedocs.io/en/latest/tutorials/introduction.html) 

**Python dispone di due tipi di editor: versione web e versione offline**

1\.  Versione web: [https://python.microbit.org/v/1.1](https://python.microbit.org/v/1.1)

![](./media/Python_693f76f5.png)

2\.  L'altro è anche il compilatore offline — Mu ![](./media/Python_153c77ed.png)

Sito ufficiale di Mu: [https://codewith.mu/](https://codewith.mu/)

### Mu

Mu, un editor di codice Python, è adatto ai principianti. Non supporta Windows a 32 bit.

1\.  **Scaricare Mu**

Clicca su “This PC” e fai clic con il tasto destro su Proprietà per verificare la versione del tuo computer.

![](./media/Python_3a58be54.png)

Controlla il tipo di sistema del tuo computer.

![](./media/Python_e774ae15.png)

Vai al link di MU: [https://codewith.mu/en/download](https://codewith.mu/en/download) per scaricare la versione corrispondente di Mu.

![](./media/Python_ceb4cfa6.png)

2\.  **Eseguire l'installazione**

Apri il file qui sotto

![](./media/Python_8bcfe24c.png)

Mac OSX: [https://codewith.mu/en/howto/1.1/install_macos](https://codewith.mu/en/howto/1.1/install_macos).

Linux: [https://codewith.mu/en/howto/1.2/install_linux](https://codewith.mu/en/howto/1.2/install_linux).

**Windows 10**

Vedrai comparire una finestra, quindi clicca su “More info”.

![](./media/Python_877beb7b.png)

Quindi clicca su “Run anyway”.

![](./media/Python_c87475e5.png)

3\. Contratto di licenza

Clicca su “Install”.

![](./media/Python_33f42b66.png)

![](./media/Python_f5c6698f.png)

Dopo l'installazione, clicca su “finish”.

![](./media/Python_c6ec7436.png)

4\. Avviare Mu

Successivamente, trovalo come nella figura seguente

![](./media/Python_c4adbdd1.png)

La sua interfaccia principale è mostrata come di seguito:

![](./media/Python_3697c0c7.png)

### Utilizzo delle modalità & barra dei menu

Imposta “<span style="color: rgb(255, 76, 65);">**Mode**</span>” su BBC micro:bit.

Nel menu, clicca su “**Mode**” per impostarlo su “**BBC micro：bit**”. La modalità micro:bit sa come interagire e connettersi a un micro:bit.

![](./media/Python_18512c7e.png)

Clicca per [Start with Mu](https://codewith.mu/en/tutorials/1.1/start).

### Come Mu importa una libreria sul Micro:bit

<span style="color: rgb(255, 76, 65);">**Prima di importare le librerie, dobbiamo caricare un codice .py (un codice vuoto va bene) sulla scheda micro:bit. Qui prendiamo come esempio un codice vuoto.**</span>

Collega la scheda al computer tramite cavo USB. Apri Mu e clicca su “Flash” per caricare il file .py (anche vuoto) sulla scheda.

![Img](./media/Python_611b2c4e.png)

In questo tutorial viene utilizzato il file di libreria "keyes_mecanum_Car_V2.py". Pertanto, importa il file di libreria "keyes_mecanum_Car_V2.py" nel micro:bit. Questo file contiene il metodo di controllo del Micro:bit 4WD Mecanum Robot Car V2.0.

La directory predefinita in cui Mu salva i file è “mu_code” nella directory principale della cartella utente.

Link di riferimento: [https://codewith.mu/en/tutorials/1.0/files](https://codewith.mu/en/tutorials/1.0/files)

**Metodi per trovare la cartella "mu_code":**

**Metodo Uno:**

Ad esempio, su un sistema Windows, supponiamo che il sistema sia installato sull'unità C del computer e che il nome utente sia "**Administrator**", allora il percorso della directory "**mu_code**" è "**C:\Users\Administrator\mu_ code**". Nei sistemi Linux, il percorso della directory "**mu_code**" è "**~/home/mu_code**".

Apri la cartella “**mu_code**”.

![](./media/Python_d271a924.png)

**Metodo Due:**

Cerca la cartella “mu_code” sul Disco (C:).

![Img](./media/Python_03ff037e.png)

![Img](./media/Python_54199d45.png)

Apri “mu_code”.

![Img](./media/Python_4841ca3f.png)

Il percorso della cartella dati in cui si trova il file di libreria “keyes_mecanum_Car.py” che forniamo è il seguente:

![Img](./media/Python_7adb2b68.png)

Copia il file di libreria “keyes_mecanum_Car.py” nella cartella “mu_code”。Quando la copia è completata, come mostrato di seguito:

![](./media/Python_d753d652.png)

Apri prima il software Mu e collega il micro:bit al tuo computer, quindi clicca sul pulsante "Files" e trascina il file di libreria "keyes_mecanum_Car.py" sul micro:bit.

![](./media/Python_aeaae2b7.png)

Dopo alcuni secondi, l'importazione è completata e puoi vederlo nella casella a sinistra.

![](./media/Python_2be967ca.png)