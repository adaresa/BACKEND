#include <Servo.h>

/* Defines ------------------------------------------------------------------ */
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
#define qti_threshold   430 // kõrgem -> must(1), madalam -> valge(0)

/* Global variables ------------------------------------------ */
Servo g_left_wheel;
Servo g_right_wheel;

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
  
  /* Set LED pins to output mode */
  pinMode(right_led, OUTPUT);
  pinMode(left_led, OUTPUT);

  /* Attach servos to digital pins defined earlier */
  g_left_wheel.attach(left_servo_pin);
  g_right_wheel.attach(right_servo_pin);

  /* Initiate wheels to standstill */
  setWheels();
}

void loop() {
  /* Start reading QTI values and adjust wheels accordingly */
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
  setWheels(1550, 1450);
}
 void vasakule(){
  // keerab vasakule
  setLed(HIGH, LOW); // vasak led põleb, parem ei põle
  setWheels(1450, 1400);
}
 void paremale(){
  // keerab paremale
  setLed(LOW, HIGH); // vasak led kustus, parem põleb
  setWheels(1600, 1550);
}

