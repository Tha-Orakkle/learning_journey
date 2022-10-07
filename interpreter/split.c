#include "monty.h"

/**
 * count_words - count the words in a sting
 * @s: string
 *
 * Return: return number of words
 */

int count_words(char *s)
{
	int i = 0, words = 0, flag = 1;

	while (s[i] != '\0')
	{
		if (s[i] == ' ' && s[i + 1] != '\0')
			flag = 1;
		if (flag == 1)
		{
			words++;
			flag = 0;
		}
		i++;
	}
	return (words);
}

/**
 * split_into_words - splits a string into words
 * saves the splited words to the extern struct member **words
 */

void split_into_words(char *str)
{
	char *token;
	int words, i = 0;

	words = count_words(str);

	file_data.words = malloc(sizeof(char *) * (words + 1));
	if (!file_data.words)
		return;
	token = strtok(str, " ");
	while (token)
	{
		file_data.words[i++] = token;
		token = strtok(NULL, " ");
	}
	file_data.words[i] = NULL;
}
