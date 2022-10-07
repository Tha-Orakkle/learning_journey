#include "monty.h"

/**
 * push - handles the push instruction
 * @stack: double pointer to the stack to push to
 * @line_number: number of the line in the file
 */

void push(stack_t **stack, unsigned int line_number)
{
	stack_t *new;
	int num = 0, i;

	if (file_data.words[1] == NULL)
	{
		dprintf(STDERR_FILENO, PUSH_FAIL, line_number);
		free_data();
		free_stack();
		exit(EXIT_FAILURE);
	}

	for (i = 0; file_data.words[1][i]; i++)
	{
		if (isalpha(file_data.words[1][i]) != 0)
		{
			dprintf(STDERR_FILENO, PUSH_FAIL, line_number);
			free_data();
			free_stack();
			exit(EXIT_FAILURE);
		}
	}
	num = atoi(file_data.words[1]);

	if (file_data.s_or_q == 0)
		new = add_dnodeint(stack, num);
	else if (file_data.s_or_q == 1)
		new = add_dnodeint_end(stack, num);
	if (!new)
	{
		dprintf(STDERR_FILENO, MALLOC_FAIL);
		free_data();
		free_stack();
		exit(EXIT_FAILURE);
	}
}


/**
 * pall_handler - handles the pall instruction
 * @stack: double pointer to the stack to push to
 * @line_number: number of the line in the file
 */
void pall_handler(stack_t **stack, unsigned int line_number)
{
	(void) line_number;
	if (*stack)
		print_dlistint(*stack);
}
