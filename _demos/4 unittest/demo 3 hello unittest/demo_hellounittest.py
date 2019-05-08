import unittest

class TestMe(unittest.TestCase):
    def setUp(self):
        print("setup")
    
    def tearDown(self):
        # raise Exception("John")
        pass

    def runTest(self):
        print("a")
       

    def testJohn(self):
        print('bla')
        self.assertEqual(1,3)

    def testJohnB(self):
        print('bla')

        


#results = unittest.TextTestRunner().run(TestMe())
#print(results)
if __name__ == "__main__":
    unittest.main()