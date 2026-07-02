## プロジェクト 7: Accelerometer

![](./media/Makecode_66670811.jpg)

[Click to download the code 1 for this lesson](./Code/Accelerometer.hex)

[Click to download the code 2 for this lesson](./Code/Accelerometer2.hex)

### (1)プロジェクトの説明:

Micro: Bit main board V2 には、LSM303AGR の重力加速度センサー（一般に加速度計と呼ばれる）が内蔵されており、分解能は 8/10/12 ビットです。コード内で測定レンジを 1g、2g、4g、8g に設定できます。

加速度計は機械の状態検出によく使用されます。本プロジェクトでは、加速度計を使って基板の姿勢を測定する方法を紹介し、加速度計が出力する元の三軸データを確認します。

### (2)必要な部品:

Micro:bit main board V2

Micro USB ケーブル

### (3)テストコード 1:

パソコンと micro:bit ボードを Micro USB ケーブルで接続し、MakeCode エディタでプログラムします。

![](./media/Makecode_2cd48603.gif)

完全なプログラム:

![](./media/Makecode_ba28162b.png)

### (4)テスト結果 1:

テストコード 1 を micro:bit V2 ボードにアップロードした後、基板の向きを変えると 5x5 ドットマトリクスに異なる数字が表示されます。

![](./media/Makecode_2e6708e6.gif)

Micro: Bit main board V2 を振ると、どの方向であっても LED ドットマトリクスは数字「1」を表示します。

基板を直立させ（ロゴが LED ドットマトリクスの上に来るように）保持すると、数字 2 が表示されます。

![](./media/Makecode_67247ae1.jpg)

基板を逆さまに（ロゴが LED ドットマトリクスの下に来るように）保持すると、下図のように表示されます。

![](./media/Makecode_1668a9d0.jpg)

机の上に静置し、表側が上を向いているときは、数字 4 が表示されます。

![](./media/Makecode_0dd33fa1.jpg)

机の上に静置し、裏側が上を向いているときは、数字 5 が表示されます。

基板が左に傾くと、LED ドットマトリクスは下図のように数字 6 を表示します。

![](./media/Makecode_ce2b3501.jpg)

基板が右に傾くと、LED ドットマトリクスは下図のように数字 7 を表示します。

![](./media/Makecode_d098ff98.jpg)

基板を床に落とすと、この過程は自由落下とみなすことができ、LED ドットマトリクスは数字 8 を表示します。（このテストは基板を破損する可能性があるため推奨しません。）

注意：この機能を試したい場合、加速度を 3g、6g、または 8g に設定することもできます。ただし、当社としては推奨しません。

### (5)テストコード 2:

![](./media/Makecode_99083bf6.gif)

完全なプログラム:

![](./media/Makecode_42654b0e.png)

### (6) テスト結果 2

テストコードを Micro: Bit main board V2 にアップロードし、USB ケーブルで基板の電源を供給してから "Show console Device" をクリックします。

以下の画面は、X 軸、Y 軸、Z 軸それぞれの加速度の分解値と、加速度合成（重力およびその他の外力の合成）を示しています。

![](./media/Makecode_c17f5477.gif)

MMA8653FC のデータマニュアルおよび Micro: Bit main board V2 のハードウェア回路図を参照すると、Micro: Bit V2 マザーボードの加速度計座標は下図のようになります：

![](./media/Makecode_79d90885.jpg)

Windows 10 ではなく Windows 7 または 8 を使用している場合、Google Chrome からはデバイスを認識できません。データを読み取るには CoolTerm シリアルモニタソフトを使用する必要があります。CoolTerm を開き、Options をクリックし、SerialPort を選択して COM ポートを設定し、ボーレートを 115200 に設定します（テストにより、Micro: Bit main board V2 の USB シリアルポート通信のボーレートは 115200 です）、OK をクリックして Connect します。CoolTerm シリアルモニタには X 軸、Y 軸、Z 軸のデータが表示されます。下図を参照してください：

![](./media/Makecode_2a63fc72.gif)