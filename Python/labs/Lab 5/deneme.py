from random import randint

pile = []
cards = 45
div = randint(1, 9)
step = 0
print(f"the cards will be divided into {div} piles")
for x in range(div):
    a = randint(1, 9)
    pile.append(a)
for x in range(div):
    while sum(pile) < 45:
        pile[x] += 1
pile = sorted(pile)
print(f"the initial sizes of the piles are {pile}")
for x in range(div):
    a = x + 1
    while pile[x] > a:
        pile[x] = pile[x] - 1
        step += 1
        print(f"step {step}: {pile}")
    if pile[x] == a:
        continue
