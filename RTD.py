def roll():
    import random
    diceOne = random.randint(1,6)
    diceTwo = random.randint(1,6)
    while diceOne != diceTwo:
        print("Dice one:",diceOne,"\nDice two:",diceTwo,"\n")
        diceOne = random.randint(1,6)
        diceTwo = random.randint(1,6)
    print ("Dice one:",diceOne,"\nDice two:",diceTwo,"\nYou Win!")


