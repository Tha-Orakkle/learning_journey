/**
 * hasCycle - Checks if a linked list has a cycle
 *
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    struct ListNode *slow;
    struct ListNode *fast;

    if (!head || !head->next)
        return false;
    slow = head;
    fast = head->next;

    while (fast && fast->next) {
        if (slow == fast)
            return true;
        slow = slow->next;
        fast = fast->next->next;
    }
    return false;
}
