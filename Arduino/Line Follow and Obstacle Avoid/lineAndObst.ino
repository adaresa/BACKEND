#include <Servo.h>
#include <NewPing.h>
#include <TimerFreeTone.h>

/* Defines ------------------------------------------------------------------ */
#define trigPin 4
#define echoPin 3
#define right_servo_pin 5
#define left_servo_pin  6
#define right_led       7
#define left_led        8
#define left_qti        A0
#define middle_qti      A1
#define right_qti       A2
#define buzzer_pin      A5    // sumisti pin
#define min_pulse       1300
#define max_pulse       1700
#define standstill      1500
#define qti_threshold   430   // kõrgem -> must(1), madalam -> valge(0)
#define MAX_DISTANCE 350

NewPing sonar(trigPin, echoPin, MAX_DISTANCE); // NewPing setup of pins and maximum distance.

/* Global variables ------------------------------------------ */
Servo g_left_wheel;
Servo g_right_wheel;
int g_distance = 0; // muutuja ultraheli sensori kauguse mõõtmiseks cm's

/* Private functions ------------------------------------------------- */
byte readQti (byte qti) {                               // Function to read current position on map
  digitalWrite(qti, HIGH);                              // Send an infrared signal
  delayMicroseconds(1000);                               // Wait for 1ms, very important!
  digitalWrite(qti, LOW);                               // Set the pin low again
  return (analogRead(qti) > qti_threshold ? 1 : 0);    // Return the converted result: if analog value more then 100 return 1, else 0
}

void setWheels(int delay_left = 1500, int delay_right = 1500) {
  g_left_wheel.writeMicroseconds(delay_left);
  g_right_wheel.writeMicroseconds(delay_right);
  delay(20);
}

void setLed(byte value_left = LOW, byte value_right = LOW) {
  digitalWrite(right_led, value_right);
  digitalWrite(left_led, value_left);
}

int getDistance(){
  g_distance = sonar.ping_cm();
  if (g_distance == 0){
    g_distance = 30;
  }
  return g_distance;  
}
/* Arduino functions ---------------------------------------------------------------- */
void setup() {
  /* Start serial monitor */
  Serial.begin(9600);
  
  /* Set LED pins to output mode */
  pinMode(right_led, OUTPUT);
  pinMode(left_led, OUTPUT);

  /* Attach servos to digital pins defined earlier */
  g_left_wheel.attach(left_servo_pin);
  g_right_wheel.attach(right_servo_pin);

  /* Initiate wheels to standstill */
  setWheels();
  TimerFreeTone(buzzer_pin, 2000, 700);
  delay(800);
}

void loop() {

  g_distance = getDistance();
  
  if (g_distance <= 10){
    setWheels();
    TimerFreeTone(buzzer_pin, 2000, 700);
    delay(500);
    around();
  }

  // vasak joonel, parem joonel -> sõida edasi
  if (readQti(left_qti) && readQti(right_qti)){edasi();}
  // vasak joonel, parem paberil -> keera vasakule
  else if (readQti(left_qti) && !readQti(right_qti)){vasakule();}
  // vasak paberil, parem joonel -> keera paremale
  else if (!readQti(left_qti) && readQti(right_qti)){paremale();}
  // vasak paberil, parem paberil -> sõida edasi
  else{edasi();}
}

void edasi(){
  // sõidab edasi
  setLed(LOW, LOW); // ledid kustus
  setWheels(1700, 1300);
}
void vasakule(){
  setLed(HIGH, LOW); // vasak led põleb, parem ei põle
  setWheels(1450, 1400);
}
void paremale(){
  setLed(LOW, HIGH); // vasak led kustus, parem põleb
  setWheels(1600, 1550);
}
void around(){
  // TAGURDUS
  setWheels(1400, 1600);
  delay(200);
  
  // VASAKULE
  setWheels(1400, 1400); //pööre vasakule
  delay(500);

  // EDASI
  setWheels(1700, 1300);
  delay(850);

  // PAREMALE
  setWheels(1600, 1600); //pööre paremale
  delay(350);

  // EDASI
  do{
    setWheels(1600, 1460);
  }while(!readQti(left_qti) && !readQti(right_qti));
  
  delay(150);
  setWheels(1400, 1400);
  delay(440);
}#include <Servo.h>
#include <NewPing.h>
#include <TimerFreeTone.h>

