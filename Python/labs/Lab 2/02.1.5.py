from math import pi

q1 = int(input("First charge: "))
q2 = int(input("Second charge: "))
r = int(input("Distance: "))
print(f"Force = {(q1*q2)/(4 * pi * 8.854 * (10**-12) * (r**2))}")
