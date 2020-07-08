age = int(input("age : "))
cigarette = True
chronic = input("chronic : ")
immune = input("is your immune system too weak? : ")
if age > 75 and bool(cigarette) and chronic == "yes" and immune == "yes":
    print("You are in risky grup")
else :
    print("You are not  in risky grup")