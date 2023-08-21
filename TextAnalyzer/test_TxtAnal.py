from TextAnalyzer.TxtAnal import TextAnalyzer


class TestTxtAnal:
    test_case = "This is a sample text. It has multiple sentences. This is just for testing."

    def test_word_count(self):
        text = TextAnalyzer(self.test_case)

        assert text.word_count() == 14

    def test_sentence_count(self):
        text = TextAnalyzer(self.test_case)

        assert text.sentence_count() == 3

    def test_unique_words_count(self):
        text = TextAnalyzer(self.test_case)

        assert text.unique_words_count() == 12
