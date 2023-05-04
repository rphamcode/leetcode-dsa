from typing import List

class Solution:
    def validate_stack_sequences(self, pushed: List[int], popped: List[int]) -> bool:
        # initialize stack and index
        stack = []
        i = 0

        # iterate through pushed 
        for num in pushed:
            # append num to stack
            stack.append(num)

            # while stack is not empty and i is less than length of popped and top of stack is equal to popped[i]
            while i < len(popped) and stack and stack[-1] == popped[i]:
                # pop from stack and increment i
                stack.pop()
                i += 1

        # return true if stack is empty
        return not stack

solution = Solution()
print(solution.validate_stack_sequences([1,2,3,4,5], [4,5,3,2,1]))