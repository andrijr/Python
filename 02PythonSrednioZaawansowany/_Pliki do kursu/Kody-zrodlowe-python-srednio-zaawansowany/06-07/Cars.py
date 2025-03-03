class Car:
    howManyCars = 0

    @classmethod
    def __init__(cls,self,brand):
        self.brand = brand
        cls.howManyCars += 1