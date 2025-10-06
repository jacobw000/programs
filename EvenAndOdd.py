numberlist = [25, 54, 60, 12, 11, 15, 22]
def EvenAndOdd():
    even = 0
    odd = 0
    for x in numberlist:
        if (x % 2 == 1):
            odd = odd + 1
        else:
            even = even + 1
    print(odd, "odd numbers.")
    print(even, "even numbers.")

EvenAndOdd()
        
    
    
