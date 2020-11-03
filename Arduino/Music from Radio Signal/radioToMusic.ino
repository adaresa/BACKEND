/* Includes ----------------------------------------------------- */
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24Network.h>
#include <RF24.h>

/* User defines ------------------------------------------------------ */
#define node_address 011 // Ask this from supervisor
#define radio_channel 127 //Do not change!

/* Defines ------------------------------------------------------ */
#define button_pin 2
#define sonic_echo_pin 3
#define sonic_trig_pin 4
#define right_servo_pin 5
#define left_servo_pin 6
#define right_led 7
#define left_led 8
#define left_qti A0
#define middle_qti A1
#define right_qti A2
#define ir_receiver A3
#define buzzer_pin A4
#define min_pulse 1300
#define max_pulse 1700
#define standstill 1500

/* Global variables -------------------------------------------- */
byte g_pin_states[] = {0, 0};
byte tempo = 150; // Initial song speed
/* For receiveing and storing radio data packet */
uint16_t incomingData = 0;
int index = 0;
int note = 0;
int duration = 0;
int node = 0;
long freq = 0;
int vasak; // Kas vasak tuli põleb
int viies = 0; // Kas on viies noot

/*
    Create an RF24 instance called "radio" by calling a constructor RF24
    The instance uses pins CE = 9 and CSN = 10
    Library functions are available from https://tmrh20.github.io/RF24/classRF24.html
*/
RF24 g_radio(9, 10);               // Pin setup for UNO
RF24Network network(g_radio);      // Include the radio in the network

/* Address through which the module communicates */
const uint16_t this_node = node_address;   // Address of our node in Octal! format ( 04,031, etc)
const uint16_t master = 00;    // Address of the other node in Octal! format

/* Private functions -------------------------------------------- */
void setLed(byte value_left = LOW, byte value_right = LOW)
{
  g_pin_states[1] = value_right;
  digitalWrite(right_led, value_right);
  g_pin_states[0] = value_left;
  digitalWrite(left_led, value_left);
}


/* Radio instance setup function */
bool radioSetup() {
  /* Start the radio instance */
  if (!g_radio.begin()) return 0;
  /* Checking if the radio is connected */
  if (!g_radio.isChipConnected()) return 0;

  network.begin(radio_channel, this_node);  //(channel, node address)
  g_radio.setDataRate(RF24_250KBPS); // RF24_250KBPS for 250kbs, RF24_1MBPS for 1Mbps, or RF24_2MBPS for 2Mbps
  g_radio.setPALevel(RF24_PA_MAX); // RF24_PA_MIN=-18dBm, RF24_PA_LOW=-12dBm, RF24_PA_MED=-6dBM, and RF24_PA_HIGH=0dBm.
  g_radio.setAutoAck(false);
  return 1;
}


/* Arduino functions -------------------------------------------- */
void setup()
{

  setLed(HIGH,LOW);
  vasak = 1;
  
  /* Start serial monitor */
  Serial.begin(9600);
  /* Initialize buzzer pin */
  pinMode(buzzer_pin, OUTPUT);
  /* Set the pin mode of LED pins as output */
  pinMode(right_led, OUTPUT);
  pinMode(left_led, OUTPUT);

  /* Set button pin as input */
  pinMode(button_pin, INPUT);

  /* Call radio setup, if failed then infinite loop */
  if (!radioSetup()) while (1);
  Serial.println("Radio initialized.");

  /* Inform about the end of the setup() function */
  Serial.println("--- Ardunio ready ---\n");

}

void loop()
{
  /* To keep the radio network running */
  network.update();
  
  while (network.available() ) { // stop here to wait for data or until 5 seconds have passed without answer from intersection controller
    RF24NetworkHeader header_master;
    
    /* More information about the network.read() 
     *  function is found in here: 
     *  https://tmrh20.github.io/RF24Network/classRF24Network.html#ac1369794c26042ebe9e3874adaec371a
     *  For header use the "header_master"
     *  For data use "incomingData
     */
     
    network.read(header_master, &incomingData, sizeof(incomingData)); // Read the incoming data
    Serial.println(incomingData,BIN);

    // Kui bitid 12-15 = 0, siis on indeks
    if(!bitRead(incomingData,12)&&!bitRead(incomingData,13)&&!bitRead(incomingData,14)&&!bitRead(incomingData,15)){
      indexDecoder(incomingData);
    }
    // Muidu on heli pakett
    else{
      // Kui on viies noot, siis töötle helipakett lahti
      decoder(incomingData);
    }
    /* Receive the signal
     * Serial print the signal value 
     * Try to understand which part is index and which is packet
     * Decode packet
     * Convert note from highTime to freq
     * Output note
     */
   
  }
}
bool indexDecoder(uint16_t packet) {    
  int i;
  int indx = 0;
  // Index kümnendnumbriks
  for(i=0;i<8;i++){
    if(bitRead(packet, i)){
      indx += pow(2,i);
    }
  }
  // Kui on viies noot, tähista ära
  if(indx%5 == 0){
    viies = 1;
  }

  return 1;
}


bool decoder(uint16_t packet) {    
  int i, temp = 0;
  int kestvus = 0;
  int korgus = 0;
  // Bitid 0-11 (heli kõrgus) kümnendarvuks, timeHigh ühikus
  for(i=0;i<12;i++){
    if(bitRead(packet, i)){
      korgus += pow(2,i);
    }
  }
  // Bitid 12-15 (kestvus) kümnendarvuks
  for(i=12;i<16;i++){
    if(bitRead(packet, i)){
      kestvus += pow(2,temp);
    }
    temp += 1;
  }
 
  korgus = (1000000 / (2*korgus)) + 1; // timeHigh ühikust sagedusele

  // Mängi nooti
  playToneRadio(korgus, kestvus);
  
  /* Write the decoder function to get the
   * note and its duration information from 
   * the data packet. A lot of black magic
   * is needed.
   */

  return 1;
}

void playToneRadio(int noteTone, int duration)
{
  /* Play a tone until duration
     also keep in mind that notes can sometimes equal to 0
     this means that it's a pause!
     Also keep in mind that our host sends notes in "highTime"
     but function tone() requires frequency value.
  */

  freq = noteTone;
  
  // Kui sagedus on 0, siis on paus
  if(freq<=0){
    delay(duration * tempo);
  }
  else{
    // Mängi nooti antud sageduse ja kestvusega
    tone(buzzer_pin, freq, duration * tempo);
    // Kui vasak led põleb, paneb vastupidi
    if(vasak){
      setLed(LOW, HIGH);
      vasak = 0;
    }
    // Kui parem põleb, siis vastupidi
    else{
      setLed(HIGH,LOW);
      vasak = 1;
    }
  }
}