
print("################### 7-1 #######################")

mystery = '\U0001f4a9'
print(mystery)
print(type(mystery))

import unicodedata

print(unicodedata.name(mystery))

print("################### 7-2 #######################")

print("len=" + str(len(mystery)) )
pop_bytes = mystery.encode('utf-8')
print(pop_bytes)
print("len=" + str(len(pop_bytes)) )
print(type(pop_bytes))

print("################### 7-3 #######################")
pop_string = pop_bytes.decode('utf-8')
print(pop_string)

if mystery == pop_string:
    print("same!!!")

print("################### 7-4 #######################")

source = """My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now thinks he's a %s""" % ('roast beef', 'ham', 'head', 'clam')

print(source)

print("################### 7-5 #######################")

letter = """Dear {salutation} {name},

Thank you for your letter, We are sorry that our {product} {verbed} in your
{room}. Please note that it should never be used in a {room}, especially near
any {animals}.

Send us your receipt and {amount} for shipping and handling. We will send
you another {product} that, in our tests, is {percent}% less likely to
have {verbed}.

Thank you for your support.

Sincerely,
{spokesman}
{job_title}
"""

print("################### 7-6 #######################")

response = { 'salutation' : 'aaaaa',
             'name' : 'tomoaki',
             'product' : 'PC',
             'verbed' : 'saw',
             'room' : 'Kikunoma',
             'animals' : 'fox',
             'amount' : 100,
             'percent' : 18,
             'spokesman' : 'Tomoaki Seike',
             'job_title' : 'Vice President'}

print(letter)
print(letter.format(**response))


print("################### 7-7 #######################")

mammoth = """We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.

All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.

Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.

May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Paris.

Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.

We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon.
"""

print(mammoth)

print("################### 7-8 #######################")
import re
pat1 = r'\bc\w*'
print(re.findall(pat1, mammoth))

print("################### 7-9 #######################")
pat2 = r'\bc\w{3}\b'
print(re.findall(pat2, mammoth))

print("################### 7-10 #######################")
pat3 = r'\b\w*r\b'
print(re.findall(pat3, mammoth))

print("################### 7-11 #######################")
pat4 = r'\b\w*[aiueo]{3}\w*\b'
print(re.findall(pat4, mammoth))
