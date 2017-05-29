#!/usr/bin/env python2

import argparse
import logging
import sys

raku = [0xb76d5eedL, 0xee281300L, 0x85bcae01L, 0x4b387af7L]

prefix = """dozmarbinwansamlitsighidfidlissogdirwacsabwissib\
rigsoldopmodfoglidhopdardorlorhodfolrintogsilmir\
holpaslacrovlivdalsatlibtabhanticpidtorbolfosdot\
losdilforpilramtirwintadbicdifrocwidbisdasmidlop\
rilnardapmolsanlocnovsitnidtipsicropwitnatpanmin\
ritpodmottamtolsavposnapnopsomfinfonbanmorworsip\
ronnorbotwicsocwatdolmagpicdavbidbaltimtasmallig\
sivtagpadsaldivdactansidfabtarmonranniswolmispal\
lasdismaprabtobrollatlonnodnavfignomnibpagsopral\
bilhaddocridmocpacravripfaltodtiltinhapmicfanpat\
taclabmogsimsonpinlomrictapfirhasbosbatpochactid\
havsaplindibhosdabbitbarracparloddosbortochilmac\
tomdigfilfasmithobharmighinradmashalraglagfadtop\
mophabnilnosmilfopfamdatnoldinhatnacrisfotribhoc\
nimlarfitwalrapsarnalmoslandondanladdovrivbacpol\
laptalpitnambonrostonfodponsovnocsorlavmatmipfip"""

suffix = """zodnecbudwessevpersutletfulpensytdurwepserwylsun\
rypsyxdyrnuphebpeglupdepdysputlughecryttyvsydnex\
lunmeplutseppesdelsulpedtemledtulmetwenbynhexfeb\
pyldulhetmevruttylwydtepbesdexsefwycburderneppur\
rysrebdennutsubpetrulsynregtydsupsemwynrecmegnet\
secmulnymtevwebsummutnyxrextebfushepbenmuswyxsym\
selrucdecwexsyrwetdylmynmesdetbetbeltuxtugmyrpel\
syptermebsetdutdegtexsurfeltudnuxruxrenwytnubmed\
lytdusnebrumtynseglyxpunresredfunrevrefmectedrus\
bexlebduxrynnumpyxrygryxfeptyrtustyclegnemfermer\
tenlusnussyltecmexpubrymtucfyllepdebbermughuttun\
bylsudpemdevlurdefbusbeprunmelpexdytbyttyplevmyl\
wedducfurfexnulluclennerlexrupnedlecrydlydfenwel\
nydhusrelrudneshesfetdesretdunlernyrsebhulryllud\
remlysfynwerrycsugnysnyllyndyndemluxfedsedbecmun\
lyrtesmudnytbyrsenwegfyrmurtelreptegpecnelnevfes"""

def get_syllable(s, i):
	return s[i*3:(i+1)*3]

def get_prefix(i):
	return get_syllable(prefix, i)

def get_suffix(i):
	return get_syllable(suffix, i)


def feen(pyn):
	if pyn >= 0x10000 and pyn <= 0xffffffff:
		return 0x10000 + fice(pyn - 0x10000)

	if pyn >= 0x100000000 and pyn <= 0xffffffffffffffff:
		lo = pyn & 0xffffffff
		hi = pyn & 0xffffffff00000000
		return (hi | feen(lo))

	return pyn


def fend(cry):
	if cry >= 0x10000 and cry < 0xffffffff:
		return 0x10000 + teil(cry - 0x10000)

	if cry >= 0x100000000 and cry <= 0xffffffffffffffff:
		lo = cry & 0xffffffff
		hi = cry & 0xffffffff00000000
		return (hi | fend(lo))

	return cry


def fice(nor):
	sel = [ nor % 65535, nor / 65535 ]
	for i in xrange(0, 4):
		sel = rynd(i, sel[0], sel[1])

	res = 65535*sel[0] + sel[1]

	logging.debug("fice(%x)=%x" % (nor, res))
	return res


