void setup() {
Serial.begin(9600); //Set's up Serial port so Pi can listen
Serial.println("Program Starting"); 
// wait for the long string to be sent 
delay(100); 

// Set up our 4 IR sensors on ports 0, 1, 2, 3
pinMode(0, INPUT);
pinMode(1, INPUT);
pinMode(2, INPUT); 
pinMode(3, INPUT);
//declare the variable 
}
int var = 0;
int indx = 1;
void loop() {

//without sensors, run this to test the reading / writing is correct
//int var = 1100 | indx;
//int temp = B0;
//int tot = B0;
//for (int a = 0; a <= 1; a++){
//  for (int b = 0; b <= 1; b++){
//    for (int c = 0; c <= 1; c++){
//      for (int d = 0; d <= 1; d++){
//        temp = d;
//        tot = temp;
//       temp = c << 1;
//        tot = temp | tot;
//        temp = b << 2;
//        tot = temp | tot;
//        temp = a << 3;
//        tot = temp | tot;
//        if(tot < 2)Serial.print(B0);
//        if(tot < 4)Serial.print(B0);
//        if(tot < 8)Serial.print(B0);
//        Serial.println(tot, BIN);
//        Serial.print('\n');
//        delay(100);
//      }
//    }
//  }
//}
//delay(2000);

//iterate through sensing pins to make make a 4 bit number
   for (int count = 0; count <= 3; count++ ){
    int temp = digitalRead(count);
    temp = temp << count;//shift data value to the left
    var = temp | var; //functionally concatinate the sensor data by bit ORing them after shifting
    } // end of for count
   //var is now a 4 bit number of syntax <pin3><pin2><pin1><pin0>
   //Serial.print("Measurement "); //used for debugging only. Sending this confuses the Pi who expects sensor data only
   //Serial.print(indx);
   //delay(100);
   //Serial.print('\n');
   if(var < 2)Serial.print(B0);
   if(var < 4)Serial.print(B0);
   if(var < 8)Serial.print(B0);//make sure that leading 0's are still sent
   Serial.print(var, BIN);//since serial.print omits them
   Serial.print('\n');
   delay(200);
   indx += 1;
   var = 0; //just double check ensure that var is cleared of old data
}
