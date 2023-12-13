x = int(input("Write a 5 digit number: "))

if x > 99999 or x < 10000:
    print("Wrong input")
else:
    print("\n".join([*str(x)]))