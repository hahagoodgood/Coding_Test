#include <stdio.h>

int main(void)
{
	int D[3],i,M=0;
	

	scanf("%d %d %d", &D[0], &D[1], &D[2]);
	
	if (D[1] == D[2] && D[0] == D[2])
		printf("%d", 10000 + D[1] * 1000);
	else if (D[0] == D[1] || D[1] == D[2] || D[0] == D[2]) {
		for (i = 0; i < 3; i++)
			if (D[i] == D[(i + 1) % 3])
				printf("%d", 1000 + D[i] * 100);
	}
	else {
		for (i = 0; i < 3; i++)
			if (D[M] < D[i])
				M = i;
		printf("%d", D[M] * 100);
		}
}