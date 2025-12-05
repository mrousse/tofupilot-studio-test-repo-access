import random


class Counter:
    def __init__(self):
        self.value = 0

    def get_value(self):
        return self.value


class FailingPlug:
    def __init__(self):
        raise RuntimeError("Plug initialization failed intentionally")
