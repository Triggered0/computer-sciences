/*  ######       /******************************************************\
|*  #######      * CLASS EXAMPLE FOR "COMPUTER SCIENCES" (04JCJ**)      *
|*  ####   \     * https://github.com/squillero/computer-sciences       *
|*   ###G  c\    *                                                      *
|*   ##     _\   * Copyright © Giovanni Squillero <squillero@polito.it> *
|*   |    _/     * Licensed under the EUPL-1.2 <https://eupl.eu/>       *
\*   |   _/      \******************************************************/

#include <stdio.h>
#include <stdlib.h>

#define MAX_DIGIT 12

int main()
{
    int binary[MAX_DIGIT];
    printf("Insert number (%d digits): ", MAX_DIGIT);
    for (int d = 0; d < MAX_DIGIT; ++d)
    {
        scanf("%d", &binary[d]);
    }

    int value = 0;
    for (int d = 0; d < MAX_DIGIT; ++d)
    {
        value = value * 2 + binary[d];
    }
    printf("Value: %d\n", value);

    return 0;
}
