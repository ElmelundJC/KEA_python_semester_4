class Car:

    def __init__(self, make, model, bhp, mph):
        self.make = make
        self.model = model
        self.bhp = bhp
        self.mph = mph

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, make):
        self.__make = make

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def bhp(self):
        return self.bhp

    @bhp.setter
    def bhp(self, bhp):
        self.__bhp = bhp

    @property
    def mph(self):
        return self.mph

    @mph.setter
    def mph(self, mph):
        self.__mph = mph
