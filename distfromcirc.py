def distfromcirc():
    
    import math

    x = float(input("Enter x-coordinate of circle center: "))
    y = float(input("Enter y-coordinate of circle center: "))
    r = float(input("Enter radius of the circle: "))


    x1 = float(input("Enter x-coordinate of the point: "))
    y1 = float(input("Enter y-coordinate of the point: "))


    distance = math.sqrt(math.pow(x1-x,2)+math.pow(y1-y,2))


    if distance < r:
        print("Point lies inside the circle")
    elif distance == r:
        print("Point lies on the circle")
    else:
        print("Point lies outside the circle")

distfromcirc()
