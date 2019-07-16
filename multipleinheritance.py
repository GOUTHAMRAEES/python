class A:
    def m1(self):
        print("m1")

class B:
    def m1(self):
        print("m2")

class C(A,B):
    def m3(self):
        print("m3")
    


c=C()
c.m1()
print(issubclass(C,B))
