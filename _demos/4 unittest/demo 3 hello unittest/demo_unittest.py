import unittest
import sys

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([1,2,3]),6, "should be equal to 6")
    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


singletest = TestSum("test_sum")
singleclass = unittest.defaultTestLoader.loadTestsFromTestCase(TestSum)

testresults = unittest.TextTestRunner(stream=sys.stderr, descriptions=True, verbosity=2).run(singleclass)
print(testresults.wasSuccessful())
print(testresults.testsRun)


#if __name__ == "__main__":
#    unittest.main()

