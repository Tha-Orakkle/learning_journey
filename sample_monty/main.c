#include "monty.h"

unsigned long int line_number;
char *file_name;
data_t data = {NULL, NULL, NULL, NULL, 0};

void monty(char *file_name, unsigned long int line_number)
{
	size_t size;
	int val;
	void(*code_func)(stack_t **, unsigned int);

	data->fptr = fopen(file_name, "r");
	if (!data.fptr)
	{
		dprintf(SRDERR_FILENO, FILE_ERROR, file_name);
		exit(EXIT_FAILURE);
	}
	while (1)
	{
		line_numeber++;
		val = getline(&(data.line), &size, data.fptr);

		if (val < 0)
			break;
		data.words = split_into_words(data.line);






int main(int argc, char *argv[])
{
	if (argc != 2)
	{
		dprintf(STDERR_FILENO, USAGE);
		exit(EXIT_FAILURE);
	}

	line_number = 0;
	file_name = argv[1];
	monty(file_name, line_number);

	return (EXIT_SUCCESS);
}

