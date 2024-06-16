#include <stdio.h>
#include <stdlib.h>

/**
 * convertToTitle - converts int to corresponding column title
 * 	as it appears in an excel sheet
 * @columnNumber: integer to convert
 *
 * Return: converted string
 */
char * convertToTitle(int columnNumber){
	int len = 0;
	int temp = columnNumber;
	
	char *result = (char *)malloc(len + 1);

	while (temp > 0)
	{
		temp = (temp - 1) / 26;
		len++;
	}

	result[len] = '\0';

	while (columnNumber > 0)
	{
		len--;
		columnNumber -= 1;
		result[len] = columnNumber % 26 + 'A';
		columnNumber /= 26;
	}

	return (result);
}


/**
 * main - entry point
 *
 * Return: 0 if successful
 */
int main(void)
{
	int n = 30;
	char *title;

	title = convertToTitle(n);
	printf("%s", title);

	return (0);
}
