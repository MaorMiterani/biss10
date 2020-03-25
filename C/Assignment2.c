#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>

int strstr(char *str1, char *str2)
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
			return 1;
	}
	return 0;
}

void main()
{
	printf("%d\n", strstr("I have a beautiful face", "beautiful"));
	getchar();
}
