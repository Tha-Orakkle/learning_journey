#include "monty.h"

/**
 * free_data - free line and words
 */
void free_data(void)
{
	if (file_data.line)
	{
		free(file_data.line);
		file_data.line = NULL;
		free(file_data.words);
		file_data.words = NULL;
	}
}

/**
 * free_stack - frees stack and closes FILE
 */
void free_stack(void)
{
	if (file_data.stack)
	{
		free_dlistint(file_data.stack);
		file_data.stack = NULL;
	}
	if (file_data.fptr)
	{
		fclose(file_data.fptr);
		file_data.fptr = NULL;
	}
}
