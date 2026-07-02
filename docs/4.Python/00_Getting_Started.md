## Resource Download

Um schnell die zugehörigen Codes, Bibliotheken und anderen unterstützenden Dateien für dieses Produkt zu erhalten, klicken Sie bitte auf die folgenden Links, um sie herunterzuladen:

- [Python Code and library downloads](./PythonCode.7z)

## Einstieg in Python

Dieses Tutorial ist für die Programmiersprache Python geschrieben. Wenn Sie grafische Programmierung verwenden möchten, lesen Sie bitte das Handbuch "Makecode Tutorial". Im Stammverzeichnis der heruntergeladenen Ressourcen befindet sich ein Ordner mit dem Namen "Python tutorial", in dem sich sämtlicher Python-Code des Micro:bit 4WD Mecanum Robot Car V2.0 befindet. Die Python-Code-Datei ist eine Datei mit der Endung ".py".

### Was ist MicroPython?

Python ist eine textbasierte Sprache, die weit verbreitet in der Bildung eingesetzt wird und auch von professionellen Programmierern in Bereichen wie Data Science und Machine Learning verwendet wird.

Der Micro: bit kann in Python programmiert werden. Da es sich um einen Mikrocontroller handelt, verhindern Hardware-Unterschiede, dass der Micro: bit Python vollständig unterstützt. MicroPython ist speziell für micro：bit entwickelt und stellt eine effiziente Implementierung der Programmiersprache Python3 dar. Es enthält einen kleinen Teil der Python-Standardbibliothek und ist für die Ausführung auf micro:bit-Mikrocontrollern optimiert.

Die von BBC micro: bit verwendete Python-Version heißt MicroPython. MicroPython ist ideal für alle, die mehr über Programmierung lernen möchten. Es unterstützt Sie beim Programmieren mit einer Reihe von Code-Snippets sowie verschiedenen vorgefertigten Grafiken und Musik.

