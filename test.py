import time

class a:
    def a(self):
        print("a")
class b(a):
    def a(self):
        print("b")
a_ = [0,1]
b__ = a_.copy()
b__[0] = 2
print(a_)