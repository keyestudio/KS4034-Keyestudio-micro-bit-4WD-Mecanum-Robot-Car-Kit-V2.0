## Proyecto 5: Detección de temperatura

![](./media/Makecode_22c6434f.jpg)

[Haga clic para descargar el código 1 de esta lección](./Code/Temperature-Detection.hex)

[Haga clic para descargar el código 2 de esta lección](./Code/Temperature-Detection2.hex)

### (1)Descripción del proyecto:

La Micro:bit main board V2 no está equipada con un sensor de temperatura dedicado, sino que utiliza el sensor de temperatura integrado en el chip NFR52833 para la detección. Por lo tanto, la temperatura detectada está más cercana a la del chip y puede diferir de la temperatura ambiente.

### (2)Componentes necesarios:

Micro:bit main board V2

Cable Micro USB

### (3)Código de prueba 1 :

![](./media/Makecode_e6674fe9.gif)

### (4)Resultados de la prueba 1:

Tras subir el código de prueba 1 a la Micro:bit main board V2, alimentar la placa mediante el cable USB y hacer clic en "Show console Device", los datos de temperatura se muestran en la página del monitor serie como se indica a continuación.

![](./media/Makecode_898eded8.gif)

Si está utilizando Windows 7 u 8 en lugar de Windows 10, Google Chrome no podrá emparejar los dispositivos. Deberá usar el software de monitor serie CoolTerm para leer los datos. Abra CoolTerm, haga clic en Options, seleccione SerialPort, ajuste el puerto COM y establezca la velocidad en baudios a 115200 (tras las pruebas, la velocidad en baudios de la comunicación USB SerialPort en la Micro:bit main board V2 es 115200), haga clic en OK y luego en Connect. El monitor serie CoolTerm muestra el cambio de temperatura en el entorno actual, como se muestra en las siguientes imágenes:

![](./media/Makecode_268159a1.gif)

### (5)Código de prueba 2 :

Enlace el ordenador con la placa micro:bit mediante un cable Micro USB y programe en el editor MakeCode,

![](./media/Makecode_4057bdd7.gif)

Programa completo :

![](./media/Makecode_ec457959.png)

### (6)Resultados de la prueba 2:

Después de subir el código 2, cuando la temperatura ambiente es inferior a 35℃, la matriz de puntos LED 5x5 muestra ![](./media/Makecode_350d26c6.png). Cuando la temperatura es igual o superior a 35℃ aparece el patrón ![](./media/Makecode_ef8d7c88.png).

---