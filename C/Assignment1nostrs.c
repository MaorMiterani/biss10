#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef int bool;
#define true 1
#define false 0

bool strstr2(char *str1, char *str2)
{
	int str2Len = strlen(str2);
	int equalChars = 0;
	for (int i = 0; i < strlen(str1); i++)
	{
		equalChars = 0;
		if (str1[i] == str2[0])
		{
			for (int j = 0; j < str2Len; j++)
			{
				if (str1[i + j] == str2[j])
				{
					equalChars++;
				}
			}
		}
		if (equalChars == str2Len)
			return true;
	}
	return false;
}

char* StringAppend(char str[], char stradd[])
{
	int j = strlen(str);
	if (strlen(str) == 1)
		j = 0;
	for (int i = j; i - j <= strlen(stradd); i++)
	{
		str[i] = stradd[i - j];
	}
	
}

void main()
{
	char str[10000];
	char uniqueWords[10000] = { " " };
	char word[50];
	int uniques = 0;
	char c;
	FILE *fp = fopen("C:\\aladdin.txt", "r");
	if (fp == NULL) {
		printf("Could not open file");
		return;
	}
	int i = 0;
	while (1) 
	{
		c = fgetc(fp);
		if (c != '"' && c != '.' && c != '!' && c != '?' && c != '.' && c != ',' && c != '\'' && c != '\n')
			str[i] = c;
		else
			str[i] = ' ';
		if (feof(fp)) {
			str[i] = '\0';
			break;
		}
		i++;
	}
	i = 0;
	int j = 0;
	while (str[i] != '\0')
	{
		if (str[i] != ' ')
		{
			for (j = 0; str[i + j] != ' ' && str[i + j] != '\0'; j++)
			{
				word[j] = str[i + j];
			}
			word[j] = ' ';
			word[j+1] = '\0';
			if (strstr2(uniqueWords, word) == false)
			{
				StringAppend(uniqueWords, word);
				uniques++;
				i += j;
			}
			else
			{
				i++;
			}
		}
		else
			i++;
	}
	fclose(fp);
	printf("This text has %d unique words", uniques);
	getchar();
}
