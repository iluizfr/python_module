from pydantic import BaseModel, model_validator, Field, ValidationError
from typing import Optional, List
from enum import Enum
import datetime


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime.datetime = Field()
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: Optional[str] = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def __validator(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Missions Id must starts with 'M'")

        cap = 0
        for member in self.crew:
            if member.rank == Rank.CAPTAIN or member.rank == Rank.COMMANDER:
                cap += 1
        if not cap:
            raise ValueError("At least one Commander or Captain")

        if self.duration_days > 365:
            crew_size = len(self.crew)
            experienced_member = 0

            for member in self.crew:
                if not member.is_active:
                    raise ValueError("All crew members must be active")
                if member.years_experience > 5:
                    experienced_member += 1

            if experienced_member < crew_size / 2:
                message = "half of crew of experienced members"
                raise ValueError(f"Long missions must have {message}")

        return self

    def info(self) -> None:
        print("Mission:", self.mission_name)
        print("ID:", self.mission_id)
        print("Destination:", self.destination)
        print(f"Durations: {self.duration_days} days")
        print(f"Budget: ${self.budget_millions}M")
        print("Crew size:", len(self.crew))
        print("Crew members:")
        for member in self.crew:
            esp = member.specialization
            print(f"- {member.name} ({member.rank.value}) - ({esp})")


def helper_info(member_id: str, name: str, rank: Rank, age: int,
                specialization: str, years_experience: int,
                is_active: bool) -> dict:
    return {
        "member_id": member_id,
        "name": name,
        "rank": rank,
        "age": age,
        "specialization": specialization,
        "years_experience": years_experience,
        "is_active": is_active
        }


def main() -> None:
    member_info01 = helper_info("AGV-12", "Sarah Connor", Rank.COMMANDER,
                                30, "Mission Commander", 6, True)
    member_info02 = helper_info("AGB-d6", "John Smit", Rank.LIEUTENANT,
                                34, "Navigator", 8, True)
    member_info03 = helper_info("ZGB-d6", "Alice Johnson", Rank.OFFICER,
                                27, "Engineering", 6, True)
    member_info04 = helper_info("AGD-12", "Jose Connor", Rank.CADET,
                                30, "Mission Commander", 5, True)
    member_info05 = helper_info("AGH-d6", "Nath Smit", Rank.CADET,
                                34, "Navigator", 8, True)
    member_info06 = helper_info("ZLB-d6", "Vodka Johnson", Rank.OFFICER,
                                27, "Engineering", 6, True)

    crew01 = [member_info01, member_info02, member_info03]
    crew02 = [member_info04, member_info05, member_info06]

    space_mission_info01 = {
        "mission_id": "M2024_MARS",
        "mission_name": "Mars Colony Establishment",
        "destination": "Mars",
        "launch_date": datetime.datetime.now(datetime.UTC),
        "duration_days": 900,
        "crew": crew01,
        "budget_millions": 2500.0
    }

    space_mission_info02 = {
        "mission_id": "M2024_MARS",
        "mission_name": "Zeptain Colony Establishment",
        "destination": "Zeptain",
        "launch_date": datetime.datetime.now(datetime.UTC),
        "duration_days": 400,
        "crew": crew02,
        "budget_millions": 500.0
    }

    print("Space Mission Crew Validation")
    print("=========================================")
    try:
        first_mission = SpaceMission.model_validate(space_mission_info01)
        print("Valid mission created:")
        first_mission.info()
    except ValidationError as err:
        for erro in err.errors():
            print(f"{erro['msg']}")

    print("\n=========================================")
    try:
        second_mission = SpaceMission.model_validate(space_mission_info02)
        second_mission.info()
    except ValidationError as err:
        print("Expected validation error:")
        for erro in err.errors():
            print(f"{erro['msg']}")


if __name__ == "__main__":
    main()
