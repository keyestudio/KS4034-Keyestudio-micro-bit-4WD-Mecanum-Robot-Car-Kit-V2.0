## Resource Download

Para ayudarte a obtener rápidamente los códigos relacionados, bibliotecas y otros archivos de soporte para este producto, haz clic en los enlaces siguientes para descargar:

- [Python Code and library downloads](./PythonCode.7z)

## Comenzando con Python

Este tutorial está escrito para el lenguaje Python. Si deseas usar programación mediante gráficos, consulta el manual "Makecode Tutorial". En el directorio raíz del recurso que descargaste hay una carpeta llamada "Python tutorial", que almacena todo el código Python del Micro:bit 4WD Mecanum Robot Car V2.0. El archivo de código Python es un archivo que termina con ".py".

### ¿Qué es MicroPython?

Python es un lenguaje basado en texto, ampliamente utilizado en educación y también empleado por programadores profesionales en campos como ciencia de datos y aprendizaje automático.

Micro: bit puede programarse en Python; al tratarse de un microcontrolador, las diferencias de hardware impiden que el micro: bit soporte Python por completo. MicroPython está dedicado al micro：bit y es una implementación eficiente del lenguaje de programación Python3. Contiene una pequeña porción de la biblioteca estándar de Python y está optimizado para ejecutarse en microcontroladores micro:bit.

La versión de Python utilizada por BBC micro: bit se llama MicroPython. MicroPython es perfecto para quienes desean aprender más sobre programación; te ayuda a programar con una serie de fragmentos de código y una variedad de gráficos y música predefinidos.

Enlace para BBC microbit MicroPyth: [BBC micro:bit MicroPython ](https://microbit-micropython.readthedocs.io/en/latest/tutorials/introduction.html) 

**Python tiene dos tipos de editores: versión web y versión sin conexión**

1\.  Versión web: [https://python.microbit.org/v/1.1](https://python.microbit.org/v/1.1)

![](./media/Python_693f76f5.png)

2\.  El otro es también el compilador offline — Mu ![](./media/Python_153c77ed.png)

Sitio oficial de Mu: [https://codewith.mu/](https://codewith.mu/)

### Mu

Mu, un editor de código Python, es adecuado para principiantes. No es compatible con Windows de 32 bits.

1\.  **Descargar Mu**

Haz clic en “This PC” y haz clic derecho en Propiedades para comprobar la versión de tu equipo.

![](./media/Python_3a58be54.png)

Comprueba el tipo de sistema de tu equipo.

![](./media/Python_e774ae15.png)

Accede al enlace de MU: [https://codewith.mu/en/download](https://codewith.mu/en/download) para descargar la versión correspondiente de Mu.

![](./media/Python_ceb4cfa6.png)

2\.  **Ejecutar instalación**

Abre el archivo a continuación

![](./media/Python_8bcfe24c.png)

Mac OSX: [https://codewith.mu/en/howto/1.1/install_macos](https://codewith.mu/en/howto/1.1/install_macos).

Linux: [https://codewith.mu/en/howto/1.2/install_linux](https://codewith.mu/en/howto/1.2/install_linux).

**Windows 10**

Verás que aparece una ventana emergente; haz clic en “More info”.

![](./media/Python_877beb7b.png)

Luego haz clic en “Run anyway”.

![](./media/Python_c87475e5.png)

3\. Acuerdo de licencia

Haz clic en “Install”.

![](./media/Python_33f42b66.png)

![](./media/Python_f5c6698f.png)

Tras la instalación, haz clic en “finish”.

![](./media/Python_c6ec7436.png)

4\. Iniciar Mu

A continuación, encuéntralo según la imagen siguiente

![](./media/Python_c4adbdd1.png)

Su interfaz principal se muestra a continuación:

![](./media/Python_3697c0c7.png)

### Uso de modos y barra de menús

Configure “<span style="color: rgb(255, 76, 65);">**Mode**</span>” en BBC micro:bit.

En el menú, haga clic en “**Mode**” para configurarlo en “**BBC micro：bit**”. El modo micro:bit sabe cómo interactuar y conectarse a un micro:bit.

![](./media/Python_18512c7e.png)

Haga clic para [Start with Mu](https://codewith.mu/en/tutorials/1.1/start).

### Cómo Mu importa una biblioteca al Micro:bit

<span style="color: rgb(255, 76, 65);">**Antes de importar bibliotecas, necesitamos cargar un código .py (un código vacío también está bien) en la placa micro:bit. Aquí tomamos un código vacío como ejemplo.**</span>

Conecte la placa al ordenador mediante un cable USB. Abra Mu y haga clic en “Flash” para cargar el código .py (incluso vacío) en la placa.

![Img](./media/Python_611b2c4e.png)

En este tutorial se utiliza el archivo de biblioteca "keyes_mecanum_Car_V2.py". Por lo tanto, importe el archivo de biblioteca "keyes_mecanum_Car_V2.py" en el micro:bit. Este archivo contiene el método de control del Micro:bit 4WD Mecanum Robot Car V2.0.

El directorio predeterminado donde Mu guarda los archivos es “mu_code” en el directorio raíz del usuario.

Enlace de referencia: [https://codewith.mu/en/tutorials/1.0/files](https://codewith.mu/en/tutorials/1.0/files)

**Los métodos para encontrar la carpeta "mu_code":**

**Método uno:**

Por ejemplo, en el sistema Windows, supongamos que su sistema está instalado en la unidad C del ordenador y el nombre de usuario es "**Administrator**", entonces la ruta del directorio "**mu_code**" es "**C:\Users\Administrator\mu_ code**". En sistemas Linux, la ruta del directorio "**mu_code**" es "**~/home/mu_code**".

Abra la carpeta “**mu_code**”.

![](./media/Python_d271a924.png)

**Método dos:**

Busque la carpeta “mu_code” en el Disco (C:).

![Img](./media/Python_03ff037e.png)

![Img](./media/Python_54199d45.png)

Abra “mu_code”.

![Img](./media/Python_4841ca3f.png)

La ruta de la carpeta de datos donde se encuentra el archivo de biblioteca “keyes_mecanum_Car.py” que proporcionamos es la siguiente:

![Img](./media/Python_7adb2b68.png)

Copie el archivo de biblioteca “keyes_mecanum_Car.py” en la carpeta “mu_code”。Cuando se complete la copia, como se muestra a continuación:

![](./media/Python_d753d652.png)

Primero abra el software Mu y conecte el micro:bit a su ordenador, luego haga clic en el botón "Files" y arrastre el archivo de biblioteca "keyes_mecanum_Car.py" al micro:bit.

![](./media/Python_aeaae2b7.png)

Pasados unos segundos, la importación se completa y puede verlo en el cuadro de la izquierda.

![](./media/Python_2be967ca.png)