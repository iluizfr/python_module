def validate_ingredients(ingredients: str) -> str:
    elements = ["fire", "water", "earth", "air"]
    split_ingredients = ingredients.split()

    for element in elements:
        for ingredient in split_ingredients:
            if element == ingredient:
                return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
