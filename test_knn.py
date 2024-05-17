import unittest
from KNN import classify

class TestClassifier(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(classify(150, 60), 'A')

    def test_case_2(self):
        self.assertEqual(classify(20, 7), 'B')

    def test_case_3(self):
        self.assertEqual(classify(30, 10), 'B')

    def test_case_4(self):
        self.assertEqual(classify(170, 80), 'A')

    def test_case_5(self):
        self.assertEqual(classify(50, 3), 'B')

    def test_case_6(self):
        self.assertEqual(classify(150, 70), 'A')

if __name__ == '__main__':
    unittest.main()
