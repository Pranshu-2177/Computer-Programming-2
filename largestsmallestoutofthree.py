def largestsmallestoutofthree():

    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    if(a>b and b>c):
        print("a is largest and c is smallest")
    elif(b>a and a>c):
        print("b is largest and c is smallest")
    elif(c>a and a>b):
        print("c is largest and b is smallest")
    elif(b>c and c>a):
        print("b is largest and a is smallest")
    else:
        print("c is largest and a is smallest")

largestsmallestoutofthree()
        
    
