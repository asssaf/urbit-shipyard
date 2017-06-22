import unittest

from .context import ob_util

class ObUtilTest(unittest.TestCase):
    def test_generate_planets(self):
        planets = ob_util.generate_planets(0x100)
        self.assertEquals(planets.next(), 0x10100)
        self.assertEquals(planets.next(), 0x20100)

        planets = ob_util.generate_planets(0x4141)
        self.assertEquals(planets.next(), 0x14141)
        self.assertEquals(planets.next(), 0x24141)

    def test_find_prefix_syllable(self):
        results = ob_util.find_prefix_syllable('*')
        self.assertEquals(results.next(), 'doz')
        self.assertEquals(results.next(), 'mar')

        results = ob_util.find_prefix_syllable('n*')
        self.assertEquals(results.next(), 'nar')
        self.assertEquals(results.next(), 'nov')

        results = ob_util.find_prefix_syllable('*n')
        self.assertEquals(results.next(), 'bin')
        self.assertEquals(results.next(), 'wan')

        results = ob_util.find_prefix_syllable('*in')
        self.assertEquals(results.next(), 'bin')
        self.assertEquals(results.next(), 'rin')

    def test_find_suffix_syllable(self):
        results = ob_util.find_suffix_syllable('*')
        self.assertEquals(results.next(), 'zod')
        self.assertEquals(results.next(), 'nec')

        results = ob_util.find_suffix_syllable('n*')
        self.assertEquals(results.next(), 'nec')
        self.assertEquals(results.next(), 'nup')

        results = ob_util.find_suffix_syllable('*n')
        self.assertEquals(results.next(), 'pen')
        self.assertEquals(results.next(), 'sun')

        results = ob_util.find_suffix_syllable('*yn')
        self.assertEquals(results.next(), 'byn')
        self.assertEquals(results.next(), 'syn')

    def test_find_words_by_prefix(self):
        results = list(ob_util.find_words('doz', '*'))
        self.assertEquals(len(results), 256)
        self.assertEquals(results[0], 'dozzod')

        results = list(ob_util.find_words('do*', '*'))
        self.assertEquals(len(results), 9*256)

        results = list(ob_util.find_words('d*', '*'))
        self.assertEquals(len(results), 26*256)

        results = list(ob_util.find_words('doz', 'n*'))
        self.assertEquals(len(results), 25)

        results = list(ob_util.find_words('doz', 'ne*'))
        self.assertEquals(len(results), 11)

    def test_find_words_by_suffix(self):
        results = list(ob_util.find_words('*', 'zod'))
        self.assertEquals(len(results), 256)
        self.assertEquals(results[0], 'dozzod')

        results = list(ob_util.find_words('*', 'fy*'))
        self.assertEquals(len(results), 3*256)

        results = list(ob_util.find_words('*', 'f*'))
        self.assertEquals(len(results), 16*256)

        results = list(ob_util.find_words('*', '*'))
        self.assertEquals(len(results), 256*256)
