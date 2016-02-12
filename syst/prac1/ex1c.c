main(){
	char c;
	int s[256];
	char readIterator=0;
	while(read(0,&c,1) ==1){
		s[readIterator] = c;
	} 
	for(readIterator=0; readIterator<256;readIterator++){
		write(1, s[readIterator],1);
	}
}
