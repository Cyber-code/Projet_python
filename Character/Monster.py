"""from Character import *
from Equipements import *

class Monster(Character):
    def __init__(self):
        Character.__init__(self)
        self.inventory = None


    def generate_new_monster(self, level):
        self.lvl = level
        self.hp = randint(int(level * 2), int(level * 4))
        self.max_hp = self.hp
        self.mp = randint(int(level * 2), int(level * 4))
        self.min_atk = randint(int(level * 2), int(level * 4))
        self.max_atk = randint(int(level * 5), int(level * 7))
        self.armor = randint(int(level * 2), int(level * 4))


    def generate_gold_after_death(self, hero):
        gold = randint(int(self.lvl * 3), int(self.lvl * 6))
        hero.inventory.gold += gold

    def generate_exp_after_death(self, hero):
        hero.requiredexp += 1

    def generate_random_stuff_after_death(self, hero):
        random_stuff = randint(1, 7) # There are only 7 type of equipement, we ive one random equipement
        if random_stuff == 1:
            weapon = Weapon()
            weapon = Weapon.generate_random_weapon(self, hero.lvl + 1)
            print("Vous avez drop une weapon !")
            hero.inventory.equipement.loot.append(weapon)
        elif random_stuff == 2:
            jewel = Jewel()
            jewel = Jewel.generate_random_jewel(self, hero.lvl + 1)
            print("Vous avez droppé un nouveau jewel !")
            hero.inventory.equipement.loot.append(jewel)
        elif random_stuff == 3:
            head = Head()
            head = Head.generate_random_head(self, hero.lvl + 1)
            print("Vous avez droppé une head !")
            hero.inventory.equipement.loot.append(head)
        elif random_stuff == 4:
            chest = Chest()
            chest = Chest.generate_random_chest(self, hero.lvl + 1)
            print("Vous avez droppé un chest !")
            hero.inventory.equipement.loot.append(chest)
        elif random_stuff == 5:
            legs = Legs()
            legs = Legs.generate_random_legs(self, hero.lvl + 1)
            print("Vous avez droppé un legs !")
            hero.inventory.equipement.loot.append(legs)
        elif random_stuff == 7:
            shoes = Legs()
            shoes = Shoes.generate_random_shoes(self, hero.lvl + 1)
            print("Vous avez droppé des shoes !")
            hero.inventory.equipement.loot.append(shoes)


    def after_monster_death(self, hero):
        self.generate_exp_after_death(hero)
        self.generate_gold_after_death(hero)
        self.generate_random_stuff_after_death(hero)

    def generate_monsters(self, level):
        monster = Monster()
        monster.generate_new_monster(level)
        return monster

    def show_monster_information(self):
        return self.hp

    def attack_monster(self, value):
        self.hp -= value

    def reduce_defence_monster(self, value):
        self.armor -= value

    def reduce_atk_monster(self, value):
        print("Vous avez diminué l'attaque du monstre de ", value)
        self.min_atk -= 0.2 * self.min_atk
        self.max_atk -= 0.2 * self.max_atk

    def check_if_monster_is_dead(self):
        if self.hp > 0:
            print("Le monstre a", self.hp, "hp après votre attaque.")
            return False
        else:
            print("Le monstre est mort après votre attaque.")
            return True

    def attack_hero(self, hero, monster_number):
        damage = random.randint(int(self.min_atk), int(self.max_atk))
        print("Le monstre vous a infligé : ", damage, " dégats")
        hero.receive_damage(damage)
        print("Vous disposez désormais de ", hero.hp," points de vie")
