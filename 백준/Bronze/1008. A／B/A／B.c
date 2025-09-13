#include <stdio.h>

int main(void){
	double A , B;
	scanf("%lf %lf", &A, &B);
	double C = A / B;
	printf("%.9lf\n", C);
	return 0;
}