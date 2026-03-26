from .elements import create_water, create_fire, create_earth, create_air


def healing_potion() -> str:
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion() -> str:
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
    air = create_air()
    water = create_water()
    return f"Invisibility potion brewed with {air} and {water}"


def wisdom_potion() -> str:
    water = create_water()
    earth = create_earth()
    fire = create_fire()
    air = create_air()
    return f"Wisdom potion brewed with all elements: {water, earth, fire, air}"
