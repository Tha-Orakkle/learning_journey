#include <stdio.h>
#include <stdlib.h>

typedef struct ListNode_s
{
	int val;
	struct ListNode_s *next;
} ListNode_t;

ListNode_t *addTwoNumbers(ListNode_t *l1, ListNode_t *l2)
{
	int rem = 0, flag = 0;
	int _sum, x, y;
	ListNode_t *current = NULL;
	ListNode_t *result = malloc(sizeof(ListNode_t));

	if (!result)
		return (NULL);

	result->next = NULL;
	current = result;

	while (l1 || l2 || rem)
	{
		if (flag == 1)
		{
			current->next = malloc(sizeof(ListNode_t));
			if (!current->next)
				return (NULL);
			current = current->next;
			current->next = NULL;
		}
		x = l1 ? l1->val : 0;
		y = l2 ? l2->val : 0;

		_sum = x + y + rem;
		rem = _sum / 10;
		current->val = _sum % 10;
		l1 = l1 ? l1->next : NULL;
		l2 = l2 ? l2->next : NULL;
		flag = 1;
	}

	return (result);
}

ListNode_t *add_node(ListNode_t **head, int val)
{
	ListNode_t *new_node, *temp;


	new_node = malloc(sizeof(ListNode_t));
	if (!new_node)
		return (NULL);

	new_node->val = val;
	new_node->next = NULL;

	if (!(*head))
	{
		(*head) = new_node;
		return (*head);

	}
	temp = (*head);

	while (temp && temp->next)
	{
		temp = temp->next;
	}
	temp->next = new_node;

	return (*head);
}



void printall(ListNode_t *head)
{
	while (head)
	{
		printf("%d\n", head->val);
		head = head->next;
	}
}

int main(void)
{
	ListNode_t *list1 = NULL;
	ListNode_t *list2 = NULL;
	ListNode_t *sumList = NULL;

	add_node(&list1, 2);
	add_node(&list1, 4);
	add_node(&list1, 9);
	add_node(&list1, 9);
	add_node(&list1, 9);


	add_node(&list2, 5);
	add_node(&list2, 6);
	add_node(&list2, 4);

	sumList = addTwoNumbers(list1, list2);
//	printall(list1);
//	printf("\n");
//	printall(list2);
	printall(sumList);

	return (0);
}
