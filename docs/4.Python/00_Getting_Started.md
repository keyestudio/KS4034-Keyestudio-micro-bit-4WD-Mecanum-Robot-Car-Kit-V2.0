## Resource Download

Pour vous aider à obtenir rapidement les codes, bibliothèques et autres fichiers de support liés à ce produit, veuillez cliquer sur les liens ci-dessous pour les télécharger :

- [Python Code and library downloads](./PythonCode.7z)

## Premiers pas avec Python

Ce tutoriel est rédigé pour le langage Python. Si vous souhaitez utiliser une programmation graphique, veuillez vous référer au manuel "Makecode Tutorial". Dans le répertoire racine de la ressource que vous avez téléchargée, il y a un dossier nommé "Python tutorial", qui contient tout le code Python de la Micro:bit 4WD Mecanum Robot Car V2.0. Le fichier de code Python est un fichier se terminant par ".py".

### Qu'est-ce que MicroPython ?

Python est un langage textuel, largement utilisé dans l'éducation et également employé par des programmeurs professionnels dans des domaines tels que la science des données et l'apprentissage automatique.

Le Micro: bit peut être programmé en Python ; il s'agit d'un microcontrôleur et les différences matérielles empêchent le micro: bit de prendre en charge Python dans son intégralité. MicroPython est dédié au micro：bit, c'est une implémentation efficace du langage Python3. Il contient une petite partie de la bibliothèque standard Python et est optimisé pour fonctionner sur les microcontrôleurs micro:bit.

La version de Python utilisée par le BBC micro: bit s'appelle MicroPython. MicroPython est parfait pour ceux qui souhaitent en apprendre davantage sur la programmation ; il vous aide à programmer avec une série d'extraits de code, ainsi qu'une variété de graphiques et de musiques préconçus.

Lien pour BBC microbit MicroPyth : [BBC micro:bit MicroPython ](https://microbit-micropython.readthedocs.io/en/latest/tutorials/introduction.html) 

**Python dispose de deux types d'éditeurs : version web et version hors ligne**

1\.  Version web : [https://python.microbit.org/v/1.1](https://python.microbit.org/v/1.1)

![](./media/Python_693f76f5.png)

2\.  L'autre est aussi le compilateur hors ligne — Mu ![](./media/Python_153c77ed.png)

Site officiel de Mu : [https://codewith.mu/](https://codewith.mu/)

### Mu

Mu, un éditeur de code Python, convient aux débutants. Il ne prend pas en charge Windows 32 bits.

1\.  **Télécharger Mu**

Cliquez sur « This PC » puis faites un clic droit sur Propriétés pour vérifier la version de votre ordinateur.

![](./media/Python_3a58be54.png)

Vérifiez le type de système de votre ordinateur.

![](./media/Python_e774ae15.png)

Accédez au lien de MU : [https://codewith.mu/en/download](https://codewith.mu/en/download) pour télécharger la version correspondante de Mu.

![](./media/Python_ceb4cfa6.png)

2\.  **Exécuter le programme d'installation**

Ouvrez le fichier ci-dessous

![](./media/Python_8bcfe24c.png)

Mac OSX : [https://codewith.mu/en/howto/1.1/install_macos](https://codewith.mu/en/howto/1.1/install_macos).

Linux : [https://codewith.mu/en/howto/1.2/install_linux](https://codewith.mu/en/howto/1.2/install_linux).

**Windows 10**

Une fenêtre contextuelle s'affichera, cliquez ensuite sur « More info ».

![](./media/Python_877beb7b.png)

Puis cliquez sur « Run anyway ».

![](./media/Python_c87475e5.png)

3\. Contrat de licence

Cliquez sur « Install ».

![](./media/Python_33f42b66.png)

![](./media/Python_f5c6698f.png)

Après l'installation, cliquez sur « finish ».

![](./media/Python_c6ec7436.png)

4\. Démarrer Mu

Ensuite, localisez-le selon l'image suivante

![](./media/Python_c4adbdd1.png)

Son interface principale est affichée comme ci-dessous :

![](./media/Python_3697c0c7.png)

### Utilisation des modes & barre de menu

Réglez “<span style="color: rgb(255, 76, 65);">**Mode**</span>” sur BBC micro:bit.

Dans le menu, cliquez sur « **Mode** » pour le définir sur « **BBC micro：bit** ». Le mode micro:bit sait comment interagir avec et se connecter à un micro:bit.

![](./media/Python_18512c7e.png)

Cliquez pour [Start with Mu](https://codewith.mu/en/tutorials/1.1/start).

### Comment Mu importe une bibliothèque dans le Micro:bit

<span style="color: rgb(255, 76, 65);">**Avant d'importer des bibliothèques, nous devons téléverser un code .py (un code vide convient également) sur la carte micro:bit. Ici nous prenons un code vide en exemple.**</span>

Connectez la carte à l'ordinateur via un câble USB. Ouvrez Mu et cliquez sur « Flash » pour téléverser le code .py (même vide) sur la carte.

![Img](./media/Python_611b2c4e.png)

Dans ce tutoriel, le fichier de bibliothèque "keyes_mecanum_Car_V2.py" est utilisé. Par conséquent, importez le fichier de bibliothèque "keyes_mecanum_Car_V2.py" dans le micro:bit. Ce fichier contient la méthode de contrôle du Micro:bit 4WD Mecanum Robot Car V2.0.

Le répertoire par défaut dans lequel Mu enregistre les fichiers est « mu_code » à la racine du répertoire utilisateur.

Lien de référence : [https://codewith.mu/en/tutorials/1.0/files](https://codewith.mu/en/tutorials/1.0/files)

**Méthodes pour trouver le dossier "mu_code" :**

**Méthode Une :**

Par exemple, sur le système Windows, supposons que votre système est installé sur le lecteur C de l'ordinateur, et que le nom d'utilisateur est "**Administrator**", alors le chemin du répertoire "**mu_code**" est "**C:\Users\Administrator\mu_ code**". Sur les systèmes Linux, le chemin du répertoire "**mu_code**" est "**~/home/mu_code**".

Ouvrez le dossier « **mu_code** ».

![](./media/Python_d271a924.png)

**Méthode Deux :**

Recherchez le dossier « mu_code » sur le disque (C:).

![Img](./media/Python_03ff037e.png)

![Img](./media/Python_54199d45.png)

Ouvrez « mu_code ».

![Img](./media/Python_4841ca3f.png)

Le chemin du dossier de données où se trouve le fichier de bibliothèque “keyes_mecanum_Car.py” que nous fournissons est le suivant :

![Img](./media/Python_7adb2b68.png)

Copiez le fichier de bibliothèque “keyes_mecanum_Car.py” dans le dossier “mu_code”。Lorsque la copie est terminée, cela ressemble à l'image ci-dessous :

![](./media/Python_d753d652.png)

Ouvrez d'abord le logiciel Mu et connectez le micro:bit à votre ordinateur, puis cliquez sur le bouton "Files" et faites glisser le fichier de bibliothèque "keyes_mecanum_Car.py" vers le micro:bit.

![](./media/Python_aeaae2b7.png)

Après quelques secondes, l'importation est terminée et vous pouvez le voir dans la boîte à gauche.

![](./media/Python_2be967ca.png)