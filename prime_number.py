prime_number = int(input("enter number : "))

for i in range(2,prime_number):
    if prime_number % i == 0:

        print("number is not a prime number")
        break
    else:

        print("number is a prime number")
        break
