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
