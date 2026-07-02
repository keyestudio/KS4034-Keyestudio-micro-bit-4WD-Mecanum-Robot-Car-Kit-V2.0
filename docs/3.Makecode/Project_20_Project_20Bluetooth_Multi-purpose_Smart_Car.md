## Proyecto 20：Bluetooth Multi-purpose Smart Car

### Proyecto 20.1：Read Bluetooth Data

![](./media/Makecode_55b2424d.png)

1\. **Descripción**

La placa principal micro:bit viene con un Bluetooth integrado que puede usarse para comunicarse con ella. El Micro:bit también puede ser controlado por Bluetooth o transmitir señales de vuelta al smartphone o al ordenador a través de éste. Este Bluetooth puede comunicarse con el Bluetooth incorporado en otros dispositivos o con una aplicación Bluetooth para controlar otros equipos.

Es compatible con los sistemas Android e iOS. Hemos diseñado dos aplicaciones Bluetooth para ambos sistemas.

La conexión del Bluetooth de la placa con estas dos aplicaciones es similar. En esta lección, presentaremos las funciones de todas las teclas y patrones en las aplicaciones y controlaremos el coche inteligente mediante la aplicación Bluetooth.

2\. **Preparación**

- Inserte la placa micro:bit en la ranura del keyestudio 4WD Mecanum Robot Car V2.0

- Coloque las baterías en el portapilas

- Gire el interruptor de alimentación a la posición ON

- Conecte el micro:bit a su ordenador mediante un cable USB

- Abra la versión web de Makecode

**Si elige arrastrar el código manualmente, primero debe añadir la biblioteca de extensión Bluetooth. Haga clic en el icono de engranaje (Settings) en la esquina superior derecha, luego en Extensions para ir a la pantalla de selección de archivos de la biblioteca, y después haga clic en la biblioteca de extensión "Bluetooth" (si no existe, busque Bluetooth), como se muestra a continuación:** 

![](./media/Makecode_4e308360.png)

Como Bluetooth y la extensión radio no pueden funcionar juntos, sus bibliotecas de extensión no son compatibles.

Por lo tanto, elimine otras extensiones y añada Bluetooth si aparece el siguiente cuadro de aviso.

![](./media/Makecode_aee56e76.png)

3\. **Código de prueba**

![](./media/Makecode_ac5ffe1a.png)

Haga clic en “JavaScript” para ver el código JavaScript correspondiente:

![](./media/Makecode_24191138.png)

4\. **Resultado de la prueba**

Si arrastra los bloques paso a paso, deberá configurar lo siguiente después de terminar el código de prueba.

![](./media/Makecode_01b256e5.png)

![](./media/Makecode_982334c8.png)

![](./media/Makecode_09767d5e.png)

Sin embargo, puede omitir este paso si importa directamente el código de prueba.

Después de configurar, descargue el código en la placa micro:bit, no desconecte el cable USB. A continuación, descargue la aplicación.

**Para iOS:**

a\. Abra App Store;

![](./media/Makecode_27924fdb.png)

b\. Busque **mecanum_robot** y haga clic en “![](./media/Makecode_962a57f9.png)” para descargar la aplicación Bluetooth mecanum_robot;

c\. Tras descargar la APP, haga clic en "OPEN" o toque la aplicación mecanum_robot en el escritorio del teléfono/iPad para abrir la APP. Aparecerá un cuadro de diálogo en la interfaz de la APP; haga clic en "OK" en el cuadro de diálogo.

d\. Primero active el Bluetooth del móvil/iPad y luego haga clic en el botón de conexión (control) en la esquina superior izquierda de la interfaz de la APP para realizar una búsqueda Bluetooth. En los resultados, haga clic en "BCC micro:bit". Tras unos segundos, el Bluetooth quedará conectado.

**Para Android:**

a\. Utilice la función de escaneo del navegador para escanear e identificar el código QR

![](./media/Makecode_d9acbfab.png)

