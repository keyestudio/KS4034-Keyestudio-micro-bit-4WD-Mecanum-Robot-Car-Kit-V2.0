### プロジェクト16：モーター

![](./media/Python_32655f47.png)

1\.  **説明**

Keyestudio 4WD Mecanum Robot Car は 4 つの DC 減速モーター（ギア減速モーター）を搭載しています。これは通常の DC モーターをベースに開発されており、対応するギア減速ボックスにより低速で大きなトルクを提供します。さらに、減速比の異なるボックスにより速度とトルクを変えることができます。

ギアモーターはギアとモーターの統合体であり、鉄鋼や機械工業で広く応用されています。

Micro:bit 用モータードライバーシールドには STC8G と HR8833 チップが搭載されています。IO ポートのリソースを節約するために、HR8833 チップで 4 つの DC ギアモーターの回転方向と速度を制御します。

**チップの詳細：**

![](./media/Python_d7132b53.jpg)

前面

![](./media/Python_4919ce3b.png)

背面

![](./media/Python_fbfa17f7.png)

STC8G1K08 チップ回路図

![](./media/Python_47cdde6b.png)

HR8833 モータードライバー回路図

2\. **準備**

- micro:bit ボードを keyestudio 4WD Mecanum Robot Car V2.0 のスロットに差し込む

- 電池を電池ホルダーに入れる

- 電源スイッチを ON にする

- micro:bit を USB ケーブルでコンピュータに接続する

- Mu のオフライン版を起動する

3\. **テストコード1**

Mu を起動し、ファイル “microbit-Motor Driving-1\.py” を開いてコードを読み込みます。編集ウィンドウに自分でコードを入力してもかまいません。

（注：すべての英単語と記号は英語で記述する必要があります。）

Click“Files”to import“keyes_mecanum_Car.py”library file to micro:bit . 

「Check」をクリックしてコードのエラーを確認します。下線やカーソルが表示されている場合はプログラムに誤りがあります。

コードが正しければ、micro:bit をコンピュータに接続して「Flash」をクリックし、コードを micro:bit ボードに書き込みます。

![](./media/Python_71476377.png)

```python
from microbit import *
from keyes_mecanum_Car_V2 import *
mecanumCar = Mecanum_Car_Driver_V2()
while True:
    display.show(Image.ARROW_S)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    display.show(Image.ARROW_N)
    mecanumCar.Motor_Upper_L(0, 100)
    mecanumCar.Motor_Lower_L(0, 100)
    mecanumCar.Motor_Upper_R(0, 100)
    mecanumCar.Motor_Lower_R(0, 100)
    sleep(1000)
    display.show(Image.ARROW_E)
    mecanumCar.Motor_Upper_L(0, 100)
    mecanumCar.Motor_Lower_L(0, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    display.show(Image.ARROW_W)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(0, 100)
    mecanumCar.Motor_Lower_R(0, 100)
    sleep(1000)
    display.show(Image("00900:""09990:""99999:""99999:""09090"))
    mecanumCar.Motor_Upper_L(0, 0)
    mecanumCar.Motor_Lower_L(0, 0)
    mecanumCar.Motor_Upper_R(0, 0)
    mecanumCar.Motor_Lower_R(0, 0)
    sleep(1000)
```

4\. **テスト結果1**

コードをボードに正常にダウンロードした後、**外部電源（DIPスイッチをONにする）**、および micro:bit のリセットボタンを押します。

![Img](./media/Python_bb3e1312.png)

すると車は 1 秒前進、1 秒後退、1 秒左旋回、1 秒右旋回、反時計回りに 1 秒、時計回りに 1 秒、そして 1 秒停止します。マトリックス表示にもパターンが表示されます。

5\. **テストコード2**

Mu を起動し、ファイル “microbit-Motor Driving-2\.py” を開いてコードを読み込みます。編集ウィンドウに自分でコードを入力してもかまいません。

（注：すべての英単語と記号は英語で記述する必要があります。）

Click“Files”to import“keyes_mecanum_Car.py“library file to micro:bit. 

「Check」をクリックしてコードのエラーを確認します。下線やカーソルが表示されている場合はプログラムに誤りがあります。

コードが正しければ、micro:bit をコンピュータに接続して「Flash」をクリックし、コードを micro:bit ボードに書き込みます。

![](./media/Python_96230faf.png)

```python
from microbit import button_a, button_b, display, Image, sleep
from keyes_mecanum_Car_V2 import *
mecanumCar = Mecanum_Car_Driver_V2()

show_L = Image("90000:""90000:""90000:""90000:""99999")
show_O = Image("09990:""90009:""90009:""90009:""09990")
a = 0
b = 0
def run_L():
    global b
    sleep(1000)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    mecanumCar.Motor_Upper_L(0, 100)
    mecanumCar.Motor_Lower_L(0, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(650)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    mecanumCar.Motor_Upper_L(0, 0)
    mecanumCar.Motor_Lower_L(0, 0)
    mecanumCar.Motor_Upper_R(0, 0)
    mecanumCar.Motor_Lower_R(0, 0)
    b = 0
def run_O():
    global b
    sleep(1000)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    mecanumCar.Motor_Upper_L(0, 100)
    mecanumCar.Motor_Lower_L(0, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(620)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    mecanumCar.Motor_Upper_L(0, 100)
    mecanumCar.Motor_Lower_L(0, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(620)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    mecanumCar.Motor_Upper_L(0, 100)
    mecanumCar.Motor_Lower_L(0, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(620)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    mecanumCar.Motor_Upper_L(0, 0)
    mecanumCar.Motor_Lower_L(0, 0)
    mecanumCar.Motor_Upper_R(0, 0)
    mecanumCar.Motor_Lower_R(0, 0)
    b = 0
while True:
    if button_a.was_pressed():
        a = a + 1
        if a >= 3:
            a = 0
    if button_b.was_pressed():
        b = 1
    if (a == 1):
        display.show(show_L)
        if b == 1:
            run_L()
    elif a == 2:
        display.show(show_O)
        if b == 1:
            run_O()
```

6\. **テスト結果2**

コードをボードに正常にダウンロードした後、**外部電源（DIPスイッチをONにする）**、および micro:bit のリセットボタンを押します。

![Img](./media/Python_bb3e1312.png)

最初に A ボタンと B ボタンが押されると、micro:bit は「L」を表示し、車の走行パターンは「L」になります。もう一度押すと micro:bit は「口」を表示し、車の走行パターンは「口」になります。これを繰り返します。

7\.  **コード説明**

![Img](./media/Python_70b4e70f.png)

![Img](./media/Python_e3250a8a.png)

---