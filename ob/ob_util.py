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
	all = (ob.get_syllable(set, i) for i in xrange(0, 0x100))
	if pattern == '*':
		return all

	if pattern.startswith('*'):
		pattern = pattern[1:]
		syllables = ifilter(lambda x: x.endswith(pattern), all)
		return syllables

	elif pattern.endswith('*'):
		pattern = pattern[:-1]
		syllables = ifilter(lambda x: x.startswith(pattern), all)
		return syllables

	elif ob.is_syllable(set, pattern):
		return [pattern]

	else:
		raise Exception("Invalid argument: '%s'" % pattern)


def find_prefix_syllable(pattern):
	return find_syllable(ob.prefix, pattern)


def find_suffix_syllable(pattern):
	return find_syllable(ob.suffix, pattern)


def find_words(prefix_pattern, suffix_pattern):
	prefix = list(find_prefix_syllable(prefix_pattern))
	suffix = list(find_suffix_syllable(suffix_pattern))
	return ((p + s) for p in prefix for s in suffix)
