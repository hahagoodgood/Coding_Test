#include <stdio.h>

int main(void)
{
	int H, M, C;
	scanf("%d %d\n%d", &H, &M, &C);
	M += C;
	printf("%d %d", (H + M / 60) % 24, M % 60);
	return 0;
}