## Progetto 11: Microfono

![](./media/Makecode_d2f14bdc.jpg)

[Click to download the code 1 for this lesson](./Code/Microphone.hex)

[Click to download the code 2 for this lesson](./Code/Microphone2.hex)

### (1)Descrizione del progetto:

La scheda principale Micro:bit main board V2 è dotata di un microfono che può misurare il volume dell’ambiente circostante. Quando battete le mani, il LED indicatore del microfono si accende. Poiché può misurare l’intensità del suono, è possibile realizzare una scala del rumore o un’illuminazione da disco che cambia con la musica. Il microfono è posizionato sul lato opposto rispetto al LED indicatore del microfono e vicino a dei fori che lasciano passare il suono. Quando la scheda rileva un suono, il LED indicatore si accende.

### (2)Componenti necessari:

Micro:bit main board V2

Cavo Micro USB

### (3)Codice di test 1:

Collegate il computer alla scheda micro:bit con un cavo Micro USB e programmate nell’editor MakeCode,

![](./media/Makecode_7c037c9b.gif)

Programma completo:

![](./media/Makecode_1ea97896.png)

### (4)Risultati del test 1:

Dopo aver caricato il codice, viene visualizzata un’icona grande a forma di cuore quando viene rilevato il suono ambientale, e un’icona a forma di cuore più piccola quando l’ambiente è silenzioso (Nota: suoni troppo deboli per essere rilevati non attiveranno la risposta).

![](./media/Makecode_facbbb50.gif)

### (5)Codice di test 2:

Collegate il computer alla scheda micro:bit con un cavo Micro USB e programmate nell’editor MakeCode,

![](./media/Makecode_68e37f22.gif)

Programma completo:

![](./media/Makecode_9851e889.png)

### (6)Risultati del test 2:

![](./media/Makecode_0b914334.gif)

Dopo aver caricato il codice, la matrice di punti pulsa in sincronia con le variazioni del suono. Premendo il tasto “A” viene visualizzato il valore numerico del suono corrente.