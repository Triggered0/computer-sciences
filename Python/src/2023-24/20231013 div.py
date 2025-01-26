# Copyright © 2023 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
<<<<<<< HEAD
# Free for personal or classroom use; see 'LICENSE.md' for details.
=======
# Free under certain conditions — see the license for details.
>>>>>>> 89fb55792fc0bb2c474d460a143d13ae9b20111d

num = int(input("Number :"))

n = 2
while num > 1:
    if num % n == 0:
        print(f"Can be divided by {n}")
        num = num // n
    else:
        n = n + 1
        