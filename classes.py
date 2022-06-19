#!/usr/bin/python/deskop/inspire with stem/classes.py

#######       classes
#       Name : Collins muli
#       Date : 18/6/2022
######################################

#person class
class Person:
    def __init__(self,_name,_age):
            self.name=_name
            self.age= _age

    def sayHi(self):
        print('Hello my name is ' +str(self.name)+' and i am ' +str(self.age) + ' years old')
person1 = Person('Collins',22)
person1.sayHi()
person2 = Person('Spencer',20)
person2.sayHi()

#employee class
class Employee:
    def __init__(self,_name,_salary):
        self.name = _name
        self.salary = _salary
    def sayHi(self):
        print('hello my name is ' + str(self.name) + ' and i earn ' + str(self.salary) + ' as my salary')
employee1=Employee('Collins',995499)
employee1.sayHi()
employee2=Employee('Spencer',699999)
employee2.sayHi()


#vehicle class
class Vehicle:
    def  __init__(instance,_speed,_mileage):
        instance.speed=_speed
        instance.mileage= _mileage
        
    def sayHi(instance):
        print('maximum speed is ' + str(instance.speed) + ' Km/h while mileage is '+str(instance.mileage)+" kilometeres")

Toyota = Vehicle(360,200988)
Mercedes= Vehicle(240,500789)
Toyota.sayHi()
Mercedes.sayHi()