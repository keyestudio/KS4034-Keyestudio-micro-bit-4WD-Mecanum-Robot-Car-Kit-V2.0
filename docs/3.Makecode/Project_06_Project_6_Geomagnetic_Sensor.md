## Projet 6 : Capteur géomagnétique

[Cliquez pour télécharger le code 1 de cette leçon](./Code/Geomagnetic-Sensor.hex)

[Cliquez pour télécharger le code 2 de cette leçon](./Code/Geomagnetic-Sensor2.hex)

### (1)Description du projet :

(1) Description du projet : Ce projet vise à expliquer l'utilisation du capteur géomagnétique du Micro:bit, qui peut non seulement détecter l'intensité du champ géomagnétique, mais aussi être utilisé comme boussole pour trouver les caps. Il constitue également une partie importante du système de référence d'assiette et de cap (AHRS). Le Micro:bit main board V2 utilise le capteur géomagnétique LSM303AGR, et la plage dynamique du champ magnétique est de ± 50 gauss. Sur la carte, le module magnétomètre est utilisé à la fois pour la détection magnétique et comme boussole. Dans cette expérience, la boussole sera d'abord présentée, puis les données brutes du magnétomètre seront vérifiées. Le composant principal d'une boussole courante est une aiguille magnétique, qui peut être tournée par le champ géomagnétique et pointer vers le pôle Nord géomagnétique (qui est proche du pôle Sud géographique) pour déterminer la direction.

### (2)Composants nécessaires :

Micro:bit main board V2

 Câble Micro USB

### (3)Code de test 1 :

Reliez l'ordinateur à la carte micro:bit avec un câble Micro-USB et programmez dans l'éditeur MakeCode.

![](./media/Makecode_5805c7de.gif)

Programme complet :

![](./media/Makecode_5a958132.png)

### (4)Résultats du test 1 :

Après avoir téléversé le code de test sur le Micro:bit main board V2 et alimenté la carte via le câble USB, et après avoir appuyé sur le bouton A, la carte demande de calibrer la boussole et la matrice de points LED affiche "TILT TO FILL SCREEN". Ensuite, on entre dans la page de calibration. Faites tourner la carte jusqu'à ce que les 25 LED soient allumées en rouge comme illustré ci‑dessous.

![](./media/Makecode_b0a4ebf1.jpg)

calibrer la boussole :

![](./media/Makecode_05a88e21.gif)

Après cela, un motif souriant ![](./media/Makecode_74a69436.png)apparaît, ce qui implique que la calibration est terminée. Une fois le processus de calibration terminé, appuyer sur le bouton A affichera la lecture du magnétomètre directement à l'écran. Et les directions nord, est, sud et ouest correspondent respectivement à 0°, 90°, 180° et 270°.

![](./media/Makecode_23b07bfb.gif)

### (5) Code de test 2 :

Ce module peut continuer à lire des données pour déterminer la direction, il indique donc le pôle Nord magnétique actuel par une flèche.

Reliez l'ordinateur à la carte micro:bit avec un câble Micro-USB et programmez dans l'éditeur MakeCode,

![](./media/Makecode_db8b2d7e.gif)

Programme complet :

![](./media/Makecode_ef823069.png)

### (6) Résultats du test 2

Téléversez le code 2. Après la calibration, inclinez la carte micro:bit, et la matrice de points LED affiche les symboles de direction.

![](./media/Makecode_d8944d5f.gif)

---