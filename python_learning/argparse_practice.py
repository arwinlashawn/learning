# argparse_practice
# credit: https://www.youtube.com/watch?v=cdblJqEUDNo

import math
import argparse

parser = argparse.ArgumentParser(description='Calculate volume of a cylinder')
parser.add_argument('-r', '--radius', type=int, metavar='', required=True, help='Radius of cylinder')
parser.add_argument('-H', '--height', type=int, metavar='', required=True, help='Height of cylinder')
# we can also make it accept more optional arguments to make the result description vary
# in this case, quiet results in just the volume
# verbose results in a full sentence specifying all variables
# mutually exclusive, means you can only specify either one, or not specify at all
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='print quiet')
group.add_argument('-v', '--verbose', action='store_true', help='print verbose')
args = parser.parse_args()

def cylinder_volume(radius, height):
	vol = (math.pi) * (radius ** 2) * (height)
	return vol

if __name__ == '__main__':
	volume = cylinder_volume(args.radius, args.height)
	if args.quiet:
		print(volume)
	elif args.verbose:
		print("Volume of a cylinder with radius %s and height %s is %s" % (args.radius, args.height, volume))
	else:
		print(("Volume of the cylinder = %s") % volume)

# advantage:
# quickly run programs on your command line
# can use help flags to see exactly what you need to pass
# don't need to change things in the original program
