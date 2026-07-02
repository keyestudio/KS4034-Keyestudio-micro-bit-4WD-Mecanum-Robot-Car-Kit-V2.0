## プロジェクト5：温度検出

![](./media/Makecode_22c6434f.jpg)

[このレッスンのコード1をダウンロードするにはクリック](./Code/Temperature-Detection.hex)

[このレッスンのコード2をダウンロードするにはクリック](./Code/Temperature-Detection2.hex)

### (1)プロジェクトの説明：

Micro:bit main board V2 は温度センサーを搭載していませんが、NFR52833 チップに内蔵された温度センサーを使用して温度を検出します。したがって、検出される温度はチップの温度に近く、周囲温度とは差が生じる場合があります。

### (2)必要なコンポーネント：

Micro:bit main board V2

Micro USB ケーブル

### (3)テストコード1：

![](./media/Makecode_e6674fe9.gif)

### (4)テスト結果1：

テストコード1を Micro:bit main board V2 にアップロードし、USBケーブルでボードに電源を供給し、"Show console Device" をクリックすると、下図のようにシリアルモニターページに温度データが表示されます。

![](./media/Makecode_898eded8.gif)

Windows 10 ではなく Windows 7 または 8 を使用している場合、Google Chrome はデバイスをマッチングできません。データを読み取るには CoolTerm シリアルモニターソフトを使用する必要があります。CoolTerm を開き、Options をクリックし、SerialPort を選択して COM ポートを設定し、ボーレートを 115200 に設定します（テストによれば、Micro:bit main board V2 の USB SerialPort 通信のボーレートは 115200 です）。OK をクリックして Connect を押すと、CoolTerm シリアルモニターに現在の環境の温度変化が表示されます。以下の図を参照してください：

![](./media/Makecode_268159a1.gif)

### (5)テストコード2：

Micro USB ケーブルでコンピュータと micro:bit ボードを接続し、MakeCode エディタでプログラムを作成します、

![](./media/Makecode_4057bdd7.gif)

完全なプログラム：

![](./media/Makecode_ec457959.png)

### (6)テスト結果2：

コード2をアップロードした後、周囲温度が35℃未満の場合、5×5 LED ドットマトリクスは ![](./media/Makecode_350d26c6.png) を表示します。温度が35℃以上の場合は、パターン ![](./media/Makecode_ef8d7c88.png) が表示されます。

---