Link für BBC microbit MicroPyth：[BBC micro:bit MicroPython ](https://microbit-micropython.readthedocs.io/en/latest/tutorials/introduction.html) 

**Python hat zwei Arten von Editoren: Web-Version und Offline-Version**

1\.  Web-Version: [https://python.microbit.org/v/1.1](https://python.microbit.org/v/1.1)

![](./media/Python_693f76f5.png)

2\.  Die andere ist der Offline-Compiler — Mu ![](./media/Python_153c77ed.png)

Offizielle Webseite von Mu: [https://codewith.mu/](https://codewith.mu/)

### Mu

Mu, ein Python-Code-Editor, eignet sich für Einsteiger. Er unterstützt kein 32-Bit-Windows.

1\.  **Mu herunterladen**

Klicken Sie auf „This PC“ und klicken Sie mit der rechten Maustaste auf Eigenschaften, um die Version Ihres Computers zu überprüfen.

![](./media/Python_3a58be54.png)

Überprüfen Sie den Systemtyp Ihres Computers.

![](./media/Python_e774ae15.png)

Rufen Sie die MU-Seite auf: [https://codewith.mu/en/download](https://codewith.mu/en/download) und laden Sie die entsprechende Version von Mu herunter.

![](./media/Python_ceb4cfa6.png)

2\.  **Installation ausführen**

Öffnen Sie die nachstehende Datei

![](./media/Python_8bcfe24c.png)

Mac OSX: [https://codewith.mu/en/howto/1.1/install_macos](https://codewith.mu/en/howto/1.1/install_macos).

Linux: [https://codewith.mu/en/howto/1.2/install_linux](https://codewith.mu/en/howto/1.2/install_linux).

**Windows 10**

Es erscheint ein Popup-Fenster, klicken Sie dann auf „More info“.

![](./media/Python_877beb7b.png)

Klicken Sie anschließend auf „Run anyway“.

![](./media/Python_c87475e5.png)

3\. Lizenzvereinbarung

Klicken Sie auf „Install“.

![](./media/Python_33f42b66.png)

![](./media/Python_f5c6698f.png)

Nach der Installation klicken Sie auf „finish“.

![](./media/Python_c6ec7436.png)

4\. Mu starten

Suchen Sie Mu anschließend wie in der Abbildung gezeigt

![](./media/Python_c4adbdd1.png)

Die Hauptoberfläche sieht wie folgt aus:

![](./media/Python_3697c0c7.png)

### Verwendung von Modi & Menüleiste

Setzen Sie “<span style="color: rgb(255, 76, 65);">**Mode**</span>” auf BBC micro:bit.

Klicken Sie im Menü auf „**Mode**“, um es auf „**BBC micro：bit**“ einzustellen. Der micro:bit-Modus weiß, wie er mit einem micro:bit interagiert und sich mit ihm verbindet.

![](./media/Python_18512c7e.png)

Klicken Sie, um zu [Start with Mu](https://codewith.mu/en/tutorials/1.1/start) zu gelangen.

### Wie Mu Bibliotheken in den Micro:bit importiert

<span style="color: rgb(255, 76, 65);">**Bevor Bibliotheken importiert werden, müssen wir eine .py-Datei (auch eine leere Datei ist ausreichend) auf das micro:bit-Board hochladen. Hier verwenden wir als Beispiel eine leere Datei.**</span>

Verbinden Sie das Board über ein USB-Kabel mit dem Computer. Öffnen Sie Mu und klicken Sie auf „Flash“, um die .py-Datei (auch leer) auf das Board hochzuladen.

![Img](./media/Python_611b2c4e.png)

In diesem Tutorial wird die Bibliotheksdatei "keyes_mecanum_Car_V2.py" verwendet. Importieren Sie daher die Datei "keyes_mecanum_Car_V2.py" in den micro:bit. Diese Datei enthält die Steuerungsmethoden des Micro:bit 4WD Mecanum Robot Car V2.0.

Das Standardverzeichnis, in dem Mu Dateien speichert, ist „mu_code“ im Stammverzeichnis des Benutzerverzeichnisses.

Referenzlink: [https://codewith.mu/en/tutorials/1.0/files](https://codewith.mu/en/tutorials/1.0/files)

**Methoden zum Auffinden des "mu_code"-Ordners:**

**Methode Eins:**

Zum Beispiel: Auf einem Windows-System, wenn Ihr System auf dem Laufwerk C installiert ist und der Benutzername "**Administrator**" lautet, dann ist der Pfad des Verzeichnisses "**mu_code**" "**C:\Users\Administrator\mu_ code**". Auf Linux-Systemen lautet der Pfad des Verzeichnisses "**mu_code**" "**~/home/mu_code**".

Öffnen Sie den Ordner „**mu_code**“.

![](./media/Python_d271a924.png)

**Methode Zwei:**

Suchen Sie auf Laufwerk (C:) nach dem Ordner „mu_code“.

![Img](./media/Python_03ff037e.png)

![Img](./media/Python_54199d45.png)

Öffnen Sie „mu_code“.

![Img](./media/Python_4841ca3f.png)

Der Pfad des Datenordners, in dem sich die von uns bereitgestellte Bibliotheksdatei “keyes_mecanum_Car.py” befindet, ist wie folgt:

![Img](./media/Python_7adb2b68.png)

Kopieren Sie die Bibliotheksdatei “keyes_mecanum_Car.py” in den Ordner “mu_code”。Wenn das Kopieren abgeschlossen ist, sieht es wie unten gezeigt aus:

![](./media/Python_d753d652.png)

Öffnen Sie zuerst die Mu-Software und verbinden Sie den micro:bit mit Ihrem Computer. Klicken Sie dann auf die Schaltfläche "Files" und ziehen Sie die Bibliotheksdatei "keyes_mecanum_Car.py" auf den micro:bit.

![](./media/Python_aeaae2b7.png)

Nach ein paar Sekunden ist der Import abgeschlossen und Sie können sie im Feld links sehen.

![](./media/Python_2be967ca.png)