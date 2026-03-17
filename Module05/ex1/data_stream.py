from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id = stream_id
        self.stream_type = stream_type

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"Stream id": self.stream_id,
                "Type": self.stream_type}


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")
        print("\nInitializing Sensor Stream...")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if not isinstance(data_batch, list):
                raise ValueError("Data batch must be a list")

            print(f"Processing sensor batch{data_batch}")

            op = len(data_batch)
            soma = 0
            tmp_len = 0

            for data in data_batch:
                for key, value in data.items():
                    if key == "temp":
                        soma += value
                        tmp_len += 1

            if tmp_len == 0:
                raise ZeroDivisionError("No 'temp' in list")

            avg = soma / tmp_len

            return f"Sensor analysis: {op} reading processed, avg temp: {avg:.1f}°C"

        except Exception:
            return "Something went wrong"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")
        print("\nInitializing Transaction Stream...")


class EventStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id, "System Events")
        print("\nInitializing Event Stream...")


class StreamProcessor:
    pass


def main():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    sensor_stream = SensorStream("SENSOR_001")
    print(sensor_stream.get_stats())
    sensor_stream.process_batch(["temp": 22.5, "humidity": 65, "pressure": 1013])

if __name__ == "__main__":
    main()
