#include <stdio.h>
#include <stdlib.h>
int main() {
typedef struct{
char nome[80];
int idade;
}treg;
char nome[80];
int idade;
treg reg;
strcpy(reg.nome, "Maria");
reg.idade = 30;
printf("%s%s%d%s",reg.nome," tem ",reg.idade," anos");
return 0;
}
