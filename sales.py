def sales():

    gross = int(input("Gross sales: "))

    netsales = gross - (gross*0.1)

    print("Net sales: ", netsales)

sales()