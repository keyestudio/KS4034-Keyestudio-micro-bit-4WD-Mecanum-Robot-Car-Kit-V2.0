## Progetto 20：Bluetooth Multi-purpose Smart Car

### Progetto 20.1：Read Bluetooth Data

![](./media/Makecode_55b2424d.png)

1\. **Descrizione**

La scheda principale micro:bit è dotata di Bluetooth integrato che può essere utilizzato per comunicare con essa. Inoltre, il Micro:bit può essere controllato via Bluetooth o trasmettere segnali a smartphone o computer tramite esso. Questo Bluetooth può comunicare con il Bluetooth presente in altri dispositivi o con un'app Bluetooth per controllare altre apparecchiature.

È compatibile sia con Android che con iOS. Abbiamo progettato due app Bluetooth per entrambi i sistemi.

La connessione del Bluetooth della scheda con queste due app è simile. In questa lezione introdurremo le funzioni di tutti i tasti e dei modelli nelle app e controlleremo l'auto smart tramite l'app Bluetooth.

2\. **Preparazione**

- Inserire la scheda micro:bit nello slot del keyestudio 4WD Mecanum Robot Car V2.0

- Inserire le batterie nel vano batteria

- Portare l'interruttore di alimentazione su ON

- Collegare il micro:bit al computer tramite un cavo USB

- Aprire la versione Web di Makecode

**Se scegli di trascinare il codice manualmente, è necessario aggiungere prima la libreria di estensione Bluetooth. Fare clic sull'icona dell'ingranaggio (Settings) nell'angolo in alto a destra, quindi su Extensions per accedere alla schermata di selezione delle librerie e quindi fare clic sulla libreria di estensione "Bluetooth" (se non esiste, cercare Bluetooth), come mostrato di seguito:** 

![](./media/Makecode_4e308360.png)

Poiché Bluetooth e l'estensione radio non possono funzionare insieme, le loro librerie di estensione non sono compatibili.

Pertanto, rimuovere le estensioni e aggiungere Bluetooth se viene visualizzata la seguente finestra di avviso.

![](./media/Makecode_aee56e76.png)

3\. **Codice di test**

![](./media/Makecode_ac5ffe1a.png)

Fare clic su “JavaScript” per visualizzare il codice JavaScript corrispondente:

![](./media/Makecode_24191138.png)

4\. **Risultato del test**

Se trascinate i blocchi passo dopo passo, è necessario impostare come segue dopo aver completato il codice di test.

![](./media/Makecode_01b256e5.png)

![](./media/Makecode_982334c8.png)

![](./media/Makecode_09767d5e.png)

Tuttavia, è possibile saltare questo passaggio se si importa direttamente il codice di test.

Dopo le impostazioni, scaricare il codice sulla scheda micro:bit, non staccare il cavo USB. Successivamente scaricare l'app.

**Per il sistema iOS:**

a\. Aprire l'App Store;

![](./media/Makecode_27924fdb.png)

b\. Cercare **mecanum_robot** e fare clic su “![](./media/Makecode_962a57f9.png)” per scaricare l'app Bluetooth mecanum_robot;

c\. Dopo il download dell'APP, fare clic su "OPEN" o toccare l'app mecanum_robot sul desktop del telefono/iPad per aprire l'APP. Apparirà una finestra di dialogo sull'interfaccia dell'APP; fare clic su "OK" nella finestra di dialogo.

d\. Prima attivare il Bluetooth del telefono/iPad, quindi fare clic sul pulsante di connessione (control) in alto a sinistra dell'interfaccia dell'APP per eseguire la ricerca Bluetooth. Nei risultati della ricerca fare clic su "BCC micro:bit". Dopo pochi secondi il Bluetooth sarà connesso.

**Per il sistema Android:**

a\. Usare la funzione di scansione del browser per scansionare e identificare il codice QR

![](./media/Makecode_d9acbfab.png)

