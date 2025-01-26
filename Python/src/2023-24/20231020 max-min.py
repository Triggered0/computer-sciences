# Copyright © 2023 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
<<<<<<< HEAD
# Free for personal or classroom use; see 'LICENSE.md' for details.
=======
# Free under certain conditions — see the license for details.
>>>>>>> 89fb55792fc0bb2c474d460a143d13ae9b20111d

max_ = None
min_ = None
user = input("Number (enter to exit): ")
while user:
    number = int(user)
    if max_ is None or number > max_:
        max_ = number
    if min_ is None or number < min_:
        min_ = number
    user = input("Number (enter to exit): ")

print(f"Minimum: {min_}, maximum: {max_}")
