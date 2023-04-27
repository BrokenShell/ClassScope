from random import randint


class Monster:
    damage_dice = 0

    def __init__(self, name: str, level: int):
        self.name = name
        self.level = level

    def __call__(self):
        return sum(randint(1, self.damage_dice) for _ in range(self.level))

    def __str__(self):
        return "\n".join(f"{k}: {v}" for k, v in vars(self).items())


class Undead(Monster):
    damage_dice = 6


class Dragon(Monster):
    damage_dice = 12


if __name__ == '__main__':
    monster = Undead("Vampire", 13)
    print(monster)
