#!/usr/bin/env python
"""
Escape special characters in the 'doi' field of BibTeX entries

"""
from __future__ import absolute_import, print_function

from argparse import ArgumentParser, FileType
import re
import sys


def escape_doi(line):
    """Escape the required characters in a doi entry."""
    for char in ('<', '>'):
        # Match the current character provided it is not already escaped.
        expr = re.compile('(?<!\$){0:s}(?!\$)'.format(char))
        line = expr.sub('${:s}$'.format(char), line)
    return line


def main(argv=None):
    if argv is None:
        argv = sys.argv
    ap = ArgumentParser(description=__doc__)
    ap.add_argument('bibfile', nargs='?', type=FileType('r'),
                    default=sys.stdin,
                    help=('an optional input .bib file, if not present input '
                          'will be read from stdin'))
    try:
        argns = ap.parse_args(argv[1:])
        for line in argns.bibfile:
            if line.strip().lower().startswith('doi'):
                line = escape_doi(line)
            print(line, end='')
        return 0
    except IOError as e:
        print('error: {!s}'.format(e))
        return 1


if __name__ == '__main__':
    sys.exit(main())
