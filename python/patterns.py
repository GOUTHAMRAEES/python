for i in range(5,0,-1):
	print()
	for j in range(i):
		print('*',end='')



print()



for i in range(1,7):
	print()
	for k in range(7-i):
			print(end=' ')
	for j in range(i):
		print('*',end=' ')



print()


mov=["The Holy Grail","The Life of Brain","The Meaning of Life"]
year=[1975,1979,1983]
lst1=[]
for i in range(len(mov)):
	lst1.append(mov[i])
	lst1.append(year[i])


print()




cprice=int(input(" Enter the cover price: "))
dis=int(input("Enter discount percentage: "))
num=int(input("Enter the number of copies: "))
ship=int(input("Enter the shipping price: "))
addico=int(input("Enter the shipping price for additional copies: "))
price=cprice*(1-(dis/100))
tot=(price*num) + (addico*(num-1)) + ship
print("The total wholesale price is {}".format(tot))
print()













lst1=[10,['user1','user2'],10.25,('test1','test2'),True,None]
lst2=[]
for i in lst1:
	if type(i)== list or type(i)==tuple:
		for j in i:
			lst2.append(j)
	else:
		lst2.append(i)

print(lst1)
print(lst2)

