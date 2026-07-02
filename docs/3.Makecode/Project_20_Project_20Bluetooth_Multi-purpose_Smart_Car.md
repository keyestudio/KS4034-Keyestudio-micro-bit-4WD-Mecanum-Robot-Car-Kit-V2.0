## Project 20：Bluetooth Multi-purpose Smart Car

### Project 20.1：Read Bluetooth Data

![](./media/Makecode_55b2424d.png)

1\. **Beschreibung**

Das micro:bit Hauptboard verfügt über ein integriertes Bluetooth, mit dem kommuniziert werden kann. Der Micro:bit kann per Bluetooth gesteuert werden oder Signale an ein Smartphone oder einen Computer zurücksenden. Dieses Bluetooth kann mit den in anderen Geräten vorhandenen Bluetooth-Modulen oder mit einer Bluetooth-App kommunizieren, um andere Geräte zu steuern.

Es ist sowohl mit Android als auch mit iOS kompatibel. Wir haben für beide Systeme je eine Bluetooth-App entwickelt.

Die Verbindung des Board-Bluetooth mit diesen beiden Apps ist ähnlich. In dieser Lektion stellen wir die Funktionen aller Tasten und Muster in den Apps vor und steuern das Smart Car über die Bluetooth-App.

2\. **Vorbereitung**

- Setzen Sie das micro:bit-Board in den Steckplatz des keyestudio 4WD Mecanum Robot Car V2.0 ein

- Legen Sie die Batterien in den Batteriefach ein

- Schalten Sie den Netzschalter auf ON

- Verbinden Sie das micro:bit mit Ihrem Computer über ein USB-Kabel

- Öffnen Sie die Web-Version von Makecode

**Wenn Sie den Code manuell per Drag & Drop erstellen möchten, müssen Sie zuerst die Bluetooth-Erweiterungsbibliothek hinzufügen. Klicken Sie auf das Zahnrad-Symbol (Settings) oben rechts, dann auf Extensions, um zum Auswahldialog der Bibliotheken zu gelangen, und klicken Sie dann auf die Erweiterungsbibliothek "Bluetooth" (falls sie nicht vorhanden ist, suchen Sie nach Bluetooth), wie unten gezeigt:** 

![](./media/Makecode_4e308360.png)

Da Bluetooth und die Erweiterung radio nicht gleichzeitig arbeiten können, sind ihre Erweiterungsbibliotheken nicht kompatibel.

Bitte entfernen Sie daher andere Erweiterungen und fügen Sie Bluetooth hinzu, falls das folgende Hinweisfenster erscheint.

![](./media/Makecode_aee56e76.png)

3\. **Testcode**

![](./media/Makecode_ac5ffe1a.png)

Klicken Sie auf “JavaScript”, um den entsprechenden JavaScript-Code anzuzeigen:

![](./media/Makecode_24191138.png)

4\. **Testergebnis**

Wenn Sie die Blöcke schrittweise ziehen, müssen Sie nach Abschluss des Testcodes die folgenden Einstellungen vornehmen.

![](./media/Makecode_01b256e5.png)

![](./media/Makecode_982334c8.png)

![](./media/Makecode_09767d5e.png)

Sie können diesen Schritt jedoch überspringen, wenn Sie den Testcode direkt importieren.

Nach den Einstellungen laden Sie den Code auf das micro:bit-Board herunter, ziehen Sie das USB-Kabel nicht ab. Als Nächstes die App herunterladen.

**Für iOS-System:**

a\. Öffnen Sie den App Store;

![](./media/Makecode_27924fdb.png)

b\. Suchen Sie nach **mecanum_robot** und klicken Sie auf “![](./media/Makecode_962a57f9.png)”, um die Bluetooth-App mecanum_robot herunterzuladen;

c\. Nach dem Herunterladen der APP klicken Sie auf "OPEN" oder tippen Sie auf das App-Symbol mecanum_robot auf dem Telefon-/iPad-Desktop, um die APP zu öffnen. Auf der APP-Oberfläche erscheint ein Dialogfenster; klicken Sie im Dialog auf "OK".

d\. Schalten Sie zuerst das Bluetooth Ihres Mobiltelefons/iPads ein und klicken Sie dann auf die Verbindungstaste (control) oben links in der APP-Oberfläche, um eine Bluetooth-Suche durchzuführen. Klicken Sie in den Suchergebnissen auf "BCC micro:bit". Nach einigen Sekunden ist die Bluetooth-Verbindung hergestellt.

**Für Android-System:**

a\. Verwenden Sie die Scan-Funktion im Browser, um den QR-Code zu scannen und zu identifizieren

![](./media/Makecode_d9acbfab.png)

