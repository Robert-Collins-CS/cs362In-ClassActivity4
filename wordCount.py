import unittest
import pytest


def wordCount():
    sentence = getUserInput()
    count = len(sentence.split())
    return count


def getUserInput():
    userInp = input("Please enter a string: \n")
    return userInp


class TestStringMethods(unittest.TestCase):

    def test_wordCount(self):
        wordSentence = wordCount()
        self.assertTrue(type(wordSentence), int)
        self.assertEqual(wordSentence, 2)


def pytest_count():
    sentence = wordCount()
    assert type(sentence) is int
    assert sentence == 2


if __name__ == '__main__':
    unittest.main()
