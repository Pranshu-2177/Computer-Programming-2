def interest():

    principle = int(input("Principle: "))
    rate = int(input("Rate: "))
    number = int(input("Number: "))

    intr = (principle*rate*number) / 100

    print("Interest: ", intr)

interest()