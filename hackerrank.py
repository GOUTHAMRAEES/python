x = [int(x) for x in input().split()] 
print("Number of list is: ", x)
b=[]
for i in range(x[0]):
    y = [int(y) for y in input().split()] 
    b.append(y)

sum=0
for i in b:
    sq=max(i)
    sq=sq**2
    sum=sum+sq

print(sum%x[1])