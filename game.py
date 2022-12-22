class Warrior:
    def __init__(self, name='warrior', health=100, stamina=100):
        self.name = name
        self.health = health
        self.stamina = stamina

    def introduces(self):
        print("--------")
        print(f'Class: {self.__class__.__name__}\n'
              f'Name : {self.name}\n'
              f'Health: {self.health}\n'
              f'Stamina: {self.stamina}')
        print("--------")

    def heals(self, target):
        if self.stamina < 20:
            print("Недостаточный запас сил для лечения травами")
        else:
            print("--------")
            print(f'{self.name} собирает целебные травы и накладывает повязку',
                  f'на {target.name}')
            target.health += 10
            self.stamina -= 20
            print(f'Здоровье у {target.name} повышено до {target.health}\n',
                  f'У {self.name} осталось {self.stamina} единиц сил')
            print("--------")

    def attacks(self, target):
        print("--------")
        print(f'{self.name} наносит урон мечом {target.name}')
        target.health -= 15
        if target.health <= 0:
            print("--------")
            print(f'{target.name} погиб в бою')
            print("--------")
        else:
            print(f'Здоровье у {target.name} понижено до {target.health}')
            print("--------")

    def counterattack(self, target):  # Каждое действие должно иметь противодействие, по этому добавляем контратаку
        print('----------')
        print(f'{self.name} контратакует {target.name}')
        target.health -= 8
        if target.health <= 0:
            print("--------")
            print(f'{target.name} погиб в бою')
            print("--------")
        else:
            print(f'Здоровье у {target.name} понижено до {target.health}')
            print("--------")


class Mage:
    def __init__(self, name='mage', health=60, mana=100):
        self.name = name
        self.health = health
        self.mana = mana

    def introduces(self):
        print("--------")
        print(f'Class: {self.__class__.__name__}\n'
              f'Name : {self.name}\n'
              f'Health: {self.health}\n'
              f'Mana: {self.mana}')
        print("--------")

    def heals(self, target):
        if self.mana < 20:
            print("Недостаточно маны для заклинания лечения")
        else:
            print("--------")
            print(f'{self.name} применяет заклинание лечения',
                  f'на {target.name}')
            target.health += 10
            self.mana -= 20
            print(f'Здоровье у {target.name} повышено до {target.health}\n',
                  f'У {self.name} осталось {self.mana} единиц маны')
            print("--------")

    def attacks(self, target):
        print("--------")
        print(f'{self.name} наносит урон магией {target.name}')
        target.health -= 11
        if target.health <= 0:
            print("--------")
            print(f'{target.name} погиб в бою')
            print("--------")
        else:
            print(f'Здоровье у {target.name} понижено до {target.health}')
            print("--------")

    def counterattack(self, target):  # Каждое действие должно иметь противодействие, по этому добавляем контратаку
        print('----------')
        print(f'{self.name} контратакует {target.name}')
        target.health -= 8
        if target.health <= 0:
            print("--------")
            print(f'{target.name} погиб в бою')
            print("--------")
        else:
            print(f'Здоровье у {target.name} понижено до {target.health}')
            print("--------")


unit1 = Warrior('Nix', stamina=50)
unit2 = Warrior('Aatrox', 80, 70)
unit3 = Mage('Sona')
unit4 = Mage('Niska', health=50, mana=110)

while True:  # делаем цикл что бы играть до победы
    if unit1.health <= 0 and unit2.health <= 0:  # условие победы магов
        print('Маги развалили Воинов')
        break
    elif unit3.health <= 0 and unit4.health <= 0:  # условие победы воинов
        print('Воины развалили Магов')
        break
    action = input('Выберите действие: 1 - атака, 2 - лечение: ')
    if action == '1':
        u = input('Выберите юнита: 1 - Nix, 2 - Aatrox, 3 - Sona, 4 - Niska: ')
        if u == '1':
            to_u = input('Выберите цель: 2 - Aatrox, 3 - Sona, 4 - Niska: ')
            if to_u == '2':
                unit1.attacks(unit2),
                if unit2.health >= 1:  # Условие для контратаки
                    unit2.counterattack(unit1)
            elif to_u == '3':
                unit1.attacks(unit3),
                if unit3.health >= 1:
                    unit3.counterattack(unit1)
            elif to_u == '4':
                unit1.attacks(unit4),
                if unit4.health >= 1:
                    unit4.counterattack(unit1)
        elif u == '2':
            to_u = input('Выберите цель: 1 - Nix, 3 - Sona, 4 - Niska: ')
            if to_u == '1':
                unit2.attacks(unit1),
                if unit1.health >= 1:
                    unit1.counterattack(unit2)
            elif to_u == '3':
                unit2.attacks(unit3),
                if unit3.health >= 1:
                    unit3.counterattack(unit2)
            elif to_u == '4':
                unit2.attacks(unit4),
                if unit4.health >= 1:
                    unit4.counterattack(unit2)
        elif u == '3':
            to_u = input('Выберите цель: 1 - Nix, 2 - Aatrox, 4 - Niska: ')
            if to_u == '1':
                unit3.attacks(unit1),
                if unit1.health >= 1:
                    unit1.counterattack(unit3)
            elif to_u == '2':
                unit3.attacks(unit2),
                if unit2.health >= 1:
                    unit2.counterattack(unit3)
            elif to_u == '4':
                unit3.attacks(unit4),
                if unit4.health >= 1:
                    unit4.counterattack(unit4)
        elif u == '4':
            to_u = input('Выберите цель: 1 - Nix, 2 - Aatrox, 3 - Sona: ')
            if to_u == '1':
                unit4.attacks(unit1),
                if unit1.health >= 1:
                    unit1.counterattack(unit4)
            elif to_u == '2':
                unit4.attacks(unit2),
                if unit2.health >= 1:
                    unit2.counterattack(unit4)
            elif to_u == '3':
                unit4.attacks(unit3),
                if unit3.health >= 1:
                    unit3.counterattack(unit4)
    elif action == '2':
        u = input('Выберите юнита: 1 - Nix, 2 - Aatrox, 3 - Sona, 4 - Niska: ')
        if u == '1':
            to_u = input('Выберите цель: 2 - Aatrox, 3 - Sona, 4 - Niska: ')
            if to_u == '2':
                unit1.heals(unit2)
            elif to_u == '3':
                unit1.heals(unit3)
            elif to_u == '4':
                unit1.heals(unit4)
        elif u == '2':
            to_u = input('Выберите цель: 1 - Nix, 3 - Sona, 4 - Niska: ')
            if to_u == '1':
                unit2.heals(unit1)
            elif to_u == '3':
                unit2.heals(unit3)
            elif to_u == '4':
                unit2.heals(unit3)
        elif u == '3':
            to_u = input('Выберите цель: 1 - Nix, 2 - Aatrox, 4 - Niska: ')
            if to_u == '1':
                unit3.heals(unit1)
            elif to_u == '2':
                unit3.heals(unit2)
            elif to_u == '4':
                unit3.heals(unit4)
        elif u == '4':
            to_u = input('Выберите цель: 1 - Nix, 2 - Aatrox, 3 - Sona: ')
            if to_u == '1':
                unit4.heals(unit1)
            elif to_u == '2':
                unit4.heals(unit2)
            elif to_u == '3':
                unit4.heals(unit3)

print('Game over')
