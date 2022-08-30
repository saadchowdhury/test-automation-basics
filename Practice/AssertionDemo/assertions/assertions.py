import unittest

class LoginTest(unittest.TestCase):
    def test_001(self):
        self.assertEqual(10, 10, '10 is not equal to 1')
        # self.assertTrue('hello', 'hello2')

    def test_002(self):
        self.assertEqual(10, 1, '10 is not equal to 1')


if __name__ == '__main__':
    unittest.main()