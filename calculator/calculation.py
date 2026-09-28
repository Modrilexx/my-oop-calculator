from abc import ABC, abstractmethod


class Calculation(ABC):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @abstractmethod
    def get_result(self):
        pass


class Add(Calculation):
    def get_result(self):
        return self.a + self.b


class Subtract(Calculation):
    def get_result(self):
        return self.a - self.b