import unittest

from .context import ob

class MyTest(unittest.TestCase):
    def test_feen(self):
        self.assertEqual(ob.feen(0x10100), 0x63b30e1c)

    """
    > `@ux`(muk 0x0 32 0x1)
    0x734e.58c3
    > `@ux`(muk 0x0 31 0x1)
    0x2cd0.3592
    > `@ux`(muk 0x0 1 0x1)
    0xe45a.d1ab

    > `@ux`(muk 0 2 0x101)
    0x4208.1a9b
    > `@ux`(muk 0 2 0x201)
    0x64c7.667e

    """
    def test_muk(self):
        self.assertEqual(ob.muk(0, 2, 0x101), 0x42081a9b)
        self.assertEqual(ob.muk(0, 2, 0x201), 0x64c7667e)

    def test_syllable(self):
        self.assertEquals(ob.get_prefix(1), "mar")
        self.assertEquals(ob.get_suffix(1), "nec")

    def test_to_planet_name(self):
        self.assertEquals(ob.to_planet_name(0x10100), "doznec-marzod")
