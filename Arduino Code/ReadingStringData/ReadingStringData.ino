String userInput;
int collectionTime;

void setup() {
  Serial.begin(9600);
}

void loop() {
  if(Serial.available()>0){
    userInput = Serial.readString();
    userInput.toLowerCase();
    if(userInput.startsWith("sta")){
      Serial.println("This string starts with s.");
      Serial.println(userInput.substring(0,3));
      collectionTime = userInput.substring(3).toInt();
      Serial.println(collectionTime);
    }else{
      Serial.println("This string doesnt work.");
      Serial.println(userInput.substring(0,4));
    }
  }
}
