from LeetCodeProblemList.ContainerWithMostWater.CWMW import Solution
import pytest


params = [
    ([1,8,6,2,5,4,8,3,7], 49),
    ([1,1], 1)
]


@pytest.mark.parametrize("test_case, expected", params)
def test_max_area(test_case, expected):
    case = Solution()
    assert case.max_area(test_case) == expected


@pytest.mark.parametrize("test_case, expected", params)
def test_max_area_alt(test_case, expected):
    case = Solution()
    assert case.max_area_alt(test_case) == expected
