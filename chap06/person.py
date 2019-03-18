
class Person():
    def __init__(self,name):
        self.name = name
    
class MDPerson(Person):
    def __init__(self,name):
        self.name = "Mid" + name

class Word():
    def __init__(self,text):
        self.text = text
        
    def __eq__(self,word2):
        return self.text.lower() == word2.text.lower()
    
class Word2():
    def __init__(self,text):
        self.text = text
        
    def __eq__(self,word2):
        return self.text.lower() == word2.text.lower()

a = Person('hello')
b = MDPerson('hello')

print(a.name)
print(b.name)

a.name = 'world'
print(a.name)

w = Word("b")
w1 = Word("c")
w2 = Word("b")
w3 = Word2("b")

print(w==w1)
print(w==w2)
print(w==w3)

