import pytest
from CD import Solution


params = [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True)
]


@pytest.mark.parametrize("list_case, expected_result", params)
def test_contains_duplicate(list_case, expected_result):
    case = Solution()
    assert case.contains_duplicate(list_case) == expected_result


@pytest.mark.parametrize("list_case, expected_result", params)
def test_contains_duplicate_alt(list_case, expected_result):
    case = Solution()
    assert case.contains_duplicate_alt(list_case) == expected_result


@pytest.mark.parametrize("list_case, expected_result", params)
def test_contains_duplicate_hash_set(list_case, expected_result):
    case = Solution()
    assert case.contains_duplicate_hash_set(list_case) == expected_result
