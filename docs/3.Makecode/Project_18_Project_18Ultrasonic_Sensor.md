## Project 18：Ultrasone sensor

### Project 18.1：Ultrasone afstandsmeting

1\.  **Beschrijving**

De ultrasone sensor gebruikt sonar om, net als vleermuizen, de afstand tot een object te bepalen. Hij biedt uitstekende contactloze afstandsdetectie met hoge nauwkeurigheid en stabiele metingen in een gebruiksvriendelijke behuizing. Het bevat zowel ultrasone zender- als ontvangermodules.

De ultrasone sensor wordt in een breed scala aan elektronica-projecten gebruikt voor het creëren van toepassingen voor obstakeldetectie en afstandsmeting, evenals voor diverse andere toepassingen.

![](./media/Makecode_0180b169.png)

Het ultrasone module zendt ultrasone golven uit na trigger-signalen. Wanneer de ultrasone golven een object treffen en teruggekaatst worden, geeft het module een echo-signaal uit, zodat de afstand tot het object kan worden bepaald uit het tijdsverschil tussen trigger-signaal (TRIG) en echo-signaal (ECHO).

Zoals op de afbeelding te zien is, lijkt het op twee ogen. De ene is de zendzijde, de andere de ontvangzijde.

Volgens het bovenstaande aansluitdiagram is de geïntegreerde poort van het ultrasone sensormodule verbonden met de 5V G P15 P16-poort op de micro:bit motor driver basisplaat. De Trig (T)-pin wordt aangestuurd door P15 van de micro:bit en de Echo (E)-pin is aangesloten op P16.

![](./media/Makecode_1174e0ec.png)

2\. **Werkingsprincipe**

![](./media/Makecode_8ff02741.png)

(1) Trek TRIG naar laag en genereer vervolgens een hoog signaal van minimaal 10 µs;

(2) Na het triggeren zal het module automatisch acht pulsen van 40 kHz uitzenden en detecteren of er een signaalretour is;

(3) Als er een signaalretour is, geeft ECHO (E) een hoog niveau uit; de duur van dat hoge niveau is de tijd van zenden tot ontvangen van de ultrasone golven. Dan testafstand = hoog-niveau duur \*340m/s\*0.5. 

3\. **Parameters**

- Werkspanning: 3-5.5V (DC)

- Stroomverbruik: 15mA

- Werkingfrequentie: 40 kHz

- Maximale detectieafstand: ongeveer 3 m

- Minimale detectieafstand: 2-3 cm

- Nauwkeurigheid: tot 0,2 cm

- Detectiehoek: minder dan 15 graden

- Ingang triggerpuls: 10 µs TTL-niveau

- Uitgang echo signaal: TTL-niveau signaal (hoog), evenredig met de afstand

4\. **Voorbereiding**

- Plaats de micro:bit kaart in de sleuf van de keyestudio 4WD Mecanum Robot Car V2.0

- Plaats batterijen in de batterijhouder

- Zet de stroomschakelaar op ON

- Verbind de micro:bit met uw computer via een USB-kabel

- Open de webversie van Makecode


5\. **Testcode**

![](./media/Makecode_497760b1.png)

Klik op “JavaScript” om de bijbehorende JavaScript-code te bekijken:

![](./media/Makecode_387f3243.png)

6\.  **Testresultaat**

Download de code naar de micro:bit, houd de USB-kabel aangesloten en zet de POWER-schakelaar op ON. De afstandswaarde wordt op de monitor weergegeven.

![](./media/Makecode_2cd74c16.png)

De monitor toont de afstand tussen het obstakel en de ultrasone sensor (zoals hieronder weergegeven).

![](./media/Makecode_422adea3.png)

Open CoolTerm, klik op Options om SerialPort te selecteren. Stel de COM-poort en baudrate in op 115200 (de baudrate van de USB-seriële communicatie van de Micro:bit is tijdens de test 115200). Klik op “OK” en “Connect”.

De CoolTerm seriële monitor toont de afstandswaarde als volgt:

![](./media/Makecode_69b06998.png)

### Project 18.2：Ultrasone uitwijking

![Img](./media/Makecode_13139b46.png)

1\. **Beschrijving**

In dit project integreren we een ultrasone sensor en een auto om een ultrasone uitwijkauto te maken.

Het principe is om de afstand tussen de auto en het obstakel te detecteren via de ultrasone sensor om zo de beweging van de slimme auto te regelen.

2\.  **Voorbereiding**

- Plaats de micro:bit kaart in de sleuf van de keyestudio 4WD Mecanum Robot Car V2.0

- Plaats batterijen in de batterijhouder

- Zet de stroomschakelaar op ON

- Verbind de micro:bit met uw computer via een USB-kabel

- Open de webversie van Makecode

3\.  **Stroomschema**

![Img](./media/Makecode_e2adae4b.png)

4\.  **Testcode**

![](./media/Makecode_05a4740b.png)

![Img](./media/Makecode_d7879887.png)

Klik op “JavaScript” om de bijbehorende JavaScript-code te bekijken:

![](./media/Makecode_c8f86a24.png)

![](./media/Makecode_13baf1d6.png)

5\.  **Testresultaat**

Download de code naar de micro:bit, zet het apparaat aan en zet de POWER op ON. Wanneer de afstand tot het obstakel groter is dan 20 cm, rijdt de auto vooruit; anders draait de slimme auto naar links.

### Project 18.3：Ultrasoon volgen

![Img](./media/Makecode_d17a7889.png)

1\. **Beschrijving**

In de vorige les hebben we het basisprincipe van de lijnvolgsensor geleerd. Vervolgens combineren we de ultrasone sensor met de auto om een ultrasone volgauto te maken.

De ultrasone sensor detecteert de afstand van het obstakel en bestuurt de bewegingsstatus van de auto.

2\. **Voorbereiding**

- Plaats de micro:bit kaart in de sleuf van de keyestudio 4WD Mecanum Robot Car V2.0

- Plaats batterijen in de batterijhouder

- Zet de stroomschakelaar op ON

- Verbind de micro:bit met uw computer via een USB-kabel

- Open de webversie van Makecode

3\. **Stroomschema**

![Img](./media/Makecode_f5026aed.png)

4\. **Testcode**

![](./media/Makecode_03b95531.png)

Klik op “JavaScript” om de bijbehorende JavaScript-code te bekijken:

![](./media/Makecode_a93c8245.png)

5\. **Testresultaat**

Download de code naar de micro:bit, zet de POWER-schakelaar op ON op het shield; de slimme auto kan het obstakel volgen en zich verplaatsen.