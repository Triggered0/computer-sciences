# Copyright © 2022 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
<<<<<<< HEAD
# Free for personal or classroom use; see 'LICENSE.md' for details.
=======
# Free under certain conditions — see the license for details.
>>>>>>> 89fb55792fc0bb2c474d460a143d13ae9b20111d

seconds = 23_456_675_987

years = seconds // (365 * 24 * 60 * 60)

seconds_tmp = seconds % (365 * 24 * 60 * 60)
months = seconds_tmp // (30 * 24 * 60 * 60)

seconds_tmp = seconds_tmp % (30 * 24 * 60 * 60)
days = seconds_tmp // (24 * 60 * 60)

seconds_tmp = seconds_tmp % (24 * 60 * 60)
hours = seconds_tmp // (60 * 60)

seconds_tmp = seconds_tmp % (60 * 60)
minutes = seconds_tmp // 60

seconds_tmp = seconds_tmp % 60

print(years, months, days, hours, minutes, seconds_tmp)
