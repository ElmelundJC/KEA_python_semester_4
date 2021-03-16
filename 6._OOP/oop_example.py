class Person:

    spicies = 'Mammal'  # class variable

    def __init__(self, *args):
        # self.name = name        # instance variable

        if len(args) == 1:
            self.name = args[0]
            self.age = 123

        elif len(args) == 2:
            self.name = args[0]
            self.age = args[1]

    def name_age(self):
        return self.name + str(self.age)

#    # overwriting the old method so the old method basicly wont exist
#    def __init__(self, name=None, age=None):
#        self.name = name
#        self.age = age


class Instructor:
    def __init__(self, course):
        self.course = course


class Student(Person, Instructor):

    def __init__(self, *args):
        # be aware that the second parameter is overwritten from the person __init__ class.. that is the parent class super can take many parameters, but the 444 overwrites 123 at the moment.
        Person.__init__(self, args[0], 444)
        Instructor.__init__(self, args[1])
        # super().__init__(name) if we have 2 classes that get implementet then we cant use the super(). method to call the parent class. but instead define what parent class we are calling instead.
