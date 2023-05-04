from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # initialize dummy_head, current, and carry
        dummy_head = current = ListNode()
        carry = 0

        # iterate through l1, l2, and carry
        while l1 or l2 or carry:
            # initialize v1 to l1.val if l1 else 0
            v1 = l1.val if l1 else 0
            # initialize v2 to l2.val if l2 else 0
            v2 = l2.val if l2 else 0

            # calculate sum
            total = v1 + v2 + carry
            # calculate carry
            carry = total // 10
            # calculate remainder
            remainder = total % 10

            # set current.next to ListNode(remainder)
            current.next = ListNode(remainder)

            # increment current
            current = current.next
            # increment l1 if l1 else None
            l1 = l1.next if l1 else None
            # increment l2 if l2 else None
            l2 = l2.next if l2 else None

        # return dummy_head.next
        return dummy_head.next

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
l1 = solution.list_to_linked_list([2, 4, 3])
l2 = solution.list_to_linked_list([5, 6, 4])
result = solution.add_two_numbers(l1, l2)

print_linked_list(result)