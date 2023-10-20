# Copyright © 2023 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
# Free for personal or classroom use; see 'LICENSE.md' for details.

total = 0

user = ""  # Whatever, but not 'end'
count = 0
while user != "end":
    user = input("Number ('end' to exit): ")
    if user != "end":
        count = count + 1
        number = int(user)
        total = total + number

if count > 0:
    print(f"Average is: {total/count:.2f}")
else:
    print("D'ho!?")
