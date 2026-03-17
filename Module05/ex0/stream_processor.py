from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        print("\nInitializing Numeric Processor...")

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid data")

            dlen = len(data)
            dsum = sum(data)
            davg = dsum / dlen
            return f"Processed {dlen} numeric values, sum={dsum}, avg={davg}"

        except Exception:
            return "Something went wrong.."

    def validate(self, data: Any) -> bool:
        if type(data) is not list:
            print("Validation: Data must be a list of integers.")
            return False

        else:
            for i in data:
                if type(i) is not int:
                    print("Validation: Only numbers in the list.")
                    return False

            print("Validation: Numeric data verified")
            return True

    def format_output(self, result: Any) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        print("\nInitializing Text Processor...")

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid data")

            len_data = len(data)
            n_word = len(data.split())
            return f"Processed text: {len_data} characters, {n_word} words"

        except Exception:
            return "Something went wrong.."

    def validate(self, data: Any) -> bool:
        if data.__class__ is not str:
            print("Validation: Data must be a string..")
            return False

        if not data.strip():
            print("Validation: Empty string..")
            return False

        print("Validation: Text data verified")
        return True

    def format_output(self, result: Any) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        print("\nInitializing Log Processor...")

    def process(self, data: Any) -> str:
        try:
            sep_data = data.split(":", 1)

            if sep_data[0] == "ERROR":
                return f"[ALERT] ERROR level detected: {sep_data[1]}"

            if sep_data[0] == "INFO":
                return f"[INFO] INFO level detected: {sep_data[1]}"

            return "Unknown log level"

        except Exception:
            return "Something went wrong.."

    def validate(self, data: Any) -> bool:
        if data.__class__ is not str:
            print("Validation: Log entry must be a string")
            return False

        if not data.strip():
            print("Validation: Empty Log entry..")
            return False

        try:
            sep_log = data.split(":", 1)

            if len(sep_log) != 2:
                print('Validation: Log must be: "level: message"')
                return False

            if sep_log[0] != "ERROR" and sep_log[0] != "INFO":
                print("Validation: Log must be: \"nivel: message\"")
                return False

        except Exception:
            return "Something went wrong.."

        print("Validation: Log entry verified")
        return True

    def format_output(self, result: Any) -> None:
        return super().format_output(result)


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    numeric_processor = NumericProcessor()
    data = [1, 2, 3, 4, 5]
    print(f"Processing data: {data}")
    numeric_processor.process(data)
    numeric_processor.validate(data)
    print(numeric_processor.format_output(numeric_processor.process(data)))

    text_processor = TextProcessor()
    data02 = "Hello Nexus World"
    print(f"processing data: {data02}")
    text_processor.process(data02)
    text_processor.validate(data02)
    print(text_processor.format_output(text_processor.process(data02)))

    log_processor = LogProcessor()
    data03 = "ERROR: Connection timeout"
    print(f"Processing data: {data03}")
    log_processor.process(data03)
    log_processor.validate(data03)
    print(log_processor.format_output(log_processor.process(data03)))

    print("\n=== Polymorphic Processing Demo ===\n")
    print("Processing multiple data types through same interface...")

    test_all = [numeric_processor, text_processor, log_processor]
    datas = [[1, 2, 3], "Hello World!", "INFO: System ready!"]
    i = 0
    j = 1
    for test in test_all:
        print(f"Result {j}: {test.format_output(test.process(datas[i]))}")
        i += 1
        j += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
