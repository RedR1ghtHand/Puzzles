import pytest
from LeetCodeProblemList.LongestSubstringWithoutRepeatingCharacters.LSWRC import Solution


params = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("dvdf", 3),
    ("abc", 3),
    ("au", 2),
    ("", 0)
]


@pytest.mark.parametrize('case_string, expected_result', params)
def test_length_0f_longest_substring(case_string, expected_result):
    case = Solution
    assert case.length_0f_longest_substring(case_string) == expected_result
