# Copyright © 2023 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
<<<<<<< HEAD
# Free for personal or classroom use; see 'LICENSE.md' for details.
=======
# Free under certain conditions — see the license for details.
>>>>>>> 89fb55792fc0bb2c474d460a143d13ae9b20111d

data = list("Giovanni Adolfo Pietro Pio")
print(data)

for index in range(
    0, len(data), 2
):  # Yeuch! Terrible but understandable
    print(index, data[index])

for index, element in enumerate(data):  # YES!
    if index % 2 == 0:
        print(index, element)
