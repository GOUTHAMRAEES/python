class A:
    def m1(self):
        print("m1 method")
    
    def m2(self):
        print("m2 method")

class B(A):         #inheritance if it inherites two or more classes means use (ClassName ,ClassName,..........)
    def m3(self):
        print("m3 method")
    
    def m4(self):
        print("m4 method")


a=A() #m1,m2
b=B() #m3,m4 if it is not inherited
b.m1() #because it is inherited