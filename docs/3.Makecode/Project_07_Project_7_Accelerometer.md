## Proyecto 7: Accelerometer

![](./media/Makecode_66670811.jpg)

[Haga clic para descargar el código 1 de esta lección](./Code/Accelerometer.hex)

[Haga clic para descargar el código 2 de esta lección](./Code/Accelerometer2.hex)

### (1)Descripción del proyecto:

La Micro: Bit main board V2 tiene un sensor de aceleración gravitatoria integrado LSM303AGR, también conocido como acelerómetro, con una resolución de 8/10/12 bits. En la sección de código se puede establecer el rango en 1g, 2g, 4g y 8g.

A menudo utilizamos acelerómetros para detectar el estado de las máquinas. En este proyecto, introduciremos cómo medir la posición de la placa con el acelerómetro y, a continuación, veremos los datos originales de tres ejes que proporciona el acelerómetro.

### (2)Componentes necesarios:

Micro:bit main board V2

Cable Micro USB

### (3)Código de prueba 1:

Conecte el ordenador a la placa micro:bit mediante un cable Micro USB y programe en el editor MakeCode,

![](./media/Makecode_2cd48603.gif)

Programa completo:

![](./media/Makecode_ba28162b.png)

### (4)Resultados de la prueba 1:

Después de cargar el Código de Prueba 1 en la placa micro:bit V2, cambiar la orientación de la placa hará que la matriz de puntos 5x5 muestre diferentes números.

![](./media/Makecode_2e6708e6.gif)

Si agitamos la Micro: Bit main board V2, sin importar la dirección, la matriz de LED muestra el dígito "1".

Cuando se mantiene en posición vertical (con su logotipo sobre la matriz de LED), aparece el número 2.

![](./media/Makecode_67247ae1.jpg)

Cuando se mantiene boca abajo (con su logotipo debajo de la matriz de LED), se muestra como abajo.

![](./media/Makecode_1668a9d0.jpg)

Cuando se coloca quieta en el escritorio con el lado delantero hacia arriba, aparece el número 4.

![](./media/Makecode_0dd33fa1.jpg)

Cuando se coloca quieta en el escritorio con el lado trasero hacia arriba, aparece el número 5.

Cuando la placa se inclina hacia la izquierda, la matriz de LED muestra el número 6 como se muestra a continuación.

![](./media/Makecode_ce2b3501.jpg)

Cuando la placa se inclina hacia la derecha, la matriz de LED muestra el número 7 como se muestra a continuación.

![](./media/Makecode_d098ff98.jpg)

Cuando la placa se golpea contra el suelo, este proceso puede considerarse una caída libre y la matriz de LED muestra el número 8. (tenga en cuenta que esta prueba no se recomienda porque puede dañar la placa principal.)

Atención: si desea probar esta función, también puede configurar la aceleración en 3g, 6g u 8g. Aun así, no lo recomendamos.

### (5)Código de prueba 2:

![](./media/Makecode_99083bf6.gif)

Programa completo:

![](./media/Makecode_42654b0e.png)

### (6) Resultados de la prueba 2

Cargue el código de prueba en la Micro: Bit main board V2, alimente la placa principal a través del cable USB y haga clic en "Show console Device".

La interfaz siguiente muestra los valores de descomposición de la aceleración en los ejes X, Y y Z respectivamente, así como la síntesis de la aceleración (combinación de la gravedad y otras fuerzas externas).

![](./media/Makecode_c17f5477.gif)

Tras consultar el manual de datos del MMA8653FC y el diagrama esquemático de hardware de la Micro: Bit main board V2, las coordenadas del acelerómetro de la placa base Micro: Bit V2 se muestran en la figura siguiente:

![](./media/Makecode_79d90885.jpg)

Si está usando Windows 7 u 8 en lugar de Windows 10, Google Chrome no podrá emparejar los dispositivos. Deberá usar el software de monitor serie CoolTerm para leer los datos. Puede abrir CoolTerm, hacer clic en Options, seleccionar SerialPort, configurar el puerto COM y ajustar la velocidad en baudios a 115200 (tras las pruebas, la velocidad en baudios de la comunicación USB SerialPort en Micro: Bit main board V2 es 115200), hacer clic en OK y Connect. El monitor serie CoolTerm muestra los datos de los ejes X, Y y Z, como se muestra en las figuras siguientes:

![](./media/Makecode_2a63fc72.gif)