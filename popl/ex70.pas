program  mutex;
var   C : integer;
var flag1: boolean;
var flag2: boolean;

process  type P1;
var l : integer;
begin
	for l := 1 to 20 do
begin
		while flag2 do
		     null;
		flag1 := true;
		C := C + 1;
		flag1 :=false
end
end;

process  type P2;
var l : integer;
begin
	while flagstart do
		null;
	for l := 1 to 20 do
begin
		while flag1 do
		     null;
		flag2 := true;
		C := C + 1;
		flag2 :=false
end
end;

var call1 : P1;
var call2 : P2;

begin
	C := 0;
	flagstart := true;
	flag1 := false;
	flag2 := false;
	cobegin
		call1;
		call2
	coend;
write(C)
end.
