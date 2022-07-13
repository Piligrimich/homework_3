from typing import Union
from heroes import Superman, SuperHero, Information, ChackNorris
from places import Kostroma, Tokyo


def save_the_place(hero: Union[Superman, SuperHero, ChackNorris], place: Union[Kostroma, Tokyo], info):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    info.create_news(place)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma(), Information('Superman'))
    print('-' * 20)
    save_the_place(ChackNorris(), Tokyo(), Information('Chack Norris'))
    print('-' * 20)
    save_the_place(SuperHero('Nick Fury', False), Tokyo(), Information('Nick Fury'))
