def healing_potion() -> str:
    try:
        from .elements import create_fire, create_water
        return (f"Healing potion brewed with "
                f"{create_fire()} and {create_water()}")
    except Exception as err:
        return f"Import Error: {err}"


def strength_potion() -> str:
    try:
        from .elements import create_earth, create_fire
        return ("Strength potion brewed with "
                f"{create_earth()} and {create_fire()}")
    except Exception as err:
        return f"Import Error: {err}"


def invisibility_potion() -> str:
    try:
        from .elements import create_air, create_water
        air = create_air()
        water = create_water()
        return f"Invisibility potion brewed with {air} and {water}"
    except Exception as err:
        return f"Import Error: {err}"


def wisdom_potion() -> str:
    try:
        from .elements import create_water, create_earth
        from .elements import create_fire, create_air
        water = create_water()
        earth = create_earth()
        fire = create_fire()
        air = create_air()

        return ("Wisdom potion brewed with all elements: "
                f"{water, earth, fire, air}")
    except Exception as err:
        return f"Import Error: {err}"
