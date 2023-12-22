def pascalTriangle(n):
    
    lPascalTriangle = [[1]] # First row
    
    for i in range(n): # Build the next n rows
        
        l = [1] # The new row starts with 1
        
        for j in range(len(lPascalTriangle[-1])-1): 
            l.append(lPascalTriangle[-1][j]+lPascalTriangle[-1][j+1]) # Each inner element of the row is the sum of two consecutive elements of the previous row
            
        l.append(1) # The last element of the row is also 1
        
        lPascalTriangle.append(l)
        
    return lPascalTriangle

# Given a and b, return the list of coefficients for the polynomial terms. The first element corresponds to the coefficient of x^n, the last element to the coefficient of y^n
def computeCoefficients(a, b, n):

    tartRow = pascalTriangle(n)[n]
    lCoeff = []

    for yPow in range(n+1):
        xPow = n - yPow
        coeff = tartRow[xPow]*a**xPow*b**yPow
        lCoeff.append(coeff)
    return lCoeff

# Given the list of coefficients of the polynomial terms, print the polynomial with the required format
def printPolyFromCoefficiens(lCoeff):

    n = len(lCoeff) - 1

    for yPow in range(n+1):
        xPow = n - yPow
        coeff = lCoeff[yPow]
        if yPow == 0 and coeff >= 0:
            print(coeff, end = " ")
        elif yPow == 0 or coeff < 0:
            print ("-", abs(coeff), end = " ")
        else:
            print("+", coeff, end = " ")
            
        if xPow > 1:
            print('x^%d' % xPow, end = " ")
        elif xPow == 1:
            print('x', end = ' ')
        if yPow > 1:
            print('y^%d' % yPow, end = " ")
        elif yPow == 1:
            print('y', end = ' ')


    print()

def main():

    try:
        f = open("powers.txt", "r")
    except IOError:
        print("Cannot open file")
        raise

    coefficients = f.readline().strip().split()
    a = float(coefficients[0])
    b = float(coefficients[1])

    header = "Powers of ("
    header = header + str(a)
    header = header + "x"
    if b >=0 :
        header = header + " + " + str(b)
    else:
        header = header + " - " + str(abs(b))
    header = header + "y)^N"
    print(header)

    for line in f:
            n = int(line)
            lCoeff = computeCoefficients(a, b, n)
            print("N =", n)
            printPolyFromCoefficiens(lCoeff)

    f.close()

main()
