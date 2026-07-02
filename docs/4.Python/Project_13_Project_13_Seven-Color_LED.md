### プロジェクト 13: 七色LED

![](./media/Python_804e502b.png)

1\.  **説明**

このモジュールは、一般的に使用される7色のLEDで構成されていますが、見た目は白色です。通常のLEDと同様にハイレベルが入力されると自動的に異なる色を点滅させ、素晴らしい光の効果を作り出すことができます。

2\.  **準備**

- micro:bitボードをkeyestudio 4WD Mecanum Robot Car V2.0のスロットに挿入します

- 電池を電池ホルダーに入れます

- 電源スイッチをONにします

- USBケーブルでmicro:bitをコンピュータに接続します

- Muのオフライン版を開きます。

3\.  **テストコード**

Muソフトウェアを起動し、ファイル“Colorful lights\.py”を開いてコードをインポートします。編集ウィンドウに自分でコードを入力することもできます。

（**注意：すべての単語と記号は英語で記述してください**。）

![](./media/Python_010a8a12.png)

```python
from microbit import *
from keyes_mecanum_Car_V2 import *

mecanumCar = Mecanum_Car_Driver_V2()

while True:
    mecanumCar.left_led(1)
    mecanumCar.right_led(1)
    sleep(3000)
    mecanumCar.left_led(0)
    mecanumCar.right_led(0)
    sleep(3000)
```

**重要なお知らせ：** ライブラリファイル 'keyes_mecanum_Car_V2.py' がまだmicro:bitボードにインポートされていない場合は、まずライブラリファイルをmicro:bitボードにインポートする必要があります。ライブラリのインポート方法は次のリンクをクリックして確認してください： [How to Import Library to Micro:bit](https://docs.keyestudio.com/プロジェクトs/KS4034/en/latest/docs/Python/Python.html#how-mu-import-library-to-micro-bit) 。指示に従わないとコードは実行されません。

ライブラリファイルが正常にインポートされたら、コードをチェックするために「Check」ボタンもクリックする必要があります。特定の行にカーソルや下線が表示される場合、そのプログラムにはエラーがあります。

![](./media/Python_ce67f468.png)

ただし、このプロセス中に、コードにエラーがなくても次のようなプロンプトが表示されることがあります。これらのプロンプトは警告であり、コードのエラーメッセージではありません。

![](./media/Python_863bb61b.png)

![](./media/Python_ccfbfa56.png)

コードが正しければ、micro:bitをコンピュータに接続し、「Flash」をクリックしてコードをmicro:bitボードにダウンロードします。

![](./media/Python_39512a13.png)

「Flash」ボタンをクリックした後にエラーが表示される場合は、提供されたライブラリファイル "keyes_mecanum_Car_V2.py" をインポートしているか確認してください。

**注意：** Micropythonでプログラミングする前に、ライブラリファイル "keyes_mecanum_Car_V2.py" をmicro:bitにインポートする必要があります。別のmicro:bitでプログラムする場合は、ライブラリファイル "keyes_mecanum_Car_V2.py" を新しいmicro:bitに再度インポートする必要があります。

4\. **テスト結果**

コードをボードに正常にダウンロードしたら、**外部電源（DIPスイッチをONにする）**し、micro:bitのリセットボタンを押します。

![Img](./media/Python_bb3e1312.png)

七色LEDは3秒間点滅し、次に3秒間停止し、このパターンを繰り返します。

5\. **コードの説明**

![Img](./media/Python_a4a670c0.png)