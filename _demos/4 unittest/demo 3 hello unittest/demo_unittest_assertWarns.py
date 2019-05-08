import unittest
import warnings

warnings.simplefilter('ignore')

class TestSum(unittest.TestCase):
    def testIsZero(self):
        with self.assertWarns(UserWarning):
            self.isZero(0)

    def isZero(self,i):
        if i == 0:
            print("OK")
        else:
            warnings.warn("bad", UserWarning)
        return i

if __name__ == "__main__":
    unittest.main()

