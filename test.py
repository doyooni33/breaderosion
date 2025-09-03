import time

class a:
    def a(self):
        print("a")
class b(a):
    def a(self):
        print("b")
a_ = a()
b__ = b()
b_ = 1
if type(a_) == type(b__) :
    print("a==b")