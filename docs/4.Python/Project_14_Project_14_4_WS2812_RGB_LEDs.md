### プロジェクト14: 4個のWS2812 RGB LED

![](./media/Python_eecf79fe.png)

1\.  **説明**

このドライバシールドは4個のWS2812 RGB LEDと連携し、micro:bitボードに対応しP7で制御されます。本レッスンでは、P7を使ってRGB LEDに異なる色を表示させます。本レッスンでは、4個のWS2812 RGB LEDにさまざまなエフェクトを表示させるためのテストコードを3セット提供します。

![Img](./media/Python_0be70eda.png)

2\.  **準備**

- micro:bitボードをkeyestudio 4WD Mecanum Robot Car V2.0のスロットに差し込む

- 電池を電池ホルダーに入れる

- 電源スイッチをON側に切り替える

- micro:bitをUSBケーブルでコンピュータに接続する

- Muのオフライン版を開く。

3\.  **テストコード1**

Muソフトを起動し、ファイル“4 WS2812 RGB LEDs-1\.py”を開いてコードをインポートします\ または編集ウィンドウに自分でコードを入力することもできます。

(**注意: すべての英単語と記号は英語で記述してください。**)

“Check”をクリックしてコードのエラーを確認します。下線やカーソルが表示されている場合、プログラムに誤りがあります。 

![](./media/Python_5b5266e2.png)

```python
from microbit import *
import neopixel
np = neopixel.NeoPixel(pin7, 4)
while True:
    for pixel_id1 in range(0, len(np)):
        np[pixel_id1] = (255, 0, 0)
        np.show()
    sleep(1000)
    for pixel_id2 in range(0, len(np)):
        np[pixel_id2] = (255, 165, 0)
        np.show()
    sleep(1000)
    for pixel_id3 in range(0, len(np)):
        np[pixel_id3] = (255, 255, 0)
        np.show()
    sleep(1000)
    for pixel_id4 in range(0, len(np)):
        np[pixel_id4] = (0, 255, 0)
        np.show()
    sleep(1000)
    for pixel_id5 in range(0, len(np)):
        np[pixel_id5] = (0, 0, 255)
        np.show()
    sleep(1000)
    for pixel_id6 in range(0, len(np)):
        np[pixel_id6] = (75, 0, 130)
        np.show()
    sleep(1000)
    for pixel_id7 in range(0, len(np)):
        np[pixel_id7] = (238, 130, 238)
        np.show()
    sleep(1000)
    for pixel_id8 in range(0, len(np)):
        np[pixel_id8] = (160, 32, 240)
        np.show()
    sleep(1000)
    for pixel_id9 in range(0, len(np)):
        np[pixel_id9] = (255, 255, 255)
    sleep(1000)
```

コードが正しければ、micro:bitをコンピュータに接続し“Flash”をクリックしてコードをmicro:bitボードに書き込みます。

![](./media/Python_56a9ab63.png)

4\.  **テスト結果1**

コードをボードに正常にダウンロードした後、**外部電源を入れる（DIPスイッチをONにする）**、そしてmicro:bitのリセットボタンを押します。

![Img](./media/Python_bb3e1312.png)

4個のWS2812RGB LEDが順番に周期的に異なる色で点灯します。

5\.  **テストコード2**

Muソフトを起動し、ファイル“4 WS2812 RGB LEDs-2\.py”を開いてコードをインポートします。編集ウィンドウに自分でコードを入力することもできます。

(**注意: すべての英単語と記号は英語で記述してください**.)

“Check”をクリックしてコードのエラーを確認します。下線やカーソルが表示されている場合、プログラムに誤りがあります。 

コードが正しければ、micro:bitをコンピュータに接続し“Flash”をクリックしてコードをmicro:bitボードに書き込みます。

![](./media/Python_8cb1dd7c.png)

```python
from microbit import *
import neopixel
np = neopixel.NeoPixel(pin7, 4)
while True:
    for index in range(0, 4):
        np.clear()
        np[index] = (255, 0, 0)
        np.show()
        sleep(100)
    for index1 in range(0, 4):
        np.clear()
        np[index1] = (255, 165, 0)
        np.show()
        sleep(100)
    for index2 in range(0, 4):
        np.clear()
        np[index2] = (255, 255, 0)
        np.show()
        sleep(100)
    for index3 in range(0, 4):
        np.clear()
        np[index3] = (0, 255, 0)
        np.show()
        sleep(100)
    for index4 in range(0, 4):
        np.clear()
        np[index4] = (0, 0, 255)
        np.show()
        sleep(100)
    for index5 in range(0, 4):
        np.clear()
        np[index5] = (75, 0, 130)
        np.show()
        sleep(100)
    for index6 in range(0, 4):
        np.clear()
        np[index6] = (238, 130, 238)
        np.show()
        sleep(100)
    for index7 in range(0, 4):
        np.clear()
        np[index7] = (160, 32, 240)
        np.show()
        sleep(100)
    for index8 in range(0, 4):
        np.clear()
        np[index8] = (255, 255, 255)
        np.show()
        sleep(100)
```

6\.  **テスト結果2**

コードをボードに正常にダウンロードした後、**外部電源を入れる（DIPスイッチをONにする）**、そしてmicro:bitのリセットボタンを押します。

![Img](./media/Python_bb3e1312.png)

WS2812RGB LEDは流れる光のような表示をします。

7\.  **テストコード3**

Muソフトを起動し、ファイル“4 WS2812 RGB LEDs-3\.py”を開いてコードをインポートします。編集ウィンドウに自分でコードを入力することもできます。

(**注意: すべての英単語と記号は英語で記述してください。**)

“Check”をクリックしてコードのエラーを確認します。下線やカーソルが表示されている場合、プログラムに誤りがあります。 

コードが正しければ、micro:bitをコンピュータに接続し“Flash”をクリックしてコードをmicro:bitボードに書き込みます。

![](./media/Python_b248f1c5.png)

```python
from microbit import *
import neopixel
np = neopixel.NeoPixel(pin7, 4)
from random import randint
R = 0
G = 0
B = 0
while True:
   for index in range(0, 4):
        R = randint(10, 255)
        G = randint(10, 255)
        B = randint(10, 255)
        np.clear()
        np[index] = (R, G, B)
        np.show()
        sleep(500)
```

8\.  **テスト結果3**

コードをボードに正常にダウンロードした後、**外部電源を入れる（DIPスイッチをONにする）**、そしてmicro:bitのリセットボタンを押します。

![Img](./media/Python_bb3e1312.png)

各WS2812RGBライトが順番にランダムな色を表示します。

5\.  **コードの説明**

![Img](./media/Python_d1e3977b.png)

---