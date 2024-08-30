#!/usr/bin/env python
"""rncp: Copy source files to target in a randomized order."""

import sys
import os
import random
import shutil
import argparse

def main():
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("-v", "--verbose", help="Verbose mode", action="store_true")
	parser.add_argument("-d", "--dry", help="Dry run (do no actual copying)", action="store_true")
	# parser.add_argument("-f", "--foo", help="number of foo", type=int)
	parser.add_argument("src", help="Source files", nargs="+")
	parser.add_argument("dst", help="Destination directory")

	if len(sys.argv)==1:
		# parser.print_help()
		print(__doc__)
		parser.print_usage() # for just the usage line
		parser.exit()

	args = parser.parse_args()

	if len(sys.argv) >= 3:
		destDir = sys.argv[-1]
		if os.path.isdir(destDir):
			fileList= [file for file in sys.argv[1:-1]]

			random.shuffle(fileList)
	  
			counter = 0
	  
			for file in fileList:
				if os.path.isfile(file):
					shutil.copy2(file, destDir)
					counter = counter + 1
				elif os.path.isdir(file):
					print("rncp: " + file + " is a directory (not copied)")
				else:
					print("rncp: " + file + ": No such file or directory")
			print("rncp: Copied " + str(counter) + " items")
		else:
			print("rncp: " + destDir + "is not a directory")
	else:
		print(__doc__)
  
if __name__ == "__main__":
	main()