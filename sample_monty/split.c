#include "monty.h"

/**
 * count_word - helper function to count the number of words in a string
 * @s: string to evaluate
 *
 * Return: number of words
 */
int count_word(char *s)
{
	int flag = 0, i, words = 0;

	for (i = 0; s[i] != '\0'; i++)
	{
		if (s[i] == ' ')
			flag = 0;
		else if (flag == 0)
		{
			flag = 1;
			words++;
		}
	}

	return (words);
}

/**
 * split_into_words - splits a string into words
 * @str: string to split
 *
 * Return: pointer to an array of strings (Success)
 * or NULL (Error)
 */
void split_into_words(char *str)
{
	char *token;
	int words, i = 0;

	words = count_word(str);

	data.words = malloc(sizeof(char *) * (words + 1));
	if (!data.words)
		return;

	if (words == 1)
		data.words[i++] = str;
	else
	{
		token = strtok(str, " ");
		while (token)
		{
			data.words[i++] = token;
			token = strtok(NULL, " ");
		}
	}
	data.words[i] = NULL;
}
