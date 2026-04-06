from enum import Enum
from ex0.Card import Card


class EffectType(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = self.__set_effect(effect_type)
        self.kind = "Spell"

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Deal 3 damage to target"}

    def __set_effect(self, effect_type: str):
        for effect in EffectType:
            if effect == effect_type:
                return effect
        return "Error: Wrong effect type [damage, heal, buff, debuff]"

    def resolve_effect(self, targets: list) -> dict:
        if self.effect_type == "damage":
            return {
                "effect": "damage",
                "targets": targets,
                "value": 3}

        elif self.effect_type == "heal":
            return {
                "effect": "heal",
                "targets": targets,
                "value": 3}

        elif self.effect_type == "buff":
            return {
                "effect": "buff",
                "targets": targets,
                "value": "+2 attack"}

        elif self.effect_type == "debuff":
            return {
                "effect": "debuff",
                "targets": targets,
                "value": "-2 attack"}

        return {"effect": "none"}
