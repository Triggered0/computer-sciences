x = int(input("Number: "))


def isprime(x):
    prime = False

    if x <= 1:
        prime = False
    elif x == 2:
        prime = True
    else:
        for i in range(2, x):
            if x % i == 0:
                prime = False
                break
            else:
                prime = True
    return prime


for i in range(0, x):
    if isprime(i):
        print(i)
