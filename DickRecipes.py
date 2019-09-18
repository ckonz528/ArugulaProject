from definitions import *
import pickle

recipes = {
    "Basic bread": {
        "name": "Basic bread",
        "ingredients": {
            "yeast": (1.2, Unit.ML),
            "flour": (1301, Unit.ML),
            "salt": (15, Unit.ML),
            "sugar": (59, Unit.ML),
            "oil": (30, Unit.ML),
            "butter": (1, Unit.CT),
            "water": (532, Unit.ML)
        },
        "directions": "",
        "time": 210,
        "flags": DietaryRestriction.VEGETARIAN,
        "category": MealType.BREAD
    },

    "Guacamole": {
        "name": "Guacamole",
        "ingredients": {
            "avocado": (4, Unit.CT),
            "roma tomato": (2, Unit.CT),
            "onion": (0.5, Unit.CT),
            "lime": (2, Unit.CT),
            "jalapeno": (1, Unit.CT),
            "cilantro": (.5, Unit.CT),
            "salt": (10, Unit.ML),
        },
        "directions": "",
        "time": 20,
        "flags": DietaryRestriction.VEGETARIAN | DietaryRestriction.VEGAN | DietaryRestriction.GF | DietaryRestriction.DF,
        "category": MealType.SNACK
    },

    "Amish sugar cookies": {
        "name": "Amish sugar cookies",
        "ingredients": {
            "flour": (1065, Unit.ML),
            "baking soda": (5, Unit.ML),
            "cream of tartar": (5, Unit.ML),
            "sugar": (237, Unit.ML),
            "powdered sugar": (237, Unit.ML),
            "oil": (237, Unit.ML),
            "butter": (237, Unit.ML),
            "eggs": (2, Unit.CT),
            "vanilla": (5, Unit.ML)
        },
        "directions": "",
        "time": 25,
        "flags": DietaryRestriction.VEGETARIAN,
        "category": MealType.DESSERT
    },

    "Honey Dijon Garlic Chicken Breasts": {
        "name": "Honey Dijon Garlic Chicken Breasts",
        "ingredients": {
            "chicken breasts": (4, Unit.CT),
            "butter": (44, Unit.ML),
            "garlic cloves": (6, Unit.CT),
            "honey": (80, Unit.ML),
            "dijon mustard": (30, Unit.ML),
        },
        "directions": "",
        "time": 40,
        "flags": DietaryRestriction.GF,
        "category": MealType.ENTREE
    },

    "Gooey Butter Cookies": {
        "name": "Gooey Butter Cookies",
        "ingredients": {
            "butter": (118, Unit.CT),
            "cream cheese": (1, Unit.CT),
            "eggs": (1, Unit.CT),
            "vanilla": (1.2, Unit.ML),
            "yellow cake mix": (1, Unit.CT),
            "powdered sugar": (237, Unit.ML),
        },
        "directions": "",
        "time": 22,
        "flags": DietaryRestriction.VEGETARIAN,
        "category": MealType.DESSERT
    },

    "Condensed Cream of Mushroom Soup": {
        "name": "Condensed Cream of Mushroom Soup",
        "ingredients": {
            "chopped mushrooms": (177, Unit.ML),
            "flour": (79, Unit.ML),
            "milk": (158, Unit.ML),
            "vegetable broth": (296, Unit.ML),
            "onion powder": (5, Unit.ML),
            "garlic powder": (5, Unit.ML),
            "celery salt": (1.2, Unit.ML),
            "salt": (1.2, Unit.ML),
            "pepper": (1.2, Unit.ML)
        },
        "directions": "",
        "time": 20,
        "flags": DietaryRestriction.VEGETARIAN,
        "category": MealType.SOUP
    },

    "Caprese Pasta Salad": {
        "name": "Caprese Pasta Salad",
        "ingredients": {
            "rotini pasta": (1, Unit.CT),
            "box of cherry tomatoes": (1, Unit.CT),
            "8oz mozzarella pearls": (1, Unit.CT),
            "fresh basil": (120, Unit.ML),
            "pesto": (60, Unit.ML),
            "olive oil": (44, Unit.ML),
            "balsamic vinegar": (30, Unit.ML),
            "salt": (1.2, Unit.ML),
            "pepper": (1.2, Unit.ML)
        },
        "directions": "",
        "time": 15,
        "flags": DietaryRestriction.VEGETARIAN,
        "category": MealType.SALAD
    },

    "Buffalo Chicken Dip": {
        "name": "Buffalo Chicken Dip",
        "ingredients": {
            "cooked chicken": (480, Unit.ML),
            "cream cheese": (1, Unit.CT),
            "buffalo sauce": (120, Unit.ML),
            "cheddar cheese": (240, Unit.ML),
            "monterey jack cheese": (240, Unit.ML),
        },
        "directions": "",
        "time": 45,
        "flags": DietaryRestriction.GF,
        "category": MealType.APP
    },

    "Bacon-wrapped Jalapeno Poppers": {
        "name": "Bacon-wrapped Jalapeno Poppers",
        "ingredients": {
            "jalapeno peppers": (6, Unit.CT),
            "cream cheese": (1, Unit.CT),
            "bacon": (12, Unit.CT),
        },
        "directions": "",
        "time": 30,
        "flags": DietaryRestriction.GF,
        "category": MealType.APP
    },

    "Cracker Barrel Green Beans": {
        "name": "Cracker Barrel Green Beans",
        "ingredients": {
            "bacon": (4, Unit.CT),
            "canned green beans": (3, Unit.CT),
            "onion": (120, Unit.ML),
            "sugar": (5, Unit.ML),
            "salt": (1.2, Unit.ML),
            "pepper": (1.2, Unit.ML)
        },
        "directions": "",
        "time": 20,
        "flags": DietaryRestriction.GF,
        "category": MealType.SIDE
    },

    "Green Bean Casserole": {
        "name": "Green Bean Casserole",
        "ingredients": {
            "canned green beans": (2, Unit.CT),
            "cream of mushroom soup": (1, Unit.CT),
            "French's fried onions": (1, Unit.CT),
            "milk": (160, Unit.ML),
            "onion powder": (2.5, Unit.ML),
            "garlic powder": (2.5, Unit.ML),
            "salt": (1.2, Unit.ML),
            "pepper": (1.2, Unit.ML)
        },
        "directions": "",
        "time": 20,
        "flags": DietaryRestriction.VEGETARIAN,
        "category": MealType.SIDE
    },

    "Chicken Parmesan": {
        "name": "Chicken Parmesan",
        "ingredients": {
            "chicken breasts": (4, Unit.CT),
            "salt": (2.5, Unit.ML),
            "pepper": (1.2, Unit.ML),
            "eggs": (2, Unit.CT),
            "flour": (60, Unit.ML),
            "bread crumbs": (240, Unit.ML),
            "parmesan cheese": (120, Unit.ML),
            "olive oil": (30, Unit.ML),
            "butter": (30, Unit.ML),
            "marinara sauce": (240, Unit.ML),
            "mozzarella cheese": (240, Unit.ML)
        },
        "directions": "",
        "time": 30,
        "flags": DietaryRestriction.NONE,
        "category": MealType.ENTREE
    },

    "Vanilla Bean Frappuccino": {
        "name": "Vanilla Bean Frappuccino",
        "ingredients": {
            "ice": (240, Unit.ML),
            "milk": (360, Unit.ML),
            "vanilla bean ice cream": (3, Unit.CT),
            "sugar": (5, Unit.ML),
            "vanilla": (1.2, Unit.ML),
            "whipped cream": (1, Unit.CT),
        },
        "directions": "",
        "time": 10,
        "flags": DietaryRestriction.GF | DietaryRestriction.VEGETARIAN,
        "category": MealType.DRINK
    },

    "Bloody Mary": {
        "name": "Bloody Mary",
        "ingredients": {
            "tomato juice": (118, Unit.ML),
            "vodka": (89, Unit.ML),
            "lemon juice": (2.5, Unit.ML),
            "worcestershire sauce": (10, Unit.ML),
            "salt": (1.2, Unit.ML),
            "pepper": (1.2, Unit.ML),
            "hot sauce": (5, Unit.ML),
            "horseradish": (10, Unit.ML),
        },
        "directions": "",
        "time": 10,
        "flags": DietaryRestriction.ALCOHOLIC | DietaryRestriction.DF | DietaryRestriction.VEGETARIAN | DietaryRestriction.VEGAN,
        "category": MealType.DRINK
    },

}

if __name__ == '__main__':
    pickle.dump(recipes, open("Recipes.yum", "wb"), protocol=4)
