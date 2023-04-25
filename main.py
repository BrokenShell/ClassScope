from typing import Union


class Wizard:
    def attack(self):
        print("Wizard is casting arcane spell")


class Gladiator:
    def attack(self):
        print("Gladiator is swinging a melee weapon")


class Archer:
    def attack(self):
        print("Archer is shooting bow and arrow")


class Druid:
    def attack(self):
        print("Druid is casting nature spell")


Character = Union[
    Wizard,
    Gladiator,
    Archer,
    Druid,
]


def combat(player_1: Character, player_2: Character):
    player_1.attack()
    player_2.attack()


if __name__ == '__main__':
    combat(Druid(), Gladiator())
