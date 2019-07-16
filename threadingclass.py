from threading import Thread
import time

class A(Thread):
    def run(self):
        for i in range(1,3):
            print("t1")
            time.sleep(2)

class B(Thread):
    def run(self):
        for i in range(1,3):
            print("t2")
            time.sleep(2)

a=A()
b=B()
a.start()
b.start()
a.join()
b.join()
