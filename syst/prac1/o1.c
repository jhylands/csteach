#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>

main(){
	int fd;
	fd = open("in1.txt", O_RDONLY);
	printf("%d\n",fd);
}
