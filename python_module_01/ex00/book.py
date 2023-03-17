from recipe import Recipe
import time


class Book:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Cookbook - Name has to be a string")
        self.name = name
        self.creation_date = time.time()
        self.last_update = time.time()
        self.recipes_list = {
            "starter": [],
            "lunch": [],
            "dessert": []
            }

    def get_recipe_by_name(self, name):
        for i in self.recipes_list:
            for j in self.recipes_list[i]:
                if (j.name == name):
                    return j
        return (None)

    def get_recipes_by_types(self, recipe_type):
        for i in self.recipes_list:
            if (i == recipe_type):
                return self.recipes_list[i]
        return (None)

    def add_recipe(self, recipe):
        if not isinstance(recipe, Recipe):
            raise ValueError("Cookbook - Add only recipes")
        for i in self.recipes_list:
            if (i == recipe.recipe_type):
                self.recipes_list[i].append(recipe)
        self.last_update = time.time()
