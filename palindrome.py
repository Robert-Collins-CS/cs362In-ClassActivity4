import unittest
import pytest


def boolPalindrome():
    palin = getUserInput()
    isPalindrome = (palin == palin[::-1])
    return isPalindrome


def getUserInput():
    userInp = input("Please enter a string: \n")
    return userInp


class TestStringMethods(unittest.TestCase):

    def test_boolPalin(self):
        isDrome = boolPalindrome()
        self.assertTrue(isDrome)  # Pass


def pytest_palin():
    isDrome = boolPalindrome()
    assert isDrome is True


if __name__ == '__main__':
    unittest.main()
