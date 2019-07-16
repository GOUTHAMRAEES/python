class Account:
    def __init__(self,id):
        self.__id=id
        self.__balance=None
    
    def openBalance(self,amount):
        if amount>=10000:
            self.__balance=amount
        else:
            print("pay with 10000 as min balance")

    def deposit(self):
        amt=0
        cur=int(input("Enter the Multiple amount of 50 to be depsoited"))
        amt=amt+(cur*50)
        cur=int(input("Enter the Multiple amount of 100 to be depsoited"))
        amt=amt+(cur*100)
        cur=int(input("Enter the Multiple amount of 200 to be depsoited"))
        amt=amt+(cur*200)
        cur=int(input("Enter the Multiple amount of 500 to be depsoited"))
        amt=amt+(cur*500)
        cur=int(input("Enter the Multiple amount of 1000 to be depsoited"))
        amt=amt+(cur*1000)
        self.__balance=self.__balance+amt

    def withdraw(self,amt):
        if amt < self.__balance and self.__balance-amt > 5000:
            print("ENter the number of 100 200 5000 1000 notes as your preference order")
            a=[]
            for i in range(4):
                a.append(int(input()))
            cash=a[0]*100+a[1]*200+a[2]*500+a[3]*1000
            if cash == amt:
                print("Ammount withdrawed")0
                self.__balance=self.__balance-cash
            else:
                self.withdraw(amt)

    def checkBalance(self):
        return self.__balance


a=Account(1)
a.openBalance(10000)
a.deposit()
print(a.checkBalance())
a.withdraw(1000)
print(a.checkBalance())
