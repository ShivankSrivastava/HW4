import unittest
from unittest import mock

from HW4a import connect


class TesConnect(unittest.TestCase):

    @mock.patch('HW4a.connect')
    def testConnect(self):
        self.assertEqual(connect('?'), False)

    @mock.patch('HW4a.connect')
    def testConnect2(self):
        self.assertEqual(connect('ShivankSrivastava'), True)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