o introduzca el enlace: [http://8.210.52.206/mecanum_robot.apk](http://8.210.52.206/mecanum_robot.apk) para descargar. Tras la identificación, haga clic en "go to website" para entrar en la página de descarga mecanum_robot.apk y haga clic en "Download" para descargar la aplicación mecanum_robot.

b\. Haga clic en “Allow allow” para entrar en el diagrama de instalación; haga clic en “install” para instalar la aplicación.

![](./media/Makecode_638d0a4a.png)

c\. Haga clic en "Open" o toque la aplicación mecanum_robot en el escritorio del teléfono para abrir la APP; aparecerá un cuadro de diálogo. En el cuadro de diálogo haga clic en "Allow" para activar el Bluetooth del teléfono. También puede activar el Bluetooth del teléfono antes de abrir la APP.

![](./media/Makecode_c818fd71.png)

![](./media/Makecode_0c35f0dc.png)

d\. Haga clic en ![](./media/Makecode_d3f566b9.png) en la esquina superior derecha para buscar Bluetooth y haga clic en “connect”; unos segundos después, el Bluetooth estará emparejado.

![](./media/Makecode_3d21cf87.png)

![](./media/Makecode_4a23b197.png)

Abra CoolTerm, haga clic en Options para seleccionar SerialPort. Configure el puerto COM y la velocidad en baudios a 115200. Haga clic en “OK” y “Connect”.

Apunte a la placa micro:bit y pulse los iconos en la APP; los caracteres correspondientes se muestran en el monitor de CoolTerm.

![](./media/Makecode_0ed4a53e.png)

A través de la prueba, obtenemos las funciones de cada icono, como se muestra a continuación:

![](./media/Makecode_05c3d32b.jpg)

### Proyecto 20.2：Multi-purpose Smart Car

![Img](./media/Makecode_ce6ec959.png)

1\. **Descripción**

En esta lección controlaremos el coche inteligente para que realice funciones múltiples.

2\. **Preparación**

- Inserte la placa micro:bit en la ranura del keyestudio 4WD Mecanum Robot Car V2.0

- Coloque las baterías en el portapilas

- Ponga el interruptor de alimentación en ON

- Conecte el micro:bit a su ordenador mediante un cable USB

- Abra la versión web de Makecode

**Pasos：** Haga clic en el icono de engranaje (Settings) en la esquina superior derecha, luego en Extensions para ir a la pantalla de selección de archivos de la biblioteca, y después haga clic en la biblioteca de extensión "Bluetooth" (si no existe, busque Bluetooth), como se muestra a continuación: 

![](./media/Makecode_4e308360.png)

Como Bluetooth y la extensión radio no pueden funcionar juntos, sus bibliotecas de extensión no son compatibles.

Por lo tanto, elimine otras extensiones y añada Bluetooth si aparece el siguiente cuadro de aviso.

![](./media/Makecode_aee56e76.png)

3\. **Código de prueba**

Dado que el código es bastante largo, no se mostrará aquí. Puede ir directamente a la ruta siguiente para encontrar el código correspondiente.

![Img](./media/Makecode_836c42ce.png)

Haga clic en “JavaScript” para ver el código JavaScript correspondiente:

![](./media/Makecode_a73529d6.png)

4\. **Resultado de la prueba**

Este experimento combina los proyectos anteriores para que el coche ejecute acciones vía Bluetooth.

Entre en el editor en línea Makecode→Projecting Settings→![](./media/Makecode_bef5b734.png), habilite “No Pairing....”(puede omitir este paso si importa el código de prueba directamente)

Descargue el código a la placa micro:bit, ponga POWER en ON y conecte el Bluetooth; entonces podrá controlar el coche a través de la aplicación Bluetooth mecanum_robot.

**Nota:** ![](./media/Makecode_81da4f47.jpg) se usa para ajustar la velocidad, y ![](./media/Makecode_adc3be60.jpg) solo se puede arrastrar.