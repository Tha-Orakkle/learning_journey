#include <stdio.h>



/**
 * Definition for singly-linked list.
 */
struct ListNode {
	int val;
	struct ListNode *next;
};

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
	struct ListNode *head = list1;
}

struct ListNode *addNodeEnd(struct ListNode **head, int val)
{
	struct ListNode *temp = head;
	struct ListNode *new;

	new = malloc(sizeof(struct ListNode));
	if (!new)
		return (NULL);

	new->val = val;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (*head);
	}
	while (temp->next)
		temp = temp->next;
	temp->next = new;

	return (new);
}
