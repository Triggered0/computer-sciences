# Copyright © 2022 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
<<<<<<< HEAD
# Free for personal or classroom use; see 'LICENSE.md' for details.
=======
# Free under certain conditions — see the license for details.
>>>>>>> 89fb55792fc0bb2c474d460a143d13ae9b20111d

size = int(input("Size: "))

for n in range(1, size+1):
    print(" "*(size-n), "#"*n, "#"*(n-1), sep='')
for n in range(1, size+1):
    print(" "*n, "#"*(size-n), "#"*(size-n-1), sep='')

