### プロジェクト12：スピーカーの制御

1\.  **説明**

これまでのプロジェクトでは、タッチ感知ロゴとスピーカーについてそれぞれ学びました。本プロジェクトでは、これら二つのコンポーネントを組み合わせて音楽を再生します。

2\.  **必要な部品**

|![](./media/Python_021507bd.png)|![](./media/Python_84cdea05.jpg)|
|-|-|
|Micro:bit main board \*1|USB cable\*1|


3\.  **配線図**

Micro:bit main board を USB ケーブルでコンピュータに接続します。

![](./media/Python_611b2c4e.png)

4\.  **テストコード**

Mu ソフトウェアを起動し、ファイル “Touch the Logo to control the speaker\.py” を開いてコードをインポートします。編集ウィンドウに直接コードを入力することもできます。

(**注意：すべての単語と記号は英語で記述してください**.)

![](./media/Python_600c8fa6.png)

```python
from microbit import *

import music

display.show(Image.MUSIC_QUAVER)

while True:

    if pin_logo.is_touched():
        music.play(music.BIRTHDAY)
```

“Check” をクリックしてコード内のエラーを確認します。下線やカーソルが表示されている場合はプログラムに誤りがあります。

![](./media/Python_dcc17127.png)

コードに問題がなければ、micro:bit をコンピュータに接続し、“Flash” をクリックしてコードを micro:bit ボードに書き込みます。

![](./media/Python_be3d4ee9.png)

5\.  **テスト結果**

コードをボードに正常にダウンロードしたら、**micro USB ケーブルまたは外部電源で電源を入れてください（DIP スイッチを ON にしてください）**。その後、micro:bit のリセットボタンを押します。

![Img](./media/Python_bb3e1312.png)

ロゴに触れるとスピーカーから「*Happy Birthday to You*」が再生されます。

6\.  **コードの説明**

![Img](./media/Python_852be78f.png)

**Bluetooth 無線通信**

micro:bit は低消費電力の Bluetooth モジュールを搭載して通信できますが、RAM は 16 KB です。しかし、BLE のヒープ/スタックが 12 KB を占有するため、microPython を実行するための十分な空きがありません。

現時点では、microPython は Bluetooth サービスをサポートしていません。

[https://microbit-micropython.readthedocs.io/en/latest/ble.html](https://microbit-micropython.readthedocs.io/en/latest/ble.html)

これまでのプロジェクトはセンサーとモジュールの導入です。以降のレッスンは初心者にとってより難易度が上がります。

(**注意：micro:bit ボードが焼損しないように、車用拡張ボードに取り付ける前に micro USB ケーブルを抜き、micro:bit motor driver base plate の電源を切り、POWER スイッチを OFF にしてください。同様に、メインボードを車用拡張ボードから取り外す前にも micro USB ケーブルを抜き、micro:bit motor driver base plate の電源を切ってください。**)