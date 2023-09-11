#!/usr/bin/env python
"""rncp: Copy source files to target in a randomized order.
usage: rncp source_file ... target_directory"""

import sys
import os
import random
import shutil
import fnmatch

def main():
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