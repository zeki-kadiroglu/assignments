n = int(input("enter number : "))

over_num = set()

for i in range(2,n):
	for j in range(2,i):
		if i % j == 0 :
			over_num.add(i)

n = set(range(3,n))
prime_number = filter(lambda x: True if x  not in  over_num  else False ,n)
print(list(prime_number))