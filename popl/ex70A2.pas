program  mutex;
var   C : integer;
var   inFlip : boolean;
var   p1Flip : boolean;
var   p2Flip : boolean;

process  type PA;
var l : integer;
begin
	while inFlip do
	null;
	for l := 1 to 20 do
	C := C + 1
end;

process  type PB;
var l : integer;
begin
	for l := 1 to 20 do
	C := C + 1
	inFlip:=false;
end;

var
P1 : PA;
P2 : PB;
begin
        inFlip := true;
	p1Flip := false;
	p2Flip := false;
	C := 0;
	cobegin
		P1;
		P2
	coend;
	write(C)
end.
