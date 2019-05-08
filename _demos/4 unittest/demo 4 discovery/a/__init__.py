import unittest 

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([1,2,2]),6, "should be equal to 6")