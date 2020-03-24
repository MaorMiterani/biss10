#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <string.h>


void main()
{
	char str[10000];
	char uniqueWords[10000] = { " " };
	int uniques = 0;
	FILE *alladin = fopen("C:\\aladdin.txt", "r");
	if (alladin == NULL) {
		printf("Could not open file");
		return;
	}
	while (fgets(str, 10000, alladin) != NULL)
	{
		char *word = strtok(str, " ,-\":?.!'");
		while (word != NULL) {
			if (strstr(uniqueWords, word) == NULL)
			{
				strcat(uniqueWords, word);
				uniques++;
			}


			word = strtok(NULL, " ,-?:\".!'");
		}
	}
	printf("This text has %d unique words", uniques);
	getchar();
}
