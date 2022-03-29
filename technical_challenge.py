from flask import Flask
import xlrd
import csv
from datetime import datetime, timedelta
import math

# this function takes in a number of minutes and rounds it up to the nearest multiple of 15
def fifteen(minutes):
    return math.ceil(minutes * 1.0 / 15) * 15


# open up the spreadsheet (NOTE: xlrd would not read xlsx file)
loc = ("sales data 2019 1-3.xls")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

sheet.cell_value(0, 0)

# initialize dictionary to store transaction info for each 15-minute interval
# dictionary format: { day: {first time: [sales, transactions], second time: [sales, transaction]...}, day2: ...}
dict = {}

# parse through the spreadsheet
for i in range(1, sheet.nrows):
    row = sheet.row_values(i)
    date = row[2]

    if date not in dict.keys():
        dict[date] = {}

    time_exact = row[3]*1440
    # ceiling time up to next 15 minute interval
    time = fifteen(time_exact)/1440

    if time not in dict[date].keys():
        dict[date][time] = [0, 0]

    value = row[5]

    dict[date][time][0] += value
    dict[date][time][1] += 1

#p rint(dict)

# open and write to the csv
f = open('transactions.csv', 'w')
writer = csv.writer(f)
writer.writerow(['day', 'time', 'sales', 'transactions'])

# write a row to the csv file for each 15 minute interval
for day in dict.keys():
    for interval in dict[day].keys():
        sales = dict[day][interval][0]
        transactions = dict[day][interval][1]
        row = [day, interval, sales, transactions]
        writer.writerow(row)


f.close()


