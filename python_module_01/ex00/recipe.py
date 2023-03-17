class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description=None):
        meal_type = ["starter", "lunch", "dessert"]
        if not isinstance(name, str):
            raise ValueError("Name has to be a string")
        if not isinstance(cooking_lvl, int) or cooking_lvl not in range(1, 6):
            text = "Cooking Level has to be an integer between 1 and 5"
            raise ValueError(text)
        if not isinstance(cooking_time, int) or cooking_time <= 0:
            raise ValueError("Cooking Time has to be a positive integer")
        if not isinstance(ingredients, list) or not all(isinstance(i, str) for i in ingredients):
            raise ValueError("Ingredients has to be a list of strings")
        if not isinstance(recipe_type, str) or not meal_type.count(recipe_type):
            raise ValueError("Recipe type has to be “starter”, “lunch” or “dessert”")
        if not isinstance(description, str) and description is not None:
            raise ValueError("Description has to be a string")
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.recipe_type = recipe_type
        self.description = description

    def __str__(self):
        text = f"Recipe name: {self.name}\nCooking time: {self.cooking_time}\nIngredients: {self.ingredients}\nRecipe type: {self.recipe_type}"
        if self.description is not None and self.description is not "":
            text += f"\nDescription: {self.description}"
        return text
