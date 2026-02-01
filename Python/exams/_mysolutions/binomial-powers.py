def read_file(file):
    try:
        with open(file) as f:
            return f.read()
    except OSError as e:
        exit(f"ERROR!!! {e}")


def pascalTriangle(n: int):
    triangle = [[1]]

    for i in range(n):
        last = triangle[len(triangle) - 1]
        arr = [1]

        for j in range(len(last) - 1):
            arr.append(last[j]+last[j+1])

        arr.append(1)
        triangle.append(arr)
    return triangle


def main():
    data = read_file("powers.txt").splitlines()
    a, b = [float(x) for x in data[0].split()]
    powers = data[1:]

    print(f"Powers of ({a}x {"+"if b > 0 else "-"} {abs(b)}y)^N")
    for power in powers:
        print(f"N = {power}")
        power = int(power)
        triangle = pascalTriangle(power)[power]
        arr = []
        for i in range(power+1):
            coeff = triangle[i] * (a ** (power - i)) * (b ** i)
            arr.append(
                f"{"+ "if coeff > 0 else "- "}{abs(coeff)}{f" x^{power-i}" if power-i != 0 else ""}{f" y^{i}" if i != 0 else ""}")
        print(" ".join(arr))


if __name__ == "__main__":
    main()
