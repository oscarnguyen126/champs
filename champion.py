from database import Database

database=Database()
class Champion:
    def __init__(self, name, hp, atk, atk_speed, range):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.atk_speed = atk_speed
        self.range = range

    def normal_attack(self, champ):
        champ.hp = champ.hp - self.atk
        print(f'{self.name} has deal {self.atk} damages to {champ.name}')

    def add_item(self, item):
        if item.attribute == "hp":
            self.hp += item.value
            print(f"{self.name}'s hp has increased to {self.hp} \n")

        elif item.attribute == "atk_damage":
            self.atk += item.value
            print(f"{self.name}'s damages has increased to {self.atk} \n")

        elif item.attribute == "atk_speed":
            self.atk_speed += item.value
            print(f"{self.name}'s attach speed has increased to {self.atk_speed} \n")

        else:
            self.range += item.value
            print(f"{self.name}'s range attach has increased to {self.range} \n")

    @classmethod
    def get_all(cls):
        champion_dicts = database.get_all_champion("Select * from champions")
        champions = [Champion(
            name=champion_dict.get('name'),
            hp=champion_dict.get('hp'),
            atk=champion_dict.get('atk_damage'),
            atk_speed=champion_dict.get('atk_speed'),
            range=champion_dict.get('atk_range')
        ) for champion_dict in champion_dicts]
        return [champion for champion in champions]
