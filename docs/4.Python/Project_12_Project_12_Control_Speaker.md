### Progetto 12: Controllo dello speaker

1\.  **Descrizione**

Nei progetti precedenti abbiamo studiato rispettivamente il logo sensibile al tocco e lo speaker. In questo progetto combineremo questi due componenti per riprodurre musica.

2\.  **Componenti necessari**

|![](./media/Python_021507bd.png)|![](./media/Python_84cdea05.jpg)|
|-|-|
|Micro:bit main board \*1|USB cable\*1|


3\.  **Schema di collegamento**

Collegare il Micro:bit main board al computer tramite il cavo USB.

![](./media/Python_611b2c4e.png)

4\.  **Codice di prova**

Avviare il software Mu e aprire il file “Touch the Logo to control the speaker\.py” per importare il codice. È anche possibile inserire il codice direttamente nella finestra di modifica.

(**Nota: Tutte le parole e i simboli devono essere scritti in inglese**.)

![](./media/Python_600c8fa6.png)

```python
from microbit import *

import music

display.show(Image.MUSIC_QUAVER)

while True:

    if pin_logo.is_touched():
        music.play(music.BIRTHDAY)
```

Fare clic su “Check” per verificare eventuali errori nel codice. Il programma è sbagliato se vengono mostrati sottolineature e cursori.

![](./media/Python_dcc17127.png)

Se il codice è corretto, collegare il micro:bit al computer e fare clic su “Flash” per scaricare il codice sulla scheda micro:bit.

![](./media/Python_be3d4ee9.png)

5\.  **Risultato del test**

Dopo aver scaricato correttamente il codice sulla scheda, **alimentare tramite il cavo micro USB o un alimentatore esterno (portare l’interruttore DIP su ON)** e premere il pulsante di reset sul micro:bit.

![Img](./media/Python_bb3e1312.png)

Lo speaker riproduce la canzone “*Happy Birthday to You*” quando il logo viene toccato.

6\.  **Spiegazione del codice**

![Img](./media/Python_852be78f.png)

**Comunicazione wireless Bluetooth**

Il micro:bit dispone di un modulo Bluetooth a basso consumo per la comunicazione, ma ha 16 KB di RAM. Tuttavia, lo heap/stack BLE occupa 12 KB di RAM, pertanto non c’è spazio sufficiente per eseguire microPython.

Al momento, microPython non supporta il servizio Bluetooth.

[https://microbit-micropython.readthedocs.io/en/latest/ble.html](https://microbit-micropython.readthedocs.io/en/latest/ble.html)

I progetti precedenti sono un’introduzione ai sensori e ai moduli. Le lezioni successive sono più impegnative per i principianti.

(**Nota: Per evitare che la scheda micro:bit si bruci, scollegare il cavo micro USB e spegnere l’alimentazione della micro:bit motor driver base plate prima di installarla sulla scheda di espansione per auto e portare l’interruttore POWER su OFF. Analogamente, prima di rimuovere la scheda principale dalla scheda di espansione per auto, scollegare il cavo micro USB e spegnere l’alimentazione della micro:bit motor driver base plate.**)