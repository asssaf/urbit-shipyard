#!/usr/bin/env python2

import argparse

from ob import ob, ob_util
from itertools import ifilter, combinations_with_replacement

def print_addr(addr):
    scrambled = ob.feen(addr)
    name = ob.to_planet_name(scrambled, scramble=False)

    print("0x%08x 0x%08x %s" % (addr, scrambled, name))


def print_all_star_planets(star):
    for planet in ob_util.generate_planets(star):
        print_addr(planet)


def print_star_and_planet(planet):
    star = planet & 0xffff
    star_name = ob.to_star_name(star)
    planet_name = ob.to_planet_name(planet)
    print("0x%04x %s: %s" % (star, star_name, planet_name))


def find_planet_with_prefixes(galaxy, star, words):
    for prefix in words:
        find_planet_with_prefix(galaxy, star, prefix)


def find_planet_with_prefix(galaxy, star, prefix):
    addr = ob.from_ship_name(prefix) * 0x10000

    planet_range = (addr + i for i in xrange(0x1, 0x10000))
    planets = find_planet(planet_range, galaxy, star)

    for planet in planets:
        print_star_and_planet(planet)


def find_planet_with_suffixes(galaxy, star, words):
    for suffix in words:
        find_planet_with_suffix(galaxy, star, suffix)


def find_planet_with_suffix(galaxy, star, suffix):
    addr = ob.from_ship_name(suffix)

    planet_range = (addr + i*0x10000 for i in xrange(0x1, 0x10000))
    planets = find_planet(planet_range, galaxy, star)

    for planet in planets:
        print_star_and_planet(planet)


def find_planet_with_double(galaxy, star):
    # increment both low word and high word so by 0x10001
    planet_range = (i*0x10001 for i in xrange(0x1, 0x10000))
    planets = find_planet(planet_range, galaxy, star)

    for planet in planets:
        print_star_and_planet(planet)


def find_planet_with_both(galaxy, star, words):
    # generate all word combinations from the word list
    combinations = combinations_with_replacement(words, 2)
    planets = (ob.from_ship_name("%s-%s" % c) for c in combinations)
    planets = filter_by_galaxy(galaxy, planets)
    planets = filter_by_star(star, planets)

    for planet in planets:
        print_star_and_planet(planet)


def filter_by_galaxy(galaxy, planets):
    galaxy_pred = lambda x: x & 0xff == galaxy
    return ifilter(galaxy_pred, planets)


def filter_by_star(star, planets):
    if star:
        star_pred = lambda x: x & 0xff00 == star & 0xff00

    else:
        star_pred = lambda x: x & 0xff00 != 0

    return ifilter(star_pred, planets)


def find_planet(addr_range, galaxy, star=None):
    planets = (ob.fend(i) for i in addr_range)
    planets = filter_by_galaxy(galaxy, planets)
    planets = filter_by_star(star, planets)

    return planets


def find_words(prefix, suffix):
    for word in ob_util.find_words(prefix, suffix):
        print(word)


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

    word_parser = subparsers.add_parser('word', help='find words based on glob pattern')
    word_parser.add_argument('--prefix', help='pattern for prefix such as *od or z*', default='*')
    word_parser.add_argument('--suffix', help='pattern for suffix such as bi* or *n', default='*')

    planet_parser = subparsers.add_parser('planet', help='find planet by partial name')
    planet_parser.add_argument('-g', '--galaxy', default='0x0', help='galaxy to search in')
    planet_parser.add_argument('-s', '--star', help='star to search in')
    planet_parser.add_argument('--type', choices=['prefix', 'suffix', 'both', 'double', 'star'], help='search type')
    planet_parser.add_argument('name', help='name to search for', nargs='+')

    args = parser.parse_args()

    if args.command == 'scramble':
        address = int(args.address, 16)
        print("0x%x" % ob.feen(address))

    if args.command == 'unscramble':
        address = int(args.address, 16)
        print("0x%x" % ob.fend(address))

    elif args.command == 'address':
        print("0x%x" % ob.from_ship_name(args.name))

    elif args.command == 'name':
        address = int(args.address, 16)
        print(ob.to_ship_name(address))

    elif args.command == 'word':
        find_words(args.prefix, args.suffix)

    elif args.command == 'planet':
        galaxy = int(args.galaxy, 16)
        star = None
        if args.star:
            star = int(args.star, 16)

        search_type = args.type

        if search_type == 'prefix':
            find_planet_with_prefixes(galaxy, star, args.name)

        elif search_type == 'suffix':
            find_planet_with_suffixes(galaxy, star, args.name)

        elif search_type == 'both':
            find_planet_with_both(galaxy, star, args.name)

        elif search_type == 'double':
            find_planet_with_double(galaxy, star)

        elif search_type == 'star':
            star = ob.from_ship_name(args.name, 2)
            print_all_star_planets(star)
