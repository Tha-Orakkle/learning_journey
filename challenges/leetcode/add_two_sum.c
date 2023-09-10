#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>

/**
 * Temporary Description:
 * Adds the elements of the nodes of two linked lists
 */
typedef struct ListNode_s
{
    int val;
    struct ListNode_s *next;
} ListNode_t;


void reverse_list(ListNode_t **head);
int64_t gets_nodeint(ListNode_t **head);
ListNode_t *sum_Linkedlist(int64_t num);
ListNode_t *add_node(ListNode_t **head, int num);
void printall(ListNode_t *head);
ListNode_t* addTwoNumbers(ListNode_t *l1, ListNode_t *l2);


int main(void)
{
        ListNode_t *list1 = NULL;
        ListNode_t *list2 = NULL;
        ListNode_t *sumoftwo = NULL;


        add_node(&list1, 3);
        add_node(&list1, 4);
        add_node(&list1, 2);

        add_node(&list2, 4);
        add_node(&list2, 6);
        add_node(&list2, 5);

        sumoftwo = addTwoNumbers(list1, list2);
        printall(sumoftwo);

        return (0);
}

void printall(ListNode_t *head)
{
        while (head)
        {
                printf("%d\n", head->val);
                head = head->next;
        }
}

ListNode_t* addTwoNumbers(ListNode_t *l1, ListNode_t *l2)
{
    int64_t sum_val, value1, value2;
    ListNode_t *sum_list;

    reverse_list(&l1);
    value1 = gets_nodeint(&l1);
    reverse_list(&l2);
    value2 = gets_nodeint(&l2);
    sum_val = value1 + value2;

    sum_list = sum_Linkedlist(sum_val);
    reverse_list(&sum_list);

    return (sum_list);
}

void reverse_list(ListNode_t **head)
{
    ListNode_t *next = NULL;
    ListNode_t *prev = NULL;
    ListNode_t *current = *head;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    (*head) = prev;
}

int64_t gets_nodeint(ListNode_t **head)
{
    int64_t value = 0, weight = 1;
    ListNode_t *current = *head;

    while (current)
    {
        value = (value * weight) + current->val;
        current = current->next;
        weight = 10;
    }

    return (value);
}

ListNode_t *sum_Linkedlist(int64_t num)
{
    ListNode_t *new = NULL;
    int rem;

    if (num == 0)
	    add_node(&new, num);
    else
    {
	    while (num != 0)
	    {
		    rem = num % 10;
		    add_node(&new, rem);
		    num = num / 10;
	    }
    }

    return (new);
}

ListNode_t *add_node(ListNode_t **head, int num)
{
    ListNode_t *new_node;

    new_node = malloc(sizeof(ListNode_t));

    if (!new_node)
        return (NULL);

    new_node->val = num;
    new_node->next = (*head);
    (*head) = new_node;

    return (*head);

}
