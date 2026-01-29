def string(s):
    print("First Character: ",s[0])
    print("Last Character: ",s[-1])
    if len(s)%2!=0:
        print("Middle Character: ",s[len(s)//2])
    else:
        print("No Single Middle Character")
s=input("Enter String ")
string(s)
