from .. import core
from typing import Callable, Any, List
from dataclasses import dataclass
import inspect


@dataclass
class ModMethod:
    func: Callable

    def __call__(self, *args: Any, **kwargs: Any):
        return self.func(*args, **kwargs)


class FuncZip(core.FuncZip):
    def __init__(self, func: Callable, *args: Any, **kwargs: Any) -> None:
        self.modifiers: List[Callable] = []
        self.args: Any = []
        self.kwargs: Any = {}
        self.func: Callable = func
        self.setup(*args, **kwargs)
        for name, method in inspect.getmembers(self):
            if not name.startswith("_"):
                if isinstance(method, ModMethod):

                    self.add_mod(method)

    def setup(self, *args: Any, **kwargs: Any) -> None:
        pass

    def add_args(self, *args: Any, **kwargs: Any) -> None:
        self.args = args
        self.kwargs = kwargs

    def __call__(self) -> Any:
        func = self
        for mod_ in self.modifiers:
            func = mod_(func)
        return func.func(*self.args, **self.kwargs)


def mod(func: Callable) -> None:
    return ModMethod(func)

