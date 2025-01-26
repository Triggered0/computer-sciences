# Copyright © 2023 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
<<<<<<< HEAD
# Free for personal or classroom use; see 'LICENSE.md' for details.
=======
# Free under certain conditions — see the license for details.
>>>>>>> 89fb55792fc0bb2c474d460a143d13ae9b20111d

f0 = 1
f1 = 1
print(f"{f0}\n{f1}")
while f1 < 10_000_000_000_000_000_000:
    f2 = f0 + f1
    print(f"{f2:,}")
    f0 = f1
    f1 = f2

print("\\")