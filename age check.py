def age():
    while True:
        age = int(input("Enter age."))
        if age >= 0 and age <= 130:
            print("Valid age input.")
            break
        else:
            print("Invalid age input, try again.")
            


print (age())
