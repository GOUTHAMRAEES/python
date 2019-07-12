import random
name=str(input("Enter your name: "))
print("Hello {} , I am thinking of a number between 1 and 10".format(name))
a=random.randint(1,10)
for i in range(1,6):
    guess=int(input("Take a guess: "))
    if a<guess:
        print("Your guess is high")
    elif a>guess:
        print("Your guess is low")
    else:
        print("You Win")
