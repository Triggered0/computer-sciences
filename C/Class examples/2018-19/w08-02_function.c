/*  ######       /******************************************************\
|*  #######      * CLASS EXAMPLE FOR "COMPUTER SCIENCES" (04JCJ**)      *
|*  ####   \     * https://github.com/squillero/computer-science        *
|*   ###G  c\    *                                                      *
|*   ##     _\   * Copyright © Giovanni Squillero <squillero@polito.it> *
|*   |    _/     * Licensed under the EUPL-1.2 <https://eupl.eu/>       *
\*   |   _/      \******************************************************/

#include <stdio.h>
#include <stdlib.h>

int mario(int first, int second)
{
    int sum = first + second;
    return sum;

    printf("This line is never executed!\n");
}

int main()
{
    printf("Hello function world!\n");

    int first = 20;
    int x = 22;
    int z = mario(x, first);
    printf("The answer is %d\n", z);
    mario(z, z);

    return 0;
}