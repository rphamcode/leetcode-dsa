class Solution:
    def is_palindrome(self, x: int) -> bool: 
        # if x is negative, return False
        if x < 0:
            return False

        # initialize div
        div = 1

        # find div 
        while x >= div * 10:
            div *= 10

        # iterate through x
        while x:
            # find left and right digits of x 
            left = x // div
            right = x % 10

            # if left and right digits are not equal, return False
            if left != right:
                return False

            # remove left and right digits from x 
            x = (x % div) // 10
            # remove two zeros from div
            div //= 100
        
        # return True
        return True

solution = Solution()
print(solution.is_palindrome(121))