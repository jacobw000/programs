import random

def uppercase():
    uppercase = random.randint(65,90)
    uppercase = chr(uppercase)
    return uppercase

def lowercase():
    lowercase = random.randint(97,122)
    lowercase = chr(lowercase)
    return lowercase

def digit():
    digit = random.randint(48,57)
    digit = chr(digit)
    return digit
    
def symbol():
    symbol = random.randint(33,47)
    symbol = chr(symbol)
    return symbol
    
def length():
    
    length = False
    while length == False:
        passLength = int(input("Enter desired password length 8-25."))
        if (passLength >= 8) and  (passLength<= 25):
            length = True
    return passLength
            
def passgen():
    password = ""
    passLength = length()
    
    for x in range (passLength):
        rand = random.randint(1,4)
        if rand == 1:
            password =  password + (uppercase())
        elif rand == 2:
                password =  password + (lowercase())
        elif rand == 3:
                password =  password + (digit())
        elif rand == 4:
                password =  password + (symbol())
    print(password)


if __name__ == "__main__":
    passgen()
