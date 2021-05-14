import palindrome
import unittest

class isPalindromeTest(unittest.TestCase):
    def test1(self):
        res = palindrome.isPalindrome(" ")
        self.assertEqual(res, True)

    def test2(self):
        res = palindrome.isPalindrome("aaaaaaaa")
        self.assertEqual(res, True)

    def test3(self):
        res = palindrome.isPalindrome("abcddcba")
        self.assertEqual(res, True)

    def test4(self):
        res = palindrome.isPalindrome("ab ba")
        self.assertEqual(res, True)

    def test5(self):
        res = palindrome.isPalindrome("12!abccba!21")
        self.assertEqual(res, True)

if __name__ == "__main__":
    #0: nothing
    #1: default setting, shows .F
    #2: Shows details - which cases are okay and which cases are failed
    unittest.main(verbosity=2)

    