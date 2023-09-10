#include <stdio.h>
#include <ctype.h>

#define MAX_SIZE 10

int roman_to_integer(char c);
int romanToInt(char *s);

/**
 * romanToInt - main conversion procedure
 * @s: roman numeral to be converted
 *
 * Return: integer
 */
int romanToInt(char *s)
{
	int i, int_num = roman_to_integer(s[0]);
	int prev_num, current_num;

	for (i = 1; s[i] != '\0'; i++)
	{
		prev_num = roman_to_integer(s[i - 1]);
		current_num = roman_to_integer(s[i]);
		
		if (prev_num < current_num)
			int_num = int_num - prev_num + (current_num - prev_num);
		else
			int_num += current_num;
	}
	return (int_num);
}

/**
 * roman_to_integer - helper function for conversion
 * @c: character
 *
 * Return: integer of the character received
 */
int roman_to_integer(char c)
{
	switch(c)
	{
		case 'I':
			return (1);
		case 'V':
			return (5);
		case 'X':
			return (10);
		case 'L':
			return (50);
		case 'C':
			return (100);
		case 'D':
			return (500);
		case 'M':
			return (1000);
		default:
			return (0);
	}
}

/**
 * main - converts roman numerals to an integer
 *
 * Return: 0 for success
 */
int main(void)
{
	int i;
	char *str;
	char str1[MAX_SIZE];

	printf("Enter a Roman Numeral:\n");
	scanf("%s", str);
	for (i = 0; str[i] != '\0'; i++)
	{
		if (isupper(str[i]) == 0)
			str1[i] = str[i] - 32;
		else
			str1[i] = str[i];
	}
	str1[i] = '\0';

	printf("Original roman numeral is: %s\n", str1);
	printf("Roman to integer: %d\n", romanToInt(str1));

	return (0);
}
