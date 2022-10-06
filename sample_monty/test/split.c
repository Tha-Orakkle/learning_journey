#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/** count_words - count the words in a string
 * @s: string
 *
 * Return: number of words
 */

int count_words(char *s)
{
	int state = 0, i, count = 0;

	for (i = 0; s[i] != '\0'; i++)
	{
		if (s[i] == ' ')
			state = 0;
		else if (state == 0)
		{
			state = 1;
			count++;
		}
	}

	return (count);
}

char **split_into_words(char *str)
{
	char **splited_words;
	int i = 0, j, words;
	char *token, *delim = " ";
	char string[1024];

	words = count_words(str);
	splited_words = (char **)malloc(sizeof(char *) * (words + 1));
	if (!splited_words)
		return (NULL);

	for (j = 0; str[j] != '\0'; j++)
		string[j] = str[j];
	string[j] = '\0';
	token = strtok(string, delim);
	splited_words[i] = strdup(token);
	while (token)
	{
		token = strtok(NULL, delim);
		i++;
		splited_words[i] = strdup(token);
	}
	splited_words[i + 1] = NULL;
	return (splited_words);
}

int main(void)
{
	char **matrix;
	char *line = "this is a new line to be splited";

	matrix = split_into_words(line);
	printf("%s\n", *matrix);

	return (0);
}
