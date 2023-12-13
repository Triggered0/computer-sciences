from random import randint

pile = []
total = 0
pile_amount = randint(1, 45)

while total != 45:
    for i in range(pile_amount):
        rand = randint(0, 45 - total)
        total += rand
        if rand != 0:
            pile.append(rand)

print_pile = [str(x) for x in pile]
print(f"Initial Pile: {" - ".join(print_pile)}")

while pile != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    for i in range(len(pile)):
        pile[i] = pile[i] - 1
    pile.append(len(pile))
    pile = [x for x in pile if x > 0]

    print_pile = [str(x) for x in pile]
    print(f'New pile: {" - ".join(print_pile)}')
