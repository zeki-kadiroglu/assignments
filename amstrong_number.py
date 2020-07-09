number = input("enter positive integer : ")
list = list(number)
amstrong = 0
total = []
for i in number :
    amstrong = int(i) ** len(list)
    i += i
    total.append(amstrong)
if sum(total) == int(number):
    print(number," : is amstrong number")
else:
    print(number, ": is not amstrong number")