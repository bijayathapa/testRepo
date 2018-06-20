import random
for i in range (10):
	x = random.randint(1,100)
	#print(x)

	ratings[x] = input("Enter rating for book {}:".format(x))

for i in range(10):
	print(ratings)