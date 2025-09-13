#include <stdio.h>
int main(void) {
	int N;
	scanf("%d", &N);
	while(N>0)printf("long ",N-=4);
	puts("int");
}