#include <IRremote.h>

int RECV_PIN = 2;

IRrecv irrecv(RECV_PIN);
decode_results results;

// specific button codes that were used in this project
#define CRVENO 0x707005FA
#define ZELENO 0x7070857A

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  irrecv.enableIRIn();
}

void loop() {
  // put your main code here, to run repeatedly:
  if(irrecv.decode(&results)) {
    if(results.value == CRVENO) Serial.println(CRVENO);
    if(results.value == ZELENO) Serial.println(ZELENO);
    irrecv.resume();
    delay(200);
  }
  else {
    Serial.println(3);
    delay(200);
  }
  
}
