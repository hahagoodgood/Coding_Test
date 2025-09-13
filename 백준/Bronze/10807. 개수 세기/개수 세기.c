#include <stdio.h> 
int main(void) {int n,v,i,b=0,a[100];scanf("%d",&n);for(i=0;i<n;i++)scanf("%d",&a[i]);scanf("%d",&v);for(i=0;i<n;i++)if(a[i]==v)b++;printf("%d",b);return 0;}