def teil(vip):
	sel = [ vip % 65535, vip / 65535 ]
	for i in xrange(3, -1, -1):
		sel = rund(i, sel[0], sel[1])

	res = 65535*sel[0] + sel[1]

	logging.debug("teil(%x)=%x" % (vip, res))
	return res


def rynd(n, l, r):
	res = [0, 0]
	res[0] = r

	if (n % 2) == 0:
		m = 65535
	else:
		m = 65536

	res[1] = (l + muk(raku[n], 2, r)) % m

	logging.debug("rynd(%d, %x, %x)=[%x, %x]" % (n, l, r, res[0], res[1]))
	return res


def rund(n, l, r):
	res = [0, 0]
	res[0] = r

	if (n % 2) == 0:
		m = 65535
	else:
		m = 65536

	h = muk(raku[n], 2, r)
	res[1] = (m + l - (h%m)) % m

	logging.debug("rund(%d, %x, %x)=[%x, %x]" % (n, l, r, res[0], res[1]))
	return res


def muk(syd, len, key):
	lo = key & 0xff
	hi = (key & 0xff00) / 256
	res = murmur3_x86_32(chr(lo) + chr(hi), seed=syd)
	logging.debug("muk(%x, %s, %x)=%x" % (syd, len, key, res))

	return res


def murmur3_x86_32(data, seed = 0):
    c1 = 0xcc9e2d51
    c2 = 0x1b873593

    length = len(data)
    h1 = seed
    roundedEnd = (length & 0xfffffffc)  # round down to 4 byte block
    for i in range(0, roundedEnd, 4):
      # little endian load order
      k1 = (ord(data[i]) & 0xff) | ((ord(data[i + 1]) & 0xff) << 8) | \
           ((ord(data[i + 2]) & 0xff) << 16) | (ord(data[i + 3]) << 24)
      k1 *= c1
      k1 = (k1 << 15) | ((k1 & 0xffffffff) >> 17) # ROTL32(k1,15)
      k1 *= c2

      h1 ^= k1
      h1 = (h1 << 13) | ((h1 & 0xffffffff) >> 19)  # ROTL32(h1,13)
      h1 = h1 * 5 + 0xe6546b64

    # tail
    k1 = 0

    val = length & 0x03
    if val == 3:
        k1 = (ord(data[roundedEnd + 2]) & 0xff) << 16
    # fallthrough
    if val in [2, 3]:
        k1 |= (ord(data[roundedEnd + 1]) & 0xff) << 8
    # fallthrough
    if val in [1, 2, 3]:
        k1 |= ord(data[roundedEnd]) & 0xff
        k1 *= c1
        k1 = (k1 << 15) | ((k1 & 0xffffffff) >> 17)  # ROTL32(k1,15)
        k1 *= c2
        h1 ^= k1

    # finalization
    h1 ^= length

    # fmix(h1)
    h1 ^= ((h1 & 0xffffffff) >> 16)
    h1 *= 0x85ebca6b
    h1 ^= ((h1 & 0xffffffff) >> 13)
    h1 *= 0xc2b2ae35
    h1 ^= ((h1 & 0xffffffff) >> 16)

    return h1 & 0xffffffff


def to_galaxy_name(galaxy):
	return to_ship_name(galaxy, 1)


def to_star_name(star):
	return to_ship_name(star, 2)


def to_planet_name(scrambled, scramble=True):
	name = ""
	s = scrambled
	return to_ship_name(s, 4, scramble)


def to_ship_name(addr, min_bytes=None, scramble=True):
	if not min_bytes:
		# guess by size
		if addr < 0x100:
			min_bytes = 1

		elif addr < 0x10000:
			min_bytes = 2

		else:
			min_bytes = 4

	if min_bytes == 4 and scramble:
		addr = feen(addr)

	name = ""
	for i in xrange(0, min_bytes):
		byte = addr % 256
		if i % 2 == 1:
			syllable = get_prefix(byte)
		else:
			syllable = get_suffix(byte)

		if (i == 2):
			name = "-" + name

		name = syllable + name
		addr = addr / 256

	return name


