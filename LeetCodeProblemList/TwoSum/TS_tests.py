from LeetCodeProblemList.TwoSum.TS import TS


class TestTwoSum:
    case_1 = [[2,7,11,15], 9]
    case_2 = [[3,2,4], 6]
    case_3 = [[3,3], 6]

    def test_case_1(self):
        sol = TS()
        assert sol.twoSum(*self.case_1) == [0, 1]

    def test_case_2(self):
        sol = TS()
        assert sol.twoSum(*self.case_2) == [1, 2]

    def test_case_3(self):
        sol = TS()
        assert sol.twoSum(*self.case_3) == [0, 1]


