class Solution:
    def is_valid(self, s: str) -> bool:
        # initialize stack and pairs
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        # iterate through string
        for c in s:
            # if c is a closing bracket
            if c in pairs:
                # if stack is empty or top of stack is not the opening bracket
                if len(stack) == 0 or stack.pop() != pairs[c]:
                    return False
            # if c is an opening bracket
            else:
                stack.append(c)

        # if stack is empty, return True
        return len(stack) == 0

solution = Solution()
print(solution.is_valid("()[{}]"))
print(solution.is_valid("()["))