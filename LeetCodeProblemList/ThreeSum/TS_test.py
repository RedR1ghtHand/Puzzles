from LeetCodeProblemList.ThreeSum.TS import three_sum, three_sum_with_two_pointers
import pytest


params = [
    ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
    ([0,1,1], []),
    ([0,0,0], [[0,0,0]])
]


@pytest.mark.parametrize("test_case, expected", params)
def test_three_sum(test_case, expected):
    assert three_sum(test_case) == expected


@pytest.mark.parametrize("test_case, expected", params)
def test_three_sum_with_two_pointers(test_case, expected):
    assert three_sum_with_two_pointers(test_case) == expected

