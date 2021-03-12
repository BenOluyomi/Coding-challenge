def multiples():
    y = 7
    z = 8
    c = 9
    print("The following are multiples of 7 up to 100")
    for x in range (7,100):
        if x%y == 0:
            print(x)
    print("The following are multiples of 8 up to 200")
    for x in range (8,200):
        if x%y == 0:
            print(x)
    print("The following are multiples of 9 up to 300")
    for x in range (9,300):
        if x%y == 0:
            print(x)



multiples()