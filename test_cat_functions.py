import unittest

from cat_functions import *

# Unit tests

class TestCatFunctions(unittest.TestCase):

    def test_meow(self):
        self.assertEqual(meow(1),"Persian","Meow # 1 should come from a Persian")


    def test_answers(self):
        c = Cat()
        self.assertIn(c.ask(question="Why?"),["The cat doesn't care.","The cat purrs.","The cat walks away.","The cat sleeps."], "Answer should be one of four choices")

    def test_truth(self):
        self.assertTrue(cat_logic(True,True), "Both true should lead to true")
        self.assertTrue(cat_logic(False,False), "Both false should lead to true")



if __name__ == "__main__":
    unittest.main()


