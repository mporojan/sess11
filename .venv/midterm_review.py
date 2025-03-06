
def multiple_of_6():
    while True:
        try:
            number = input("Please give me a multiple of 6: ")
            n = int(n)
            if n % 6 == 0:
                return n
            else:
                print("That is not a multiple of 6")
        except ValueError:
            print("That is not a valid number")


multiple_of_6()