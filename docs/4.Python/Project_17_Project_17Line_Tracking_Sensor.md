### Project 17：Lijnvolgsensor

#### Project 17.1：Lijnvolgsensor detecteren

![](./media/Python_ea7f6c8c.png)

1\. **Beschrijving**

De motorbesturingsprint van de Keyestudio 4WD Mecanum Robot Car heeft een 3-kanaals lijnvolgsensor, die TCRT5000 IR-buizen en 3 potentiometers gebruikt.

De TCRT5000 IR-buis bevat een IR-zendbuis en een IR-ontvangbuis. Wanneer de infraroodsignalenn van de zendbuis via reflectie door de ontvangbuis worden opgevangen, verandert de weerstand van de ontvangbuis, wat doorgaans wordt weergegeven als een spanningsverandering in het circuit.

De weerstand varieert afhankelijk van de intensiteit van de infraroodsignalen die door de ontvangbuis worden ontvangen, wat vaak afhangt van de kleur van het reflecterende oppervlak en de afstand tussen dat oppervlak en de ontvangbuis. Bij detectie geldt dat zwart een actief hoog niveau is en wit een actief laag niveau.

2\.  **Werking**

Als de auto over een witte ondergrond rijdt, straalt de onder de auto gemonteerde IR-zendbuis infrarood uit om de ondergrond te detecteren en de ontvangbuis ontvangt de teruggekaatste signalen. De uitgang geeft dan een laag niveau (0); wanneer er zwarte lijnen worden gedetecteerd, geeft de uitgang een hoog niveau (1).

De geïntegreerde 3-kanaals volgensor-poort op de 4WD Mecanum Robot Car is verbonden met de aansluitingen G, 5V, P10, P4 en P3 op de micro:bit uitbreidingsplaat, en wordt bestuurd door P10, P4 en P3 van de micro:bit. De linker TCRT5000 IR-paarbuis op de sensor wordt door P3 aangestuurd, de middelste door P4 en de rechter door P10.

Plaats een wit papier onder de 4WD Mecanum Robot Car en draai aan de potentiometers van de 3-weg volgensor. Wanneer het indicatielampje op het sensormodule brandt, til dan de auto op zodat de twee wielen van de 4WD Mecanum Robot Car vrij komen. De hoogte (afstand tussen sensor en papier) is ongeveer 1,5 cm; wanneer het indicatielampje op het sensormodule uitgaat, is de gevoeligheid goed afgesteld.

**Opmerking: omdat de 5x5 dot-matrix de pinnen P3, P4, P6, P7 en P10 gebruikt, moeten we de dot-matrix functie uitschakelen wanneer we de lijnvolgsensor gebruiken.**

3\.  **Voorbereiding**

- Steek de micro:bit in de houder van de keyestudio 4WD Mecanum Robot Car V2.0

- Plaats batterijen in de batterijhouder

- Zet de aan/uit-schakelaar op ON

- Verbind de micro:bit met de computer via een USB-kabel

- Open de offline versie van Mu.

4\.  **Testcode**

Open de Mu-software en open het bestand “Line tracking detection.py” om de code te laden. Je kunt de code ook zelf in het bewerkingsvenster invoeren.

(**Opmerking: alle Engelse woorden en symbolen moeten in het Engels geschreven zijn**.)

Klik op “Check” om fouten in de code te controleren. Het programma bevat fouten als er onderstrepingen en cursors worden weergegeven.

Als de code correct is, verbind de micro:bit met je computer en klik op “Flash” om de code naar de micro:bit te downloaden.

![](./media/Python_2c7b1c21.png)

```python
from microbit import *
display.off()

val_L = 0
val_C = 0
val_R = 0
while True:
    val_L = pin3.read_digital()
    val_C = pin4.read_digital()
    val_R = pin10.read_digital()
    print("digital signal:", end = ' ')
    print(val_L, end = ' ')
    print(val_C, end = ' ')
    print(val_R)
    sleep(200)
```

5\.  **Testresultaat**

Nadat de code succesvol naar het board is gedownload en de USB-kabel is aangesloten, klik je op “REPL” en druk je vervolgens op de resetknop.

![Img](./media/Python_bb3e1312.png)

De door de linker TCRT5000 IR-buis gedetecteerde waarden worden in de monitor weergegeven.

Wanneer de linker TCRT5000 IR-buis een wit object detecteert, wordt 0 weergegeven en brandt het linker indicatielampje; wanneer er alleen een zwart object wordt gedetecteerd, wordt 1 weergegeven en is het indicatielampje uit, zoals hieronder weergegeven:

![](./media/Python_6a25b450.png)

6\.  **Code-uitleg**

![Img](./media/Python_5dad345e.png)


