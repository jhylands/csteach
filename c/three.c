// ConsoleApplication3.cpp : Defines the entry point for the console application.
//
#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
/*
int setUpBoard(char *board);
int printBoard(char board[]);
int playerMove(char *board, char player);
char checkForWin(char board[]);
struct vector getCoord();
*/
struct vector
{
	int x;
	int y;
};

int main(void)
{
	printf("Welcome to tic tac toe!");
	char board[9];
	setUpBoard(&(board[0]));
	while (checkForWin(board) == '-'){
		playerMove(&(board[0]), 'X');
		if (checkForWin(board) == '-') {
			playerMove(&(board[0]), 'O');
		}
	}
	return 0;
}

char setUpBoard(char board[]) {
	for (int i = 0; i < 3; i++) {
		for (int n = 0; n < 3; i++) {
			board[i*3+n] = '-';
		}
	}
	return board;
}
int printBoard(char board[]) {
	for (int i = 0; i < 3; i++) {
		printf("\n");
		for (int n = 0; n < 3; n++) {
			printf("%c" , board[i*3+n]);
			printf("|");
		}
	}
	return 0;
}
int playerMove(char *board, char player) {
	struct vector coord;
	do {
		coord = getCoord();
	} while (*(board + coord.x * 3 + coord.y) != '-');
	*(board+coord.x*3 + coord.y) = player;
	return 0;
}
char checkForWin(char board[]) {
	/*check rows*/
	for (int i = 0; i < 3; i++) {
		if ( board[2 * 3 + i] == board[3 + i] && board[i] == board[3 + i]) {
			return board[i];
		}
	}
	/*check columns*/
	for (int i = 0; i < 3; i++) {
		if ( board[i*3+2] == board[i*3+1] && board[i * 3] == board[i * 3 + 1] ) {
			return board[i*3];
		}
	}
	if (board[0] == board[4] && board[4] == board[9]) {
		return board[4];
	}
	return '-';
}
struct vector getCoord() {
	printf("Please enter the coordinates of where you would like to go:\n");
	printf("0,0|1,0|2,0\n0,1|1,1|2,1\n0,2|1,2|2,2");
	printf("x:");
	struct vector coord;
	scanf("%d", &coord.x);
	printf("/ny:");
	scanf("%d", &coord.y);
	return coord;
}// ConsoleApplication3.cpp : Defines the entry point for the console application.
//
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int setUpBoard(char *board);
int printBoard(char board[]);
int playerMove(char *board, char player);
char checkForWin(char board[]);
struct vector getCoord();

struct vector
{
	int x;
	int y;
};

int main(void)
{
	printf("Welcome to tic tac toe!");
	char board[9];
	setUpBoard(&(board[0]));
	while (checkForWin(board) == '-'){
		playerMove(&(board[0]), 'X');
		if (checkForWin(board) == '-') {
			playerMove(&(board[0]), 'O');
		}
	}
	return 0;
}

int setUpBoard(char *board) {
	for (int i = 0; i < 3; i++) {
		for (int n = 0; n < 3; i++) {
			*(board+i*3+n) = '-';
		}
	}
	return 0;
}
int printBoard(char board[]) {
	for (int i = 0; i < 3; i++) {
		printf("\n");
		for (int n = 0; n < 3; n++) {
			printf("%c" , board[i*3+n]);
			printf("|");
		}
	}
	return 0;
}
int playerMove(char *board, char player) {
	struct vector coord;
	do {
		coord = getCoord();
	} while (*(board + coord.x * 3 + coord.y) != '-');
	*(board+coord.x*3 + coord.y) = player;
	return 0;
}
char checkForWin(char board[]) {
	/*check rows*/
	for (int i = 0; i < 3; i++) {
		if ( board[2 * 3 + i] == board[3 + i] && board[i] == board[3 + i]) {
			return board[i];
		}
	}
	/*check columns*/
	for (int i = 0; i < 3; i++) {
		if ( board[i*3+2] == board[i*3+1] && board[i * 3] == board[i * 3 + 1] ) {
			return board[i*3];
		}
	}
	if (board[0] == board[4] && board[4] == board[9]) {
		return board[4];
	}
	return '-';
}
struct vector getCoord() {
	printf("Please enter the coordinates of where you would like to go:\n");
	printf("0,0|1,0|2,0\n0,1|1,1|2,1\n0,2|1,2|2,2");
	printf("x:");
	struct vector coord;
	scanf("%d", &coord.x);
	printf("/ny:");
	scanf("%d", &coord.y);
	return coord;
}
