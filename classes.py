class BasicWord:
    def __repr__(self):
        return f"self.word: {self.word}\n" \
               f"self.subwords: {self.subwords}"

    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def check_word(self, word):
        return word in self.subwords

    def subwords_count(self):
        return len(self.subwords)


class Player:
    def __repr__(self):
        return f"Имя игрока: {self.name}\n" \
               f"Использованные слова: {self.used_words}"

    def __init__(self, name):
        self.name = name
        self.used_words = []

    def used_words_count(self):
        return len(self.used_words)

    def append_word(self, word):
        self.used_words.append(word)

    def is_word_used(self, word):
        return word in self.used_words
