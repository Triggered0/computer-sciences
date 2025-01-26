# Copyright © 2023 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
<<<<<<< HEAD
# Free for personal or classroom use; see 'LICENSE.md' for details.
=======
# Free under certain conditions — see the license for details.
>>>>>>> 89fb55792fc0bb2c474d460a143d13ae9b20111d

NUMBER = 1732817328

number = NUMBER
total = 0
while number > 0:
    # print(f"Number: {number}")
    digit = number % 10
    # print(f"Last digit: {digit}")
    number = number // 10
    total = total + digit

print(f"The sum of all digits of {NUMBER} is {total}")