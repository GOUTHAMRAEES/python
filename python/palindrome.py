a=input("Enter the string")
b=""
for i in range(len(a)-1,-1,-1):
    b=b+a[i]

if(b==a):
    print("it is palindrome")
else:
    print("Not a palindrome")
    
