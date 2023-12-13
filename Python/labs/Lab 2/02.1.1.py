x = int(input("First number: "))
y = int(input("Second number: "))
str = f"""Sum: {x + y}
Difference: {x - y}
Product: {x * y}
Average: {(x + y) / 2}
Distance: {abs(x - y)}
Maximum: {max(x, y)}
Minimum: {min(x, y)}"""
print(str)