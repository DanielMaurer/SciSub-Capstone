int dtime = 0;
int temperature = 0;
int pressure = 0;
int turbidity = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("Time\tTemperature\tPressure\tTurbidity\n");
}

void loop() {
  dtime+=1;
  Serial.print(dtime);
  Serial.print('\t');
  temperature+=1;
  Serial.print(temperature);
  Serial.print('\t');
  pressure+=1;
  Serial.print(pressure);
  Serial.print('\t');
  turbidity+=1;
  Serial.print(turbidity);
  Serial.print('\n');
  //Serial.println(dtime + '\t' + temperature + '\t' + pressure + '\t' + turbidity + '\n');
  delay(1000);
  
}
