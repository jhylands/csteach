#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>

main(){
	int fd;
	fd = open("out2.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
	if (fd <0){
		perror("o3");
		exit(1);
	}
}
