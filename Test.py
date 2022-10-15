import unittest

from HW4a import connect

class TesConnect(unittest.TestCase):
    def testConnect(self):
        self.assertEqual(connect('?'), False)

    def testConnect2(self):
        self.assertEqual(connect('ShivankSrivastava'), True)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
