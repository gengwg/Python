stocks = [
    ('GOOG', 100, 490.1),
    ('AAPL', 50, 545.75),
    ('FB', 150, 7.45),
    ('HPQ', 75, 33.2),
]

# remove old database
import os
try:
    os.remove('database.db')
except OSError:
    pass

import sqlite3

# connect to database using connect() function with parameters
db = sqlite3.connect('database.db')

# to do anything with the data, you need a cursor
c = db.cursor()
# once having cursor, you can execute sql queries
c.execute('create table portfolio (symbol text, share integer, price real)')
db.commit()

# insert a sequence of rows into the data
c.executemany('insert into portfolio values (?,?,?)', stocks)
db.commit()

# perform a query
# for row in db.execute('select * from portfolio'):
for row in c.execute('select * from portfolio'):
    print(row)

# escape parameters using ?
min_price = 100
for row in c.execute('select * from portfolio where price >= ?',
                     (min_price,)):
    print(row)
