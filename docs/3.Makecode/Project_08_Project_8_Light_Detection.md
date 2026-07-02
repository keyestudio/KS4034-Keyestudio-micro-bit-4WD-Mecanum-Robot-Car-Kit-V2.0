## Proyecto 8: Detección de luz

![](./media/Makecode_14063ef9.jpg)

[Haga clic para descargar el código de esta lección](./Code/Light-Detection.hex)

### (1) Descripción del proyecto:

En este proyecto, nos centramos en la función de detección de luz del Micro: Bit main board V2. Se logra mediante la matriz de puntos LED, ya que la placa principal no está equipada con una fotorresistencia.

### (2) Componentes necesarios:

Micro:bit main board V2

Cable Micro USB

### (3) Código de prueba:

Enlaza el ordenador con la placa micro:bit mediante el cable Micro USB y programa en el editor MakeCode,

![](./media/Makecode_38ffa3b8.gif)

Programa completo :

![](./media/Makecode_5b9a2acf.png)

### (4) Resultados de la prueba:

Sube el código de prueba al micro:bit main board V2, alimenta la placa a través del cable USB y haz clic en "Show console Device".

Cuando la matriz de puntos LED está cubierta con la mano, la intensidad de luz mostrada es aproximadamente 0; cuando la matriz de puntos LED está expuesta a la luz, la intensidad de luz mostrada se vuelve más fuerte con la luz como se muestra a continuación.

![](./media/Makecode_11dd3c0b.gif)

Si estás usando Windows 7 u 8 en lugar de Windows 10, Google Chrome no podrá emparejar los dispositivos. Necesitarás usar el software monitor serie CoolTerm para leer los datos.

Puedes abrir el software CoolTerm, hacer clic en Options, seleccionar SerialPort, configurar el COM port y poner la baud rate a 115200 (después de las pruebas, la baud rate de la comunicación USB SerialPort en el Micro: Bit main board V2 es 115200), hacer clic en OK y Connect. El monitor serie CoolTerm muestra el valor de la intensidad de la luz, como se muestra en las figuras a continuación :

![](./media/Makecode_3c6eae52.gif)

---