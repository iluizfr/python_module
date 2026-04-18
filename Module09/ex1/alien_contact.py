from pydantic import BaseModel, model_validator, Field, ValidationError
from typing import Optional
from enum import Enum
import datetime


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPHATIC = "telephatic"


class AlianContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime.datetime = Field()
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=100.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def __validator(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("Error: ID Contact from alian must start with AC")

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise Exception("Error: Physical must be verified")

        c_type = ContactType.TELEPHATIC
        if self.contact_type == c_type and self.witness_count < 3:
            raise ValueError("Error: Telephatic contact must have 3 witness")

        if self.signal_strength > 7.0 and not self.message_received:
            raise Exception("Error: Strong signal must include a message")
        return self

    def info(self) -> None:
        print("ID:", self.contact_id)
        print("Type:", self.contact_type.value)
        print("Location:", self.location)
        print(f"Signal: {self.signal_strength/10:.1f}/10")
        print(f"Duration: {self.duration_minutes} minutes")
        print("Witnesses:", self.witness_count)
        print(f"Message: '{self.message_received}'")


def main() -> None:
    good_params = {
        "contact_id": "AC_2024_001",
        "timestamp": datetime.datetime.now(datetime.UTC),
        "location": "Area 51, Nevada",
        "contact_type": ContactType.RADIO,
        "signal_strength": 85.0,
        "duration_minutes": 45,
        "witness_count": 5,
        "message_received": "Greetings from Zeta Reticuli"
    }

    bad_params = {
        "contact_id": "AC_2024_002",
        "timestamp": datetime.datetime.now(datetime.UTC),
        "location": "Area 52, Nevada",
        "contact_type": ContactType.TELEPHATIC,
        "signal_strength": 85.0,
        "duration_minutes": 45,
        "witness_count": 1,
        "message_received": "Greetings from Zeta Reticuli"
    }

    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    try:
        first_alian_contact = AlianContact.model_validate(good_params)
        first_alian_contact.info()
    except ValidationError as err:
        for erro in err.errors():
            print(f"{erro['msg']}")

    print("\n======================================")
    print("Expected validation error:")
    try:
        second_alian_contact = AlianContact.model_validate(bad_params)
        second_alian_contact.info()
    except ValidationError as err:
        for erro in err.errors():
            print(f"{erro['msg']}")


if __name__ == "__main__":
    main()
