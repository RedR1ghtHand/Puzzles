class LoLW:
    def length_of_last_word(self, s: str) -> int:
        counter = 0
        for i in s[::-1]:
            if i in [' ', '.', '!', '?']:
                if counter == 0:
                    continue
                else:
                    break
            else:
                counter += 1
        return counter

    def length_of_last_word_alt(self, s: str) -> int:
        result = s.split()
        return len(result[-1])
