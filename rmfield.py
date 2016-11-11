#!/usr/bin/env python
"""
Remove fields from BibTeX entries

"""
from __future__ import absolute_import, print_function

from argparse import ArgumentParser, FileType
import sys


def main(argv=None):
    if argv is None:
        argv = sys.argv
    ap = ArgumentParser(description=__doc__)
    ap.add_argument('fields', type=str,
                    help='a comma separated list of field names')
    ap.add_argument('bibfile', nargs='?', type=FileType('r'),
                    default=sys.stdin,
                    help=('an optional input .bib file, if not present input '
                          'will be read from stdin'))
    try:
        argns = ap.parse_args(argv[1:])
        fields = [field for field in argns.fields.split(",") if field]
        for line in argns.bibfile:
            if any([line.strip().lower().startswith(field)
                    for field in fields]):
                continue
            else:
                print(line, end='')
        return 0
    except IOError as e:
        print('error: {!s}'.format(e))
        return 1


if __name__ == '__main__':
    sys.exit(main())
