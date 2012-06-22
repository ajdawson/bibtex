#!/usr/bin/env python
"""Remove fields from BibTeX entries."""
import os
import sys
import re
from argparse import ArgumentParser


def is_entry(line, entry_type):
    return line.strip().lower().startswith(entry_type)


def valid_line(line, fields):
    for entry_type in fields:
        if is_entry(line, entry_type):
            return False
    return True


def process_bibtex_file(inbibfile, outbibfile, fields):
    for line in inbibfile.readlines():
        if valid_line(line, fields):
            outbibfile.write(line)


def main(argv=None):
    if argv is None:
        argv = sys.argv
    ap = ArgumentParser(prog=os.path.basename(argv[0]),
            description=__doc__)
    ap.add_argument('-f', '--fields', nargs=1, default=[''])
    ap.add_argument('inbibfile', nargs=1)
    try:
        argns = ap.parse_args(argv[1:])
        outbibfile = sys.stdout
        inbibfile = open(argns.inbibfile[0], 'r')
        fields = argns.fields[0].split(',')
        try:
            fields.remove('')
        except ValueError:
            pass
        print fields
        process_bibtex_file(inbibfile, outbibfile, fields)
        inbibfile.close()
        return 0
    except IOError, e:
        print >> sys.stderr, 'error: {0:s}'.format(e)
        return 1


if __name__ == '__main__':
    sys.exit(main())

