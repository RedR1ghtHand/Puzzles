from LeetCodeProblemList.LengthofLastWord.LoLW import LoLW


class TestLengthOfLastWordMethod:
    case_1 = "Hello World!"
    case_2 = "   fly me   to   the moon?  "
    case_3 = "luffy is still joyboy!!?"

    def test_case_1(self):
        sol = LoLW()
        assert sol.length_of_last_word(self.case_1) == 5

    def test_case_2(self):
        sol = LoLW()
        assert sol.length_of_last_word(self.case_2) == 4

    def test_case_3(self):
        sol = LoLW()
        assert sol.length_of_last_word(self.case_3) == 6


class TestLengthOfLastWordAltMethod:
    case_1 = "Hello World"
    case_2 = "   fly me   to   the moon  "
    case_3 = "luffy is still joyboy"

    def test_case_1(self):
        sol = LoLW()
        assert sol.length_of_last_word_alt(self.case_1) == 5

    def test_case_2(self):
        sol = LoLW()
        assert sol.length_of_last_word_alt(self.case_2) == 4

    def test_case_3(self):
        sol = LoLW()
        assert sol.length_of_last_word_alt(self.case_3) == 6
