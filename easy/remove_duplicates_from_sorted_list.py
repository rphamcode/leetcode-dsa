from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initialize current to head
        current = head

        # iterate through the linked list
        while current and current.next:
            # if current.val is equal to current.next.val
            if current.val == current.next.val:
                # set current.next to current.next.next
                current.next = current.next.next
            # otherwise
            else:
                # increment current
                current = current.next

        # return head
        return head

    def list_to_linked_list(self, lst):
        # initialize dummy_head and current
        dummy_head = current = ListNode()

        # iterate through lst
        for i in lst:
            # set current.next to ListNode(i)
            current.next = ListNode(i)
            # increment current
            current = current.next

        # return dummy_head.next
        return dummy_head.next


def print_linked_list(head):
    current = head

    while current:
        print(current.val, end = ' -> ' if current.next else '\n')
        current = current.next

solution = Solution()
head = solution.list_to_linked_list([1, 1, 2, 3, 3])
print_linked_list(solution.delete_duplicates(head))