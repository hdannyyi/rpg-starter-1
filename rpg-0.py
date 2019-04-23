##Refactored
class Hero:
    def __init__(self, name, health, power):
        self.health = health
        self.power = power

    def attack(self, goblin):
        goblin.health -= self.power
        print("You do %d damage to the goblin." % self.power)

    def alive(self):
        if self.health > 0:
            return True

    def print_hero_status(self):
        print("You have %d health and %d power." % (hero.health, hero.power))


class Goblin:
    def __init__(self, name, health, power):
        self.health = health
        self.power = power

    def attack(self, hero):
        hero.health -= self.power
        print("The goblin does %d damage to you." % self.power)

    def alive(self):
        if self.health > 0:
            return True

    def print_goblin_status(self):
        print("The goblin has %d health and %d power." % (goblin.health, goblin.power))

hero = Hero('hero', 10, 5)
goblin = Goblin('goblin', 6, 2)




"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

def main():
    """hero_health = 10
    hero_power = 5
    goblin_health = 6
    goblin_power = 2"""

    while goblin.alive() and hero.alive():
        """print("You have %d health and %d power." % (hero.health, hero.power))
        print("The goblin has %d health and %d power." % (goblin.health, goblin.power))"""
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
            """print("You do %d damage to the goblin." % hero.power)"""
            if goblin.health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.health > 0:
            # Goblin attacks hero
            hero.health -= goblin.power
            print("The goblin does %d damage to you." % goblin.power)
            if hero.health <= 0:
                print("You are dead.")

main()
