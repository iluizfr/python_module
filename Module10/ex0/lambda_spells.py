def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda p: p["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda p: p["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda p: "*" + p + "*", spells))


def mage_stats(mages: list[dict]) -> dict:
    powerful_mage = max(mages, key=lambda p: p["power"])
    weakest_mage = min(mages, key=lambda p: p["power"])
    total = 0

    for mage in mages:
        total += mage["power"]

    avg_power = len(mages) / total
    return {
         "max_power": powerful_mage,
         "min_power": weakest_mage,
         "avg_power": round(avg_power, 2)
    }


def main() -> None:
    artifact01 = {
        "name": "Olho de pedra",
        "power": 10,
        "type": "Uso unico"
    }
    artifact02 = {
        "name": "Orbe",
        "power": 15,
        "type": "Uso unico"
    }
    artifact03 = {
        "name": "Mao de pedra",
        "power": 20,
        "type": "Uso unico"
    }
    mage01 = {
        "name": "Alfredo",
        "power": 49,
        "element": "Agua"
    }
    mage02 = {
        "name": "Robert",
        "power": 51,
        "element": "fogo"
    }
    mage03 = {
        "name": "Rogerio",
        "power": 59,
        "element": "terra"
    }

    artifacts = [artifact01, artifact02, artifact03]
    mages = [mage01, mage02, mage03]
    spells = ["fogo", "cura", "gelo"]

    print("Testing artifact sorter by power...")
    print("=================================")
    sorted_artifacts = artifact_sorter(artifacts)
    for artifact in sorted_artifacts:
        print(f"{artifact["name"]} ({artifact["power"]}), {artifact["type"]}")

    print("\nTesting mages who have enough power (>= 50)")
    print("=================================")
    sorted_mages = power_filter(mages, 50)
    for mage in sorted_mages:
        print(f"{mage["name"]}, power: {mage["power"]}")

    print("\nTesting spell trasformer..")
    print("=================================")
    trasformed_spells = spell_transformer(spells)
    for spell in trasformed_spells:
        print(spell)


if __name__ == "__main__":
    main()
