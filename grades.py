def get_grade(marks):
    if marks <= 39:
        return "F"
    elif marks <= 44:
        return "P"
    elif marks <= 49:
        return "C"
    elif marks <= 54:
        return "B"
    elif marks <= 59:
        return "B+"
    elif marks <= 69:
        return "A"
    elif marks <= 79:
        return "A+"
    else:
        return "O"

def grades():
    s1 = int(input("Marks of Subject1: "))
    s2 = int(input("Marks of Subject2: "))
    s3 = int(input("Marks of Subject3: "))

    total = s1 + s2 + s3
    avg = total / 3

    print("Total marks:", total)
    print("Average marks:", avg)

    if s1 <= 39 or s2 <= 39 or s3 <= 39:
        print("FAIL")
    else:
        print("PASS!!")

    print("Grade in Subject1:", get_grade(s1))
    print("Grade in Subject2:", get_grade(s2))
    print("Grade in Subject3:", get_grade(s3))

grades()
