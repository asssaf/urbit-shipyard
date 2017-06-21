def nth_planet_of_star(star, n):
	return n * 65536 + star

def generate_planets(star):
	planet_index = 1
	while planet_index < 65536:
		yield nth_planet_of_star(star, planet_index)
		planet_index += 1
