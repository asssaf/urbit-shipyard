#!/usr/bin/env python2

import argparse

from ob import ob, ob_util


def print_addr(addr):
	scrambled = ob.feen(addr)
	name = ob.to_planet_name(scrambled, scramble=False)

	print("0x%08x 0x%08x %s" % (addr, scrambled, name))


def print_all_star_planets(star):
	for planet in ob_util.generate_planets(star):
		print_addr(planet)


def find_planet_with_prefix(galaxy, prefix):
	addr = ob.from_ship_name(prefix) * 65536
	for i in xrange(1, 65536):
		current = addr + i
		unscrambled = ob.fend(current)
		if (unscrambled & 0xff) == galaxy:
			star = unscrambled & 0xffff
			star_name = ob.to_star_name(star)
			planet = ob.to_planet_name(unscrambled)
			print("0x%04x %s: %s" % (star, star_name, planet))


def find_planet_with_suffix(galaxy, suffix):
	addr = ob.from_ship_name(suffix)
	for i in xrange(1, 65536):
		current = addr + (i * 65536)
		unscrambled = ob.fend(current)
		if (unscrambled & 0xff) == galaxy:
			star = unscrambled & 0xffff
			star_name = ob.to_star_name(star)
			planet = ob.to_planet_name(unscrambled)
			print("0x%04x %s: %s" % (star, star_name, planet))


def find_planet_with_double(galaxy):
	for i in xrange(1, 65536):
		current = i + (i * 65536)
		unscrambled = ob.fend(current)
		if (unscrambled & 0xff) == galaxy:
			star = unscrambled & 0xffff
			star_name = ob.to_star_name(star)
			planet = ob.to_planet_name(unscrambled)
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
	find_planet.add_argument('--type', choices=['prefix', 'suffix', 'both', 'star'], help='search type')
	find_planet.add_argument('name', help='name to search for')

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

	elif args.command == 'planet':
		galaxy = int(args.galaxy, 16)
		search_type = args.type

		if search_type == 'prefix':
			find_planet_with_prefix(galaxy, args.name)

		elif search_type == 'suffix':
			find_planet_with_suffix(galaxy, args.name)

		elif search_type == 'both':
			find_planet_with_double(galaxy)

		elif search_type == 'star':
			star = ob.from_ship_name(args.name, 2)
			print_all_star_planets(star)
