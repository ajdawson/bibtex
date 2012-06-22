#!/usr/bin/env python
"""Escape special characters in the 'doi' field of BibTeX entries."""
import os
import sys
import re
from argparse import ArgumentParser


# Define the characters that should be escaped in doi entries.
ESCAPE_CHARACTERS = ('>', '<')


def is_doi_entry(line):
    """Check if a line is a doi entry."""
    return line.strip().lower().startswith('doi')


def escape_character(char):
    """Given a character, return its escaped form."""
    return '$%c$' % char


def process_doi_line(key):
    """Escape the required characters in a doi entry."""
    for char in ESCAPE_CHARACTERS:
        # Match the current character provided it is not already escaped.
        expr = re.compile('(?<!\$)%c(?!\$)' % char)
        key = expr.sub(escape_character(char), key)
    return key


def process_bibtex_line(line):
    """Process a line from a BibTeX file."""
    if not is_doi_entry(line):
        return line
    line = process_doi_line(line)
    return line


def process_bibtex_file(inbibfile, outbibfile):
    """Escape special characters in doi BibTeX entries."""
    for line in inbibfile.readlines():
        line = process_bibtex_line(line)
        outbibfile.write(line)


def main(argv=None):
    if argv is None:
        argv = sys.argv
    ap = ArgumentParser(prog=os.path.basename(argv[0]),
            description=__doc__)
    ap.add_argument('inbibfile', nargs='?', default=None)
    ap.add_argument('-o', '--outbibfile', nargs=1, default=[None])
    try:
        argns = ap.parse_args(argv[1:])
        outfilename = argns.outbibfile[0]
        if outfilename is not None:
            outbibfile = open(outfilename, 'w')
        else:
            outbibfile = sys.stdout
        infilename = argns.inbibfile
        if infilename is not None:
            inbibfile = open(infilename, 'r')
        else:
            inbibfile = sys.stdin
        process_bibtex_file(inbibfile, outbibfile)
        inbibfile.close()
        outbibfile.close()
        return 0
    except IOError, e:
        print >> sys.stderr, 'error: %s' % e
        return 1

if __name__ == '__main__':
    sys.exit(main())

