#include <stdio.h>
typedef int bool;
#define true 1
#define false 0

bool strstr(char *str1, char *str2)
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

void main()
{
	printf("%d\n", strstr("I have a beautiful face", "beautiful"));
	getchar();
}
