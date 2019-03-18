print("###############6-1###############")

class Thing():
    pass

example = Thing()
example2 = Thing

print(Thing)
print(example)
print(example2)

print("###############6-2###############")

class Thing2():
    def __init__(self, name):
        self.letters = name

class Thing3():
    def set(self,name):
        self.letters = name

exam = Thing2('abc')
print(exam.letters)

exam2 = Thing3()
exam2.set('hello')

print(exam2.letters)

print("###############6-4###############")

class Element():
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    @property
    def name(self):
        return self.__name
    @property    
    def symbol(self):
        return self.__symbol
    @property    
    def number(self):
        return self.__number
    def dump(self):
        print(self.__name)
        print(self.__symbol)
        print(self.__number)
    def __str__(self):
        return self.__name + ' ' + self.__symbol + ' ' + str(self.__number)

e = Element('Hydrogen', 'H', 1)

print("###############6-5###############")

dict = {
    'name' : 'Hydrogen',
    'symbol' : 'H',
    'number' : 1 }

hydrogen = Element(dict['name'],dict['symbol'],dict['number'])
print(hydrogen.name)

print("###############6-6###############")

hydrogen.dump()

print("###############6-7###############")

print(hydrogen)

print("###############6-8###############")

print(hydrogen.name)
print(hydrogen.symbol)
print(hydrogen.number)

print("###############6-9###############")

class Bear():
    def eats(self):
        return 'barries'
    
class Rabbit():
    def eats(self):
        return 'clover'

class Octothorpe():
    def eats(self):
        return 'campers'

b = Bear()
r = Rabbit()
o = Octothorpe()
print(b.eats())
print(r.eats())
print(o.eats())
 
print("###############6-10###############")

class Laser():
    def does(self):
        return 'disintegrate'

class Claw():
    def does(self):
        return 'crush'

class SmartPhone():
    def does(self):
        return 'ring'

class Robot():
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartPhone = SmartPhone()
    def does(self):
        return self.laser.does() + " " + self.claw.does() + " " + self.smartPhone.does()

r = Robot()
print(r.does())
