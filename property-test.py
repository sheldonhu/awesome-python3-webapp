# -*- encoding:utf-8 -*-
# 学习@property使用

class Person(object):

    def __init__(self):
        self._age = 11
        self._name = 'fd'
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, _name):
        self._name = _name

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, _age):
        if not isinstance(_age, int):
            raise ValueError("age must be an integer !")
        if _age < 0 or _age > 150:
            raise ValueError("age must between 0 and 150")
        self._age = _age

p1 = Person()
p1.age = 10
p1.name='hu'
print("%s is %s years old"%(p1.name, p1.age))