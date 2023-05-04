from typing import List

class Solution:
    def two_sum(self, num: List[int], target: int) -> List[int]:
        # initialize prev_map
        prev_map = {}

        # iterate through num
        for i, n in enumerate(num):
            # calculate diff
            diff = target - n
            # if diff is in prev_map, return [prev_map[diff], i]
            if diff in prev_map:
                return [prev_map[diff], i]
            # add n to prev_map
            prev_map[n] = i

        # if no solution, return []
        return []

solution = Solution()
print(solution.two_sum([2, 7, 11, 15], 9))