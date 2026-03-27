def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    result = validate_ingredients(ingredients)
    split_result = result.split()
    for arg in split_result:
        if arg == "VALID":
            valid = validate_ingredients(ingredients)
            return f"Spell recorded: {spell_name} ({valid})"

    not_valid = validate_ingredients(ingredients)
    return f"Spell rejected: {spell_name} ({not_valid})"
