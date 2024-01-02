"""
Question: Define a class, which have a class parameter and have a same instance parameter.

Hints: Define a instance parameter, need add it in init method. You can init a object with construct parameter
or set the value later
"""


class test_class:
    # Class Parameter
    class_param = "cp"

    def __init__(self, instance_param):
        # Instance Parameter
        self.instance_param = instance_param


tc1 = test_class("ip1")
print(tc1.class_param, tc1.instance_param)


class Person:
    # Define the class parameter "name"
    name = "Person"

    def __init__(self, name=None):
        # self.name is the instance parameter
        self.name = name


jeffrey = Person("Jeffrey")
print("%s name is %s" % (Person.name, jeffrey.name))

nico = Person()
# Person.name = "Nico"
nico.name = "Nico"
print("%s name is %s" % (Person.name, nico.name))



