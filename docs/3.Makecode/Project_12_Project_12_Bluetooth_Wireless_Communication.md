## Project 12: Bluetooth Draadloze Communicatie

![](./media/Makecode_041ff91a.jpg)

### (1)Projectbeschrijving:

Opmerking: Deze les is gericht op het uitleggen hoe code via Bluetooth met een app geüpload wordt, dus er wordt geen code geleverd. Volg de stappen in de geanimeerde gif.

De Micro: Bit main board V2 is uitgerust met een nRF52833-processor (met een ingebouwd BLE (Bluetooth Low Energy)-apparaat, Bluetooth 5.1) en een 2,4 GHz-antenne voor Bluetooth-draadloze communicatie en 2,4 GHz-draadloze communicatie. Met hun hulp kan de board communiceren met verschillende Bluetooth-apparaten, inclusief smartphones en tablets.

In dit project concentreren we ons voornamelijk op de Bluetooth-draadloze communicatiefunctie van deze main board. Verbonden via Bluetooth kan het code of signalen verzenden. Hiervoor moeten we een Apple-apparaat (een telefoon of een iPad) met de board verbinden.

Aangezien het instellen van Android-telefoons voor draadloze overdracht vergelijkbaar is met dat van Apple-apparaten, hoeft dit niet opnieuw te worden toegelicht.

### (2) Voorbereiding

Sluit de Micro:bit main board V2 aan op uw computer via de Micro USB-kabel.

Een Apple-apparaat (een telefoon of een iPad) of een Android-apparaat;

### (3) Installeer Micro:bit:

For Android

![](./media/Makecode_0cf9abf0.gif)

For ios

![](./media/Makecode_5937459b.gif)

(4)Testcode:

Vervolgens gebruiken we onze telefoons om code te schrijven en verbinding te maken via Bluetooth (Opmerking: het proces is identiek voor zowel Android- als iOS-apparaten; deze demonstratie gebruikt een Android-telefoon).

1、Open de software en verbind met Bluetooth.

![](./media/Makecode_dcb2416a.gif)

2、Druk achtereenvolgens op Microbit's knop A, knop B en de resetknop aan de achterkant. De main board zal dan een pictogram weergeven.

![](./media/Makecode_6985c2b1.gif)

3、Voer het patroon in dat in stap twee wordt weergegeven in de telefooninterface.

![](./media/Makecode_9095fb35.gif)

Code schrijven en uploaden

1、Ga naar de code-programmeerinterface en schrijf een code.

![](./media/Makecode_b7c8c1ca.gif)

2、Druk achtereenvolgens op knop A, knop B en de resetknop. (Opmerking: deze procedure moet elke keer worden herhaald wanneer code via de app wordt geüpload.)

 ![](./media/Makecode_86ab2b39.gif)

3、Nadat u hebt bevestigd dat het Microbit-pictogram overeenkomt met het pictogram dat op uw telefoon wordt weergegeven, klikt u eenvoudig op “Next.”

![](./media/Makecode_f3c17f45.gif)

Tot slot ziet u de Microbit-board het patroon uit de code weergeven.

Hiermee hebben we het proces van het uploaden van code naar de telefoon voltooid. Het is belangrijk op te merken:

1. Om de telefoon met de Microbit-board te verbinden, drukt u achtereenvolgens op de A-, B- en Reset-knoppen. Het puntmatrixdisplay zal dan een patroon tonen, dat in de telefoon moet worden ingevoerd.
2. De Microbit-board kan worden gevoed via een USB-kabel of door 3V aan te leggen op de voedingsingang van de board via een batterijpack. Opmerking: de spanning mag niet hoger zijn dan 3V; overschrijding van deze limiet kan de board beschadigen.