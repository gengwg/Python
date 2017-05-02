#!/usr/bin/env python3

"""
Print out all rows in sheet 0 of an MS Excel file,
tab delimited.
"""

import xlrd
book = xlrd.open_workbook("myfile.xls")
print("The number of worksheets is {0}".format(book.nsheets))
print("Worksheet name(s): {0}".format(book.sheet_names()))
sh = book.sheet_by_index(0)
print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
print("Cell D30 is {0}".format(sh.cell_value(rowx=29, colx=3)))
for rx in range(sh.nrows):
    for cx in range(sh.ncols):
        print(sh.cell_value(rx, cx), end='\t')
    print("\n", end='')
