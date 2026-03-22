from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:

        if criteria is None:
            return data_batch

        filtered_data = []
        criteria_lower = criteria.lower()

        for item in data_batch:
            item_str = str(item).lower()

            if criteria_lower in item_str:
                filtered_data.append(item)

        return filtered_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream id": self.stream_id,
            "processed_count": self.processed_count
        }


class SensorStream(DataStream):
    sensor_type = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            temps: List[float] = []
            total_items = len(data_batch)

            for item in data_batch:
                if isinstance(item, dict):
                    if "temp" in item:
                        temps.append(item["temp"])

            self.processed_count += total_items
            if len(temps) > 0:
                soma = 0.0

                for temp in temps:
                    soma += temp

                avg_temp = soma / len(temps)
            else:
                avg_temp = 0.0

            return f"{total_items} readings processed, avg temp: {avg_temp}°C"

        except Exception as err:
            return f"Sensor error: {err}"

    def filter_data(self, data_batch: List[Any],
                    criteria: str | None = None) -> List[Any]:
        if criteria == "critical":
            filtered_data = []

            for item in data_batch:
                if not isinstance(item, dict):
                    continue

                temperature = item.get("temp", 0)
                if temperature > 50:
                    filtered_data.append(item)

            return filtered_data

        return super().filter_data(data_batch, criteria)


class TransactionStream(DataStream):
    transaction_type = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:

            blc = 0
            for item in data_batch:
                if isinstance(item, dict):
                    for key, value in item.items():
                        if key == "buy":
                            blc -= value
                        elif key == "sell":
                            blc += value

            self.processed_count += len(data_batch)

            n_trans = len(data_batch)
            return f"Transactions: {n_trans} operations, net flow: {blc}"
        except Exception as err:
            return f"Transaction error: {err}"

    def filter_data(self, data_batch: List[Any],
                    criteria: str | None = None) -> List[Any]:
        if criteria == "large":
            filtered_data = []

            for item in data_batch:
                if not isinstance(item, dict):
                    continue

                amount = item.get("amount", 0)
                if amount > 100:
                    filtered_data.append(item)

            return filtered_data

        return super().filter_data(data_batch, criteria)


class EventStream(DataStream):
    event_type = "System Events"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            errors = sum(1 for item in data_batch if item == "error")

            self.processed_count += len(data_batch)

            return f"Events {len(data_batch)} events, {errors} error detected"
        except Exception as err:
            return f"Event error: {err}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "error":
            return [err for err in data_batch if err == "error"]
        return super().filter_data(data_batch, criteria)


class StreamProcessor:
    def __init__(self) -> None:
        self.streams = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batches: List[List[Any]]) -> None:
        print("\n=== Polymorphic Processing ===")

        for stream, batch in zip(self.streams, batches):
            result = stream.process_batch(batch)
            print(result)

    def filter_all(self, batches: List[List[Any]], criteria: str) -> None:
        print(f"\nFiltering with criteria: {criteria}")

        for stream, batch in zip(self.streams, batches):
            filtered = stream.filter_data(batch, criteria)

            if filtered:
                print(f"{stream.stream_id}: {filtered}")
            else:
                print(f"{stream.stream_id}: No mathces")


def main():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print("\nInitializing Sensor Stream...")
    ss = SensorStream("SENSOR_001")
    sensor_batch = [
        {"temp": 22.5},
        {"humidity": 65},
        {"pressure": 1013}
    ]
    print(f"Stream id: {ss.stream_id}, Type: {ss.sensor_type}")
    print(f"Processing sensor batch: {sensor_batch}")
    print(f"Sensor analysis: {ss.process_batch(sensor_batch)}")

    print("\nInitializing Transaction Stream...")
    ts = TransactionStream("TRANS_001")
    transactional_batch = [
        {"buy": 100},
        {"sell": 150},
        {"buy": 75}
    ]
    print(f"Stream id: {ts.stream_id}, Type: {ts.transaction_type}")
    print(f"Processing trasactional batch: {transactional_batch}")
    print(f"Transactional analysis: {ts.process_batch(transactional_batch)}")

    print("\nInitializing Event Stream...")
    es = EventStream("EVENT_001")
    event_batch = [
        "login",
        "error",
        "logout"
    ]
    print(f"Event id: {es.stream_id}, Type: {es.event_type}")
    print(f"Processing event batch: {event_batch}")
    print(f"Event analysis: {es.process_batch(event_batch)}")

    processor = StreamProcessor()
    processor.add_stream(ss)
    processor.add_stream(ts)
    processor.add_stream(es)

    batches = [sensor_batch, transactional_batch, event_batch]

    processor.process_all(batches)
    processor.filter_all(batches, "critical")

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
