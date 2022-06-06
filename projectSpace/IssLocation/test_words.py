import unittest
from words import words


# the class is the "test suite"
class TestCalculatorMethods(unittest.TestCase):

    def setUp(self):
        self.wrd = words()

    def test_count_vowels_consonants(self):
        resp = self.wrd.count_vowels_consonants(['Algeria', 1894])
        alg_vowels = resp['Algeria']['vowels']
        alg_consonants = resp['Algeria']['consonants']
        self.assertEqual(alg_vowels, 4, "Algeria has 4 vowels")
        self.assertEqual(alg_consonants, 3, "Algeria has 3 consonants")


if __name__ == '__main__':
    unittest.main()
