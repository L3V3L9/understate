#!/usr/bin/python
import argparse

from understate.parser import *
from understate.render import *

try:
    # Build the args parser and parse
    parser = argparse.ArgumentParser(description='Present a markdown file')

    parser.add_argument('filename', metavar='filename', type=str, 
                               help='an integer for the accumulator')

    args = parser.parse_args()

    # read the markdown file, parse and render
    f = open(args.filename,'r')
    renderer = CursesRenderer()
    Parser(CursesRenderer()).parse(f.read())
    f.close()

finally:
    renderer.clean()