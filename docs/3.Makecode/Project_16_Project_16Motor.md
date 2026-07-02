## Project 16：Motor

![](./media/Makecode_77f3b857.png)

1\.  **Beschreibung**

Das Keyestudio 4WD Mecanum Robot Car ist mit 4 DC-Reduktionsmotoren (auch als Getriebemotor bezeichnet) ausgestattet, die auf gewöhnlichen DC-Motoren basieren. Es verfügt über ein passendes Getriebegehäuse, das eine geringere Drehzahl, aber ein höheres Drehmoment liefert. Unterschiedliche Übersetzungsverhältnisse des Getriebes können zudem verschiedene Drehzahlen und Drehmomente bereitstellen.

Ein Getriebemotor ist die Integration von Getriebe und Motor und wird in der Stahl- und Maschinenbaubranche weit verbreitet angewendet.

Das micro:bit Motor-Treiber-Shield ist mit einem DRV8833-Chip bestückt. Um IO-Port-Ressourcen zu sparen, steuern wir die Drehrichtung und Geschwindigkeit der 4 DC-Getriebemotoren mit dem DRV8833-Chip.

![Img](./media/Makecode_4c9781dc.png)

Front

![](./media/Makecode_4919ce3b.png)

Back

![](./media/Makecode_59c34b6e.png)

STC8G1K08 Chip circuit

![](./media/Makecode_8874ded0.png)

HR8833 Motor driver circuit

2\.  **Vorbereitung**

- Setzen Sie das micro:bit-Board in den Slot des keyestudio 4WD Mecanum Robot Car V2.0 ein

- Legen Sie Batterien in den Batteriefachhalter ein

- Schalten Sie den Netzschalter auf die ON-Position

- Verbinden Sie das micro:bit über ein USB-Kabel mit Ihrem Computer

- Öffnen Sie die Webversion von Makecode

3\.  **Test Code1**

![](./media/Makecode_3a759dd8.png)

Klicken Sie auf“JavaScript", um den entsprechenden JavaScript-Code anzuzeigen: 

![](./media/Makecode_242ba6ca.png)

4\.  **Testergebnis1**

Laden Sie Code 1 auf das micro:bit-Board, schalten Sie den POWER-Schalter auf ON. Das Roboterauto fährt 2s vorwärts und hält 2s an.

5\.  **Test Code2**

![](./media/Makecode_a3a9d39a.png)

![Img](./media/Makecode_4eb6b574.png)

Klicken Sie auf“JavaScript", um den entsprechenden JavaScript-Code anzuzeigen: 

![](./media/Makecode_ee70b846.png)

6\.  **Testergebnis2**

Laden Sie Code 2 auf das micro:bit-Board. Das Auto fährt 2s vorwärts, fährt 2s rückwärts, fährt 2s nach links, fährt 2s nach rechts, stoppt 2s und wiederholt dieses Muster.