oppure inserire il link: [http://8.210.52.206/mecanum_robot.apk](http://8.210.52.206/mecanum_robot.apk) per scaricarlo. Dopo l'identificazione, fare clic su "go to website" per entrare nella pagina di download mecanum_robot.apk, fare clic su "Download" per scaricare l'applicazione mecanum_robot.

b\. Fare clic su “Allow allow” per entrare nella schermata di installazione; fare clic su “install” per installare l'app.

![](./media/Makecode_638d0a4a.png)

c\. Fare clic su "Open" o toccare l'app mecanum_robot sul desktop del telefono per aprire l'APP; apparirà una finestra di dialogo. Nella finestra di dialogo fare clic su "Allow" per attivare il Bluetooth del telefono. È anche possibile attivare il Bluetooth del telefono prima di aprire l'APP.

![](./media/Makecode_c818fd71.png)

![](./media/Makecode_0c35f0dc.png)

d\. Fare clic su ![](./media/Makecode_d3f566b9.png) in alto a destra per cercare il Bluetooth e fare clic su “connect”; dopo alcuni secondi il Bluetooth sarà abbinato.

![](./media/Makecode_3d21cf87.png)

![](./media/Makecode_4a23b197.png)

Aprire CoolTerm, fare clic su Options per selezionare SerialPort. Impostare la porta COM e la velocità 115200 baud. Fare clic su “OK” e “Connect”.

Puntare la scheda micro:bit e premere le icone nell'APP; i caratteri corrispondenti vengono visualizzati nel monitor di CoolTerm.

![](./media/Makecode_0ed4a53e.png)

Attraverso il test, otteniamo le funzioni di ogni icona, come mostrato di seguito:

![](./media/Makecode_05c3d32b.jpg)

### Progetto 20.2：Multi-purpose Smart Car

![Img](./media/Makecode_ce6ec959.png)

1\. **Descrizione**

In questa lezione controlleremo la smart car per eseguire funzioni multiuso.

2\. **Preparazione**

- Inserire la scheda micro:bit nello slot del keyestudio 4WD Mecanum Robot Car V2.0

- Inserire le batterie nel vano batteria

- Portare l'interruttore di alimentazione su ON

- Collegare il micro:bit al computer tramite un cavo USB

- Aprire la versione Web di Makecode

**Passaggi：** Fare clic sull'icona dell'ingranaggio (Settings) in alto a destra, quindi su Extensions per accedere alla schermata di selezione delle librerie e quindi fare clic sulla libreria di estensione "Bluetooth" (se non esiste, cercare Bluetooth), come mostrato di seguito: 

![](./media/Makecode_4e308360.png)

Poiché Bluetooth e l'estensione radio non possono funzionare insieme, le loro librerie di estensione non sono compatibili.

Pertanto, rimuovere le estensioni e aggiungere Bluetooth se viene visualizzata la seguente finestra di avviso.

![](./media/Makecode_aee56e76.png)

3\. **Codice di test**

Poiché il codice è piuttosto lungo, non verrà visualizzato qui. È possibile andare direttamente al percorso seguente per trovare il codice corrispondente.

![Img](./media/Makecode_836c42ce.png)

Fare clic su “JavaScript” per visualizzare il codice JavaScript corrispondente :

![](./media/Makecode_a73529d6.png)

4\. **Risultato del test**

Questo esperimento combina i progetti precedenti per far eseguire all'auto azioni tramite Bluetooth.

Aprire l'editor online Makecode → Projecting Settings → ![](./media/Makecode_bef5b734.png), abilitare “No Pairing....” (è possibile saltare questo passaggio se si importa direttamente il codice di test)

Scaricare il codice sulla scheda micro:bit, portare POWER su ON e connettere il Bluetooth, quindi è possibile controllare l'auto tramite l'app Bluetooth mecanum_robot.

**Nota:** ![](./media/Makecode_81da4f47.jpg) serve per regolare la velocità, e ![](./media/Makecode_adc3be60.jpg) può solo essere trascinato.