import unittest

from .context import ob

class ObTest(unittest.TestCase):
    def test_feen(self):
        self.assertEqual(ob.feen(0x10100), 0x63b30e1c)

    def test_fend(self):
        self.assertEquals(ob.fend(0x63b30e1c), 0x10100)

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

    def test_is_prefix_syllable(self):
        self.assertTrue(ob.is_prefix_syllable("mar"))
        self.assertFalse(ob.is_prefix_syllable(""))
        self.assertFalse(ob.is_prefix_syllable("mra"))
        self.assertFalse(ob.is_prefix_syllable("zod"))

    def test_is_suffix_syllable(self):
        self.assertFalse(ob.is_suffix_syllable("mar"))
        self.assertFalse(ob.is_suffix_syllable(""))
        self.assertFalse(ob.is_suffix_syllable("mra"))
        self.assertTrue(ob.is_suffix_syllable("zod"))

    def test_to_galaxy_name(self):
        self.assertEquals(ob.to_galaxy_name(0), "zod")
        self.assertEquals(ob.to_ship_name(0), "zod")

    def test_to_star_name(self):
        self.assertEquals(ob.to_star_name(0x100), "marzod")
        self.assertEquals(ob.to_ship_name(0x100), "marzod")

    def test_to_planet_name(self):
        self.assertEquals(ob.to_planet_name(0x10100), "wicdev-wisryt")
        self.assertEquals(ob.to_ship_name(0x10100, scramble=False), "doznec-marzod")

    def test_from_ship_name(self):
        self.assertEquals(ob.from_ship_name('mar'), 1)
        self.assertEquals(ob.from_ship_name('marzod'), 0x100)
        self.assertEquals(ob.from_ship_name('doznec-marzod', unscramble=False), 0x10100)
        self.assertEquals(ob.from_ship_name('wicdev-wisryt'), 0x10100)

    def test_from_ship_name_invalid_syllable(self):
        with self.assertRaises(Exception) as context:
            ob.from_ship_name('maz')

        self.assertIn('Invalid syllable: maz', context.exception.message)

    def test_from_ship_name_invalid_prefix_syllable(self):
        with self.assertRaises(Exception) as context:
            ob.from_ship_name('mazzod')

        self.assertIn('Invalid syllable: maz', context.exception.message)

    def test_from_ship_name_invalid_suffix_syllable(self):
        with self.assertRaises(Exception) as context:
            ob.from_ship_name('marrod')

        self.assertIn('Invalid syllable: rod', context.exception.message)
