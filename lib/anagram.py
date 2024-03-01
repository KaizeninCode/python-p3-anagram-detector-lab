class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = ''.join(sorted(word))
    def match(self, possible_anagrams):
        return [anagram for anagram in possible_anagrams if self.sorted_word == ''.join(sorted(anagram))]    