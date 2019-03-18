print('##################### 8-1 ####################')

test1 = 'This is a test of the emergency text system'
fout = open('test.txt','wt')
fout.write(test1)
fout.close()

print('##################### 8-2 ####################')
test2 = ''
fin = open('test.txt','rt')
while True:
    line = fin.readline()
    if not line:
        break
    test2 += line

fin.close()
print(test2)

print('##################### 8-4 ####################')
import csv

file_name = 'books.csv'
with open(file_name, 'rt') as fin:
    cin = csv.DictReader(fin)
    books = [row for row in cin]

print(books)

print('##################### 8-6 ####################')
import sqlite3
conn = sqlite3.connect('books.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE book(title varchar(100), author varchar(100), year int)''')

print('##################### 8-7,8-8,8-9 ####################')
file_name = 'books2.csv'
with open(file_name, 'rt') as fin:
    cin = csv.DictReader(fin)
    books = [row for row in cin]

print(books)

ins = 'insert into book(title,author,year) values(?,?,?)'

for book in books:
    print(book['year'])
    curs.execute(ins, (book['title'],book['author'],book['year']))

curs.execute('select title from book order by title')
rows = curs.fetchall()
for row in rows:
    print(row)

curs.execute('select * from book order by year')
rows = curs.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()

print('##################### 8-10 ####################')
import sqlalchemy as sa
conn = sa.create_engine('sqlite:///books.db')
rows = conn.execute('select title from book order by title')
for row in rows:
    print(len(row))
    print(row)

print('##################### 8-11 ####################')
import redis
conn = redis.Redis()
conn.hmset('test', {'count':'1', 'name':'Fester Bestertester'})
print(conn.hvals('test'))
