#include "monty.h"

/**
 * free_data - frees the data.line and data.words,
 * @flag: 1 or 0
 */

void free_data(int flag)
{
	int i = 0;

	if (data.line || data.words)
	{
		free(data.line);
		data.line = NULL;

		while (data.words[i])
		{
			free(data.words[i]);
			i++;
		}
		free(data.words);
		data.words = NULL;
	}

	if (flag)
	{
		if (data.stack)
		{
			free_dlistint(data.stack);
			data.stack = NULL;
		}
		if (data.fptr)
		{
			fclose(data.fptr);
			data.fptr = NULL;
		}
	}
}
