def add_recipe(cookbook):
    list = []
    name = input("Enter a name:\n")
    print("Enter ingredients:")
    ing = input()
    while (ing != ""):
        list.append(ing)
        ing = input()
    meal = input("Enter a meal type:\n")
    time = input("Enter a preparation time:\n")

    cookbook[name] = {
        "ingredients": list,
        "meal": meal,
        "prep_time": time,
    }


def del_recipe(cookbook):
    name = input("Please enter a recipe name to delete:\n")
    for i in cookbook:
        if (i == name):
            cookbook.pop(name)
            print(f"{name} recipe deleted!")
            return
    print("Not a valid recipe")


def print_recipe(cookbook):
    name = input("Please enter a recipe name to get its details:\n")
    for i in cookbook:
        if (i == name):
            print_mini_recipe(name, cookbook[i])
            return
    print("Not a valid recipe")


def print_book(cookbook):
    if len(cookbook) == 0:
        print("There are no recipes in the cookbook!")
    for i in cookbook:
        print_mini_recipe(i, cookbook[i])


def quit_cook():
    print("Cookbook closed. Goodbye !")
    exit()


def print_mini_recipe(name, recipe):
    print(f"Recipe for {name}:")
    print(f"\tIngredients list: {recipe['ingredients']}")
    print(f"\tTo be eaten for {recipe['meal']}")
    print(f"\tTakes {recipe['prep_time']} minutes to cook\n")


if __name__ == "__main__":
    cookbook = {
        'bocata': {
            "ingredients": ['jamón', 'pan', 'queso', 'tomate'],
            "meal": 'almuerzo',
            "prep_time": '10'
        },
        'tarta': {
            "ingredients": ['harina', 'azúcar', 'huevos'],
            "meal": 'postre',
            "prep_time": '60'
        },
        'ensalada': {
            "ingredients": ['aguacate', 'rúcula', 'tomates', "espinacas"],
            "meal": 'almuerzo',
            "prep_time": '15'
        },
    }

    print("Welcome to the Python Cookbook !	")
    print("List of available option:")
    print("\t1: Add a recipe")
    print("\t2: Delete a recipe")
    print("\t3: Print a recipe")
    print("\t4: Print the cookbook")
    print("\t5: Quit\n")

    while (1):
        nb = input("Please select an option:\n")
        try:
            if (int(nb) < 1 or int(nb) > 5):
                5/0
        except Exception:
            print("Sorry, this option does not exist.")
        if (nb == "1"):
            add_recipe(cookbook)
        elif (nb == "2"):
            del_recipe(cookbook)
        elif (nb == "3"):
            print_recipe(cookbook)
        elif (nb == "4"):
            print_book(cookbook)
        elif (nb == "5"):
            quit_cook()
