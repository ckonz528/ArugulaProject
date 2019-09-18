from enum import Enum, Flag, auto


class DietaryRestriction(Flag):
    NONE = 0
    VEGETARIAN = auto()
    VEGAN = auto()
    GF = auto()
    DF = auto()
    ALCOHOLIC = auto()


class MealType(Enum):
    APP = auto()
    ENTREE = auto()
    SIDE = auto()
    SOUP = auto()
    SALAD = auto()
    BREAD = auto()
    DESSERT = auto()
    DRINK = auto()
    SNACK = auto()


class Unit(Enum):
    ML = auto()
    CT = auto()