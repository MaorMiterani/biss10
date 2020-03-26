#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void getline(char *str)
{
	int i = 0;
	char c = ' ';
	char buffer[256] = { "Initialize" };
	for (i = 0; i < 256; i++)
	{
		fread(&c, 1, 1, stdin);
		if (c != '\n')
		{
			buffer[i] = c;
		}
		else
		{
			buffer[i] = '\0';
			break;
		}
	}
	for (i = 0; buffer[i] != '\0'; i++);
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
