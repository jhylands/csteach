#include <stdio.h>

int stateLocation(char name);
struct place{
	char name;
	struct place *w;
	struct place *a;
	struct place *s;
	struct place *d;
};

int main(void)
{
	int notWon;
	char lastChar;
	/*define the structure of the map*/
	struct place *pos;
	struct place outside;
	struct place door;
	struct place chair;
	struct place centreOfRoom;
	struct place bookShelf;
	struct place desk;
	struct place wall;

	pos = &outside;

	door.name = 'D';
	door.w = &centreOfRoom;
	door.a = &wall;
	door.s = &outside;
	door.d = &wall;

	outside.name = 'O';
	outside.w = &door;
	outside.a = &wall;
	outside.s = &outside;
	outside.d = &wall;

	chair.name = 'C';
	chair.w = &wall;
	chair.a = &door;
	chair.s = &centreOfRoom;
	chair.d = &desk;

	centreOfRoom.name='c';
	centreOfRoom.w = &desk;
	centreOfRoom.a = &chair;
	centreOfRoom.s = &door;
	centreOfRoom.d = &bookShelf;
	
	bookShelf.name='B';
	bookShelf.w=&wall;
	bookShelf.a=&desk;
	bookShelf.s=&centreOfRoom;
	bookShelf.d=&door;
	
	desk.name = 'd';
	desk.w = &wall;
	desk.a=&chair;
	desk.s = &centreOfRoom;
	desk.d = &bookShelf;

	wall.name='W';
	wall.w = 0;
	wall.a = 0;
	wall.s = 0;
	wall.d = 0;

	
	notWon = 1;
	printf("Welcome!\n You are outside a room. Submit wasd to move. k to use items.");
	
	while(notWon){
		lastChar=getchar();
		switch(lastChar){
		case 'w':
			pos = (*pos).w;
			break;
		case 'a':
			pos = (*pos).a;
			break;
		case 's':
			pos = (*pos).s;
			
			break;
		case 'd':
			pos = (*pos).d;
			
			break;
		case 'k':
			
			break;
		default:
			printf(">!\n");
		}
		if(stateLocation ((*pos).name)){
			break;
		}
	}
	return 0;
}

int stateLocation(char name){
	switch(name){
	case 'O':
		printf("You are outside!");
		break;
	case 'd':
		printf("You are at the desk!");
		break;
	case 'B':
		printf("You are at a bookcase!");
		break;
	case 'C':
		printf("You are at a chair!");
		break;
	case 'D':
		printf("You are at the door!");
		break;
	case 'c':
		printf("You are in the center of the room!");
		break;
	default:
		printf("Not sure where you are? You have probably hit a wall");
		return 1;
	}
	printf("\n");
	return 0;
}
