
def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"' % ( value,name,value2 ) )

unicode_test('A')
unicode_test('$')
unicode_test('\u00a2')
unicode_test('\u20ac')

unicode_test('清')
unicode_test('\uff71')
unicode_test('①')


unicode_test('\u2603')

place = 'caf\u00e9'
print(place)

snowman = '\u2603'

print('snowman length = ' + str(len(snowman)))

ds = snowman.encode('utf-8')
print(ds)
print('len =' + str(len(ds)) )

