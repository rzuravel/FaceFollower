//www.elegoo.com
//2018.12.19
#include <Servo.h>

Servo myservo;

int currentAngle;
const int setpoint = 128;
const int bound = 20;

void setup(){
  Serial.begin(9600);
  myservo.attach(9);
  myservo.write(currentAngle = 90);// move servos to center position -> 90°
} 
void loop(){
  unsigned char incomingData = 128;
  if (Serial.available() > 0)
  {
    incomingData = Serial.read();
    Serial.println(incomingData);
  }

  if (incomingData == 0)
  {
    // do nothing
  }
  else if (incomingData > setpoint + bound)
  {
    myservo.write(--currentAngle);
  }
  else if (incomingData < setpoint - bound)
  {
    myservo.write(++currentAngle);
  }
  else // incomingData == setpoint +- bound
  {
    // do nothing
  }
  delay(12);
}
