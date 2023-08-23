from LeetCodeProblemList.ReverseInteger.RI import reverse_integer


class TestReverseInteger:
    case_1 = 123
    case_2 = -123
    case_3 = 120
    case_4 = 1534236469

    def test_case_1(self):
        assert reverse_integer(self.case_1) == 321

    def test_case_2(self):
        assert reverse_integer(self.case_2) == -321

    def test_case_3(self):
        assert reverse_integer(self.case_3) == 21

    def test_case_4(self):
        assert reverse_integer(self.case_4) == 0




