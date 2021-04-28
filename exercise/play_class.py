class Dog():
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def abc(self):
        print(self.name.title())


dooog = Dog('hello',99)
dooog.abc()

print(dooog.age)
dooog.name='ok'
dooog.abc()
