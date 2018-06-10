"""Inspect smali file.

Usage:
    inspect.py -i File.smali 

Options:
    -h --help      Show this screen.
    -i <filename>  Input filename to inspect.
    -e             Inspect Exceptions
    -m             Inspect Methods
"""

from docopt import docopt
import smali.source
import smali.emulator

def main(arguments):
    filename = arguments.get('-i')


def inspect_exceptions(filename):
    """Inspect exceptions in the smali file."""
    emu = smali.emulator.Emulator()
    source = smali.source.get_source_from_file(filename)
    emu.run_source(source_code=source)
    print(emu.vm.catch_blocks)


def inspect_methods(filename):
    """Inspect methods in the smali file."""
    pass


if __name__ == '__main__':
    main(docopt(__doc__))

