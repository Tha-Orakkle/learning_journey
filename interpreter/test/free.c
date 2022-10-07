#include "monty.h"

/**
 * free_data - free memories
 * @check: signifies if the stack should also
 * be freed
 */
void free_data(int check)
{
	int i;

	if (file_data.line)
	{
		free(file_data.line);
		file_data.line = NULL;

		if (file_data.words)
		{
			for (i = 0; file_data.words[i]; i++)
				free(file_data.words[i]);
			free(file_data.words);
			file_data.words = NULL;
		}
	}
	if (check)
	{
		if (file_data.stack)
		{
			/*free a doubly linked list */
			file_data.stack = NULL;
		}
		if (file_data.fptr)
		{
			fclose(file_data.fptr);
			file_data.fptr = NULL;
		}
	}
}

