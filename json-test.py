import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    
    def getAttr(self, name):
        return self.__getattribute__(name)

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

s = Student('Bob', 20, 88)
# print(json.dumps(s,default=student2dict))
serialStud = json.dumps(s,default=lambda obj: obj.__dict__)
print(serialStud)

json.dumps()
stud = json.loads(serialStud, object_hook=dict2student)
print(stud.getAttr("age"))