oder rufen Sie den Link auf: [http://8.210.52.206/mecanum_robot.apk](http://8.210.52.206/mecanum_robot.apk) zum Herunterladen. Nach erfolgreicher Identifikation klicken Sie auf "go to website", um zur Download-Seite mecanum_robot.apk zu gelangen, und klicken Sie auf "Download", um die Anwendung mecanum_robot herunterzuladen.

b\. Klicken Sie auf “Allow allow”, um zur Installationsansicht zu gelangen; klicken Sie auf “install”, um die App zu installieren.

![](./media/Makecode_638d0a4a.png)

c\. Klicken Sie auf "Open" oder tippen Sie auf das App-Symbol mecanum_robot auf dem Startbildschirm des Handys, um die APP zu öffnen. Es erscheint ein Dialogfenster. Klicken Sie im Dialogfenster auf "Allow", um das Bluetooth des Telefons zu aktivieren. Sie können das Bluetooth auch vor dem Öffnen der APP einschalten.

![](./media/Makecode_c818fd71.png)

![](./media/Makecode_0c35f0dc.png)

d\. Klicken Sie auf ![](./media/Makecode_d3f566b9.png) oben rechts, um nach Bluetooth zu suchen, und klicken Sie auf “connect”; nach einigen Sekunden ist die Bluetooth-Kopplung abgeschlossen.

![](./media/Makecode_3d21cf87.png)

![](./media/Makecode_4a23b197.png)

Öffnen Sie CoolTerm, klicken Sie auf Options und wählen Sie SerialPort. Stellen Sie den COM-Port und die Baudrate 115200 ein. Klicken Sie auf “OK” und “Connect”.

Richten Sie das micro:bit-Board aus und drücken Sie die Symbole in der APP; die entsprechenden Zeichen werden im CoolTerm-Monitor angezeigt.

![](./media/Makecode_0ed4a53e.png)

Durch den Test erhalten wir die Funktionen jeder Taste, wie unten gezeigt:

![](./media/Makecode_05c3d32b.jpg)

### Project 20.2：Multi-purpose Smart Car

![Img](./media/Makecode_ce6ec959.png)

1\. **Beschreibung**

In dieser Lektion steuern wir das Smart Car, damit es vielseitige Funktionen ausführt.

2\. **Vorbereitung**

- Setzen Sie das micro:bit-Board in den Steckplatz des keyestudio 4WD Mecanum Robot Car V2.0 ein

- Legen Sie die Batterien in das Batteriefach ein

- Schalten Sie den Netzschalter auf ON

- Verbinden Sie das micro:bit mit Ihrem Computer über ein USB-Kabel

- Öffnen Sie die Web-Version von Makecode

**Schritte：** Klicken Sie auf das Zahnrad-Symbol (Settings) oben rechts, dann auf Extensions, um zum Auswahldialog der Bibliotheken zu gelangen, und klicken Sie dann auf die Erweiterungsbibliothek "Bluetooth" (falls sie nicht vorhanden ist, suchen Sie nach Bluetooth), wie unten gezeigt: 

![](./media/Makecode_4e308360.png)

Da Bluetooth und die Erweiterung radio nicht gleichzeitig arbeiten können, sind ihre Erweiterungsbibliotheken nicht kompatibel.

Bitte entfernen Sie daher andere Erweiterungen und fügen Sie Bluetooth hinzu, falls das folgende Hinweisfenster erscheint.

![](./media/Makecode_aee56e76.png)

3\. **Testcode**

Da der Code recht umfangreich ist, wird er hier nicht angezeigt. Sie können direkt zum folgenden Pfad gehen, um den entsprechenden Code zu finden.

![Img](./media/Makecode_836c42ce.png)

Klicken Sie auf “JavaScript”, um den entsprechenden JavaScript-Code anzuzeigen:

![](./media/Makecode_a73529d6.png)

4\. **Testergebnis**

Dieses Experiment kombiniert die vorherigen Projekte, sodass das Auto Aktionen per Bluetooth ausführt.

Öffnen Sie den Makecode Online-Editor → Projecting Settings → ![](./media/Makecode_bef5b734.png), aktivieren Sie “No Pairing....” (diesen Schritt können Sie überspringen, wenn Sie den Testcode direkt importieren)

Laden Sie den Code auf das micro:bit-Board, schalten Sie POWER auf ON und verbinden Sie das Bluetooth. Dann können Sie das Auto über die Bluetooth-App mecanum_robot steuern.

**Hinweis:** ![](./media/Makecode_81da4f47.jpg) dient zur Einstellung der Geschwindigkeit, und ![](./media/Makecode_adc3be60.jpg) kann nur gezogen werden.