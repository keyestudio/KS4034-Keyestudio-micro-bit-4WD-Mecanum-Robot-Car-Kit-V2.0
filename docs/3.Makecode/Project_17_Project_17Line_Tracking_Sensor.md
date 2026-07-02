## Project 17：Line Tracking Sensor

### Project 17.1：Detect Line Tracking Sensor

![](./media/Makecode_ea7f6c8c.png)

1\. **Beschrijving**

De motorcontroller van de Keyestudio 4WD Mecanum Robot Car wordt geleverd met een 3-kanaals lijnvolgsensor, die gebruikmaakt van TCRT5000 IR-modules en 3 potentiometers.

De TCRT5000 IR-module bevat een IR-zender en een IR-ontvanger. Wanneer de infraroodsignalen van de zender via reflectie door de ontvanger worden opgevangen, verandert de weerstand van de ontvanger, wat zich doorgaans vertaalt in een spanningsverandering in het circuit.  

De weerstand varieert afhankelijk van de intensiteit van de infraroodsignalen die door de ontvanger worden ontvangen, wat vaak afhankelijk is van de kleur van het reflecterende oppervlak en de afstand tussen dat oppervlak en de ontvanger. Bij detectie is zwart actief op hoog niveau en wit actief op laag niveau. 

2\.  **Werkingsprincipe**

Als de auto over een witte ondergrond rijdt, zendt de onder de auto geplaatste IR-zender infraroodsignalen om de ondergrond te detecteren en de IR-ontvanger ontvangt en retourneert de signalen. Vervolgens geeft de uitgang een laag niveau (0) af; wanneer hij zwarte lijnen detecteert, geeft hij een hoog niveau (1) af.

Na het plaatsen van een wit vel papier onder de 4WD Mecanum Robot Car draaien we de potentiometers van de 3-wegs volgensor. Wanneer het indicatorlampje op het sensormodule brandt, til dan de auto op zodat de twee wielen van de 4WD Mecanum Robot Car vrij draaien. De hoogte van het witte papier is ongeveer 1,5 cm; wanneer het indicatorlampje van het sensormodule uitgaat, is de gevoeligheid ingesteld.

3\.  **Voorbereiding**

- Steek de micro:bit-kaart in de sleuf van de keyestudio 4WD Mecanum Robot Car V2.0

- Plaats batterijen in de batterijhouder

- Zet de voedingsschakelaar op ON

- Verbind de micro:bit met uw computer via een USB-kabel

- Open de webversie van Makecode

4\.  **Testcode**

![](./media/Makecode_3683d83f.png)

Klik op “JavaScript” om de bijbehorende JavaScript-code te bekijken: 

![](./media/Makecode_4b440616.png)

5\.  **Testresultaat**

Download de code naar de micro:bit-kaart en zet de POWER-schakelaar op ON. 

Open CoolTerm, klik op Options om SerialPort te selecteren. Stel de COM-poort in en de baudrate op 115200. Klik op “OK” en “Connect”.

![](./media/Makecode_ea164439.png)

![](./media/Makecode_b3a18bca.png)

![](./media/Makecode_f78128c1.png)

![](./media/Makecode_13238e98.png)

De CoolTerm-seriemonitor toont de digitale signalen die door de lijnvolgsensoren worden gelezen.

![](./media/Makecode_0141051a.png)

### Project 17.2：Tracking Smart Car

![Img](./media/Makecode_547634e4.png)

1\. **Beschrijving**

In deze les combineren we een lijnvolgsensor met een motor om een lijnvolgend smartcar te maken.

De micro:bit-kaart analyseert de signalen en bestuurt de smartcar om de lijnvolgfunctie te demonstreren.

2\. **Werkingsprincipe**

De smartcar zal verschillende bewegingen uitvoeren afhankelijk van de waarden die door de 3-kanaals lijnvolgsensor worden ontvangen.

![Img](./media/Makecode_bbccdb34.png)

3\. **Voorbereiding**

- Steek de micro:bit-kaart in de sleuf van de keyestudio 4WD Mecanum Robot Car V2.0

- Plaats batterijen in de batterijhouder

- Zet de voedingsschakelaar op ON

- Verbind de micro:bit met uw computer via een USB-kabel

- Open de webversie van Makecode

**Waarschuwing:** De 3-weg volgensor moet worden gebruikt in omgevingen zonder infraroodinterferentie, zoals direct zonlicht. Zonlicht bevat veel onzichtbaar licht, zoals infrarood en ultraviolet. In een omgeving met sterke zonlicht kan de 3-weg volgensor niet correct werken.

4\.**Stroomschema**

![Img](./media/Makecode_70f1fd80.png)


5\.  **Testcode**

![](./media/Makecode_4b104155.png)

![Img](./media/Makecode_d36220cf.png)

![Img](./media/Makecode_4fff0a27.png)

![Img](./media/Makecode_ca91a31f.png)


Klik op “JavaScript” om de bijbehorende JavaScript-code te bekijken:

![](./media/Makecode_f5caa06a.png)

![](./media/Makecode_8f5f07ec.png)

5\. **Testresultaat**

Download de code naar de micro:bit en zet POWER op ON; de lijnvolgende auto rijdt vooruit langs de zwarte lijn.

**Opmerking:** zet de schakelaar aan de achterkant van de micro:bit-auto aan, de breedte van de zwarte lijn moet groter zijn dan de breedte van de lijnvolgsensor.

Vermijd het testen van de smartcar onder fel licht.