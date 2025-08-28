import unittest
from string_reader import StringReader


class TestStringReader(unittest.TestCase):
    def test_get_string(self):
        sr = StringReader("tacocat")
        self.assertEqual(sr.get_string(), "tacocat")

    def test_set_string(self):
        sr = StringReader("tacocat")
        self.assertEqual(sr.set_string("foobar"), True)
        self.assertEqual(sr.get_string(), "foobar")

    def test_set_string_whitespace(self):
        sr = StringReader("tacocat")
        self.assertEqual(sr.set_string("foobar\n\n\n\n"), True)
        self.assertEqual(sr.get_string(), "foobar")

    def test_set_string_invalid(self):
        sr = StringReader("tacocat")
        self.assertEqual(sr.set_string(1234151), False)
        self.assertEqual(sr.get_string(), "tacocat")

    def test_set_string_empty(self):
        sr = StringReader("tacocat")
        self.assertEqual(sr.set_string(""), True)
        self.assertEqual(sr.get_string(), "")

    def test_character_count_no_spaces(self):
        sr = StringReader("123456789")
        self.assertEqual(sr.character_count(), 9)

    def test_character_count_spaces(self):
        sr = StringReader("1 2 3 4 5 6 7 8 9")
        self.assertEqual(sr.character_count(True), 17)

    def test_character_count_spaces_whitespace(self):
        sr = StringReader("      1 2 3 4 5 6 7 8 9      ")
        self.assertEqual(sr.character_count(True), 17)

    def test_character_count_empty(self):
        sr = StringReader("")
        self.assertEqual(sr.character_count(), 0)

    def test_character_count_long(self):
        sr = StringReader("TypeScript is an open-source programming language developed and maintained by Microsoft. It is a superset of JavaScript, meaning it includes all of JavaScript's features and adds optional static typing. This static typing allows developers to define types for variables, functions, and objects, enabling early error detection during development rather than at runtime. TypeScript is an open-source programming language developed and maintained by Microsoft. It is a superset of JavaScript, meaning it includes all of JavaScript's features and adds optional static typing. This static typing allows developers to define types for variables, functions, and objects, enabling early error detection during development rather than at runtime. TypeScript is an open-source programming language developed and maintained by Microsoft. It is a superset of JavaScript, meaning it includes all of JavaScript's features and adds optional static typing. This static typing allows developers to define types for variables, functions, and objects, enabling early error detection during development rather than at runtime.")
        self.assertEqual(sr.character_count(), 951)

    def test_word_count(self):
        sr = StringReader("hello, world. python c++ rust")
        self.assertEqual(sr.word_count(), 5)

    def test_word_count_spaces(self):
        sr = StringReader(
            "python    rust     c++      typescript     ruby       java    swift   c#    lua")
        self.assertEqual(sr.word_count(), 9)

    def test_word_count_empty(self):
        sr = StringReader("")
        self.assertEqual(sr.word_count(), 0)

    def test_word_count_long(self):
        sr = StringReader("TypeScript is an open-source programming language developed and maintained by Microsoft. It is a superset of JavaScript, meaning it includes all of JavaScript's features and adds optional static typing. This static typing allows developers to define types for variables, functions, and objects, enabling early error detection during development rather than at runtime. TypeScript is an open-source programming language developed and maintained by Microsoft. It is a superset of JavaScript, meaning it includes all of JavaScript's features and adds optional static typing. This static typing allows developers to define types for variables, functions, and objects, enabling early error detection during development rather than at runtime. TypeScript is an open-source programming language developed and maintained by Microsoft. It is a superset of JavaScript, meaning it includes all of JavaScript's features and adds optional static typing. This static typing allows developers to define types for variables, functions, and objects, enabling early error detection during development rather than at runtime.")
        self.assertEqual(sr.word_count(), 156)

    def test_sentence_count(self):
        sr = StringReader(
            "Hello World.  This is a sentence.  This is a sentence too.")
        self.assertEqual(sr.sentence_count(), 3)

    def test_sentence_count_empty(self):
        sr = StringReader("")
        self.assertEqual(sr.sentence_count(), 0)

    def test_sentence_count_question(self):
        sr = StringReader("what is python?  what is c++?  what is rust?")
        self.assertEqual(sr.sentence_count(), 3)

    def test_sentence_count_exclamation(self):
        sr = StringReader("i love python!  i love c++!  i love rust!")
        self.assertEqual(sr.sentence_count(), 3)

    def test_sentence_count_mix(self):
        sr = StringReader("python exists.  what is c++?  i love rust!")
        self.assertEqual(sr.sentence_count(), 3)

    def test_sentence_count_long(self):
        sr = StringReader("TypeScript is an open-source programming language developed and maintained by Microsoft. It is a superset of JavaScript, meaning it includes all of JavaScript's features and adds optional static typing. This static typing allows developers to define types for variables, functions, and objects, enabling early error detection during development rather than at runtime. TypeScript is an open-source programming language developed and maintained by Microsoft. It is a superset of JavaScript, meaning it includes all of JavaScript's features and adds optional static typing. This static typing allows developers to define types for variables, functions, and objects, enabling early error detection during development rather than at runtime. TypeScript is an open-source programming language developed and maintained by Microsoft. It is a superset of JavaScript, meaning it includes all of JavaScript's features and adds optional static typing. This static typing allows developers to define types for variables, functions, and objects, enabling early error detection during development rather than at runtime.")
        self.assertEqual(sr.sentence_count(), 9)

    def test_consonant_count(self):
        sr = StringReader("rectangle")
        self.assertEqual(sr.consonant_count(), 6)

    def test_consonant_count_capital(self):
        sr = StringReader("RECTANGLE")
        self.assertEqual(sr.consonant_count(), 6)

    def test_consonant_count_mix(self):
        sr = StringReader("rEctANGle")
        self.assertEqual(sr.consonant_count(), 6)

    def test_consonant_count_empty(self):
        sr = StringReader("")
        self.assertEqual(sr.consonant_count(), 0)

    def test_vowel_count(self):
        sr = StringReader("vegetable soup")
        self.assertEqual(sr.vowel_count(), 6)

    def test_vowel_count_capital(self):
        sr = StringReader("VEGETABLE SOUP")
        self.assertEqual(sr.vowel_count(), 6)

    def test_vowel_count_mix(self):
        sr = StringReader("vegetable SOUP")
        self.assertEqual(sr.vowel_count(), 6)

    def test_vowel_count_empty(self):
        sr = StringReader("")
        self.assertEqual(sr.vowel_count(), 0)

    def test_specific_count(self):
        sr = StringReader("basketball")
        self.assertEqual(sr.specific_count("abcdefg"), 5)

    def test_specific_count_capital(self):
        sr = StringReader("BASKETBALL")
        self.assertEqual(sr.specific_count("ABC"), 4)

    def test_specific_count_mix(self):
        sr = StringReader("basKeTBAlL")
        self.assertEqual(sr.specific_count("abcDEFG"), 2)

    def test_specific_count_empty(self):
        sr = StringReader("")
        self.assertEqual(sr.specific_count("abcdefg"), 0)


if __name__ == "__main__":
    unittest.main()
