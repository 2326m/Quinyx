from flask import Flask
import xlrd
import csv
import datetime

loc = ("sales data 2019 1-3.xls")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

sheet.cell_value(0, 0)

for i in range(1, 10):
        # sheet.nrows):
    print(sheet.row_values(i))
