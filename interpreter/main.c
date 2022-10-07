#include "monty.h"

file_data_t file_data = {NULL};

/**
 * monty - helper for the main procedure
 * @file_name: argv[1] shich is the file name
 */

void monty(char *file_name)
{
	unsigned int line_num = 0;
	size_t size = 0;
	int val, i = 0;
	void (*func)(stack_t **stack, unsigned int line_number);

	file_data.fptr = fopen(file_name, "r");
	if (!file_data.fptr)
	{
		dprintf(STDERR_FILENO, CANTOPEN, file_name);
		exit(EXIT_FAILURE);
	}

	while (1)
	{
		line_number++;
		val = getline(&(file_data.line), &size, file_data.fptr);
		if (val < 0)
			break;
		split_into_words(file_data.line);
		if (file_data.words == NULL || file_data.words[0][0] == '#')
		{
			/* free the line or words */
			continue;
		}
		func = call_func(file_data.words[0]);
		if (!func)
		{
			dprintf(STDERR_FILENO, UNKNOWN, line_num, file_data.words[0]);
			/*free lines, words, and information already on stack before exit */
			exit(EXIT_FAILURE);
		}
		func(file_data.stack, line_num);
		/* free line and words for next line within the while loop */
	}
	/*free line, words if contains any file, close file_name, free stack*/

}
/**
 * main - entry point for the monty bytecode interpreter
 * @argc: arguments count
 * @argv: pointer to arguments
 *
 * Return: EXIT_SUCCESS or EXIT_FAILURE
 *
 * Description: interprets a file containing a bytecode by getting
 * esch line and finding the right and matching instruction. then
 * executing the instruction
 */

int main(int argc, char *argv[])
{
	if (argc != 2)
	{
		dprintf(STDERR_FILENO, USAGE);
		exit(EXIT_FAILURE);
	}

	monty(argv[1]);

	exit(EXIT_SUCCESS);
}
