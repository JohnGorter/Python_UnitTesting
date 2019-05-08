import unittest   
import sys

class ConfigTestCase(unittest.TestCase):
    def setUp(self):
        print('setUp')
    def testrunTest(self):
        """Test routine RunTest"""
        print('run test')
    def testRun(self):
        """Test routine TestRun"""
        print('run test 2')    
      #  self.fail("TESTRUN: Fail")    

def suite():
    """
        Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(ConfigTestCase))
    return test_suite


testresults = unittest.TextTestRunner(stream=sys.stderr, descriptions=True, verbosity=2).run(suite())
print(testresults.wasSuccessful())
print(testresults.testsRun)

#if __name__ == "__main__":
#    unittest.main()