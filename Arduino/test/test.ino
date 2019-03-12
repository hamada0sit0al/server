void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  // 1000ms
  delay(1000);

  //シリアル通信でtestを改行ありで出力
  Serial.println("test");

}