#### Project 17.2：Lijnvolgende Smart Car

![](./media/Python_f0b62e0f.jpg)

1\. Beschrijving

In deze les combineren we een lijnvolgsensor met een motor om een lijnvolgende smart car te maken.

De micro:bit zal de signalen analyseren en de smart car aansturen om de lijnvolgfunctie uit te voeren.

2\.  **Werking**

De smart car voert verschillende bewegingen uit afhankelijk van de waarden die door de 3-kanaals lijnvolgsensor worden ontvangen.

![Img](./media/Python_e672c637.png)

3\.  **Voorbereiding**

- Steek de micro:bit in de houder van de keyestudio 4WD Mecanum Robot Car V2.0

- Plaats batterijen in de batterijhouder

- Zet de aan/uit-schakelaar op ON

- Verbind de micro:bit met de computer via een USB-kabel

- Open de offline versie van Mu.

**Waarschuwing:** De 3-weg volgensor moet worden gebruikt in een omgeving zonder infraroodinterferentie zoals direct zonlicht. Zonlicht bevat veel onzichtbaar licht, zoals infrarood en ultraviolet. In een omgeving met sterk zonlicht kan de 3-weg volgensor niet goed werken.

4\.  **Stroomschema**

![Img](./media/Python_47856ed2.png)

5\.  **Testcode**

Open de Mu-software en open het bestand “Line tracking car.py” om de code te laden. Je kunt de code ook zelf in het bewerkingsvenster invoeren.

(**Opmerking: alle Engelse woorden en symbolen moeten in het Engels geschreven zijn**.)

Klik op “Files” om het bibliotheekbestand “keyes_mecanum_Car.py” naar de micro:bit te importeren.

Klik op “Check” om fouten in de code te controleren. Het programma bevat fouten als er onderstrepingen en cursors worden weergegeven.

Als de code correct is, verbind de micro:bit met je computer en klik op “Flash” om de code naar de micro:bit te downloaden.

![](./media/Python_bd395cbe.png)

```python
from microbit import *
from keyes_mecanum_Car_V2 import *
mecanumCar = Mecanum_Car_Driver_V2()
display.off()

val_L = 0
val_C = 0
val_R = 0
while True:
    val_L = pin3.read_digital()
    val_C = pin4.read_digital()
    val_R = pin10.read_digital()
    if val_C == 0:
        if val_L == 0 and val_R == 1:
            mecanumCar.Motor_Upper_L(1, 80)
            mecanumCar.Motor_Lower_L(1, 80)
            mecanumCar.Motor_Upper_R(0, 80)
            mecanumCar.Motor_Lower_R(0, 80)
        elif val_L == 1 and val_R == 0:
            mecanumCar.Motor_Upper_L(0, 80)
            mecanumCar.Motor_Lower_L(0, 80)
            mecanumCar.Motor_Upper_R(1, 80)
            mecanumCar.Motor_Lower_R(1, 80)
        else:
            mecanumCar.Motor_Upper_L(0, 0)
            mecanumCar.Motor_Lower_L(0, 0)
            mecanumCar.Motor_Upper_R(0, 0)
            mecanumCar.Motor_Lower_R(0, 0)
    else :
        if val_L == 0 and val_R == 1:
            mecanumCar.Motor_Upper_L(1, 80)
            mecanumCar.Motor_Lower_L(1, 80)
            mecanumCar.Motor_Upper_R(0, 80)
            mecanumCar.Motor_Lower_R(0, 80)
        elif val_L == 1 and val_R == 0:
            mecanumCar.Motor_Upper_L(0, 80)
            mecanumCar.Motor_Lower_L(0, 80)
            mecanumCar.Motor_Upper_R(1, 80)
            mecanumCar.Motor_Lower_R(1, 80)
        else:
            mecanumCar.Motor_Upper_L(1, 80)
            mecanumCar.Motor_Lower_L(1, 80)
            mecanumCar.Motor_Upper_R(1, 80)
            mecanumCar.Motor_Lower_R(1, 80)
```

6\.  **Testresultaat**

Nadat de code succesvol naar het board is gedownload, zorg voor externe voeding (zet de DIP-schakelaar op ON) en druk op de resetknop van de micro:bit.

![Img](./media/Python_bb3e1312.png)

De lijnvolgende auto rijdt vooruit langs de zwarte lijn.

**Opmerkingen:** (1) De breedte van de zwarte lijn moet gelijk aan of groter zijn dan de breedte van de lijnvolgsensor tijdens het volgen.

(2) Vermijd het testen van de smart car onder fel licht.

7\.  **Code-uitleg**

![Img](./media/Python_b16f9d7b.png)

![Img](./media/Python_35f35a4c.png)