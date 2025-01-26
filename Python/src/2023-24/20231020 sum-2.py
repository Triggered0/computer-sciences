# Copyright © 2023 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
<<<<<<< HEAD
# Free for personal or classroom use; see 'LICENSE.md' for details.
=======
# Free under certain conditions — see the license for details.
>>>>>>> 89fb55792fc0bb2c474d460a143d13ae9b20111d

NUMBER = 1732817328

number = str(NUMBER)
total = 0
for digit in number:
    total = total + int(digit)
    # alternative: total = total + ord(digit) - ord("0")

print(f"The sum of all digits of {NUMBER} is {total}")
