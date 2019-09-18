"""
selector:
    time_selector
    | ing_selector
    | cat_selector
    | flag_selector

time_selector:
    time between INT INT
    | time under INT
    | time over INT

cat_selector:
    category CAT

flag_selector:
    flag { flag_list }

ing_selector:
    ingredient { ingredient_list }


boobs 69420 boobs

"""

from enum import EnumMeta
from typing import Tuple
from searching import TimeSelector, CategorySelector, FlagSelector, IngredientSelector, RecipeSelector, SearchQuery
from definitions import MealType, DietaryRestriction


def ignore_whitespace(string: str, offset: int=0) -> int:
    while string[offset].isspace():
        offset += 1
    return offset


def parse_int(string: str, offset: int=0) -> Tuple[int, int]:
    offset = ignore_whitespace(string, offset)
    i = 0
    while offset + i < len(string) and string[offset+i].isdigit():
        i += 1

    if i > 0:
        return int(string[offset:offset + i]), offset + i
    raise Exception("expected int")


def parse_enum(clazz: EnumMeta, string: str, offset: int = 0) -> 'clazz':
    offset = ignore_whitespace(string, offset)
    for key, value in clazz.__members__.items():
        if string[offset:offset + len(key)].lower() == key.lower():
            return value, offset + len(key)
    raise Exception(f"expected enum {clazz}")


def parse_word(string: str, word: str, offset: int = 0):
    offset = ignore_whitespace(string, offset)
    if string[offset:offset + len(word)].lower() == word.lower():
        return word, offset + len(word)
    raise Exception(f"Expected {word}")


def parse_time_selector(string: str, offset: int = 0) -> Tuple[TimeSelector, int]:
    offset = ignore_whitespace(string, offset)
    _, offset = parse_word(string, "time", offset)

    try:
        _, offset = parse_word(string, "between", offset)
        over, offset = parse_int(string, offset)
        under, offset = parse_int(string, offset)
        return TimeSelector(TimeSelector.SelectionType.BETWEEN, under, over), offset
    except:
        pass

    try:
        _, offset = parse_word(string, "over", offset)
        over, offset = parse_int(string, offset)
        return TimeSelector(TimeSelector.SelectionType.OVER, over), offset
    except:
        pass

    try:
        _, offset = parse_word(string, "under", offset)
        under, offset = parse_int(string, offset)
        return TimeSelector(TimeSelector.SelectionType.UNDER, under), offset
    except:
        pass

    raise Exception


def consume_until(string: str, delims: str, offset: int = 0) -> Tuple[str, int]:
    offset = ignore_whitespace(string, offset)
    i = 0
    while offset + i < len(string) and string[offset + i] not in delims:
        i += 1
    return string[offset:offset + i], offset + i


def parse_any_word(string: str, offset: int = 0):
    wordchar = lambda c: c.isalnum() or c == "-"
    offset = ignore_whitespace(string, offset)
    i = 0
    while offset + i < len(string) and wordchar(string[offset + i]):
        i += 1

    if i > 0:
        return string[offset:offset + i], offset + i
    raise Exception("expected int")


def parse_category_selector(string: str, offset: int = 0) -> Tuple[CategorySelector, int]:
    offset = ignore_whitespace(string, offset)
    _, offset = parse_word(string, "category", offset)
    cat, offset = parse_enum(MealType, string, offset)
    return CategorySelector(cat), offset


def parse_flag_selector(string: str, offset: int = 0) -> Tuple[FlagSelector, int]:
    offset = ignore_whitespace(string, offset)
    _, offset = parse_word(string, "flag", offset)
    _, offset = parse_word(string, "{", offset)

    flags = DietaryRestriction.NONE

    while True:
        flag, offset = parse_enum(DietaryRestriction, string, offset)
        flags = flags | flag
        try:
            _, offset = parse_word(string, "}", offset)
            break
        except:
            pass

        try:
            _, offset = parse_word(string, "|", offset)
        except:
            pass

    return FlagSelector(flags), offset


def parse_ingredient_selector(string: str, offset: int = 0) -> Tuple[IngredientSelector, int]:
    offset = ignore_whitespace(string, offset)
    _, offset = parse_word(string, "ingredient", offset)
    _, offset = parse_word(string, "{", offset)

    ingredients = []
    words = []
    while True:
        word, offset = parse_any_word(string, offset)
        words.append(word)
        try:
            _, offset = parse_word(string, ",", offset)
            ingredients.append(" ".join(words))
            words = []
        except:
            pass

        try:
            _, offset = parse_word(string, "}", offset)
            ingredients.append(" ".join(words))
            break
        except:
            pass

    return IngredientSelector(*ingredients), offset


def parse_recipe_selector(string: str, offset: int = 0) -> Tuple[RecipeSelector, int]:
    offset = ignore_whitespace(string, offset)
    _, offset = parse_word(string, "recipe", offset)
    _, offset = parse_word(string, "\"", offset)

    words = []
    while True:
        word, offset = parse_any_word(string, offset)
        words.append(word)
        try:
            _, offset = parse_word(string, "\"", offset)
            return RecipeSelector(" ".join(words)), offset
        except:
            continue


def parse_search_query(string: str, offset: int = 0) -> SearchQuery:
    offset = ignore_whitespace(string, offset)
    _, offset = parse_word(string, "search", offset)
    selectors = []

    while True:
        try:
            sel, offset = parse_time_selector(string, offset)
            selectors.append(sel)
            continue
        except Exception as e:
            pass

        try:
            sel, offset = parse_category_selector(string, offset)
            selectors.append(sel)
            continue
        except Exception as e:
            pass

        try:
            sel, offset = parse_ingredient_selector(string, offset)
            selectors.append(sel)
            continue
        except Exception as e:
            pass

        try:
            sel, offset = parse_flag_selector(string, offset)
            selectors.append(sel)
            continue
        except Exception as e:
            pass

        try:
            sel, offset = parse_recipe_selector(string, offset)
            selectors.append(sel)
            continue
        except Exception as e:
            pass

        break

    return SearchQuery(selectors)



if __name__ == '__main__':
    # selector, offset = parse_time_selector("time between 20x 45")
    # print(selector._type)
    # print(selector.over)
    # print(selector.under)

    # print(parse_category_selector("category bread")[0])
    # print(parse_flag_selector("flag { GF | DF }")[0])
    # print(parse_ingredient_selector("ingredient { tomato, onion }")[0])
    #
    print(parse_search_query("search recipe \"basic bread\""))

    # string = "boobs"
    #
    # num, offset = parse_enum(DietaryRestriction, string, 0)
    # print(num)
