class Foo:
    pole = 3

    def __init__(self):
        self.__a = 5

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self,value):
        if value < 0:
            self.__a = 0
        else:
            self.__a = value

    #a = property(get_a,set_a)