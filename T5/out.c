#include <stdio.h>
#include <stdlib.h>
int main() {
int x;
int* endx;
x = 0;
printf("%d%s",x," e ");
endx = &x;
*endx = 1;
printf("%d",x);
return 0;
}
