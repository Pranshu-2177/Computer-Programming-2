def display(s):
    i=0
    print("Forward Order: ")
    while i<len(s):
        print(s[i],end=' ')
        i+=1
    print("\n Reverse Order: ")
    i=len(s)-1
    while i>=0:
        print(s[i],end=" ")
        i-=1
s=input("Enter String: ")
display(s)