def from_ship_name(name, unscramble=True):
	if len(name) == 3:
		return prefix.index(name) / 3

	elif len(name) == 6:
		addr = prefix.index(name[:3]) / 3
		addr *= 256
		addr += suffix.index(name[3:]) / 3
		return addr

	else:
		addr = from_ship_name(name[:6])
		addr *= 65536
		addr += from_ship_name(name[7:])
		if unscramble:
			addr = fend(addr)

		return addr


def nth_planet_of_star(star, n):
	return n * 65536 + star


def print_addr(addr):
	scrambled = feen(addr)
	name = to_planet_name(scrambled)

	print("0x%08x 0x%08x %s" % (addr, scrambled, name))


def print_nth_planet(star, n):
	print_addr(nth_planet_of_star(star, n))


def print_all_star_planets(star):
	for i in xrange(1, 65536):
		print_nth_planet_of_star(star)


def find_planet_with_prefix(galaxy, prefix):
	addr = from_ship_name(prefix) * 65536
	for i in xrange(1, 65536):
		current = addr + i
		unscrambled = fend(current)
		if (unscrambled & 0xff) == galaxy:
			star = unscrambled & 0xffff
			star_name = to_star_name(star)
			planet = to_planet_name(unscrambled)
			print("0x%04x %s: %s" % (star, star_name, planet))


def find_planet_with_suffix(galaxy, suffix):
	addr = from_ship_name(suffix)
	for i in xrange(1, 65536):
		current = addr + (i * 65536)
		unscrambled = fend(current)
		if (unscrambled & 0xff) == galaxy:
			star = unscrambled & 0xffff
			star_name = to_star_name(star)
			planet = to_planet_name(unscrambled)
			print("0x%04x %s: %s" % (star, star_name, planet))


def find_planet_with_double(galaxy):
	for i in xrange(1, 65536):
		current = i + (i * 65536)
		unscrambled = fend(current)
		if (unscrambled & 0xff) == galaxy:
			star = unscrambled & 0xffff
			star_name = to_star_name(star)
			planet = to_planet_name(unscrambled)
			print("0x%04x %s: %s" % (star, star_name, planet))


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	subparsers = parser.add_subparsers(dest='command')

	scramble = subparsers.add_parser('scramble', help='scramble an address')
	scramble.add_argument('address', help='address to scramble')

	unscramble = subparsers.add_parser('unscramble', help='unscramble an address')
	unscramble.add_argument('address', help='address to unscramble')

	address_from_name = subparsers.add_parser('address', help='get address for name')
	address_from_name.add_argument('name', help='name to lookup address of')

	name_from_address = subparsers.add_parser('name', help='get name for address')
	name_from_address.add_argument('address', help='address to lookup name of')

	find_planet = subparsers.add_parser('planet', help='find planet by partial name')
	find_planet.add_argument('-g', '--galaxy', default='0x0', help='galaxy to search in')
	find_planet.add_argument('--type', choices=['prefix', 'suffix', 'both'], help='search type')
	find_planet.add_argument('name', help='name to search for')

	args = parser.parse_args()

	if args.command == 'scramble':
		address = int(args.address, 16)
		print("0x%x" % feen(address))

	if args.command == 'unscramble':
		address = int(args.address, 16)
		print("0x%x" % fend(address))

	elif args.command == 'address':
		print("0x%x" % from_ship_name(args.name))

	elif args.command == 'name':
		address = int(args.address, 16)
		print(to_ship_name(address))

	elif args.command == 'planet':
		galaxy = int(args.galaxy, 16)
		search_type = args.type

		if search_type == 'prefix':
			find_planet_with_prefix(galaxy, args.name)

		elif search_type == 'suffix':
			find_planet_with_suffix(galaxy, args.name)

		elif search_type == 'both':
			find_planet_with_double(galaxy)
