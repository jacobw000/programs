

def InsertSort(y,itemsI):
    import time

    # Timer start
    start = time.time()
    
    # Variable with length of list
    length = len(items)

    # Loop to check each data item starting with the second (1)
    for index in range (1, length):
        
        # Temporary variable created
        current = itemsI[index]

        # Stores index of previous data item for comparison to the next
        index2 = index

        # Ensures swap only happens if previous item in the list is greater than the one being stored in current
        while (index2 > 0 and itemsI [index2-1] > current):

            # Current data item is made the same as the previous
            itemsI[index2] = itemsI [index2-1]

            # Decreases index2 by 1 so the next loop points to the correct value
            index2 = index2 - 1
            
        # Puts current in index2
        itemsI[index2] = current

    # Ends the timer
    end = time.time()

    # Makes a variable with the time taken for the search
    speed = (end - start)
    # Outputs time taken
    print(f"Insertion sort time taken: {speed}")

    
    
def BubbleSort(y,itemsB):
    import time
    # Timer start
    start2 = time.time()
    # Initialise for loop later
    swapped = True

    # Variable with length of list
    length = len(items)-1

    # If a swap has happened, do a pass
    while (swapped) and length > 0:

        swapped = False

        for index in range(0, length):

            # If first item is larger than second, swap
            if (itemsB[index] > itemsB[index+1]):
                
                num = itemsB[index]
                itemsB[index] = itemsB[index+1]
                itemsB[index+1] = num

                # Tells the code that a swap did happen, and another one will need to
                swapped = True
        length = length - 1
     
    # Ends the timer
    end2 = time.time()

    # Makes a variable with the time taken for the search
    speed2 = (end2 - start2)
    # Output time taken
    print(f"Bubble sort time taken: {speed2}")

    
# Decides list length
import random
y = int(input("Enter list length."))

# Generates a list of 0-100 numbers with y data items 
items = [random.randint(0,100) for x in range(y)]
length = len(items)-1

# Makes sure each search goes through the same list, but a different variable of each list so it's not searching through a completed list
itemsB = items.copy()
itemsI = items.copy()
InsertSort(y,itemsI)
BubbleSort(y,itemsB)



