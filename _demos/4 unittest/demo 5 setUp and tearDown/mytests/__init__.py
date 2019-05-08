import unittest 

def setUpModule():
    print("setting up module stuff")

def tearDownModule():
    print("cleaning module stuff")



class TestSum(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setting up class stuff")

    @classmethod
    def tearDownClass(cls):
        print("cleaning up class stuff")

    def setUp(self):
        print("setting up stuff")
    def tearDown(self):
        print("cleaning up stuff")

    def test_sum(self):
        self.assertEqual(sum([1,2,2]),5, "should be equal to 5")

    def test_sumtwo(self):
        self.assertEqual(sum([1,2,1]),4, "should be equal to 4")



class TestSubtract(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setting up class stuff")
        
    @classmethod
    def tearDownClass(cls):
        print("cleaning up class stuff")

    def setUp(self):
        print("setting up stuff")
    def tearDown(self):
        print("cleaning up stuff")

    def test_subtract(self):
        self.assertEqual(10-5,5, "should be equal to 5")

    def test_subtracttwo(self):
        self.assertEqual(1-2-1,-2, "should be equal to -2")