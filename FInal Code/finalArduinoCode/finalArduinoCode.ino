// Declare data values and analog input pins
int dtime = 0;
float temperature = 0.00;
const int temperatureSensor = A1;
float pressure = 0.00;
const int pressureSensor = A0;
float turbidity = 0.00;
const int turbiditySensor = A2;

String userInput;
int collectionTime;

void takeData(){
  //Serial.begin(9600);
  //Serial.println("Time (s)\tTemperature (°C)\tPressure\tTurbidity\n");
  while(dtime < collectionTime){
    dtime+=1;
    Serial.print(dtime);
    Serial.print('\t');

    //TODO: Find the temperature converstion
    temperature = (0.4868 * analogRead(temperatureSensor)) - 49.772;  
    //temperature = analogRead(temperatureSensor);
    Serial.print(temperature);
    Serial.print('\t');
    
    pressure = analogRead(pressureSensor);
    Serial.print(pressure);
    Serial.print('\t');
    turbidity = analogRead(turbiditySensor) * (5.0/1024.0);
    Serial.print(turbidity);
    Serial.print('\n');
    delay(1000);
    Serial.flush();
  }
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  if(Serial.available()>0){
    userInput = Serial.readString();
    userInput.toLowerCase();
    if(userInput.startsWith("sta")){
      collectionTime = userInput.substring(3).toInt(); // Converts everything after "sta" to an int
      takeData();
      dtime = 0;
    }else if(userInput.startsWith("end")){
      Serial.end();
    }
  }     
}//*/
