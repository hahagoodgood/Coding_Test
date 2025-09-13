#include<stdio.h>
#include<malloc.h>
int main(void) {
	int n, Max= NULL, Min = NULL, i;
	scanf("%d", &n);
	int* arr = (int*)malloc(n * sizeof(int));
	for (i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
		if (Max == NULL || Min == NULL) {
			Max = arr[i];
			Min = arr[i];
		}
		else {
			if (Max < arr[i])
				Max = arr[i];
			if (Min > arr[i])
				Min = arr[i];
		}
	}
	printf("%d %d", Min, Max);
}