## Projet 20：Bluetooth Multi-purpose Smart Car

### Projet 20.1：Read Bluetooth Data

![](./media/Makecode_55b2424d.png)

1\. **Description**

La carte principale micro:bit intègre un Bluetooth qui peut être utilisé pour communiquer avec elle. Le Micro:bit peut également être contrôlé par Bluetooth ou transmettre des signaux au smartphone ou à l'ordinateur via celui-ci. Ce Bluetooth peut communiquer avec le Bluetooth d'autres appareils ou avec une application Bluetooth pour contrôler d'autres équipements.

Il est compatible à la fois avec Android et iOS. Nous avons conçu deux applications Bluetooth pour ces deux systèmes.

La connexion du Bluetooth de la carte avec ces deux applications est similaire. Dans cette leçon, nous présenterons les fonctions de toutes les touches et motifs sur les applications et contrôlerons la voiture intelligente via l'application Bluetooth.

2\. **Préparation**

- Insérez la carte micro:bit dans le logement du keyestudio 4WD Mecanum Robot Car V2.0

- Placez les piles dans le porte-piles

- Tournez l'interrupteur d'alimentation sur ON

- Connectez le micro:bit à votre ordinateur via un câble USB

- Ouvrez la version Web de Makecode

**Si vous choisissez de glisser le code manuellement, vous devez d'abord ajouter la bibliothèque d'extension Bluetooth. Cliquez sur l'icône d'engrenage (Settings) en haut à droite, puis cliquez sur Extensions pour accéder à l'écran de sélection des fichiers de bibliothèque, puis cliquez sur la bibliothèque d'extension "Bluetooth" (si elle n'existe pas, recherchez Bluetooth), comme indiqué ci-dessous :** 

![](./media/Makecode_4e308360.png)

Comme Bluetooth et l'extension radio ne peuvent pas fonctionner ensemble, leurs bibliothèques d'extension ne sont pas compatibles.

Par conséquent, supprimez les autres extensions et ajoutez Bluetooth si la boîte de dialogue suivante apparaît.

![](./media/Makecode_aee56e76.png)

3\. **Code de test**

![](./media/Makecode_ac5ffe1a.png)

Cliquez sur “JavaScript” pour afficher le code JavaScript correspondant :

![](./media/Makecode_24191138.png)

4\. **Résultat du test**

Si vous faites glisser les blocs étape par étape, vous devez procéder aux réglages suivants après avoir terminé le code de test.

![](./media/Makecode_01b256e5.png)

![](./media/Makecode_982334c8.png)

![](./media/Makecode_09767d5e.png)

Cependant, vous pouvez ignorer cette étape si vous importez directement le code de test.

Après les réglages, téléchargez le code sur la carte micro:bit, ne débranchez pas le câble USB. Ensuite, téléchargez l'application.

**Pour iOS :**

a\. Ouvrez l'App Store ;

![](./media/Makecode_27924fdb.png)

b\. Recherchez **mecanum_robot** et cliquez sur “![](./media/Makecode_962a57f9.png)” pour télécharger l'application Bluetooth mecanum_robot ;

c\. Après le téléchargement de l'APP, cliquez sur "OPEN" ou touchez l'icône de l'application mecanum_robot sur le bureau du téléphone/iPad pour ouvrir l'APP. Une boîte de dialogue apparaît sur l'interface de l'APP ; cliquez sur "OK" dans la boîte de dialogue.

d\. Activez d'abord le Bluetooth du téléphone/iPad, puis cliquez sur le bouton de connexion (control) en haut à gauche de l'interface de l'APP pour effectuer une recherche Bluetooth. Dans les résultats, cliquez sur "BCC micro:bit". Après quelques secondes, le Bluetooth est connecté.

**Pour Android :**

a\. Utilisez la fonction de numérisation du navigateur pour scanner et identifier le code QR

![](./media/Makecode_d9acbfab.png)

ou entrez le lien : [http://8.210.52.206/mecanum_robot.apk](http://8.210.52.206/mecanum_robot.apk) pour télécharger. Après identification, cliquez sur "go to website" pour accéder à la page de téléchargement mecanum_robot.apk, puis cliquez sur "Download" pour télécharger l'application mecanum_robot.

b\. Cliquez sur “Allow allow” pour entrer dans l'écran d'installation ; cliquez sur “install” pour installer l'application.

![](./media/Makecode_638d0a4a.png)

c\. Cliquez sur "Open" ou touchez l'icône de l'application mecanum_robot sur l'écran d'accueil du téléphone pour ouvrir l'APP ; une boîte de dialogue apparaît. Dans la boîte de dialogue, cliquez sur "Allow" pour activer le Bluetooth du téléphone. Vous pouvez aussi activer le Bluetooth du téléphone avant d'ouvrir l'APP.

![](./media/Makecode_c818fd71.png)

![](./media/Makecode_0c35f0dc.png)

d\. Cliquez sur ![](./media/Makecode_d3f566b9.png) en haut à droite pour rechercher le Bluetooth et cliquez sur “connect” ; après quelques secondes, l'appariement Bluetooth est effectué.

![](./media/Makecode_3d21cf87.png)

![](./media/Makecode_4a23b197.png)

Ouvrez CoolTerm, cliquez sur Options pour sélectionner SerialPort. Réglez le port COM et le débit 115200. Cliquez sur “OK” et “Connect”.

Pointez la carte micro:bit et appuyez sur les icônes de l'APP ; les caractères correspondants s'affichent dans le moniteur CoolTerm.

![](./media/Makecode_0ed4a53e.png)

Grâce au test, nous obtenons les fonctions de chaque icône, comme indiqué ci-dessous :

![](./media/Makecode_05c3d32b.jpg)

### Projet 20.2：Multi-purpose Smart Car

![Img](./media/Makecode_ce6ec959.png)

1\. **Description**

Dans cette leçon, nous contrôlerons la voiture intelligente pour exécuter des fonctions polyvalentes.

2\. **Préparation**

- Insérez la carte micro:bit dans le logement du keyestudio 4WD Mecanum Robot Car V2.0

- Placez les piles dans le porte-piles

- Tournez l'interrupteur d'alimentation sur ON

- Connectez le micro:bit à votre ordinateur via un câble USB

- Ouvrez la version Web de Makecode

**Étapes：** Cliquez sur l'icône d'engrenage (Settings) en haut à droite, puis sur Extensions pour accéder à l'écran de sélection des bibliothèques, puis cliquez sur la bibliothèque d'extension "Bluetooth" (si elle n'existe pas, recherchez Bluetooth), comme indiqué ci-dessous : 

![](./media/Makecode_4e308360.png)

Comme Bluetooth et l'extension radio ne peuvent pas fonctionner ensemble, leurs bibliothèques d'extension ne sont pas compatibles.

Par conséquent, supprimez les autres extensions et ajoutez Bluetooth si la boîte de dialogue suivante apparaît.

![](./media/Makecode_aee56e76.png)

3\. **Code de test**

Étant donné que le code est assez long, il ne sera pas affiché ici. Vous pouvez vous rendre directement au chemin suivant pour trouver le code correspondant.

![Img](./media/Makecode_836c42ce.png)

Cliquez sur “JavaScript” pour afficher le code JavaScript correspondant :

![](./media/Makecode_a73529d6.png)

4\. **Résultat du test**

Cette expérience combine les projets précédents pour permettre à la voiture d'effectuer des actions via Bluetooth.

Entrez dans l'éditeur en ligne Makecode → Projecting Settings → ![](./media/Makecode_bef5b734.png), activez “No Pairing....” (vous pouvez passer cette étape si vous importez directement le code de test)

Téléchargez le code sur la carte micro:bit, mettez POWER sur ON et connectez le Bluetooth, puis vous pourrez contrôler la voiture via l'application Bluetooth mecanum_robot.

**Remarque :** ![](./media/Makecode_81da4f47.jpg) sert à régler la vitesse, et ![](./media/Makecode_adc3be60.jpg) ne peut être que glissé.