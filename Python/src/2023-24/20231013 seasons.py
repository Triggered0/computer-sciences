# Copyright © 2023 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
<<<<<<< HEAD
# Free for personal or classroom use; see 'LICENSE.md' for details.
=======
# Free under certain conditions — see the license for details.
>>>>>>> 89fb55792fc0bb2c474d460a143d13ae9b20111d

month = int(input("Date (month): "))
day = int(input("Date (day): "))

if 1 <= month <= 3:
    season = "winter"
    if month % 3 == 0 and day >= 21:
        season = "spring"
elif month <= 6:
    season = "spring"
    if month % 3 == 0 and day >= 21:
        season = "summer"
elif month <= 9:
    season = "summer"
    if month % 3 == 0 and day >= 21:
        season = "autumn"
else:
    season = "autumn"
    if month % 3 == 0 and day >= 21:
        season = "winter"

print(season)
