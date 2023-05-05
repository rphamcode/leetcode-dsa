from typing import List

class Solution:
    def max_area(self, height: List[int]) -> int:
        # initialize the max area
        # initialize the left pointer to the start of the array
        # initialize the right pointer to the end of the array
        max_area = 0
        l, r = 0, len(height) - 1

        # iterate through the array while the left pointer is less than the right pointer
        while l < r:
            # calculate the width
            width = r - l
            # calculate the max area by taking the minimum of the two heights and multiplying it by the width
            # and comparing it to the current max area
            max_area = max(max_area, min(height[l], height[r]) * width)

            # move the left pointer if the left height is less than the right height
            # otherwise, move the right pointer
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        # return the max area
        return max_area

solution = Solution()
print(solution.max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))