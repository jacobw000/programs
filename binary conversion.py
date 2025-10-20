def toBinary(num, strbinary):
    
    # Make an array to store binary string in
    strbinary = []
    
    # While number still has a positive value inside, keep lopping
    while num != 0:

        # If num divisible by 2, add a 1 to strbinary. Else, add a 0.
        if num % 2 == 0:
            strbinary.insert(0, "0")
            
        else:
            strbinary.insert (0, "1")
            

        # Change num value to prevent infinite looping
        num = num // 2
        
    print (strbinary)
    
strbinary = ("")
num = int(input(""))
(toBinary(num,strbinary))

