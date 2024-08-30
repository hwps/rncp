import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="verbosity", action="store_true")
parser.add_argument("-f", "--foo", help="number of foo", type=int)
parser.add_argument("src", help="source files", nargs="+")
parser.add_argument("dst", help="destination")
args = parser.parse_args()
if args.verbose:
	print("Verbose mode!")
	
print(f"Foo is {args.foo}")
if args.src:
	print(args.src)
if args.dst:
	print(args.dst)