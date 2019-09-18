from enum import Enum
from typing import List, Dict
from definitions import MealType, DietaryRestriction


class AlmostString:
    def __init__(self, string):
        self.string = string

    def __eq__(self, other):
        a = self.string.lower()
        b = other.lower()

        return a in b or b in a

    def __hash__(self):
        return self.string.__hash__()


class Selector:
    def __call__(self, recipe: Dict):
        raise NotImplemented


class TimeSelector(Selector):
    class SelectionType(Enum):
        UNDER = 1
        OVER = 2
        BETWEEN = 3

    def __init__(self, _type: SelectionType, *args: int):
        self._type = _type
        if _type == TimeSelector.SelectionType.BETWEEN:
            self.under = args[0]
            self.over = args[1]
        elif _type == TimeSelector.SelectionType.UNDER:
            self.under = args[0]
            self.over = None
        elif _type == TimeSelector.SelectionType.OVER:
            self.under = None
            self.over = args[0]

    def __call__(self, recipe: Dict):
        return (self.under is None or recipe["time"] < self.under) and \
               (self.over is None or recipe["time"] > self.over)

    def __str__(self):
        if self._type == TimeSelector.SelectionType.BETWEEN:
            return f"[time between {self.over} and {self.under}]"
        elif self._type == TimeSelector.SelectionType.OVER:
            return f"[time over {self.over}]"
        elif self._type == TimeSelector.SelectionType.UNDER:
            return f"[time under {self.under}]"


class CategorySelector(Selector):
    def __init__(self, category : MealType):
        self.cat = category

    def __call__(self, recipe: Dict):
        return AlmostString(recipe["category"]) == self.cat

    def __str__(self):
        return f"[category is {self.cat}]"


class IngredientSelector(Selector):
    def __init__(self, *ingredients: str):
        self.ingredients = ingredients

    def __call__(self, recipe: Dict):
        return all(AlmostString(ingredient) in recipe["ingredients"].keys() for ingredient in self.ingredients)

    def __str__(self):
        return f"[ingredients contains {' and '.join(self.ingredients)}]"


class FlagSelector(Selector):
    def __init__(self, flags: DietaryRestriction):
        self.flags = flags

    def __call__(self, recipe: Dict):
        return self.flags & recipe["flags"] == self.flags

    def __str__(self):
        return f"[has flags {self.flags}]"


class RecipeSelector(Selector):
    def __init__(self, recipe: str):
        self.name = recipe

    def __call__(self, recipe: Dict):
        return AlmostString(recipe["name"]) == self.name

    def __str__(self):
        return f"[name is {self.name}]"


class SearchQuery:
    def __init__(self, selectors: List[Selector]):
        self.selectors = selectors

    def __call__(self, recipes: Dict[str, Dict]):
        # return list(filter(lambda r: all(s(r) for s in self.selectors), recipes.values()))
        return [name for (name, details) in recipes.items() if all(s(details) for s in self.selectors)]

    def __str__(self):
        return f"Searching for recipes that satisfy {' '.join(map(str, self.selectors))}"