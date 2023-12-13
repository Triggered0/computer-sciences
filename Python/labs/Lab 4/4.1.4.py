def balance(year, balance, rate):
    return balance * (1 + (rate / 100)) ** year


print(f"{balance(30, 3_000_000, 5):.0f}")
