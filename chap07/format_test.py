a = "hello"
b = "good bye"

sample = "this is %s test %s " % (a,b)
print(sample)

sample = "this is {} test {} ".format(a,b)
print(sample)

sample = "this is {0} test {1} ".format(a,b)
print(sample)

sample = "this is {1} test {0} ".format(a,b)
print(sample)

sample = "this is {a} test {b} ".format(a="aaaaa",b="bbbbb")
print(sample)
