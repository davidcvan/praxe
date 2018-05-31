import random as rn
konec = False

while konec != True:
    hrac = rn.randint(1, 3)
    print(hrac)
    dal = input("pokracovat ? ")

    if dal == "y":
        konec = False
    else:
        konec = True
