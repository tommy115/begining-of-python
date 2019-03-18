import re

source = 'Young Frankenstein'
m = re.match('You', source)
if m:
    print(m.group())

m = re.match('^You', source)
if m:
    print(m.group())

m = re.match('Frank', source)
if m:
    print(m.group())

m = re.search('Frank',source)
if m:
    print(m.group())

m = re.findall('n', source)
print(m)
print('Found', len(m), 'matches')

m = re.findall('n.', source)
print(m)
print('Found', len(m), 'matches')

import string

printable = string.printable
print(len(printable))

print(printable[0:50])
print(printable[50:])
