""" Some unittests """

from triplet import CharacteristicZero, Lesson
from quentin import Quentin
import unittest

class TestZero(unittest.TestCase):

    def setUp(self):
        self.zero = CharacteristicZero(
            Lesson("a", {1:2, 2:2}), 
            Lesson("b", {1:1, 2:2}), 
            Lesson("c", {1:2, 2:2}), 
            True)
        
        self.zero_true = CharacteristicZero(
            Lesson("a", {1:0, 2:2}), 
            Lesson("b", {1:1, 2:2}), 
            Lesson("c", {1:2, 2:2}), 
            False)
    
    def test_check_false(self):
        self.assertFalse(self.zero.check())
    
    def test_check_true(self):
        self.assertTrue(self.zero_true.check())

class TestQuentin(unittest.TestCase):
    def setUp(self):
        self.q = Quentin("qent.xlsx", True)

    def test_zeros(self):
        self.assertEqual(len(self.q.get_ch_zeros()), 4)
   
if __name__ == "__main__":
   unittest.main()
