#include <stdio.h>

int* abs_val(int x[]);

int main(void)
{
	int x[2];
	x[0]=-1;
	x=abs_val(x);
	printf("Hello, Nikita!\n %d \n", x[0]);
}

int* abs_val(int x[]){
	if(x[0]<0){
		x[0]*-1;
		return x;
	}else{
		return x;
	}
}
