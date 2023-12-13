x = int(input("Number: "))
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

print(prime)
