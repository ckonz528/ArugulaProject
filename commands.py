def search(words):
    print(words[0])

command_lookup = {
    "search": search
}

command_structure = {
    "search": {
        "time": {"between": 2, "less": 1, "greater": 1},
        "ingredient": 1,
        "category": 1,
        "flags": 1
    }
}