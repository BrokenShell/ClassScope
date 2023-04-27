from random import randint


def dice(rolls, sides):
    return sum(randint(1, sides) for _ in range(rolls))


print(dice(10, 10))
