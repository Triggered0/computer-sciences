from math import pi


def sphere_volume(r):
    return (4 / 3) * pi * r**3


def sphere_surface(r):
    return 4 * pi * r**2


def cylinder_volume(r, h):
    return pi * r**2 * h


def cylinder_surface(r, h):
    return (2 * pi * r**2) + (2 * pi * r * h)


def cone_volume(r, h):
    return (1 / 3) * pi * r**2 * h


def cone_surface(r, h):
    return pi * r * ((r**2 * h**2) ** (1 / 2))


print(sphere_volume(3))
print(sphere_surface(3))
print(cylinder_volume(3, 3))
print(cylinder_surface(3, 3))
print(cone_volume(3, 3))
print(cone_surface(3, 3))
