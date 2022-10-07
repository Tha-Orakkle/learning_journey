#ifndef MONTY_H_
#define MONTY_H_


#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <ctype.h>

/**
 * struct stack_s - doubly linked list representation of a stack (or queue)
 * @n: integer
 * @prev: points to the previous element of the stack (or queue)
 * @next: points to the next element of the stack (or queue)
 *
 * Description: doubly linked list node structure
 * for stack, queues, LIFO, FIFO
 */
typedef struct stack_s
{
	int n;
	struct stack_s *prev;
	struct stack_s *next;
} stack_t;

/**
 * struct instruction_s - opcode and its function
 * @opcode: the opcode
 * @f: function to handle the opcode
 *
 * Description: opcode and its function
 * for stack, queues, LIFO, FIFO
 */
typedef struct instruction_s
{
	char *opcode;
	void (*f)(stack_t **stack, unsigned int line_number);
} instruction_t;

/**
 * file_data_s - data on a file to access corresponding functions
 * @fptr: file pointer
 * @line: line from a file
 * @words: lines splited to words
 */
typedef struct file_data_s
{
	FILE *fptr;
	char *line;
	char **words;
	stack_t *stack;
	int s_or_q;
} file_data_t;

extern file_data_t file_data;

#define USAGE "USAGE: monty file\n"
#define CANTOPEN "Error: Cant't open file %s\n"
#define UNKNOWN "L%d: unknown instruction %s\n"
#define MALLOC_FAIL "Error: malloc failed\n"
#define PUSH_FAIL "L%u: usage: push integer\n"

/* main.c */
void monty(char *file);

/* split.c */
int count_words(char *s);
void split_into_words(char *str);

/* call_func */
void (*call_func(char **search))(stack_t **stack, unsigned line_number);

/* free.c */
void free_data(void);
void free_stack(void);

/* helper_funcs.c */
size_t print_dlistint(const stack_t *h);
stack_t *add_dnodeint(stack_t **head, const int n);
stack_t *add_dnodeint_end(stack_t **head, const int n);
void free_dlistint(stack_t *head);
stack_t *insert_dnodeint_at_index(stack_t **h, unsigned int idx, int n);

/* operation_handler.c */
void push(stack_t **stack, unsigned int line_number);
void pall_handler(stack_t **stack, unsigned int line_number);



#endif
