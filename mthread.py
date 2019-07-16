import threading;
import time
def cubes():
    """for i in range(1,10):
        print("t1" )
        time.sleep(5)
    """
    pass
def squares():
    """for i in range(1,10):
        print("t2" )
        time.sleep(2)
    """
    pass
if __name__=="__main__":
    t1=threading.Thread(target=cubes,args=())
    t2=threading.Thread(target=squares,args=())
    t1.start()
    t2.start()
print(t1.getName())
print(t2.getName())
t1.setName('t1')
t2.setName('t2')
print(t1.getName())
print(t2.getName())
print(threading.activeCount())
print(t1.is_alive())
print(t2.is_alive())