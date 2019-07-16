class A:
    name="A"
    def m1(self):
        print("SS")
    
    @classmethod
    def disp(cls):
        print("Display")

class B(A):
    def m2(self):
        print("m1")

class C(A):
    def m3(self):
        print("m2")

class D(A):
    name="D"
    def m4(self):
        print("m2")

d=D()
d.m1()
d.disp()
