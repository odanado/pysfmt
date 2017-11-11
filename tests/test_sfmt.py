import unittest
import functools

from pysfmt import SFMT


class TestSFMT(unittest.TestCase):

    def setUp(self):
        self.sfmt = SFMT(42)

    def _test(self, test_func, expected, assert_func):
        for i in range(10000):
            if i % 1000 == 0:
                assert_func(expected[i // 1000],
                            test_func())

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
        self._test(self.sfmt.genrand_uint64, expected, self.assertEqual)

    def test_genrand_real1(self):
        expected = [0.266695602859066683,
                    0.320678782956832720,
                    0.645215562462158387,
                    0.275649162772029888,
                    0.415310656050059623,
                    0.165955487910182109,
                    0.215059520959635153,
                    0.710036469323103381,
                    0.792613438747966081,
                    0.384331136100071302]

        assert_func = functools.partial(self.assertAlmostEquals, places=8)
        self._test(self.sfmt.genrand_real3, expected, assert_func)

    def test_genrand_real2(self):
        expected = [0.266695602796971798,
                    0.320678782882168889,
                    0.645215562311932445,
                    0.275649162707850337,
                    0.415310655953362584,
                    0.165955487871542573,
                    0.215059520909562707,
                    0.710036469157785177,
                    0.792613438563421369,
                    0.384331136010587215]

        assert_func = functools.partial(self.assertAlmostEquals, places=8)
        self._test(self.sfmt.genrand_real2, expected, assert_func)

    def test_genrand_real3(self):
        expected = [0.266695602859066683,
                    0.320678782956832720,
                    0.645215562462158387,
                    0.275649162772029888,
                    0.415310656050059623,
                    0.165955487910182109,
                    0.215059520959635153,
                    0.710036469323103381,
                    0.792613438747966081,
                    0.384331136100071302]

        assert_func = functools.partial(self.assertAlmostEquals, places=8)
        self._test(self.sfmt.genrand_real3, expected, assert_func)

    def test_genrand_res53(self):
        expected = [0.320678782944263774,
                    0.275649162858076280,
                    0.165955487968239612,
                    0.710036469207857679,
                    0.384331136195131928,
                    0.604880350541186385,
                    0.795576802462095944,
                    0.859982004649268661,
                    0.687164563521293736,
                    0.971225608339854496]
        assert_func = functools.partial(self.assertAlmostEquals, places=8)
        self._test(self.sfmt.genrand_res53, expected, assert_func)

    def test_genrand_res53_mix(self):
        expected = [0.320678782944263774,
                    0.275649162858076280,
                    0.165955487968239612,
                    0.710036469207857679,
                    0.384331136195131928,
                    0.604880350541186385,
                    0.795576802462095944,
                    0.859982004649268661,
                    0.687164563521293736,
                    0.971225608339854496]
        assert_func = functools.partial(self.assertAlmostEquals, places=8)
        self._test(self.sfmt.genrand_res53_mix, expected, assert_func)
