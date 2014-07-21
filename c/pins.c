/*
 * blink.c:
 *      blinks the first LED
 *      Gordon Henderson, projects@drogon.net
 */

#include <stdio.h>
#include <wiringPi.h>

//pins d'entrada de la RaspPi
#define IN_BACK 	7		//7
#define IN_FRONT 	0		//11
#define IN_LEFT 	3		//15
#define IN_RIGHT 	2		//13
//pins sortida de la RaspPi, es fa servir pels leds del sostre
#define OUT_BACK 		1		//12
#define OUT_FRONT 		4		//16
#define OUT_RIGHT 		9		//5 	
#define OUT_LEFT 		8		//3	


void stopPins() {
	digitalWrite (OUT_FRONT, 0) ;
	digitalWrite (OUT_BACK, 0) ;
	digitalWrite (OUT_LEFT, 0) ;
	digitalWrite (OUT_RIGHT, 0) ;
}

void initPins(){
	pinMode (OUT_FRONT, OUTPUT) ;
	pinMode (OUT_BACK, OUTPUT) ;
	pinMode (OUT_LEFT, OUTPUT) ;
	pinMode (OUT_RIGHT, OUTPUT) ;

	stopPins();
}

int main (void)
{
	int total = 6;
	
	printf ("Raspberry Pi blink\n") ;

	if (wiringPiSetup () == -1)
		return 1 ;
	
	
	
	initPins();
	
	digitalWrite (OUT_FRONT, 1) ;  
	
	while(total--)
	{
	delay (500) ;               // mS
	digitalWrite (OUT_FRONT, 0) ;       // Off
	digitalWrite (OUT_LEFT, 1) ;
	delay (500) ;
	digitalWrite (OUT_LEFT, 0) ;       // Off
	digitalWrite (OUT_BACK, 1) ;
	delay (500) ;
	digitalWrite (OUT_BACK, 0) ;       // Off
	digitalWrite (OUT_RIGHT, 1) ;
	delay (500) ;
	digitalWrite (OUT_RIGHT, 0) ;       // Off
	digitalWrite (OUT_FRONT, 1) ;
	}
	
	stopPins();
	
	return 0 ;
}
