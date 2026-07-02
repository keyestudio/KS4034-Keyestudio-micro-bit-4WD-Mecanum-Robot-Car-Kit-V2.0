## プロジェクト 2: Light A Single LED

![](./media/Makecode_2423afc6.jpg)

[このレッスンのコードをダウンロードするにはクリックしてください](./Code/Light-A-Single-LED.hex)

### (1)プロジェクトの説明:

(1)プロジェクトの説明: LEDドットマトリクスは、5×5 の正方形に配置された25個のLEDで構成されています。これらのLEDを素早く特定するために、下図のようにこのマトリクスを座標系と見なし、行を上から下へ0〜4、列を左から右へ0〜4と番号付けして二つの軸を作ります。したがって、1行目の2番目にあるLEDは (1,0) で、4列目の5番目にあるLEDは (3,4) となり、他も同様です。

![](./media/Makecode_4ab9ecab.png)

### (2)必要なコンポーネント:

Micro:bit main board V2

Micro USB ケーブル

### (3)テストコード:

Micro USB ケーブルで Micro:bit main board V2 をコンピュータに接続し、編集を開始します。

![](./media/Makecode_1bbd8a3b.gif)

完全なプログラム:

![](./media/Makecode_da248db5.png)

### (4)テスト結果

コードをアップロードすると、Microbitボードは次のように表示します: (1,0) が0.5秒点灯して消灯し、続いて (3,4) が0.5秒点灯して消灯する、という動作がループで繰り返されます。

![](./media/Makecode_301232e3.gif)