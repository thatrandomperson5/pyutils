from dataclasses import dataclass
from typing import Any


@dataclass
class Trainable:
    value: Any

    def next(self, func, *args, **kwargs):
        a = func(self.value, *args, **kwargs)
        self.value = a

        return self

    def __call__(self):
        return self.end()

    def end(self):
        return self.value
