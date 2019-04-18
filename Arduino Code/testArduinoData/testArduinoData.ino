int dtime = 0;
float temperature = 0;
int pressure = 0;
int turbidity = 0;

char userTimeInput;

void takeData(){
  Serial.println("Time (s)\tTemperature (°C)\tPressure\tTurbidity\n");
  while(dtime < 20){
    dtime+=1;
    Serial.print(dtime);
    Serial.print('\t');
    temperature +=1;
    Serial.print(temperature);
    Serial.print('\t');
    pressure+=1;
    Serial.print(pressure);
    Serial.print('\t');
    turbidity+=1;
    Serial.print(turbidity);
    Serial.print('\n');
    delay(1000);
  }
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
    while(1){
        userTimeInput = Serial.read();
        if(userTimeInput == 's'){
            takeData();
        }
    }
}
