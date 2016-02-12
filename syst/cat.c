main(){
	char c;
	char arr[5];
	arr[0] = '1';
	while(read(0,c,1) ==1){
		write(1, &c ,1);
	}
}
