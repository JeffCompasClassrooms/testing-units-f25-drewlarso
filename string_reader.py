# Drew Larson
# August 2025

import re


class StringReader:
    def __init__(self, string=""):
        self.string = string.strip()

    def get_string(self):
        return self.string

    def set_string(self, string):
        if type(string) == str:
            self.string = string.strip()
            return True
        return False

    def character_count(self, include_spaces=False):
        count = 0
        for c in self.string:
            if c == " " and not include_spaces:
                continue
            count += 1
        return count

    def word_count(self):
        words = self.string.strip().split()
        return len(words)

    def sentence_count(self):
        sentences = re.split(r'[.!?]+', self.string)
        sentences = [s for s in sentences if s]
        return len(sentences)

    def consonant_count(self):
        consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
        return self.specific_count(consonants)

    def vowel_count(self):
        vowels = "aeiouyAEIOUY"
        return self.specific_count(vowels)

    def specific_count(self, counted_characters):
        count = 0
        for c in self.string:
            if c in counted_characters:
                count += 1
        return count


if __name__ == "__main__":
    s = """
    C++ is a compiled language meaning your program's source code must be translated (compiled) before it can be run on your computer. VS Code is first and foremost an editor, and relies on command-line tools to do much of the development workflow. The C/C++ extension does not include a C++ compiler or debugger. You will need to install these tools or use those already installed on your computer.
    """
    sr = StringReader(s)
    print(sr.character_count())
    print(sr.character_count(True))
    print(sr.word_count())
    print(sr.sentence_count())
    print(sr.consonant_count())
    print(sr.vowel_count())

    sr.set_string("tacocat")
    print(sr.is_palindrome())
