class Car:
    howManyCars = 0 # pole klasy w innych językach programowania można powiedzieć że jest to statyczna zmienna

    def __init__(self, brand):
        self.brand = brand
        # howManyCars nie możemy odwołać się do howManyCars

    @classmethod
    def addCar(cls):
        cls.howManyCars +=1



