class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        # initialize a set to store the characters in the current window 
        # and a pointer to the left of the window
        char_set = set()
        l = 0
        ans = 0

        # iterate through the string and expand the window
        for r in range(len(s)):
            # if the character is already in the set, remove the leftmost character
            # and move the left pointer to the right
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            # add the current character to the set and update the answer
            char_set.add(s[r])
            ans = max(ans, r - l + 1)

        # return the answer
        return ans

solution = Solution()
print(solution.length_of_longest_substring("abcabcbb"))