class Solution:
    def longest_palindrome(self, s: str) -> str:
        # initialize the answer and its length
        ans = ''
        ans_len = 0

        # iterate through the string and expand the window
        for i in range(len(s)):
            # odd length palindromes
            l, r = i, i
            # expand the window as long as l and r are in bounds and the characters are equal
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # update the answer if the current substring is longer than the previous answer
                # and the answer length is the length of the current substring
                if (r - l + 1) > ans_len:
                    ans = s[l:r + 1]
                    ans_len = r - l + 1
                # move the left and right pointers
                l -= 1
                r += 1

            # even length palindromes
            # set the left and right pointers to the current index and the next index
            l, r = i, i + 1
            # expand the window as long as l and r are in bounds and the characters are equal
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # update the answer if the current substring is longer than the previous answer
                # and the answer length is the length of the current substring
                if (r - l + 1) > ans_len:
                    ans = s[l:r + 1]
                    ans_len = r - l + 1
                # move the left and right pointers
                l -= 1
                r += 1
        
        # return the answer
        return ans

solution = Solution()
print(solution.longest_palindrome("babad"))