/* Defines ------------------------------------------------------------------ */
#define trigPin 4
#define echoPin 3
#define right_servo_pin 5
#define left_servo_pin  6
#define right_led       7
#define left_led        8
#define left_qti        A0
#define middle_qti      A1
#define right_qti       A2
#define buzzer_pin      A5    // sumisti pin
#define min_pulse       1300
#define max_pulse       1700
#define standstill      1500
#define qti_threshold   430   // kõrgem -> must(1), madalam -> valge(0)
#define MAX_DISTANCE 350

NewPing sonar(trigPin, echoPin, MAX_DISTANCE); // NewPing setup of pins and maximum distance.

/* Global variables ------------------------------------------ */
Servo g_left_wheel;
Servo g_right_wheel;
int g_distance = 0; // muutuja ultraheli sensori kauguse mõõtmiseks cm's

/* Private functions ------------------------------------------------- */
byte readQti (byte qti) {                               // Function to read current position on map
  digitalWrite(qti, HIGH);                              // Send an infrared signal
  delayMicroseconds(1000);                               // Wait for 1ms, very important!
  digitalWrite(qti, LOW);                               // Set the pin low again
  return (analogRead(qti) > qti_threshold ? 1 : 0);    // Return the converted result: if analog value more then 100 return 1, else 0
}

void setWheels(int delay_left = 1500, int delay_right = 1500) {
  g_left_wheel.writeMicroseconds(delay_left);
  g_right_wheel.writeMicroseconds(delay_right);
  delay(20);
}

void setLed(byte value_left = LOW, byte value_right = LOW) {
  digitalWrite(right_led, value_right);
  digitalWrite(left_led, value_left);
}

int getDistance(){
  g_distance = sonar.ping_cm();
  if (g_distance == 0){
    g_distance = 30;
  }
  return g_distance;  
}
/* Arduino functions ---------------------------------------------------------------- */
void setup() {
  /* Start serial monitor */
  Serial.begin(9600);
  
  /* Set LED pins to output mode */
  pinMode(right_led, OUTPUT);
  pinMode(left_led, OUTPUT);

  /* Attach servos to digital pins defined earlier */
  g_left_wheel.attach(left_servo_pin);
  g_right_wheel.attach(right_servo_pin);

  /* Initiate wheels to standstill */
  setWheels();
  TimerFreeTone(buzzer_pin, 2000, 700);
  delay(800);
}

void loop() {

  g_distance = getDistance();
  
  if (g_distance <= 10){
    setWheels();
    TimerFreeTone(buzzer_pin, 2000, 700);
    delay(500);
    around();
  }

  // vasak joonel, parem joonel -> sõida edasi
  if (readQti(left_qti) && readQti(right_qti)){edasi();}
  // vasak joonel, parem paberil -> keera vasakule
  else if (readQti(left_qti) && !readQti(right_qti)){vasakule();}
  // vasak paberil, parem joonel -> keera paremale
  else if (!readQti(left_qti) && readQti(right_qti)){paremale();}
  // vasak paberil, parem paberil -> sõida edasi
  else{edasi();}
}

void edasi(){
  // sõidab edasi
  setLed(LOW, LOW); // ledid kustus
  setWheels(1700, 1300);
}
void vasakule(){
  setLed(HIGH, LOW); // vasak led põleb, parem ei põle
  setWheels(1450, 1400);
}
void paremale(){
  setLed(LOW, HIGH); // vasak led kustus, parem põleb
  setWheels(1600, 1550);
}
void around(){
  // TAGURDUS
  setWheels(1400, 1600);
  delay(200);
  
  // VASAKULE
  setWheels(1400, 1400); //pööre vasakule
  delay(500);

  // EDASI
  setWheels(1700, 1300);
  delay(850);

  // PAREMALE
  setWheels(1600, 1600); //pööre paremale
  delay(350);

  // EDASI
  do{
    setWheels(1600, 1460);
  }while(!readQti(left_qti) && !readQti(right_qti));
  
  delay(150);
  setWheels(1400, 1400);
  delay(440);
}