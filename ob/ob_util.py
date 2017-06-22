import ob

from itertools import ifilter


def nth_planet_of_star(star, n):
	return n * 65536 + star


def generate_planets(star):
	planet_index = 1
	while planet_index < 65536:
		yield nth_planet_of_star(star, planet_index)
		planet_index += 1

def find_syllable(set, pattern):
	if pattern.startswith('*'):
		pattern = pattern[1:]
		syllables = (ob.get_syllable(set, i) for i in xrange(0, 0x100))
		syllables = ifilter(lambda x: x.endswith(pattern), syllables)
		return syllables

	elif pattern.endswith('*'):
		pattern = pattern[:-1]
		syllables = (ob.get_syllable(set, i) for i in xrange(0, 0x100))
		syllables = ifilter(lambda x: x.startswith(pattern), syllables)
		return syllables


def find_prefix_syllable(pattern):
    return find_syllable(ob.prefix, pattern)


def find_suffix_syllable(pattern):
    return find_syllable(ob.suffix, pattern)
