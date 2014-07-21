
#include <stdio.h>
#include <string.h>    //strlen
#include <errno.h>

/* Server */
#include <sys/socket.h>
#include <arpa/inet.h> //inet_addr
#include <unistd.h>    //write

/* LED & Serial */
#include <wiringPi.h>
#include <wiringSerial.h>



#define BUFF_SIZE 256

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


typedef struct tCommand{
	int x;
	int y;
} tCommand;



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

int init(){
	if (wiringPiSetup () == -1)
		return -1;
	
	initPins();
	
	return 0;
}

tCommand readInput(char* input){
	tCommand command;
	printf("%c", input[0]);
	command.x = 1;
	command.y = -1;
	
	return command;
}

int showLeds(tCommand com){
	if (com.x ==  1){
		digitalWrite (OUT_LEFT, 0);
		digitalWrite (OUT_RIGHT, 1);
	}
	else if (com.x ==  0){
		digitalWrite (OUT_LEFT, 0);
		digitalWrite (OUT_RIGHT, 0);
	}
	else if (com.x ==  -1){
		digitalWrite (OUT_LEFT, 1);
		digitalWrite (OUT_RIGHT, 0);
	}
		
	if (com.y ==  1){
		digitalWrite (OUT_BACK, 0);
		digitalWrite (OUT_FRONT, 1);
	}
	else if (com.y ==  0){
		digitalWrite (OUT_BACK, 0);
		digitalWrite (OUT_FRONT, 0);
	}
	else if (com.y ==  -1){
		digitalWrite (OUT_BACK, 1);
		digitalWrite (OUT_FRONT, 0);
	}
}


int serverListen(){
    int socket_desc , client_sock , c , read_size;
    struct sockaddr_in server , client;
    char client_message[BUFF_SIZE];
     
    //Create socket
    socket_desc = socket(AF_INET , SOCK_STREAM , 0);
    if (socket_desc == -1)
    {
        printf("Could not create socket");
        return -1;
    }
    puts("Socket created");
     
    //Prepare the sockaddr_in structure
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons( 44000 );
     
    //Bind
    if( bind(socket_desc,(struct sockaddr *)&server , sizeof(server)) < 0)
    {
        //print the error message
        perror("bind failed. Error");
        return -1;
    }
    puts("bind done");
     
    //Listen
    listen(socket_desc , 3);
     
    //Accept and incoming connection
    puts("Waiting for incoming connections...");
    c = sizeof(struct sockaddr_in);
     
    //accept connection from an incoming client
    while (client_sock = accept(socket_desc, (struct sockaddr *)&client, (socklen_t*)&c)){
		if (client_sock < 0)
		{
		    perror("accept failed");
		    return -1;
		}
		puts("Connection accepted");

		//Receive a message from client
		//while( (read_size = recv(client_sock , client_message , 2000 , 0)) > 0 )
		while ((read_size = read(client_sock, client_message, sizeof(client_message)-1)) > 0)
		{
			client_message[read_size] = '\0';
		    showLeds(readInput(client_message));
		    client_message[0] = '\0';
		    fflush(stdout);
		    
		    //Send the message back to client
		    //write(client_sock , client_message , strlen(client_message));
		}
		 
		if(read_size == 0)
		{
		    puts("Client disconnected");
		    fflush(stdout);
		}
		else if(read_size == -1)
		{
		    perror("recv failed");
		}
    }
}

int main(int argc , char *argv[])
{
	if (init() == -1)
		return -1;
		
	serverListen();
	
	return 0;		
}
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
