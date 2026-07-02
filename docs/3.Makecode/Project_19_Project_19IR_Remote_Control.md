## Project 19：IR Afstandsbediening

### Project 19.1：IR Afstandsbediening decoderen

![](./media/Makecode_3a3e9860.png)

1\. **Beschrijving**

Het is onmiskenbaar dat infrarood (IR) afstandsbedieningen alomtegenwoordig zijn in het dagelijks leven. Ze worden gebruikt om verschillende huishoudelijke apparaten te bedienen, zoals televisies, stereo's, videorecorders en satellietontvangers. Een IR-afstandsbediening bestaat uit een IR-zend- en een IR-ontvangstsysteem, dat wil zeggen een afstandsbediening, een IR-ontvangermodule en een microcontroller (single-chip) die kan decoderen.

![](./media/Makecode_9980b41f.png)

Het 38K IR-draaggolfsignaal dat door de afstandsbediening wordt uitgezonden, wordt gecodeerd door de coderingschip in de afstandsbediening. Het bestaat uit een sectie pilotcode, gebruikerscode, omgekeerde gebruikerscode, datacode en omgekeerde datacode. Het tijdsinterval van de puls wordt gebruikt om te onderscheiden of het een 0- of een 1-signaal is en de codering bestaat uit deze 0- en 1-signalen.

De gebruikerscode van dezelfde afstandsbediening blijft ongewijzigd. De datacode kan de toets onderscheiden.

Wanneer een knop van de afstandsbediening wordt ingedrukt, zendt de afstandsbediening een IR-draaggolfsignaal uit. Wanneer de IR-ontvanger het signaal ontvangt, decodeert het programma het draaggolfsignaal en bepaalt welke toets is ingedrukt. De MCU decodeert het ontvangen 01-signaal en bepaalt daarmee welke toets van de afstandsbediening is ingedrukt.

De infraroodontvanger die we gebruiken is een infraroodontvangermodule. Deze bestaat voornamelijk uit een IR-ontvangstkoppeling en is een apparaat dat ontvangst, versterking en demodulatie integreert. De interne IC heeft de demodulatie voltooid en kan de volledige keten van IR-ontvangst tot uitgang realiseren en is compatibel met TTL-signalen. Daarnaast is het geschikt voor IR-afstandsbediening en IR-gegevensoverdracht. De door de ontvanger vervaardigde IR-ontvangermodule heeft slechts drie pinnen: signaallijn, VCC en GND.

Volgens de bovenstaande afbeelding is de geïntegreerde poort van de IR-ontvanger verbonden met de P9 5V G-poort op de motorstuurprint en wordt deze aangestuurd door de P9 van de micro:bit.

2\. **Parameters:**

- Bedrijfsspanning: 3.3-5V（DC）

- Interface: 3PIN

- Uitgangssignaal: digitaal signaal

- Ontvangshoek: 90 graden

- Frequentie: 38khz

- Ontvangstafstand: ongeveer 5m

3\. **Voorbereiding**

- Steek de micro:bit-kaart in de sleuf van de keyestudio   4WD Mecanum Robot Car V2.0

- Plaats batterijen in de batterijhouder

- Zet de voedingsschakelaar in de stand ON

- Verbind de micro:bit via een USB-kabel met uw computer

- Open de webversie van Makecode


4\. **Testcode**

![](./media/Makecode_2e20f731.png)

Klik op “JavaScript" om over te schakelen naar de bijbehorende JavaScript-code:

![](./media/Makecode_87e18859.png)

**Code-uitleg:** Als de knoppen niet worden ingedrukt, toont de seriële monitor continu 0; wanneer ze worden ingedrukt, worden de overeenkomstige toetswaarden weergegeven.

**Opmerkingen：**

De afstandsbediening in deze kit bevat geen batterijen. We raden aan deze online te kopen. (batterijtype: CR2025).

Zorg ervoor dat de IR-afstandsbediening werkt voordat u test. Hier is een tip om dit te controleren:

Open de camera van de telefoon, richt de IR-afstandsbediening op de camera en druk op een knop. Als u een paars knipperlicht op de camerabeelden ziet, werkt de afstandsbediening.

5\. **Testresultaat**

Download de code naar de micro:bit-kaart en verwijder de USB-kabel niet. Klik![](./media/Makecode_e0580d78.png)

![](./media/Makecode_0d3198e0.png)

Richt de IR-afstandsbediening op de IR-ontvanger en druk op de knop; de seriële monitor toont de overeenkomstige toetswaarden, zoals hieronder weergegeven:

![](./media/Makecode_c7a33a4c.png)

Open CoolTerm, klik op Options om SerialPort te selecteren. Stel de COM-poort en de baudrate in op 115200. Klik op “OK” en “Connect”.

De CoolTerm-seriële monitor geeft de toetswaarde als volgt weer:

![Img](./media/Makecode_155c857a.png)

De toetswaarde wordt weergegeven ter referentie:

![](./media/Makecode_1fc0d9bb.jpg)

### Project 19.2：IR Afstandsbediening

![Img](./media/Makecode_643cb701.png)

1\. **Beschrijving**

In dit project combineren we de IR-afstandsbediening met het car shield om een IR-bedreven smart car te maken. Het principe is dat de beweging van de auto wordt geregeld door toetsensignalen van de IR-afstandsbediening naar het IR-ontvangermodule van het car shield te sturen.

2\. **Voorbereiding**

- Steek de micro:bit-kaart in de sleuf van de keyestudio   4WD Mecanum Robot Car V2.0

- Plaats batterijen in de batterijhouder

- Zet de voedingsschakelaar in de stand ON

- Verbind de micro:bit via een USB-kabel met uw computer

- Open de webversie van Makecode

**Opmerking:** De infraroodsensor en de infraroodafstandsbediening mogen niet worden gebruikt in omgevingen met infraroodinterferentie zoals direct zonlicht, omdat dit veel onzichtbaar licht bevat, zoals infrarood en ultraviolet. In een omgeving met fel zonlicht kunnen ze niet normaal werken.

3\. **Stroomschema**

![Img](./media/Makecode_e5f416e3.png)

4\. **Testcode**

![](./media/Makecode_22d06d74.png)

Klik op “JavaScript" om over te schakelen naar de bijbehorende JavaScript-code:

![](./media/Makecode_e68b6275.png)

![](./media/Makecode_94de6552.png)

5\. **Testresultaat**

Download de code naar de micro:bit-kaart en zet de POWER-schakelaar op ON.

Richt de IR-afstandsbediening op de micro:bit en druk op de knop om de smart car te bedienen.

![](./media/Makecode_d55474f3.png) de knop zorgt dat de smart car vooruit rijdt，![](./media/Makecode_5c8a6549.png) staat voor links afslaan，![](./media/Makecode_41116032.png) betekent rechts afslaan，![](./media/Makecode_369433f6.png) geeft achteruit aan，![](./media/Makecode_a8ef4b17.png) stopt de auto.

**Opmerking:** De afstand tussen de IR-afstandsbediening en de IR-ontvangskop van de smart car moet tijdens de test minder dan 5 m bedragen.

---