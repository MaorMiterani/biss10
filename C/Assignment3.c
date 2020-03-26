#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void getline(char *str)
{
	int i;
	char buffer[256] = {"Initialize"};
	gets(buffer);
	for (i = 0; buffer[i] != '\0' && buffer[i] != '\n'; i++);
	str = (char*)realloc(str, i);
	strcpy(str, buffer);
}


void main()
{
	char *str = malloc(1);
	getline(str);
	printf(str);
	getchar();
}
