#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>

int fibbonaci(int n)
{
	if (n == 0)
		return 0;
	if (n == 1)
		return 1;
	return fibbonaci(n - 1) + fibbonaci(n - 2);
}


void main()
{
	printf("%d", fibbonaci(20));
	getchar();
}
