from recipe import Recipe
from book import Book


# if __name__ == "__main__":
#     mylist = ["apple", "dsf", "cherry"]

#     try:
#         p1 = Book('Portuguese cookbook')
#         cake = Recipe("Cake", 3, 15, mylist, 'dessert')
#         p1.add_recipe(cake)
#         cake1 = Recipe("Cake2", 3, 15, mylist, 'dessert')
#         p1.add_recipe(cake1)
#         print(p1.get_recipes_by_types("dessert"))
#     except ValueError as e: print(e)

def main():
    print("\n# TESTING INPUT IN RECIPE\n(order: name, cooking_lvl, cooking_time, ingredients, recipe_type, description)")
    print("\n#Valids")
    reci = Recipe('prUebA', 1, 24, ['me', 'tienes', 'hasta', 'los...'], 'starter', 'vergaaaa')
    reci1 = Recipe('prUebA2', 1, 24, ['me', 'tienes', 'hasta', 'los...'], 'lunch', 'vergaaaa')
    reci2 = Recipe('prUebA3', 1, 24, ['me', 'tienes', 'hasta', 'los...'], 'dessert', 'vergaaaa')
    print(f"{Recipe('prUebA', 1, 24, ['me', 'tienes', 'hasta', 'los...'], 'starter', 'vergaaaa')}")
    print(f"{Recipe('prUebA', 1, 24, ['me', 'tienes', 'hasta', 'los...'], 'starter', None)}")
    print(f"{Recipe('111111', 1, 24, ['me', 'tienes', 'hasta', 'los...'], 'starter')}")
    print(f"{Recipe('      ', 1, 24, ['me', 'tienes', 'hasta', 'los...'], 'starter')}")
    print("\n#Invalids")
    try:
        print(f"{Recipe('prUebA', 1, '24', ['me', 'tienes', 'hasta', 'los...'], 'Receta que expresa que siento')}")
    except ValueError:
        print(f"Error correcto, valores incorrectos")
    try:
        print(f"{Recipe('prUebA', '1', 24, ['me', 'tienes', 'hasta', 'los...'], 'Receta que expresa que siento')}")
    except ValueError:
        print(f"Error correcto, valores incorrectos")
    try:
        print(f"{Recipe('prUebA', 1.0, 24, ['me', 'tienes', 'hasta', 'los...'], 'Receta que expresa que siento')}")
    except ValueError:
        print(f"Error correcto, valores incorrectos")
    try:
        print(f"{Recipe('prUebA', 1, 24.0, ['me', 'tienes', 'hasta', 'los...'], 'Receta que expresa que siento')}")
    except ValueError:
        print(f"Error correcto, valores incorrectos")
    try:
        print(f"{Recipe('1111111', 1, 24, ['me', 'tienes', 'hasta', 'los...'], 'Receta que expresa que siento')}")
    except ValueError:
        print(f"Error correcto, valores incorrectos")
    print("\n\n# TESTING INPUT IN BOOK\n(order: name, last_update, creation_date)")
    print("\n#Valids")
    book = Book('Libro')
    print(f"{Book('11111')}")
    print(f"{Book('     ')}")
    print(f"{Book('Ldfgfsdf4567456##%^$%^#$%^$%4')}")
    book.add_recipe(reci)
    book.add_recipe(reci1)
    book.add_recipe(reci2)
    book.get_recipe_by_name('prUebA')
    book.get_recipe_by_name('prUebA2')
    book.get_recipe_by_name('prUebA3')
    book.get_recipes_by_types('start')
    book.get_recipes_by_types('lunch')
    book.get_recipes_by_types('dessert')
    print("\n#Invalids")
    try:
        Book(233)
    except ValueError:
        print(f"Error correcto, valores incorrectos")
    try:
        book.get_recipe_by_name('nonexist')
    except ValueError:
        print(f"Error correcto, valores incorrectos")
    try:
        book.get_recipe_by_name(None)
    except ValueError:
        print(f"Error correcto, valores incorrectos")
    try:
        book.get_recipes_by_types('nonexist')
    except ValueError:
        print(f"Error correcto, valores incorrectos")
    try:
        book.get_recipes_by_types(None)
    except ValueError:
        print(f"Error correcto, valores incorrectos")
    try:
        book.add_recipe(None)
    except ValueError:
        print(f"Error correcto, valores incorrectos")
    try:
        hola = 1
        book.add_recipe(hola)
    except ValueError:
        print(f"Error correcto, valores incorrectos")


if __name__ == "__main__":
    main()
