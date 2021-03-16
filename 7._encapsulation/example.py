class P:
    def __init__(self, x):
        self.x = x  # public variable  --> becomes a property when the next is called

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x > 1000:
            self.__x = 1000
        elif x < 0:
            self.__x = 0
        else:
            self.__x = x


# This two mothods is a way to use the toString() function in python.

    def __str__(self):
        return self.x

    def __repr__(self):
        return f'{self.__dict__}'
