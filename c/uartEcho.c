#include <stdio.h>
#include <string.h>
#include <errno.h>

#include <wiringPi.h>
#include <wiringSerial.h>

int main (int argc, char* argv[])
{
	int i=10;
	int fd ;
	int nb_char=0;
	char donnee;
	
	fd = serialOpen ("/dev/ttyAMA0", 9600);			// configuration et ouverture du port serie

	if (wiringPiSetup () == -1)
	  {
	    fprintf (stdout, "oops: %s\n", strerror (errno)) ;
	    return 1 ;
	  }

	while (i>0)
	{
		printf ("nombre envoye -> %02d\n", i) ;		// affiche sur le terminal le nombre qui va etre envoye
		serialPutchar (fd, i) ;				// envoi via la patte TX le nombre i
		
		delay(100);					// attente de 100 ms

		donnee = serialGetchar (fd);			// recuperation du caractere
		printf ("nombre recu ->%02d\n\n", donnee) ;	// affichage du caractere recu

		i--;						// incrementation de i;

	}
	serialClose (fd);					// fermeture du port serie;
  	return 0 ;
}
