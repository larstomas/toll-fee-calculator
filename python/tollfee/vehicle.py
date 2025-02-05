"""
Vehicle classes for the toll fee calculator.
"""

import abc


class Vehicle(abc.ABC):

    @abc.abstractmethod
    def get_type(self):
        pass


class Car(Vehicle):

    @staticmethod
    def get_type():
        return 'Car'


class Motorbike(Vehicle):

    @staticmethod
    def get_type():
        return 'Motorbike'

class Tractor(Vehicle):

    @staticmethod
    def get_type():
        return 'Tractor'

class Emergency(Vehicle):

    @staticmethod
    def get_type():
        return 'Emergency'

class Diplomat(Vehicle):

    @staticmethod
    def get_type():
        return 'Diplomat'

class Foreign(Vehicle):

    @staticmethod
    def get_type():
        return 'Foreign'

class Military(Vehicle):

    @staticmethod
    def get_type():
        return 'Military'
