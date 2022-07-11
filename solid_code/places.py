from abc import ABC, abstractmethod


class Place(ABC):
    @abstractmethod
    def print_antagonist(self):
        pass


class Kostroma(Place):
    city_name = 'Kostroma'

    def get_orcs(self):
        print('Orcs hid in the forest')

    def print_antagonist(self):
        return self.get_orcs()


class Tokyo(Place):
    name = 'Tokyo'

    def get_godzilla(self):
        print('Godzilla stands near a skyscraper')

    def print_antagonist(self):
        return self.get_godzilla()
