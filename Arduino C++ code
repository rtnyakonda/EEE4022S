#include "Adafruit_VL53L0X.h"
// address we will assign if dual sensor is present
#define LOX1_ADDRESS 0x30
#define LOX2_ADDRESS 0x31

// set the pins to shutdown
#define SHT_LOX1 7
#define SHT_LOX2 6


Adafruit_VL53L0X lox = Adafruit_VL53L0X();
Adafruit_VL53L0X lox2 = Adafruit_VL53L0X();

volatile int flow_frequency_tank1; // Measures flow sensor pulses
volatile int flow_frequency_tank2; // Measures flow sensor pulses

unsigned int l_hour; // Calculated litres/hour
unsigned char flowsensor_tank1 = 3; // Sensor Input
unsigned char flowsensor_tank2 = 2;//sensor input f
unsigned long currentTime;
unsigned long cloopTime;
unsigned int distance= 0;
unsigned int count =0;
unsigned long previousTime=0;
const long interval = 8000; 
int motor1_state=0;
int motor2_state=0;
int Motor1_direction=12;
int Motor2_direction=13;
int Motor1_speed=10;
int Motor2_speed=11;
int buz = 4;
VL53L0X_RangingMeasurementData_t measure1;
VL53L0X_RangingMeasurementData_t measure2;

void flow_tank1 () // Interrupt function
{
   flow_frequency_tank1++;
}

void flow_tank2 () // Interrupt function
{
   flow_frequency_tank2++;
}

void setID() {
  // all reset
  digitalWrite(SHT_LOX1, LOW);    
  digitalWrite(SHT_LOX2, LOW);
  delay(10);
  // all unreset
  digitalWrite(SHT_LOX1, HIGH);
  digitalWrite(SHT_LOX2, HIGH);
  delay(10);

  // activating LOX1 and reseting LOX2
  digitalWrite(SHT_LOX1, HIGH);
  digitalWrite(SHT_LOX2, LOW);

  // initing LOX1
  if(!lox.begin(LOX1_ADDRESS)) {
    Serial.println(F("Failed to boot first VL53L0X"));
    while(1);
  }
  delay(10);

  // activating LOX2
  digitalWrite(SHT_LOX2, HIGH);
  delay(10);

  //initing LOX2
  if(!lox2.begin(LOX2_ADDRESS)) {
    Serial.println(F("Failed to boot second VL53L0X"));
    while(1);
  }
}

void read_dual_sensors() {
  
  lox.rangingTest(&measure1, false); // pass in 'true' to get debug data printout!
  lox2.rangingTest(&measure2, false); // pass in 'true' to get debug data printout!

  // print sensor one reading
  Serial.print(F("1: "));
  if(measure1.RangeStatus != 4) {     // if not out of range
    Serial.print(measure1.RangeMilliMeter);
  } else {
    Serial.print(F("Out of range"));
  }
  
  Serial.print(F(" "));

  // print sensor two reading
  Serial.print(F("2: "));
  if(measure2.RangeStatus != 4) {
    Serial.print(measure2.RangeMilliMeter);
  } else {
    Serial.print(F("Out of range"));
  }
  
  Serial.println();
}
   
void setup() {
  pinMode(Motor1_direction,OUTPUT);
  pinMode(Motor2_direction,OUTPUT);
  pinMode(Motor1_speed,OUTPUT);
  pinMode(Motor2_speed,OUTPUT);
  pinMode(buz,OUTPUT);
  
  Serial.begin(9600);

  // wait until serial port opens for native USB devices
  while (! Serial) {
    delay(1);
  }
  pinMode(SHT_LOX1, OUTPUT);
  pinMode(SHT_LOX2, OUTPUT);
  Serial.println(F("Shutdown pins inited..."));

  digitalWrite(SHT_LOX1, LOW);
  digitalWrite(SHT_LOX2, LOW);
  Serial.println(F("Both in reset mode...(pins are low)"));
  Serial.println("Starting readings");
  
  
  // power 

  pinMode(flowsensor_tank1, INPUT);
  digitalWrite(flowsensor_tank1, HIGH); // Optional Internal Pull-Up
  
  attachInterrupt(0, flow_tank1, RISING); // Setup Interrupt

  pinMode(flowsensor_tank2, INPUT);
  digitalWrite(flowsensor_tank2, HIGH); // Optional Internal Pull-Up
  
  attachInterrupt(1, flow_tank2, RISING); // Setup Interrupt
  sei(); // Enable interrupts
  currentTime = millis();
  cloopTime = currentTime;

  digitalWrite(Motor1_direction,HIGH);
  analogWrite(Motor1_speed,0);
  digitalWrite(Motor2_direction,HIGH);
  analogWrite(Motor2_speed,190);
  
  setID();
}


void loop() {
  digitalWrite(buz,HIGH);
  
  currentTime = millis();
  read_dual_sensors();
  
    
  
  if(currentTime >= (cloopTime + 1000))
   {
    cloopTime = currentTime; // Updates cloopTime
      // Pulse frequency (Hz) = 7.5Q, Q is flow rate in L/min.
    Serial.print("Tank 1 Flow frequency (number of rising edges): ");
    Serial.println(flow_frequency_tank2);
    Serial.print("Tank 2 Flow frequency (number of rising edges): ");
    Serial.println(flow_frequency_tank1);
    flow_frequency_tank1=0;
    flow_frequency_tank2=0;
    count=0;
    distance = 0;
  }
  digitalWrite(buz,LOW);
  delay(100);

}
