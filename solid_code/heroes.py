from antagonistfinder import AntagonistFinder


class SuperHero:

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)

    def attack(self):
        print('Boom')

    def ultimate(self):
        pass


class Gun:
    def fire_a_gun(self):
        print('PIU PIU')


class Lasers:
    def incinerate_with_lasers(self):
        print('Wzzzuuuup!')


class Kick:
    def roundhouse_kick(self):
        print('Bump')


class Information:
    def __init__(self, name):
        self.name = name

    def create_news(self, place):
        place_name = getattr(place, 'name', 'place')
        print(f'{self.name} saved the {place_name}!')


class Superman(SuperHero, Lasers):
    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    def ultimate(self):
        self.incinerate_with_lasers()

    def attack(self):
        print('Kick')


class ChackNorris(SuperHero):
    def __init__(self):
        super(ChackNorris, self).__init__('Chack Norris', False)

    def attack(self):
        print('PIU PIU')
