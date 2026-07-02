## Project 20：Bluetooth Multi-purpose Smart Car

### Project 20.1：Read Bluetooth Data

![](./media/Makecode_55b2424d.png)

1\. **Beschrijving**

De micro:bit hoofdbord heeft ingebouwde Bluetooth die kan worden gebruikt om ermee te communiceren. De Micro:bit kan ook via Bluetooth worden bestuurd of signalen terug naar een smartphone of computer verzenden. Deze Bluetooth kan communiceren met de Bluetooth in andere apparaten of met een Bluetooth-app om andere apparatuur te bedienen.

Het is compatibel met zowel Android- als iOS-systemen. We hebben twee Bluetooth-apps voor beide systemen ontworpen.

De verbinding van de Bluetooth op het bord met deze twee apps is vergelijkbaar. In deze les zullen we de functies van alle knoppen en patronen in de apps introduceren en de slimme auto via de Bluetooth-app bedienen.

2\. **Voorbereiding**

- Plaats het micro:bit-bord in de sleuf van de keyestudio 4WD Mecanum Robot Car V2.0

- Plaats batterijen in de batterijhouder

- Zet de aan/uit-schakelaar op ON

- Verbind de micro:bit met je computer via een USB-kabel

- Open de webversie van Makecode

**Als je ervoor kiest de code handmatig te slepen, moet je eerst de Bluetooth-extensiebibliotheek toevoegen. Klik op het tandwielpictogram (Settings) in de rechterbovenhoek, klik vervolgens op Extensions om naar het bibliotheekbestand-selectiescherm te gaan, en klik vervolgens op de "Bluetooth" extensiebibliotheek (als deze niet bestaat, zoek naar Bluetooth), zoals hieronder weergegeven:** 

![](./media/Makecode_4e308360.png)

Aangezien Bluetooth en de radio-extensie niet samen kunnen werken, zijn hun extensiebibliotheken niet compatibel.

Verwijder daarom andere extensies en voeg Bluetooth toe als het volgende promptvenster verschijnt.

![](./media/Makecode_aee56e76.png)

3\. **Testcode**

![](./media/Makecode_ac5ffe1a.png)

Klik op “JavaScript” om de bijbehorende JavaScript-code te bekijken:

![](./media/Makecode_24191138.png)

4\. **Testresultaat**

Als je blokken stap voor stap sleept, moet je na het voltooien van de testcode het volgende instellen.

![](./media/Makecode_01b256e5.png)

![](./media/Makecode_982334c8.png)

![](./media/Makecode_09767d5e.png)

Je kunt deze stap overslaan als je de testcode rechtstreeks importeert.

Na het instellen, download de code naar het micro:bit-bord, verwijder de USB-kabel niet. Vervolgens de app downloaden.

**Voor iOS-systeem:**

a\. Open App Store;

![](./media/Makecode_27924fdb.png)

b\. Zoek naar **mecanum_robot** en klik op “![](./media/Makecode_962a57f9.png)” om de Bluetooth-app mecanum_robot te downloaden;

c\. Na het downloaden van de APP, klik op "OPEN" of tik op de applicatie mecanum_robot op het telefoon-/iPad-startscherm om de APP te openen. Er verschijnt een dialoogvenster op de APP-interface; klik op "OK" in het dialoogvenster.

d\. Zet eerst de Bluetooth van de mobiele telefoon/iPad aan en klik vervolgens op de verbindingsknop (control) linksboven in de APP-interface om een Bluetooth-zoekopdracht uit te voeren. Klik in de zoekresultaten op "BCC micro:bit". Na enkele seconden is de Bluetooth verbonden.

**Voor Android-systeem:**

a\. Gebruik de scanfunctie in de browser om de QR-code te scannen en te identificeren

![](./media/Makecode_d9acbfab.png)

