

def passwordcheck():
    userC = "JohnSmith"
    passwC = "Password123!"
    attempts = 5
    while attempts != 0:
        user = input("Enter username.")
        passw = input("Enter password.")
        if user == userC and passw == passwC:
            print("Access allowed.")
            break
        else:
            attempts = attempts - 1
            print("Access denied,", attempts, "attempts left before lockout.")
            
    
passwordcheck()
