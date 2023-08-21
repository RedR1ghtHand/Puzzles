import re
from collections import Counter


class TextAnalyzer:
    def __init__(self, text):
        self.text = text

    def word_count(self):
        words = re.findall(r'\w+', self.text)
        return len(words)

    def sentence_count(self):
        sentences = re.split(r'[.!?]', self.text)
        return len([sentence for sentence in sentences if sentence.strip()])

    def unique_words_count(self):
        words = re.findall(r'\w+', self.text.lower())
        word_counts = Counter(words)
        return len(word_counts)
