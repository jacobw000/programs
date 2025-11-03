# List of numbers to search through
myList = [1, 3, 6, 7, 41, 218, 1096, 2043]

# Variable created to be checked if number is in list later on
found = False

# Asks for the number to search for
search = int(input("Enter the number you are searching for."))

# Loop through each item in the list
for x in range(len(myList)):

    # Checks if the item is the number that is being searched for
    if (search == myList[x]):
        
        found = True


# Check if the number is in the list or not and give an output

if (found == True):

    print ("Found number.")

else:

    print ("Not found number.")
        
