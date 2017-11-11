import unittest
from pysfmt import SFMT


class TestSFMT(unittest.TestCase):

    def setUp(self):
        self.sfmt = SFMT(42)

    def test_genrand_uint64(self):
        expected = [5915479438841489852,
                    5084829561375217883,
                    3061338414177701013,
                    13097861030477702153,
                    7089658108949608157,
                    11158073021648986217,
                    14675801665998462530,
                    15863867947760756011,
                    12675948839799635072,
                    17915950234878164470]
        for i in range(10000):
            if i % 1000 == 0:
                self.assertEqual(expected[i // 1000],
                                 self.sfmt.genrand_uint64())
