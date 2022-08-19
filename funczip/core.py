from typing import Callable, Any, List


class FuncZip:
    def __init__(self, func: Callable, *args: Any, **kwargs: Any):
        self.func: Callable = func
        self.args: Any = args
        self.kwargs: Any = kwargs
        self.modifiers:List[Callable]  = []

    def __str__(self) -> str:
        a = [f"{x}" for x in self.args]

        k = [f"{x}={y}" for x, y in self.kwargs.items()]
        return f"{self.func.__name__}({', '.join(a+k)})"

    def __repr__(self) -> str:
        a = [f"{x}" for x in self.args]

        k = [f"{x}={y}" for x, y in self.kwargs.items()]
        return f"<funczip target={self.func.__name__} arguments={', '.join(a+k)}>"
    def add_mod(self, mod: Callable):
        self.modifiers.append(mod)
    def __call__(self) -> Any:
        return self.func(*self.args, **self.kwargs)


def zip(*args, **kwargs):
    """Decorator for funczip.FuncZip"""

    def Inner(func):
        return FuncZip(func, *args, **kwargs)

    return Inner
