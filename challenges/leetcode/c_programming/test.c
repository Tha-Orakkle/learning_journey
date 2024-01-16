#include <stdio.h>
#include <stdlib.h>

/**
 * Temporary Description:
 * Adds the element of the nodes of a linked list
 */
struct ListNode {
	int val;
	struct ListNode *next;
};

void printall(struct ListNode *head);
struct ListNode *add_node(struct ListNode **head, int num);
struct ListNode *addTwoNumbers(struct ListNode *l1, struct ListNode *l2);
void reverse_list(struct ListNode **head);

struct ListNode* addTwoNumbers(struct ListNode *l1, struct ListNode *l2)
{
	struct ListNode *sum_list = NULL;
	int sum, carry = 0, rem;

	while (l1 || l2)
	{
		sum = (l1->val + l2->val) + carry;
		rem = sum % 10;
		add_node(&sum_list, rem);
		carry = sum / 10;
		l1 = l1->next;
		l2 = l2->next;
	}
	reverse_list(&sum_list);

	return (sum_list);

}

void reverse_list(struct ListNode **head)
{
	struct ListNode *next = NULL;
	struct ListNode *prev = NULL;
	struct ListNode *current = *head;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	(*head) = prev;
}


struct ListNode *add_node(struct ListNode **head, int num)
{
	struct ListNode *new_node;

	new_node = malloc(sizeof(struct ListNode));

	if (!new_node)
		return (NULL);

	new_node->val = num;
	new_node->next = (*head);
	(*head) = new_node;

	return (*head);
}

int main(void)
{
	struct ListNode *list1 = NULL;
	struct ListNode *list2 = NULL;
	struct ListNode *sumoftwo = NULL;


	add_node(&list1, 3);
	add_node(&list1, 4);
	add_node(&list1, 2);

	add_node(&list2, 4);
	add_node(&list2, 6);
/*	add_node(&list2, 5);*/

	sumoftwo = addTwoNumbers(list1, list2);
	printall(sumoftwo);

	return (0);
}

void printall(struct ListNode *head)
{
	while (head)
	{
		printf("%d\n", head->val);
		head = head->next;
	}
}

