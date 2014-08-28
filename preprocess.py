'''
Created on Aug 28, 2014

@author: lwoydziak
'''
from __future__ import print_function
import sys
import argparse
from re import compile, IGNORECASE

def preprocess(inputfile):
    with open("README.rst", mode='w') as output:
        regex = compile('^@@INSERT@@', IGNORECASE) # regex to matches the package name at the beginning of the line
        for _, line in enumerate(open("README.in", 'r'), start=1):
            matches = regex.match(line)
            if matches is None:
                print(line, end="", file=output)
                continue
            for _, addline in enumerate(inputfile, start=1):
                print("  "+addline, end="", file=output)

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    commandLine = argparse.ArgumentParser(description='Preprocess README.in and replace @@INSERT@@ with file contents')
    commandLine.add_argument('inputfile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    environment = commandLine.parse_args(argv)

    return preprocess(environment.inputfile)

if __name__ == '__main__':
    if sys.argv[0] is None:
        # fix for weird behaviour when run with python -m
        # from a zipped egg.
        sys.argv[0] = 'preprocess.py'
    sys.exit(main())