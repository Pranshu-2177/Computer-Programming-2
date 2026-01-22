def threepointsonsameline():

    x1 = int(input("x1: "))
    x2 = int(input("x2: "))
    x3 = int(input("x3: "))
    y1 = int(input("y1: "))
    y2 = int(input("y2: "))
    y3 = int(input("y3: "))

    if((y2-y1)/(x2-x1) ==  0 and (y3-y2)/(x3-x2)):
        print("They lie on same line")
    else:
        print("They do not line on smae line")

threepointsonsameline()
        
    
