#include "monty.h"

/**
 * call_func - finds the right function
 * @search: string from bytecode file
 *
 * Return: pointer to right function
 */

void (*call_func(char **search))(stack_t **stack, unsigned int line_num)
{
	instruction_t func_arr[] = {
		{"push", push},
		{"pall", pall},
		{"pint", pint},
		{NULL, NULL}
	}; /*num of code if func_arr*/
	int i;

	for (i = 0; func_arr[i].opcode; i++)
	{
		if (strcmp(func_arr[i].opcode, search[0]) == 0)
			return (func_arr[i].f);
	}
	return (NULL);
}
