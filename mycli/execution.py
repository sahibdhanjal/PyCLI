import sys
import argparse
from os import path

"""
read the CLI version from the VERSION file
"""
DIR_PATH = path.dirname(path.realpath(__file__))
VERSION_FILE = path.join(DIR_PATH, './../VERSION')

def add(args):
    print(args.num1 + args.num2)

def subtract(args):
    print(args.num1 - args.num2)

"""
function to create the parser with subparsers
"""
def create_parser():
    # create the main parser object
    parser = argparse.ArgumentParser(description='CLI demo')
    version = open(VERSION_FILE).read().strip()
    parser.add_argument('--version', '-V', action='version', version=version)
    # addition subparser
    subparsers = parser.add_subparsers()
    add_subparser = subparsers.add_parser('add', help='add 2 numbers')
    add_subparser.add_argument('--num1', '-a', help='first number in operation', type=int, required=True)
    add_subparser.add_argument('--num2', '-b', help='second number in operation', type=int, required=True)
    add_subparser.set_defaults(func=add)
    # subtraction subparser
    subtract_subparser = subparsers.add_parser('subtract', help='subtract 2 numbers')
    subtract_subparser.add_argument('--num1', '-a', help='first number in operation', type=int, required=True)
    subtract_subparser.add_argument('--num2', '-b', help='second number in operation', type=int, required=True)
    subtract_subparser.set_defaults(func=subtract)
    return parser

"""
the main function creating the parser and executing all commands
"""
def main():
    parser = create_parser()
    args = parser.parse_args()
    if len(sys.argv) == 1:
        sys.exit(parser.print_usage())
    args.func(args)
