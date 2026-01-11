def salary():

    gross = int(input("Gross salary: "))

    allowance = gross * 0.1

    deduction = gross * 0.03

    netsalary = gross + allowance - deduction

    print("Netsalary: ", netsalary)

salary()