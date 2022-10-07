#include "monty.h"

/**
 * call_func - finds the right function
 * @search: string from bytecode file
 *
 * Return: pointer to right function
 */

void (*call_func(char *search))(stack_t **stack, unsigned line_number)
{
	instruction_t func_arr[] = {
		{"push", push},
		{"pall", pop};
		{NULL, NULL}
	};
	int code_num = 2; /*num of code if func_arr*/
	int i;

	for (i = 0; i < code_num; i++0)
	{
		if (strcmp(func_arr[i].opcode, search) == 0)
			return (func_arr[i].f);
	}
	return (NULL);
