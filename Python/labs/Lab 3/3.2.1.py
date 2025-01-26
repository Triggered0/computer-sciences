import random


def check(x):
    y = False

    while not y:
        try:
            x = int(x)
            y = True
        except:
            x = input("Wrong input. Select again\n")
    return x


marbles = random.randint(10, 100)
player = random.randint(0, 1)
smart = random.randint(0, 1)
power2 = [1, 3, 7, 15, 31, 63]

print(f"Marbles: {marbles}")

while True:
    if marbles == 1:
        print("Computer wins") if player == 1 else print("Human wins")
        break

    if player == 0:
        player = 1

        if smart == 0:
            select = random.randint(1, int(marbles / 2))
            marbles = marbles - select
            print(f"[DUMB] Computer took: {select} marbles... {marbles} left")
        else:
            for i in range(1, 100):
                if marbles - i in power2:
                    marbles = marbles - i
                    print(f"[SMART] Computer took: {i} marbles... {marbles} left")
                    break
    else:
        player = 0

        x = input(f"How many marbles do you want to take? 1 - {marbles // 2}\n")
        x = check(x)

        while x > marbles / 2:
            x = input("Wrong input. Select again\n")
            x = check(x)

        marbles = marbles - x
        print(f"You took: {x} marbles... {marbles} left")
