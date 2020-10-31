#! /usr/bin/env python

from zipfile import ZipFile
import argparse
import sys

parser = argparse.ArgumentParser (description="Usage: {} -z <zipfile.zip> -p <passwordfile.txt>".format(sys.argv[0]))
parser.add_argument ("-z", dest="ziparchive", help="Zip Archive File")
parser.add_argument ("-p", dest="passfile", help="Password File")
parsedArgs = parser.parse_args()

try:
	print("Zipfile =  {}".format(parsedArgs.ziparchive))
	zipFile = ZipFile (parsedArgs.ziparchive)
except:
	print ("NOPEFISH!")
	exit(0)
