class Solution:
    def length_0f_longest_substring(s: str) -> int:
        max_fixed_len = 0
        uniq_chars = set()
        left = 0
        for right in range(len(s)):
            if s[right] not in uniq_chars:
                uniq_chars.add(s[right])
                max_fixed_len = max(max_fixed_len, right - left + 1)
            else:
                while s[right] in uniq_chars:
                    uniq_chars.remove(s[left])
                    left += 1
                uniq_chars.add(s[right])
        return max_fixed_len





