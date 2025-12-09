def linSe():
    # 10 item list for search
    nlist = [1,2,3,4,5,6,7,67,670,6767]
    
    # Search term
    term = int(input("Enter search term."))
    
    # Gets list length
    length = len(nlist)
    
    # Initialise to stop search later
    found = False

    # For length of list, compare term to the current item. If found, found becomes true and the index position is stored in pos
    for x in range(0,length):
        if nlist[x] == term:
           found = True
           pos = x

    # Output item position if found
    if found == True:
        print(f"Item found in position:{pos+1}")
    # Output item not found if item not found
    else:
        print("Item not found.")



def binSe():
     # 10 item Llst for search
    nlist = [1,2,3,4,5,6,7,67,670,6767]
    
    # Search term
    term = int(input("Enter search term."))

    # Gets list length
    length = len(nlist)

    # Initialise to stop search later
    found = False

    # High pointer
    low = 0
    # Low pointer
    high = length

    while found == False and high > 0:
        
        # Mid pointer
        mid = (high - low)//2
        
        # If mid pointer is term, end code
        if nlist[mid] == term:
            found = True
           
            

        # If mid pointer is larger, search lower half of list
        elif nlist[mid] > term:
            high = nlist[mid]
            
                

        # If mid pointer is lower, search upper half of list
        elif nlist[mid] < term:
            low = nlist[mid]
            
            
        if found == True:
            print("Found.")
        else:
            print("Not found.")

    # THIS CODE IS BROKEN
    # i am very smart



def bubSort():
    # Code for generating list. Not part of actual sort.
    import random
    nlist = []
    listlen = int(input("Enter list length"))
    for x in range(0,listlen):
        temp = random.randint(0,100)
        nlist.append(temp)
    print(nlist)


    swap = True
    index = 1
    temp = 0
    
    while swap == True:
        for x in range(len(nlist)):
            if nlist[index] > nlist[index+1]:
                temp = nlist[index]
                nlist[index] = nlist[index+1]
                nlist[index] = temp
                swap == True
                print(nlist)
            else:
                index = index + 1
    swap == False
    print(nlist)
            
             
            
            
            
        






























