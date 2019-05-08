import unittest
import sys

class MyTestCase(unittest.TestCase):
    def test_me(self):
        self.skipTest("not doing anything anymore")

    def test_onMac(self):
        if sys.platform.startswith("win"):
            self.skipTest("requires Non Windows OS")
        raise Exception("")
        # print("testing")


@unittest.expectedFailure
class TestA(unittest.TestCase):
    def test_me(self):
        raise Exception('no')


if __name__ == "__main__":
    unittest.main()
