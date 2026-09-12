#!/usr/bin/env python3

"""
Print out all rows in sheet 0 of an MS Excel file,
tab delimited.
"""

import xlrd
book = xlrd.open_workbook("2XL_VM_details.xlsx")
print(f"The number of worksheets is {book.nsheets}")
print(f"Worksheet name(s): {book.sheet_names()}")
sh = book.sheet_by_index(0)
print(f"{sh.name} {sh.nrows} {sh.ncols}")
print(f"Cell D30 is {sh.cell_value(rowx=29, colx=3)}")
for rx in range(sh.nrows):
    for cx in range(sh.ncols):
        print(sh.cell_value(rx, cx), end='\t')
    print("\n", end='')
