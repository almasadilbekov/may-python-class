while True:
    age=int(input("Enter your age: "))
    if age > 0 and age >= 18: 
        print("access denied")  
    elif age >= 13 and age < 18: 
        print("call your parents")
    elif age >=18:
        print("access granted")
    else:
        print("try again")