## BBC Micro:bit

### **(1) Micro:bitとは？**

Micro:bitは、British Broadcasting Corporation（BBC）がARM、Barclays、element14、Microsoftなどの機関と共同で立ち上げた、ARMアーキテクチャに基づくオープンソースのハードウェアプラットフォームです。コアにはFPUを備えた32ビットのArm Cortex‑M4を搭載しています。

クレジットカードほどの大きさですが非常に高性能です。Micro:bitメインボードには、5×5のLEDドットマトリクス、2つのプログラム可能なボタン、加速度センサ、コンパス、温度計、タッチ対応ロゴ、MEMSマイクロフォン、低消費電力のBluetoothモジュール、ブザーなど多くのコンポーネントが搭載されており、外部機器なしで様々な音を出すことができます。

さらに、このボードはバッテリー消費を抑えるスリープモードをサポートしており、裏面のReset & Powerボタンを長押しすることで入ることができます。

Micro:bit開発ボードは使いやすく拡張性も高いです。下部のゴールドフィンガー（edge connector）の設計により、ワニ口クリップなどを使って各種電子部品と接続できます。センサのデータを読み取り、サーボやRGBライトを制御したり、拡張ボードを挿してさまざまなセンサを接続することが可能です。

また、複数のプログラミング言語やグラフィカルなプログラミングプラットフォームをサポートしており、ほとんどのPCやモバイル機器と互換性があり、特別なドライバのインストールも不要です。高集積の電子モジュールとシリアルポート監視機能を備え、デバッグも容易です。

このボードは、ビデオゲームのプログラミング、光と音のインタラクション、ロボット制御、科学実験、ウェアラブル機器、ロボットや楽器などの創造的な発明に広く使われています。

### **(2) レイアウト**

![Img](./media/Introduction_5746e59b.png)

詳細は次のリンクをご参照ください：

[https://tech.microbit.org/hardware/](https://tech.microbit.org/hardware/)

[https://microbit.org/new-microbit/](https://microbit.org/new-microbit/)

[https://www.microbit.org/get-started/user-guide/overview/](https://www.microbit.org/get-started/user-guide/overview/)

[https://microbit.org/get-started/user-guide/features-in-depth/](https://microbit.org/get-started/user-guide/features-in-depth/)

### **(3) ピン配置（Pin out）**

![](./media/Introduction_ce0de295.png)

**機能：**

|                            |                                                                                                    |
|----------------------------|----------------------------------------------------------------------------------------------------|
| GPIO                       | P0, P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, P14, P15, P16, P19, P20                |
| ADC/DAC                    | P0, P1, P2, P3, P4, P10                                                                            |
| IIC                        | P19 (SCL), P20 (SDA)                                                                               |
| SPI                        | P13 (SCK), P14 (MISO), P15 (MOSI)                                                                 |
| PWM（頻繁に使用）         | P0, P1, P2, P3, P4, P10                                                                            |
| PWM（あまり使用しない）   | P5, P6, P7, P8, P9, P11, P12, P13, P14, P15, P16, P19, P20                                         |
| 使用済み                   | P3（LED Col3）, P4（LED Col1）, P5（Button A）, P6（LED Col4）, P7（LED Col2）, P10（LED Col5）, P11（Button B） |

詳細は公式サイトをご覧ください： [https://tech.microbit.org/hardware/edgeconnector/](https://tech.microbit.org/hardware/edgeconnector/)

[https://microbit.org/guide/hardware/pins/](https://microbit.org/guide/hardware/pins/)

### **(4) Micro:bit メインボード使用時の注意事項：**

a\. 精密な電子部品を保護するために、シリコン製のプロテクタ（ケース）で覆うことを推奨します。

b\. IOポートの駆動能力は低く、300mA未満の電流しか扱えません。したがって、MG995サーボやDCモーターなど大電流を必要とする機器を接続しないでください。破損する恐れがあります。機器を使用する前に必ず消費電流を確認し、通常はMicro:bit拡張ボードと併用することを推奨します。

c\. メインボードの電源はUSB経由か3Vの電池での給電を推奨します。本ボードのIOポートは3V仕様のため、5Vセンサはサポートしていません。5Vセンサを接続する場合はMicro:bit拡張ボードが必要です。

d\. LEDドットマトリクスと共有されているピン（P3、P4、P6、P7、P10）を使用する場合、それらのピンをマトリクスやLEDから遮断すると、LEDがランダムに表示されたり、接続されたセンサのデータが誤ったりする可能性があります。

e\. ピン19および20は、MakeCode上でIOポートとして表示される場合がありますが、実際にはIOポートとして使用できません。これらはI2C通信専用です。

f\. 3Vの電池端子に3.3Vを超える電池を接続するとメインボードが損傷しますので接続しないでください。

g\. 金属製品の上での運用は禁止します。短絡を避けるためです。

要するに、Micro:bit V2のメインボードは小型コンピュータのようなもので、プログラミングを手軽にし、デジタルイノベーションを促進します。プログラミング環境としてはBBCが提供するウェブサイト [https://microbit.org/code/](https://microbit.org/code/) に、使いやすいグラフィカルなMakeCodeが用意されています。

---