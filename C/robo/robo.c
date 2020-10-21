#include <Servo.h>

/* Defines ------------------------------------------------------------------ */
#define button_pin      2
#define right_servo_pin 5
#define left_servo_pin  6
#define right_led       7
#define left_led        8
#define left_qti        A0
#define middle_qti      A1
#define right_qti       A2
#define min_pulse       1300
#define max_pulse       1700
#define standstill      1500
#define qti_threshold   460 // kõrgem -> must(1), madalam -> valge(0)



/* Global variables ------------------------------------------ */
Servo g_left_wheel;
Servo g_right_wheel;
int finished = 0; // muutuja, kui saab väärtuse 1, siis stopp

/* Private functions ------------------------------------------------- */
byte readQti (byte qti) {                               // Function to read current position on map
  digitalWrite(qti, HIGH);                              // Send an infrared signal
  delayMicroseconds(1000);                               // Wait for 1ms, very important!
  digitalWrite(qti, LOW);                               // Set the pin low again
  return ( analogRead(qti) > qti_threshold ? 1 : 0);    // Return the converted result: if analog value more then 100 return 1, else 0
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

/* Arduino functions ---------------------------------------------------------------- */
void setup() {
  /* Start serial monitor */
  Serial.begin(9600);

  /* Set the pin mode of LED pins as output */
  pinMode(right_led, OUTPUT);
  pinMode(left_led, OUTPUT);

  /* Attach servos to digital pins defined earlier */
  g_left_wheel.attach(left_servo_pin);
  g_right_wheel.attach(right_servo_pin);

  /* Initiate wheels to standstill */
  setWheels();

  /* Blinking LEDs for test */
  setLed(HIGH, HIGH);
  delay(500);
  setLed();
  delay(500);
}

void loop() {
  /* Start reading QTI values and adjust wheels accordingly */
  if (readQti(left_qti)) {
    if (readQti(right_qti)){
      // vasak tume, parem tume
      if (finished){
        stopp(100000); // kui finished on väärtusega 1
      }else{
        finished = 1; // kui ületab ristmikku esimest korda, saab väärtuse 1
        edasi(500);
      }
      edasi(50);
    }
    else{
      // vasak tume, parem hele
      vasakule(50);
    } 
  }else{
    if(readQti(right_qti)){
      // vasak hele, parem tume
      paremale(50);
    }else{
      // vasak hele, parem hele
      edasi(50);
    }
  }
}

void edasi(int kestvus){
  // sõidab edasi
  setLed(LOW, LOW); // ledid kustus
  setWheels(1550, 1450);
  delay(kestvus);
  setWheels();
  setLed(LOW, LOW);
}
 void vasakule(int kestvus){
  // keerab vasakule
  setLed(HIGH, LOW); // vasak põleb, parem kustus
  setWheels(1450, 1450);
  delay(kestvus);
  setWheels();
  setLed(LOW, LOW);
}
 void paremale(int kestvus){
  // keerab paremale
  setLed(LOW, HIGH); // parem põleb, vasak kustus
  setWheels(1550, 1550);
  delay(kestvus);
  setWheels();
  setLed(LOW, LOW);
}
 void stopp(int kestvus){
  // robot jääb seisma
  setLed(HIGH, HIGH); // mõlemad ledid põlevad
  setWheels(1500, 1500);
  delay(kestvus);
  setWheels();
  setLed(LOW, LOW);
}

