class TestClass:
    def prt(self):
        print(self)
        print(self.__class__)

t = TestClass()
t.prt()

