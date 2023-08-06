#define ldrpin A0
int ldr = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(11, OUTPUT);
  pinMode(A0, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(11, HIGH);
  delay(500);
  ldr = analogRead(ldrpin);
  Serial.println(ldr);
  delay(500);
  digitalWrite(11, LOW);
  delay(1000);
}
