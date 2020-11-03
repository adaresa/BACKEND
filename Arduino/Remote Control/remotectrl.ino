/* Includes -------------------------------------------------- */
#include <Servo.h>

/* Defines ------------------------------------------------------------------ */
#define button_pin      2
#define sonic_echo_pin  3
#define sonic_trig_pin  4
#define right_servo_pin 5
#define left_servo_pin  6
#define right_led       7
#define left_led        8
#define left_qti        A0
#define middle_qti      A1
#define right_qti       A2
#define ir_receiver     A3
#define min_pulse       1300
#define max_pulse       1700
#define standstill      1500
#define qti_threshold   0

/* Global variables ------------------------------------------ */
Servo g_left_wheel;
Servo g_right_wheel;
float g_distance_in_cm = 0; // kaugus cm-s
unsigned long g_last_debounce_time = 0;  // the last time the output pin was toggled
unsigned long g_debounce_delay = 50;    // the debounce time; increase if the output flickers
int g_button_state;             // the current reading from the input pin
int g_last_button_state = LOW;   // the previous reading from the input pin
signed int g_ir_buf[32];    // Infrared data buffer
signed int g_ir_index = 0;  // Infrared loop counter variable
bool online = true;
unsigned long g_last_command;
int power = 1; // Toide sisse/välja

/* Private functions ------------------------------------------------- */
void setLed(byte value_left = LOW, byte value_right = LOW) {
  digitalWrite(right_led, value_right);
  digitalWrite(left_led, value_left);
}

float distanceInCm() {
  digitalWrite(sonic_trig_pin, HIGH); // Make sonic_trig_pin HIGH
  delayMicroseconds(10); // Wait for 10us
  digitalWrite(sonic_trig_pin, LOW); // Make the pin low
  /* 
   * Black magic, where the returned value from the sensor should be converted to cm
   * Use "pulseIn(sonic_echo_pin, HIGH);" to get the signal propagation time value
   * Try to use one-liner: "return XXX;" should do the trick
   */
  return (pulseIn(sonic_echo_pin, HIGH)/58.0); // sensori arvutus kus saab aru mitu cm objektist
}

void setWheels(int delay_left = 1500, int delay_right = 1500) {
  g_left_wheel.writeMicroseconds(delay_left);
  g_right_wheel.writeMicroseconds(delay_right);
  delay(20);
}

int irReceive () {
  while (pulseIn(ir_receiver, HIGH) > 4000) { // Wait for a start bit
    Serial.println("Start bit received");
    for (byte i = 0; i <= 31; i++) {
      g_ir_buf[i] = pulseIn(ir_receiver, HIGH); // Write all the infrared signal data to variable
    }
    Serial.println("IR buffer populated with timings");
    g_ir_index = 0;
    /* Only for serious debugging */
    /*
      for (byte i = 0; i <= 31; i++) {
      Serial.println(g_ir_buf[i]);
      }
    */
    for (byte i = 0; i <= 31; i++) {
      if (g_ir_buf[i] > 1000) {
        g_ir_buf[i] = 1;
        g_ir_index++;
      } else if (g_ir_buf[i] > 0) {
        g_ir_buf[i] = 0;
        g_ir_index++;
      } else {
        Serial.println("Wrong bit received");
      }
    }
    Serial.println("IR buffer translated to binary");
    Serial.print("Number of bits received: ");
    Serial.println(g_ir_index);
    irSerialPrint();
    whatBtn();
    if (check()) {
      return 1;
    }
    Serial.println("Waiting for start bit");
  }
  return 0;
}

void irSerialPrint() {
  Serial.println("------ Bit Correction Check ------");
  for (byte i = 16; i <= 23; i++) { // Print out the range of 16-31 bits of infrared signal buffer
    Serial.print("Bit ");
    Serial.print(i);
    Serial.print(" = ");
    Serial.print(g_ir_buf[i]);
    Serial.print(" | ");
    Serial.println(g_ir_buf[i + 8]);
  }
}

bool check() { // Check the received bits
  for(int i=16;i<=23;i++){
    if(g_ir_buf[i] != !g_ir_buf[i+8]){
      return 0;
    }
  }
  return 1;
}

