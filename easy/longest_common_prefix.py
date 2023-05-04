from typing import List

class Solution:
    def longest_common_prefix(self, strs: List[str]) -> str:
        # initialize res to empty string
        res = ''

        # iterate through strs[0]
        for i in range(len(strs[0])):
            # iterate through strs
            for s in strs:
                # if i is out of range or s[i] is not strs[0][i], return res
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            # add strs[0][i] to res
            res += strs[0][i]

        # return res
        return res

solution = Solution()
print(solution.longest_common_prefix(["flower", "flow", "flight"]))