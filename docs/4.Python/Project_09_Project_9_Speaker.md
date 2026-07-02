### プロジェクト 9：スピーカー

![](./media/Python_ac515b9a.png)

1\.  **説明**

micro:bit メインボードには内蔵スピーカーがあり、プログラムに音を追加するのが容易になります。*Ode to Joy* のような曲を再生するなど、さまざまな音色を出すようにプログラムすることもできます。

2\.  **準備**

A. USB ケーブルで micro:bit メインボードをコンピュータに接続します

B. オフライン版の Mu を開きます。

3\.  **テストコード**

Mu ソフトを起動し、ファイル “Speaker\.py” を開いてコードを読み込みます。編集ウィンドウに直接コードを入力することもできます。

(**注意: すべての単語と記号は英語で記述する必要があります**.)

![](./media/Python_eec7f643.png)

```python
from microbit import *

import audio

display.show(Image.MUSIC_QUAVER)

while True:
    audio.play(Sound.GIGGLE)
    sleep(1000)
    audio.play(Sound.HAPPY)
    sleep(1000)
    audio.play(Sound.HELLO)
    sleep(1000)
    audio.play(Sound.YAWN)
    sleep(1000)
```

“Check” をクリックしてコードのエラーを確認します。下線やカーソルが表示される場合、プログラムは誤りがあります。

![](./media/Python_f8852abf.png)

コードが正しければ、micro:bit をコンピュータに接続して “Flash” をクリックし、コードを micro:bit ボードに書き込みます。

![](./media/Python_3fd94e43.png)

4\.  **テスト結果**

コードがボードに正常にダウンロードされたら、**micro USB ケーブルまたは外部電源で電源を入れる（DIP スイッチを ON にする）**、その後 micro:bit のリセットボタンを押します。

![Img](./media/Python_bb3e1312.png)

 スピーカーから音が鳴り、LED ドットマトリクスに音楽のロゴが表示されます。

5\.  **コードの説明**

![Img](./media/Python_18c047bd.png)

---