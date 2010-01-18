#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import fileinput
import logging
import pprint
import sys

def main():
    """
    minesweeper
    """
    nlines = 0
    mcols = 0
    field = None
    field_count = 0
    expect_size_line = True
    for line in fileinput.input():
        line = line.strip()
        if expect_size_line:
            try:
                # expect two integers
                nlines, mcols = map(int, line.split())
                logging.debug('N: %s, M: %s', nlines, mcols)
            except ValueError, e:
                logging.debug('Incorrect size line: %s', e)
            finally:
                if nlines > 0:
                    # Read fields on next loop
                    expect_size_line = False
                    # initialize field 
                    field = list()
                    linecount = nlines
                    field_count += 1
        else:
            logging.info('reading next line (remain %d): %r',
                    nlines, line)
            fline = list(line)
            # sanity check
            if len(fline) != mcols:
                raise ValueError('Wrong columns count %s: %r' \
                            % (len(fline), fline))
            field.append(list(line))

            # pop line
            linecount -= 1
            if linecount == 0:
                # this is last line
                expect_size_line = True

                bomb = '*'

                def is_bomb(c):
                    return c == bomb

                def next_available(matrix, m, n):
                    if m < 0 or n < 0:
                        # negative index
                        return False
                    try:
                        # index is bomb?
                        return not is_bomb(str(matrix[m][n]))
                    except IndexError, e:
                        # index not exists
                        return False 

                # @@@ process field
                #result = [[0] * mcols] * nlines
                # prevent copying references using list expressions
                result = [[0 for _i in range(mcols)] for _j in range(nlines)]
                for i,fline in enumerate(field):
                    logging.info('processing line: %r', fline)
                    for j,col in enumerate(fline):
                        if is_bomb(col):
                            # permutations
                            for _i in range(i-1, i+1 +1):
                                for _j in range(j-1, j+1 +1):
                                    if (_i,_j) == (i,j):
                                        # same element
                                        result[i][j] = bomb
                                    else:
                                        # sum 1 adjacents
                                        if next_available(result, _i, _j):
                                            result[_i][_j] += 1
                        else:
                            # sanity check
                            if col != '.':
                                raise ValueError('Invalid input: %r' % col)

                            # not bomb, pass
                            pass

                #print '== result'
                #pprint.pprint(result)
                sys.stdout.write("Field #%d\n" % field_count)
                for _line in result:
                    for _col in _line:
                        sys.stdout.write(str(_col))
                    sys.stdout.write("\n")
                sys.stdout.write("\n")

    return 0

    

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '--debug':
        logging.basicConfig(level=logging.DEBUG)
        # needed 'coz fileinput will interpret as file
        del sys.argv[1]
    sys.exit(main())
