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
    ap.add_argument('inbibfile', nargs='?', default=[None])
    ap.add_argument('-o', '--outbibfile', nargs=1, default=[None])
    try:
        argns = ap.parse_args(argv[1:])
        outfilename = argns.outbibfile[0]
        if outfilename is not None:
            outbibfile = open(outfilename[0], 'w')
        else:
            outbibfile = sys.stdout
        infilename = argns.inbibfile[0]
        if infilename is not None:
            inbibfile = open(infilename[0], 'r')
        else:
            inbibfile = sys.stdin
        # Fields is a comma-separated list of BibTeX fields.
        fields = argns.fields[0].split(',')
        try:
            # Remove the empty string as this will match all BibTeX fields.
            fields.remove('')
        except ValueError:
            pass
        process_bibtex_file(inbibfile, outbibfile, fields)
        inbibfile.close()
        outbibfile.close()
        return 0
    except IOError, e:
        print >> sys.stderr, 'error: {0:s}'.format(e)
        return 1


if __name__ == '__main__':
    sys.exit(main())

