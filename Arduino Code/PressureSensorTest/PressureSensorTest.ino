const int pressure = A0;

void setup() {
  Serial.begin(9600);

}

void loop() {
  Serial.println(analogRead(pressure));
  delay(1000);

}