of voer de link in: [http://8.210.52.206/mecanum_robot.apk](http://8.210.52.206/mecanum_robot.apk) om te downloaden. Na succesvolle identificatie klik je op "go to website" om naar de downloadpagina mecanum_robot.apk te gaan, klik op "Download" om de applicatie mecanum_robot te downloaden.

b\. Klik op “Allow allow” om het installatiescherm te openen; klik op “install” om de app te installeren.

![](./media/Makecode_638d0a4a.png)

c\. Klik op "Open" of tik op de applicatie mecanum_robot op het startscherm van de telefoon om de APP te openen; er verschijnt een dialoogvenster. Klik in het dialoogvenster op "Allow" om de Bluetooth van de telefoon in te schakelen. Je kunt de Bluetooth van de telefoon ook inschakelen voordat je de APP opent.

![](./media/Makecode_c818fd71.png)

![](./media/Makecode_0c35f0dc.png)

d\. Klik op ![](./media/Makecode_d3f566b9.png) rechtsboven om naar Bluetooth te zoeken en klik op “connect”; enkele seconden later is de Bluetooth gekoppeld.

![](./media/Makecode_3d21cf87.png)

![](./media/Makecode_4a23b197.png)

Open CoolTerm, klik op Options om SerialPort te selecteren. Stel de COM-poort en de baudrate in op 115200. Klik op “OK” en “Connect”.

Richt op het micro:bit-bord en druk op de pictogrammen in de APP; de overeenkomstige tekens worden weergegeven in de CoolTerm-monitor.

![](./media/Makecode_0ed4a53e.png)

Door de test verkrijgen we de functies van elk pictogram, zoals hieronder weergegeven:

![](./media/Makecode_05c3d32b.jpg)

### Project 20.2：Multi-purpose Smart Car

![Img](./media/Makecode_ce6ec959.png)

1\. **Beschrijving**

In deze les zullen we de slimme auto besturen om multifunctionele taken uit te voeren.

2\. **Voorbereiding**

- Plaats het micro:bit-bord in de sleuf van de keyestudio 4WD Mecanum Robot Car V2.0

- Plaats batterijen in de batterijhouder

- Zet de aan/uit-schakelaar op ON

- Verbind de micro:bit met je computer via een USB-kabel

- Open de webversie van Makecode

**Stappen：** Klik op het tandwielpictogram (Settings) in de rechterbovenhoek, klik vervolgens op Extensions om naar het bibliotheekselectiescherm te gaan, en klik vervolgens op de "Bluetooth" extensiebibliotheek (als deze niet bestaat, zoek naar Bluetooth), zoals hieronder weergegeven: 

![](./media/Makecode_4e308360.png)

Aangezien Bluetooth en de radio-extensie niet samen kunnen werken, zijn hun extensiebibliotheken niet compatibel.

Verwijder daarom andere extensies en voeg Bluetooth toe als het volgende promptvenster verschijnt.

![](./media/Makecode_aee56e76.png)

3\. **Testcode**

Aangezien de code vrij lang is, wordt deze hier niet weergegeven. U kunt rechtstreeks naar het volgende pad gaan om de overeenkomstige code te vinden.

![Img](./media/Makecode_836c42ce.png)

Klik op “JavaScript” om de bijbehorende JavaScript-code te bekijken:

![](./media/Makecode_a73529d6.png)

4\. **Testresultaat**

Dit experiment combineert de vorige projecten zodat de auto acties uitvoert via Bluetooth.

Ga naar de Makecode online-editor→Projecting Settings→![](./media/Makecode_bef5b734.png), schakel “No Pairing....” in (u kunt deze stap overslaan als u de testcode rechtstreeks importeert)

Download de code naar het micro:bit-bord, zet POWER aan en verbind de Bluetooth; daarna kunt u de auto besturen via de Bluetooth-app mecanum_robot.

**Opmerking:** ![](./media/Makecode_81da4f47.jpg) wordt gebruikt om de snelheid aan te passen, en ![](./media/Makecode_adc3be60.jpg) kan alleen worden gesleept.