## Proyecto 6: Sensor geomagnético

[Haga clic para descargar el código 1 de esta lección](./Code/Geomagnetic-Sensor.hex)

[Haga clic para descargar el código 2 de esta lección](./Code/Geomagnetic-Sensor2.hex)

### (1)Descripción del proyecto:

(1) Descripción del proyecto: Este proyecto tiene como objetivo explicar el uso del sensor geomagnético del Micro:bit, que no solo puede detectar la intensidad del campo geomagnético, sino que también puede utilizarse como brújula para encontrar rumbos. También es una parte importante del Attitude and Heading Reference System (AHRS). El Micro:bit main board V2 utiliza el sensor geomagnético LSM303AGR, y el rango dinámico del campo magnético es ± 50 gauss. En la placa, el módulo magnetómetro se utiliza tanto en la detección magnética como en la brújula. En este experimento se introducirá primero la brújula y luego se comprobarán los datos originales del magnetómetro. El componente principal de una brújula común es una aguja magnética, que puede ser girada por el campo geomagnético y apuntar hacia el Polo Norte geomagnético (que está cerca del Polo Sur geográfico) para determinar la dirección.

### (2)Componentes necesarios:

Micro:bit main board V2

 Cable Micro USB

### (3)Código de prueba 1 :

Conecte el ordenador con la placa micro:bit mediante un cable Micro-USB y programe en el editor MakeCode.

![](./media/Makecode_5805c7de.gif)

Programa completo :

![](./media/Makecode_5a958132.png)

### (4)Resultados de la prueba 1 :

Después de cargar el código de prueba en el Micro:bit main board V2 y alimentar la placa a través del cable USB, y al presionar el botón A, la placa nos pide calibrar la brújula y la matriz de puntos LED muestra "TILT TO FILL SCREEN". Luego entra en la página de calibración. Gire la placa hasta que los 25 LED estén en rojo como se muestra a continuación.

![](./media/Makecode_b0a4ebf1.jpg)

calibrar la brújula:

![](./media/Makecode_05a88e21.gif)

Después de eso, aparece un patrón sonriente ![](./media/Makecode_74a69436.png), lo que implica que la calibración está hecha. Cuando el proceso de calibración se completa, al presionar el botón A la lectura del magnetómetro se mostrará directamente en la pantalla. Y las direcciones norte, este, sur y oeste corresponden a 0°, 90°, 180° y 270° respectivamente.

![](./media/Makecode_23b07bfb.gif)

### (5) Código de prueba 2:

Este módulo puede seguir leyendo datos para determinar la dirección, por lo que apunta al polo norte magnético actual con una flecha.

Conecte el ordenador con la placa micro:bit mediante un cable Micro-USB y programe en el editor MakeCode,

![](./media/Makecode_db8b2d7e.gif)

Programa completo :

![](./media/Makecode_ef823069.png)

### (6) Resultados de la prueba 2

Suba el código 2. Después de la calibración, incline la placa micro:bit y la matriz de puntos LED mostrará los signos de dirección.

![](./media/Makecode_d8944d5f.gif)

---