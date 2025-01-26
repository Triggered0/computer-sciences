# Copyright © 2022 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
<<<<<<< HEAD
# Free for personal or classroom use; see 'LICENSE.md' for details.
=======
# Free under certain conditions — see the license for details.
>>>>>>> 89fb55792fc0bb2c474d460a143d13ae9b20111d

from random import choice

dna = str.join("", [choice(list("ACTG")) for _ in range(10_000_000)])
gene = str.join("", [choice(list("ACTG")) for _ in range(10)])

#print(dna)
print(f"Looking for: {gene}")

slice_size = len(gene)
num_found = 0
for x in range(len(dna) - slice_size + 1):
    if dna[x:x + slice_size] == gene:
        num_found = num_found + 1
        print(f"Whoa! Found at position {x:,}")
print(f"Gene [{gene}] found {num_found:,} times")
