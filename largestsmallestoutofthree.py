def largestsmallestoutofthree():
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c

    if a <= b and a <= c:
        smallest = a
    elif b <= a and b <= c:
        smallest = b
    else:
        smallest = c

    print("Largest:", largest)
    print("Smallest:", smallest)

largestsmallestoutofthree()

        
    

