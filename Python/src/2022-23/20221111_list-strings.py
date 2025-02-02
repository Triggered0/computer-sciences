# Copyright © 2022 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
<<<<<<< HEAD
# Free for personal or classroom use; see 'LICENSE.md' for details.
=======
# Free under certain conditions — see the license for details.
>>>>>>> 89fb55792fc0bb2c474d460a143d13ae9b20111d


def main():
    monkeys = ['Alex Turner', 'Jamie Cook', 'Matt Helders', 'Nick O\'Malley']
    band = ''
    for member in monkeys[:-1]:
        band = band + member + ', '
    band = band + monkeys[-1]
    print(band)

    strokes = [
        'Julian Casablancas', 'Nikolai Fraiture', 'Albert Hammond Jr.', 'Fabrizio Moretti',
        'Nick Valensi'
    ]

    # use 'join' from str
    band = str.join(', ', strokes)
    print(band)

    # equivalent! oo-like
    band = ', '.join(strokes)
    print(band)


if __name__ == '__main__':
    main()
