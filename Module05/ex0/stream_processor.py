from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class Dataprocessor:
    def __init__(self, data: Any):
        self.data = data

    def process(self):
        print(f"Processing data: {self.data}")

    def validation(self):
        print("Validation: ", end="")

    def output(self):
        print("Processed: ")


class NumericProcessor(Dataprocessor):
    def __init__(self, data):
        super().__init__(data)

    def validation(self):
        