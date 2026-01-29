s = input("Enter a String\n")

def upper(s):
    result = ""
    for i in s:
        if 'a' <= i <= 'z':
            result += chr(ord('A') + (ord(i) - ord('a')))
        else:
            result += i
    print("Uppercase :", result)

upper(s)

def lower(s):
    result = ""
    for i in s:
        if 'A' <= i <= 'Z':
            result += chr(ord('a') + (ord(i) - ord('A')))
        else:
            result += i
    print("Lowercase: ", result)

lower(s)

def toggle(s):
    result = ""
    for i in s:
        if 'a' <= i <= 'z':
            result += chr(ord('A') + (ord(i) - ord('a')))
        else:
            result += chr(ord('a') + (ord(i) - ord('A')))
    print("Togglecase: ", result)

toggle(s)
