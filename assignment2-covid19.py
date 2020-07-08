age = int(input("age : ")).title()
cigarette = True
chronic = input("chronic : ").title()
immune = input("is your immune system too weak? : ").title()
if age > 75 and bool(cigarette) and chronic == "yes" and immune == "yes":
    print("You are in risky grup")
else :
    print("You are not  in risky grup")