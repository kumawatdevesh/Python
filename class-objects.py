class Person:
    # init method

    def __init__(self, name, age):
        self.name = name
        self.age = age
        

    def prop(self):
        print('my name is '+ self.name +  'and i am old', self.age);


person1 = Person('Devesh', 19);
person2 = Person('Vikas', 20)

person1.prop()
person2.prop()


class Car:

    wheels = 5
    
    def __init__(self):
        self.comp = 'BMW'
        self.mil = 20


c1 = Car()
c2 = Car()
c1.mil = 30
print(c1.comp, c1.mil, c1.wheels)
print(c2.comp, c2.mil, c2.wheels)





