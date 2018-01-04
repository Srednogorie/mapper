"""This Python file uses the following encoding: utf-8"""
import argparse
import json
import sys
from collections import Counter


class MyParser(argparse.ArgumentParser):
    """Overriding the error method of the ArgumentParser class."""
    def error(self, message):
        """It is going to handle all the cases where false argument is provided
           and return --help menu to the user."""
        sys.stderr.write('Please Enter Valid Arguments.\n')
        self.print_help()
        # Command line syntax error.
        sys.exit(2)


def counter(string):
    """Handle the --letter-counter flag."""
    a = list(sorted(Counter(string.lower()).items()))
    result = ["%s:%s" % x for x in a]
    # Some basic error handling.
    if len(a) == 0 or string.isspace():
        sys.stderr.write('Please Enter Valid String.\n')
        parser.print_help()
    else:
        print(result)


def flatten(data):
    """Flatten the dict."""
    print(type(data))
    for i in data:
        if not isinstance(data[i], dict):
            yield (i, data[i])
        else:
            for b in flatten(data[i]):
                yield b


def json_parser(filename):
    """Handle the --parse-json-file flag. Using load() over loads() saves notting
       but one line of code."""
    data = json.load(open(filename))
    new_data = dict(list(flatten(data)))
    print('Flatten dict: {}'.format(new_data))
    # print function over the data object returns nested dict by default.
    print('Nested dict: {}'.format(data))


parser = MyParser(description='Task')
parser.add_argument('--letter-counter', metavar='LETTERS', action='store', type=counter,
                    help='Counts every letter occurrence in a given string. Returns sorted list')
parser.add_argument('--parse-json-file', metavar='JSON_FILE', action='store', type=json_parser,
                    help='Reads given JSON formatted file and outputs flatten DICT')
# Return --help menu to the user when no any arguments are provided.
if len(sys.argv) == 1:
    sys.stderr.write('Please Enter At Least One Valid Argument.\n')
    parser.print_help()
    # All other types of error.
    sys.exit(1)
args = parser.parse_args()
