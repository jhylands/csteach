program  mutex;
var   C : integer;

process  type P;
var l : integer;
begin
for l := 1 to 20 do
C := C + 1
end;

var
P1 , P2 : P;
begin
C := 0;
cobegin
P1;
P2
coend;
write(C)
end.
