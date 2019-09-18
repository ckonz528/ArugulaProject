import pickle
from definitions import *
from command_parser import parse_search_query
from lists import show_list

recipe_file = input("Enter file name: ")

recipes = pickle.load(open(recipe_file, "rb"))

lists = {}

while True:
    command = input("\n>>> ")
    if command == "exit":
        break
    # query = parse_search_query(command)
    # print(query(recipes))
    try:
        query = parse_search_query(command, 0)
        print(query)
        lists["result"] = query(recipes)
        # for recipe in query(recipes):
        #     print(f"- {recipe}")
    except Exception as e:
        print("Sorry! I only know how to handle searches right now!")
        print("The error I got was: ", e)

    show_list(lists["result"])