from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        # initialize slow and fast to head
        slow = fast = head

        # iterate through the linked list
        # while fast and fast.next are not None
        while fast and fast.next:
            # increment slow by 1
            slow = slow.next
            # increment fast by 2
            fast = fast.next.next

            # if slow is equal to fast
            # return True
            if slow == fast:
                return True

        # return False
        return False
    
    def list_to_linked_list(self, lst, pos):
        # initialize dummy_head and current
        dummy_head = current = ListNode()

        # Create a variable to store the node at position 'pos'
        cycle_node = None
        position = 0

        # iterate through lst
        for i in lst:
            # set current.next to ListNode(i)
            current.next = ListNode(i)
            # increment current
            current = current.next

            # Check if the current position is 'pos', and if so, store the current node
            if position == pos:
                cycle_node = current
            position += 1

        # If 'pos' is within the list, create a cycle by connecting the last node to 'cycle_node'
        if cycle_node is not None:
            current.next = cycle_node

        # return dummy_head.next
        return dummy_head.next

solution = Solution()
head = solution.list_to_linked_list([1, 2, 3, 4, 5], 2)
print(solution.has_cycle(head))