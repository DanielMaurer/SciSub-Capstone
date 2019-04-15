void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  
    digitalWrite(13, HIGH);
    Serial.println("The LED is on");
    delay(500);
    digitalWrite(13, LOW);
    Serial.println("The LED is off");
    delay(1000);
  
}
