## Progetto 16：Motor

![](./media/Makecode_77f3b857.png)

1\.  **Descrizione**

La Keyestudio 4WD Mecanum Robot Car è dotata di 4 motori DC a riduzione, detti anche motori con riduttore, sviluppati a partire da un motore DC ordinario. È provvista di una scatola di riduzione abbinata che fornisce una velocità inferiore ma una coppia maggiore. Inoltre, rapporti di riduzione diversi della scatola possono fornire velocità e coppie differenti.

Il motore con riduttore è l'integrazione di motoriduttore e motore, ampiamente applicato nell'industria siderurgica e meccanica.

Lo shield driver per motore micro:bit è dotato di un chip DRV8833. Per risparmiare risorse delle porte IO, controlliamo la direzione di rotazione e la velocità dei 4 motori DC con riduttore tramite il chip DRV8833.

![Img](./media/Makecode_4c9781dc.png)

Front

![](./media/Makecode_4919ce3b.png)

Back

![](./media/Makecode_59c34b6e.png)

STC8G1K08 Chip circuit

![](./media/Makecode_8874ded0.png)

HR8833 Motor driver circuit

2\.  **Preparazione**

- Inserire la scheda micro:bit nello slot della keyestudio 4WD Mecanum Robot Car V2.0

- Inserire le batterie nel portabatterie

- Portare l'interruttore di alimentazione su ON

- Collegare il micro:bit al computer tramite un cavo USB

- Aprire la versione Web di Makecode

3\.  **Test Code1**

![](./media/Makecode_3a759dd8.png)

Cliccare su“JavaScript" per visualizzare il codice JavaScript corrispondente: 

![](./media/Makecode_242ba6ca.png)

4\.  **Risultato del test1**

Scaricare il codice 1 sulla scheda micro:bit, portare l'interruttore POWER su ON. L'auto intelligente procede in avanti per 2s e si ferma per 2s.

5\.  **Test Code2**

![](./media/Makecode_a3a9d39a.png)

![Img](./media/Makecode_4eb6b574.png)

Cliccare su“JavaScript" per visualizzare il codice JavaScript corrispondente: 

![](./media/Makecode_ee70b846.png)

6\.  **Risultato del test2**

Scaricare il codice 2 sulla scheda micro:bit: l'auto procede in avanti per 2s, retrocede per 2s, svolta a sinistra per 2s, svolta a destra per 2s, si ferma per 2s e ripete questo schema.