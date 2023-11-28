import unittest

import utils


class TestUtils(unittest.TestCase):

    # TODO test Coord

    def test_md5(self):
        self.assertEqual("098f6bcd4621d373cade4e832627b4f6", utils.md5("test"))

    def test_bit_not(self):
        self.assertEqual(65412, utils.bit_not(123, numbits=16))
        self.assertEqual(65079, utils.bit_not(456, numbits=16))
        self.assertEqual(65534, utils.bit_not(1, numbits=16))
        self.assertEqual(65535, utils.bit_not(0, numbits=16))


if __name__ == '__main__':
    unittest.main()
