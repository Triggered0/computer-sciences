# Copyright © 2023 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
<<<<<<< HEAD
# Free for personal or classroom use; see 'LICENSE.md' for details.
=======
# Free under certain conditions — see the license for details.
>>>>>>> 89fb55792fc0bb2c474d460a143d13ae9b20111d


def is_prime(num):
    prime = True
    for n in range(2, num):
        if num % n == 0:
            prime = False
    return prime


def is_prime_while(num):
    prime = True
    n = 2
    while prime is True and n < num:
        if num % n == 0:
            prime = False
        else:
            n = n + 1
    return prime


def is_prime_break(num):
    prime = True
    for n in range(2, num):
        if num % n == 0:
            prime = False
            break   # adult only
    return prime


n = 26
print(is_prime(n))
print(is_prime_while(n))
