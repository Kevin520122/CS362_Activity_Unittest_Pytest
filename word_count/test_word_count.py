from word_count import count_word
import unittest

class Word_Count_Test(unittest.TestCase):
    def test1(self):
        res = count_word("")
        self.assertEqual(res, 0)

    def test2(self):
        res = count_word("Kevin")
        self.assertEqual(res, 1)

    def test3(self):
        res = count_word("How are you?")
        self.assertEqual(res, 3)

if __name__ == "__main__":
    #0: nothing
    #1: default setting, shows .F
    #2: Shows details - which cases are okay and which cases are failed
    unittest.main(verbosity=2)

    
