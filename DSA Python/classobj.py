class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

a = person("John", 30)
print(a)


#to solve this we use _str_

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} age:{self.age}"
    
    def myfunc(abc):  #function is objects are called methods ie. Methods in objects are functions that belong to the object.
        print("My name is:", abc.name)  #self can have any name

    

a = person("John", 30)
print(a)
a.myfunc()

del a.age
del a 