/* Arduino functions ---------------------------------------------------------------- */
void setup() {
  /* Set LED pins to output mode */
  pinMode(left_led, OUTPUT);
  pinMode(right_led, OUTPUT);
  setLed(HIGH, HIGH);
  
  /* Attach servos to digital pins defined earlier */
  g_left_wheel.attach(left_servo_pin, min_pulse, max_pulse );
  g_right_wheel.attach(right_servo_pin, min_pulse, max_pulse);

  /* Set servos to standstill movement... */
  g_left_wheel.writeMicroseconds(standstill);
  g_right_wheel.writeMicroseconds(standstill);


  
  /* Start serial monitor */
  Serial.begin(9600);

  /* Set the ultrasonic sensor pins */
  pinMode(sonic_trig_pin, OUTPUT);
  pinMode(sonic_echo_pin, INPUT);

  /* Set infrared receiver pin to input mode*/
  pinMode(ir_receiver, INPUT);

  Serial.println("Starting irReceive()");
  Serial.println("Waiting for start bit");
}


void loop() {
  irReceive();
}

void whatBtn() {
  // Power nupp lülitab toite sisse/välja
  if(g_ir_buf[17] && g_ir_buf[20] == 0 && g_ir_buf[16] == 0){
      Serial.println("Nupp on: Power");
      power = !power;
  }
  // Kui toide sees, tuled põlevad
  if(power){
    setLed(HIGH, HIGH);
  }
  // Toide väljas -> tuled kustus
  else{
    setLed(LOW, LOW);
  }

  // Kui toide sees
  if(power){
    if(!check()){
    Serial.println("Signaal ei läbinud edukalt funktsiooni");
    }
    else if(g_ir_buf[17] == 0 && g_ir_buf[20] == 1){
      Serial.println("Nupp on: Channel Down");
    }
    else if(g_ir_buf[17] && g_ir_buf[20]){
      Serial.println("Nupp on: Channel Up"); 
    }
    // AV/TV nupp keerab 90 kraadi
    else if(g_ir_buf[16] && g_ir_buf[17] == 0){
      Serial.println("Nupp on: AV/TV");
      // Kestvus 700 vastab 90le kraadile
      keera(700);
    }
    // Mute nupp sõidab(edasi/tagasi) kuni on seinast 50cm kaugusel
    else if(g_ir_buf[18] && g_ir_buf[19]){
      Serial.println("Nupp on: Mute");
      fiftyCm();
    }
    // Volume- nupp sõidab seinale 10cm lähemale
    else if(g_ir_buf[17] && g_ir_buf[18] == 0 && g_ir_buf[16]){
      Serial.println("Nupp on: Volume Down");
      kymmeEdasi(); 
    }
    // Volume+ nupp sõidab seinast 10cm kaugemale
    else if(g_ir_buf[18] && g_ir_buf[19] == 0 && g_ir_buf[20] == 0){
      Serial.println("Nupp on: Volume Up"); 
      kymmeTagasi();
    }
  }
}

// Sõidab edasi
void edasi(int kestvus){
    setWheels(1700, 1300);
    delay(kestvus);
}

// Sõidab tagasi
void tagasi(int kestvus){
    setWheels(1300, 1700);
    delay(kestvus);
}

// Keerab ~90 kraadi
void keera(int kestvus){
    setWheels(1600, 1600);
    delay(kestvus);
    setWheels();
}

// Sõidab 10cm edasi
void kymmeEdasi(){
    double goal = 5;
    g_distance_in_cm = distanceInCm();
    if(g_distance_in_cm > 15){
        goal = g_distance_in_cm - 10;
    }
    while (g_distance_in_cm > goal){ // Sõidab edasi kuni praegune kaugus on algne kaugus - 10cm (minimaalselt 5cm)
        edasi(100);
        g_distance_in_cm = distanceInCm();
    }
    setWheels();
}

// Sõidab 10cm tagasi
void kymmeTagasi(){
    g_distance_in_cm = distanceInCm(); // Mõõdab praeguse kauguse
    double goal = g_distance_in_cm + 10; // Kauguseks peab saama praegune kaugus + 10cm
    while (g_distance_in_cm < goal){
        tagasi(50); // Tagurdab kuni praegune kaugus on algne kaugus + 10cm
        g_distance_in_cm = distanceInCm();
    }
    setWheels();
}

// Sõidab edasi/tagasi kuni kagus on 50cm (49-51cm)
void fiftyCm(){
    g_distance_in_cm = distanceInCm();
    while(g_distance_in_cm < 49 || g_distance_in_cm > 51){
        if(g_distance_in_cm > 50){
            edasi(50);
        }
        else{
            tagasi(50);
        }
        g_distance_in_cm = distanceInCm();
    }
    setWheels();
}