#!/usr/bin/env python2

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

def get_syllable_index(set, syllable):
    i = set.find(syllable)
    if i == -1:
        raise Exception("Invalid syllable: %s" % syllable)

    return i / 3


def feen(pyn):
    if pyn >= 0x10000 and pyn <= 0xffffffff:
        return 0x10000 + fice(pyn - 0x10000)

    if pyn >= 0x100000000 and pyn <= 0xffffffffffffffff:
        lo = pyn & 0xffffffff
        hi = pyn & 0xffffffff00000000
        return (hi | feen(lo))

    return pyn


def fend(cry):
    if cry >= 0x10000 and cry <= 0xffffffff:
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

    if sel[1] == 65535:
        res = 65535*sel[1] + sel[0]
    else:
        res = 65535*sel[0] + sel[1]

    logging.debug("fice(%x)=%x" % (nor, res))
    return res


def teil(vip):
    sel = [ vip % 65535, vip / 65535 ]
    for i in xrange(3, -1, -1):
        sel = rund(i, sel[0], sel[1])

    if sel[1] == 65535:
        res = 65535*sel[1] + sel[0]
    else:
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
        return get_syllable_index(suffix, name)

    elif len(name) == 6:
        addr = get_syllable_index(prefix, name[:3])
        addr *= 256
        addr += get_syllable_index(suffix, name[3:])
        return addr

    elif len(name) == 13:
        addr = from_ship_name(name[:6])
        addr *= 65536
        addr += from_ship_name(name[7:])
        if unscramble:
            addr = fend(addr)

        return addr

    else:
        raise Exception("Names longer than a planet are not supported: %s" % name)

def is_syllable(set, syllable):
    if not syllable or len(syllable) != 3:
        return False

    return set.find(syllable) % 3 == 0


def is_prefix_syllable(syllable):
    return is_syllable(prefix, syllable)


def is_suffix_syllable(syllable):
    return is_syllable(suffix, syllable)
