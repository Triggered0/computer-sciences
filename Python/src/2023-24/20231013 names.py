# Copyright © 2023 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
<<<<<<< HEAD
# Free for personal or classroom use; see 'LICENSE.md' for details.
=======
# Free under certain conditions — see the license for details.
>>>>>>> 89fb55792fc0bb2c474d460a143d13ae9b20111d

name = input("Name: ")

if len(name) > 20:
    print("Whoa! A LONG name...")

length = len(name)
print(name[length-1])
if name[length-1] == 'a':
    print("Ms.", name)
else:
    print("Mr.", name)
    