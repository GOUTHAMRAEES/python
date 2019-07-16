class A:
    def m1(self):
        print("SS")

class B(A):
    def m2(self):
        print("m1")

class C(A):
    def m3(self):
        print("m2")

class D(B,C):
    def m4(self):
        print("m3")
    

c=D()
c.m4()