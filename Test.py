import unittest

from HW4a import connect

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TesConnect(unittest.TestCase):
    def testConnect(self):
        self.assertEqual(connect('?'), False)

    def testConnect2(self):
        self.assertEqual(connect('ShivankSrivastava'), True)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
