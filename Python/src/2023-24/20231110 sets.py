# Copyright © 2023 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
<<<<<<< HEAD
# Free for personal or classroom use; see 'LICENSE.md' for details.
=======
# Free under certain conditions — see the license for details.
>>>>>>> 89fb55792fc0bb2c474d460a143d13ae9b20111d

from pprint import pprint

data = set()
data.add("giovanni")
data.add("furkan")
data.add("paola")
data.add("giovanni")
data.add("luca")
data.add("alvi")
data.add("iris")
data.add("muhammadmahdi")

pprint(data)
print()
data = data - {'giovanni'}
pprint(data)
print()
data = data - {'giovanni'}
pprint(data)
print()
