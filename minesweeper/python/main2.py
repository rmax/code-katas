"""
Read field from standard input and display result
Usage: $ cat input | python main2.py
"""
import fileinput
import sys

from minesweeper import Field

def main():
    nlines = 0
    mcols = 0
    field_input = None
    field_count = 0
    expect_size_line = True
    for line in fileinput.input():
        # strip \n
        line = line.strip()

        if expect_size_line:
            # expect two integers
            nlines, mcols = map(int, line.split())
            if nlines > 0:
                # Read fields in next loop
                expect_size_line = False
                # initialize field
                field_input = list()
                linecount = nlines
                field_count += 1
        else:
            # append line as list/row
            field_input.append(list(line))
            # pop line
            linecount -= 1

            if linecount == 0:
                # process next field
                expect_size_line = True

                # Read complete display result
                field = Field(field_input)

                if not field.is_empty():
                    result = field.resolve()

                    if field_count > 1:
                        sys.stdout.write("\n")

                    sys.stdout.write("Field #%d\n" % field_count)
                    for row in result:
                        for cell in row:
                            sys.stdout.write(cell)
                        sys.stdout.write("\n")

    return 0

if __name__ == '__main__':
    sys.exit(main())

