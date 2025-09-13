#include <stdio.h>

int main(void)
{
	int a, b;
	scanf("%d\n%d", &a, &b);
	printf("%d\n%d\n%d\n%d\n", a * (b % 10), a * (b % 100 - b % 10)/10, a * (b - b % 100)/100, a * b);
}