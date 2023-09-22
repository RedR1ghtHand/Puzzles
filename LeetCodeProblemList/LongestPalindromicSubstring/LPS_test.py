import pytest
from LPS import Solution


params = [
    ("babad", ("bab", "aba")),
    ("cbbd", "bb"),
    ("abaabc", "baab"),
]


@pytest.mark.parametrize("test_case, expected_result", params)
def test_longest_palindrome(test_case, expected_result):
    case = Solution
    result = case.longest_palindrome(test_case)

    match expected_result:
        case tuple():
            assert result in expected_result
        case _:
            assert result == expected_result

