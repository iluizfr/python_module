from typing import Optional
from pydantic import BaseModel, Field, ValidationError
import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime.datetime = Field()
    is_operational: Optional[bool] = True
    notes: Optional[str] = Field(default=None, max_length=200)

    def info(self):
        m = "Non-Operational"
        print(f"ID: {self.station_id}")
        print(f"Name: {self.name}")
        print(f"Crew: {self.crew_size} people")
        print(f"Power: {self.power_level}%")
        print(f"Oxygen: {self.oxygen_level}%")
        print(f"Status: {"Operational" if self.is_operational else m}")


def main() -> None:
    data01 = {
        "station_id": "IRS2000",
        "name": "LUIS SPACE-STATION",
        "crew_size": 13,
        "power_level": 54.8,
        "oxygen_level": 66.8,
        "last_maintenance": datetime.datetime.now(datetime.UTC),
        "is_operational": True,
        "notes": "The space looks good for traveling!"
    }

    data02 = {
        "station_id": "IRS2001",
        "name": "Felipe SPACE-STATION",
        "crew_size": -1,
        "power_level": 54.8,
        "oxygen_level": 66.8,
        "last_maintenance": datetime.datetime.now(datetime.UTC),
        "is_operational": True,
        "notes": "The space looks good for traveling!"
    }

    try:
        space_station01 = SpaceStation.model_validate(data01)
        print("Space Station Data Validation")
        print("========================================")
        space_station01.info()
    except ValidationError as erro:
        print("Expected validation error:")
        for error in erro.errors():
            print(f"Fild: {error['loc'][0]}, Error: {error['msg']}")

    try:
        space_station02 = SpaceStation.model_validate(data02)
        print("Space Station Data Validation")
        print("========================================")
        space_station02.info()
    except ValidationError as erro:
        print("\n========================================")
        print("Expected validation error:")
        for error in erro.errors():
            print(f"Fild: {error['loc'][0]}, Error: {error['msg']}")


if __name__ == "__main__":
    main()
