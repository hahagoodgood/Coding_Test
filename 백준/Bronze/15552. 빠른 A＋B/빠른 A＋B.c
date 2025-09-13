#include <stdio.h>
int main(void) {
	int n,a,b;
	scanf("%d",&n);
	while (n > 0) {
		scanf("%d %d", &a, &b);
		printf("%d\n", a + b);
		n -= 1;
	}
	return 0;
}