#include <stdio.h> 
int main(void) {
	int n=0, x=0, a[10000], i=0;
	scanf("%d %d", &n, &x);
	for (i = 0; i < n; i++) {
		scanf("%d", &a[i]);
	}
	for (i = 0; i < n; i++) {
		if (a[i] < x) {
			printf("%d ", a[i]);
		}
	}
	return 0;
}