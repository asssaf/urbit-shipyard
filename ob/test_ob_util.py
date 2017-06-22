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
