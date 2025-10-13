import intList
import statistics
numlist = []
count = 0
while count < 6:
    x = int(input("Enter number."))
    intList.integerinput(x,numlist)
    count = count + 1
    
print("Largest number: ",max(numlist))
print("Smallest number: ",min(numlist))
print(statistics.fmean(numlist)) 
