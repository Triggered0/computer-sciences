# Copyright © 2022 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
<<<<<<< HEAD
# Free for personal or classroom use; see 'LICENSE.md' for details.
=======
# Free under certain conditions — see the license for details.
>>>>>>> 89fb55792fc0bb2c474d460a143d13ae9b20111d

num = int(input('Num: '))
max_ = num
min_ = num
cnt = 0
while num > 0:
    cnt += 1
    max_ = max(num, max_)
    min_ = min(num, min_)
    num = int(input('Num: '))
print(f"You eneterd {cnt:,} numbers between {min_:,} and {max_:,}")
