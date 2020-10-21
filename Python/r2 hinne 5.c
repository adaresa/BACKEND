/**
  This program is free software: you can redistribute it and / or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see < https : //www.gnu.org/licenses/>.
**/

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
signed int g_ir_buf[32];    // Infrared data buffer
signed int g_ir_index = 0;  // Infrared loop counter variable
bool g_online = false;
unsigned long g_last_command;
float g_distance_in_cm = 0;
bool g_repeat = true;
byte g_pin_states[] = {0, 0};
bool power = true;          // Sisse/Välja lülitus

/* Private functions ------------------------------------------------- */           
void setWheels(int delay_left = 1500, int delay_right = 1500) {
  g_left_wheel.writeMicroseconds(delay_left);
  g_right_wheel.writeMicroseconds(delay_right);
  delay(20);
}

void setLed(byte value_left = LOW, byte value_right = LOW) {
  g_pin_states[1] = value_right;
  digitalWrite(right_led, value_right);
  g_pin_states[0] = value_left;
  digitalWrite(left_led, value_left);
}

float distanceInCm() {
  digitalWrite(sonic_trig_pin, HIGH);
  delayMicroseconds(10);
  digitalWrite(sonic_trig_pin, LOW);
  return (pulseIn(sonic_echo_pin, HIGH)/58.0); // Tagastab kauguse cm-s
}

int irReceive () {
  while (pulseIn(ir_receiver, HIGH) > 4000) { // Wait for a start bit
    for (byte i = 0; i <= 31; i++) {
      g_ir_buf[i] = pulseIn(ir_receiver, HIGH); // Write all the infrared signal data to variable
    }
    g_ir_index = 0;

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

    if (!check()) {
      Serial.println("Signaal ei läbinud edukalt funktsiooni");
      return 1
    }
    //Serial.println("Waiting for start bit");
  }
  return 0;
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
  /* Start serial monitor */
  Serial.begin(9600);

  /* Set the ultrasonic sensor pins */
  pinMode(sonic_trig_pin, OUTPUT);
  pinMode(sonic_echo_pin, INPUT);

  /* Initiate the end of the setup() function */
  Serial.println("--- Ardunio ready ---\n");
}


void loop() {
  /* Wait until a remote button press is registred */
  if (irReceive()) {
    // sisse/välja lülitamine nupust
    if(g_ir_buf[17] && g_ir_buf[20] == 0 && g_ir_buf[16] == 0){
        Serial.println("Nupp on: Power"); 
        power = !power;
    }
    // Kui robot on sees
    if(power){
        setLed(HIGH, HIGH);
        else if(g_ir_buf[17] == 0 && g_ir_buf[20] == 1){
            Serial.println("Nupp on: Channel Down");
        }
        else if(g_ir_buf[17] && g_ir_buf[20]){
            Serial.println("Nupp on: Channel Up"); 
        }
        else if(g_ir_buf[16] && g_ir_buf[17] == 0){
            Serial.println("Nupp on: AV/TV"); 
            keera(100);
        }
        else if(g_ir_buf[18] && g_ir_buf[19]){
            Serial.println("Nupp on: Mute");
            fiftyCm(); 
        }
        else if(g_ir_buf[17] && g_ir_buf[18] == 0 && g_ir_buf[16]){
            Serial.println("Nupp on: Volume Down");
            kymmeEdasi(); 
        }
        else if(g_ir_buf[18] && g_ir_buf[19] == 0 && g_ir_buf[20] == 0){
            Serial.println("Nupp on: Volume Up"); 
            kymmeTagasi();
        }
        else{
          setWheels();
        }
    }
    // Kui robot on väljas
    else{
        setWheels();
        setLed(LOW, LOW);
    }
  }
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
    }
}

// Sõidab 10cm tagasi
void kymmeTagasi(){
    g_distance_in_cm = distanceInCm(); // Mõõdab praeguse kauguse
    double goal = g_distance_in_cm + 10; // Kauguseks peab saama praegune kaugus + 10cm
    while (g_distance_in_cm < goal){
        tagasi(50); // Tagurdab kuni kaugus on praegune kaugus + 10cm
        g_distance_in_cm = distanceInCm();
    }
}

// Sõidab 10cm edasi
void kymmeEdasi(){
    double goal = 5;
    g_distance_in_cm = distanceInCm();
    if(g_distance_in_cm > 15){
        goal = g_distance_in_cm - 10;
    }
    while (g_distance_in_cm > goal){ // Sõidab edasi kuni kaugus on praegune kaugus - 10cm (minimaalselt 5cm)
        edasi(50);
        g_distance_in_cm = distanceInCm();
    }
}

// Keerab ~90 kraadi
void keera(int kestvus){
    setWheels(1600, 1600);
    delay(kestvus);
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