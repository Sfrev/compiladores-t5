#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main() {
struct {
char
 
 
nome
[50]
;
int
 
 
idade
;
}
 
 
reg
;
strcpy(
 
reg
.
nome
, "Maria");
 
reg
.
idade
 = 24;
printf("%s", reg.nome);
printf("%s", " tem ");
printf("%d", reg.idade);
printf("%s", " anos");
return 0;
}
