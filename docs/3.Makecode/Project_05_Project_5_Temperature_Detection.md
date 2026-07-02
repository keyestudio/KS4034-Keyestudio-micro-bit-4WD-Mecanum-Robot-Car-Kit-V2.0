## Projekt 5: Temperaturerkennung

![](./media/Makecode_22c6434f.jpg)

[Klicken Sie hier, um den Code 1 für diese Lektion herunterzuladen](./Code/Temperature-Detection.hex)

[Klicken Sie hier, um den Code 2 für diese Lektion herunterzuladen](./Code/Temperature-Detection2.hex)

### (1)Projektbeschreibung:

Die Micro:bit main board V2 ist nicht mit einem eigenen Temperatursensor ausgestattet, sondern verwendet den im NFR52833-Chip integrierten Temperatursensor zur Temperaturmessung. Daher entspricht die gemessene Temperatur eher der Temperatur des Chips und kann vom Umgebungstemperaturwert abweichen.

### (2)Benötigte Komponenten:

Micro:bit main board V2

Micro-USB-Kabel

### (3)Testcode 1 :

![](./media/Makecode_e6674fe9.gif)

### (4)Testergebnisse 1:

Nachdem Sie Testcode 1 auf das Micro:bit main board V2 hochgeladen, das Board über das USB-Kabel mit Strom versorgt und auf "Show console Device" geklickt haben, werden die Temperaturdaten auf der seriellen Monitorseite wie unten angezeigt.

![](./media/Makecode_898eded8.gif)

Wenn Sie Windows 7 oder 8 statt Windows 10 verwenden, kann Google Chrome die Geräte nicht erkennen. Sie müssen die CoolTerm-Software als seriellen Monitor verwenden, um die Daten zu lesen. Öffnen Sie die CoolTerm-Software, klicken Sie auf Options, wählen Sie SerialPort, legen Sie den COM-Port fest und stellen Sie die Baudrate auf 115200 ein (nach Tests ist die Baudrate der USB-SerialPort-Kommunikation auf dem Micro:bit main board V2 115200), klicken Sie OK und dann Connect. Der CoolTerm-Seriellmonitor zeigt die Temperaturänderungen in der aktuellen Umgebung, wie in den folgenden Abbildungen dargestellt:

![](./media/Makecode_268159a1.gif)

### (5)Testcode 2 :

Verbinden Sie den Computer mit dem Micro:bit-Board über ein Micro-USB-Kabel und programmieren Sie im MakeCode-Editor,

![](./media/Makecode_4057bdd7.gif)

Vollständiges Programm :

![](./media/Makecode_ec457959.png)

### (6)Testergebnisse 2:

Nach dem Hochladen von Code 2 zeigt die 5x5 LED-Punktmatrix ![](./media/Makecode_350d26c6.png), wenn die Umgebungstemperatur weniger als 35℃ beträgt. Wenn die Temperatur gleich oder größer als 35℃ ist, erscheint das Muster ![](./media/Makecode_ef8d7c88.png).

---