import random
D100 = range (1, 100)
roll = input("Type 'roll' to roll the dice:")
if roll == "roll":
    print(random.choice(D100))