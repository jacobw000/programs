

def cointoss():
    import random
    coins = 0
    heads = 0
    tails = 0
    result = 0
    while coins <= 1000:
        result = random.randint(1,2)
        if result == 1:
            heads = heads + 1
            coins = coins + 1
            print(heads, "heads.")
        else:
            tails = tails + 1
            coins = coins + 1
            print(tails, "tails.")
      
