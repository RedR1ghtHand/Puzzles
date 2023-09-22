class Solution:
    def longest_palindrome(s: str) -> str:
        # Expand from Centers solution link -> https://www.youtube.com/watch?v=E-tmN1OM9aA
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        result = ""
        for i in range(len(s)):
            sub1 = expand(i, i)
            if len(sub1) > len(result):
                result = sub1
            sub2 = expand(i, i + 1)
            if len(sub2) > len(result):
                result = sub2
        return result
