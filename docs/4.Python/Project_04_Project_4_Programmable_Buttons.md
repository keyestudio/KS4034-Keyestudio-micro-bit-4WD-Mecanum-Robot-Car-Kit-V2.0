### プロジェクト4：プログラム可能なボタン

![](./media/Python_06be84fb.png)

1\.  **説明**

![](./media/Python_b6d60ae2.png)

ボタンは回路の制御に使用できます。プッシュボタンを備えた回路では、ボタンを押している間は回路が接続され、放すと再び開放されます。

ボタンの両端は2つの山のようです。間に川があります。  
内部の金属片が両側をつなぎ、電流を通す、まるで山と山を結ぶ橋を作るようなものです。

ボタンの内部構造は次のように示されます：ボタンを押す前は1、2、3、4がオンになっています。ただし、1と3、または1と4、または2と3、または2と4の組み合わせは切断されており、これらはボタンが押されたときにのみ接続されます。 ![](./media/Python_d2a204e6.png)

micro:bitメインボードには3つのプッシュボタンがあり、2つはプログラム可能なボタン（AとBで表示）、もう1つはリセットボタンです。プログラム可能な2つのボタンを使うことで3種類の信号を入力できます。AまたはBを単独で押すか、両方を同時に押すと、LEDドットマトリクスはそれぞれA、B、ABを表示します。始めましょう。

2\.  **準備**

A. USBケーブルでmicro:bitメインボードをコンピュータに接続します。

B. オフライン版のMuを開きます。

3\.  **テストコード1**

Muソフトを起動し、ファイル “Programmable Buttons-1\.py” を開いてコードを読み込みます。編集ウィンドウに自分でコードを入力することもできます。

(**注：すべての単語と記号は英語で記述してください。**)

![](./media/Python_2637f524.png)

```python
from microbit import *

while True:
    if button_a.is_pressed():
        display.show("A")
    elif button_a.is_pressed() and button_b.is_pressed():
        display.scroll("AB")
    elif button_b.is_pressed():
        display.show("B")
```
「Check」をクリックしてコードのエラーを確認します。下線やカーソルが表示されている場合はプログラムに誤りがあります。

![](./media/Python_a0f284f3.png)

コードが正しければ、micro:bitをコンピュータに接続して「Flash」をクリックし、コードをmicro:bitボードに書き込みます。

![](./media/Python_5694d3ce.png)

4\.  **テスト結果1**

コードをボードに正常にダウンロードした後、**micro USBケーブルまたは外部電源で電源を入れてください（DIPスイッチをONにする）**。その後ボードのリセットボタンを押します。

![Img](./media/Python_bb3e1312.png)

5×5のLEDドットマトリクスは、ボタンAが押されると「A」を表示し、ボタンBが押されると「B」を表示し、AとBが同時に押されると「AB」を表示します。

5\.  **テストコード2**

Muソフトを起動し、ファイル “Programmable Buttons-2\.py” を開いてコードを読み込みます。編集ウィンドウに自分でコードを入力することもできます。

(**注：すべての単語と記号は英語で記述してください。**)

![](./media/Python_1a1126f6.png)

![](./media/Python_94849305.png)

```python
from microbit import *
a = 0
b = 0
val1 = Image("00000:""00000:""00000:""00000:""00900")
val2 = Image("00000:""00000:""00000:""00900:""99999")
val3 = Image("00000:""00000:""00900:""99999:""99999")
val4 = Image("00000:""00900:""99999:""99999:""99999")
val5 = Image("00900:""99999:""99999:""99999:""99999")
val6 = Image("99999:""99999:""99999:""99999:""99999")
display.show(val1)

while True:
    while button_a.is_pressed() == True:
        sleep(10)
        if button_a.is_pressed() == False:
            a = a + 1
            if(a >= 5):
                a = 5
            break
    while button_b.is_pressed() == True:
        sleep(10)
        if button_b.is_pressed() == False:
            a = a - 1
            if(a <= 0):
                a = 0
            break
    if a == 0:
        display.show(val1)
    if a == 1:
        display.show(val2)
    if a == 2:
        display.show(val3)
    if a == 3:
        display.show(val4)
    if a == 4:
        display.show(val5)
    if a == 5:
        display.show(val6)
```
「Check」をクリックしてコードのエラーを確認します。下線やカーソルが表示されている場合はプログラムに誤りがあります。

![](./media/Python_21771d90.png)

![Img](./media/Python_8d257384.png)

コードが正しければ、micro:bitをコンピュータに接続して「Flash」をクリックし、コードをmicro:bitボードに書き込みます。

![](./media/Python_84ba8cde.png)

![Img](./media/Python_8d257384.png)

6\.  **テスト結果2**

コードをボードに正常にダウンロードした後、**micro USBケーブルまたは外部電源で電源を入れてください（DIPスイッチをONにする）**。その後ボードのリセットボタンを押します。

![Img](./media/Python_bb3e1312.png)

ボタンAを押すと赤く点灯するLEDが増え、ボタンBを押すと赤く点灯するLEDが減ります。

7\.  **コードの説明**

![Img](./media/Python_b33858dc.png)

![Img](./media/Python_32bd1cca.png)

---