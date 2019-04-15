void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(13, HIGH);
  Serial.println("LED is on");
  delay(1000);
  digitalWrite(13, LOW);
  Serial.println("LED is off");
  delay(1000);
}
