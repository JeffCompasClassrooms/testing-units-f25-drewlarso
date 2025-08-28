# Drew Larson
# August 2025

class StringReader:
    def __init__(self, string=""):
        self.string = string.strip()

    def get_string(self):
        return self.string

    def set_string(self, string):
        self.string = string.strip()

    def character_count(self, include_spaces=False):
        count = 0
        for c in self.string:
            if c == " " and not include_spaces:
                continue
            count += 1
        return count

    def word_count(self):
        words = self.string.strip().split(" ")
        return len(words)

    def sentence_count(self):
        sentences = self.string.strip().strip(".").split(".")
        return len(sentences)

    def consonant_count(self):
        consonants = "bcdfghjklmnpqrstvwxz"
        return self.specific_count(consonants)

    def vowel_count(self):
        vowels = "aeiouy"
        return self.specific_count(vowels)

    def specific_count(self, counted_characters):
        count = 0
        for c in self.string:
            if c in counted_characters:
                count += 1
        return count

    def is_palindrome(self):
        string_reversed = self.string[::-1]
        return string_reversed == self.string


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
