'''
    sysargv-example.py
    Jeff Ondich, 21 September 2020

    A simple illustration of command-line parsing without using
    a library like argparse.
'''

import sys

def usage_statement():
    statement = f'Usage: {sys.argv[0]} person-name\n'
    statement += '    Prints a greeting to the named person.'
    return statement

def parse_command_line():
    arguments = {}
    if len(sys.argv) == 2:
        arguments['person-name'] = sys.argv[1]
    return arguments

def main(arguments):
    name = arguments['person-name']
    print(f'Hi there, {name}!')


arguments = parse_command_line()
if 'person-name' not in arguments:
    print(usage_statement())
else:
    main(arguments)

