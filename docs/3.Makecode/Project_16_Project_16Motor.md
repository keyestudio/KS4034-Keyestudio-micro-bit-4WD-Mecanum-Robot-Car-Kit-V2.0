## プロジェクト 16：Motor

![](./media/Makecode_77f3b857.png)

1\.  **説明**

Keyestudio 4WD Mecanum Robot Car は、一般的なDCモータをベースに開発された4つのDC減速モータ（ギア減速モータとも呼ばれる）を搭載しています。適合するギヤ減速箱を備えており、回転数は低くなりますがトルクは大きくなります。さらに、減速箱の減速比を変えることで、異なる速度とトルクを得ることができます。

ギアモータはギヤモータとモータの統合であり、鉄鋼・機械産業で広く応用されています。

micro:bit用モータドライバシールドにはDRV8833チップが搭載されています。IOポート資源を節約するために、DRV8833チップで4つのDCギアモータの回転方向と速度を制御します。

![Img](./media/Makecode_4c9781dc.png)

Front

![](./media/Makecode_4919ce3b.png)

Back

![](./media/Makecode_59c34b6e.png)

STC8G1K08 Chip circuit

![](./media/Makecode_8874ded0.png)

HR8833 Motor driver circuit

2\.  **準備**

- micro:bitボードをkeyestudio 4WD Mecanum Robot Car V2.0のスロットに差し込む

- 電池を電池ホルダーに入れる

- 電源スイッチをON側に合わせる

- USBケーブルでmicro:bitをコンピュータに接続する

- MakecodeのWeb版を開く

3\.  **Test Code1**

![](./media/Makecode_3a759dd8.png)

「Click“JavaScript" to view the corresponding JavaScript code:」の表示部分（UIのラベル）については、`JavaScript` の表記はそのままです。対応するJavaScriptコードを表示するには“JavaScript"をクリックしてください。 

![](./media/Makecode_242ba6ca.png)

4\.  **テスト結果1**

コード1をmicro:bitボードにダウンロードし、POWERスイッチをONにします。スマートカーは2秒前進し、2秒停止します。

5\.  **Test Code2**

![](./media/Makecode_a3a9d39a.png)

![Img](./media/Makecode_4eb6b574.png)

「Click“JavaScript" to view the corresponding JavaScript code:」の表示部分については、`JavaScript` の表記はそのままです。対応するJavaScriptコードを表示するには“JavaScript"をクリックしてください。 

![](./media/Makecode_ee70b846.png)

6\.  **テスト結果2**

コード2をmicro:bitボードにダウンロードすると、車は2秒前進し、2秒後退し、2秒左折し、2秒右折し、2秒停止し、このパターンを繰り返します。