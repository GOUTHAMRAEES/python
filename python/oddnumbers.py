def oddnumbers():
	a=[]
	for i in range(1000):
		if i%2==1:
			a.append(i)
	return a

print(oddnumbers())
