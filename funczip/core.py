from typing import Callable, Any, List


class FuncZip:
    def __init__(self, func: Callable, *args: Any, **kwargs: Any):
        self.func: Callable = func
        self.args: Any = args
        self.kwargs: Any = kwargs
        self.modifiers: List[Callable] = []

    def __str__(self) -> str:
        a = [f"{x}" for x in self.args]

        k = [f"{x}={y}" for x, y in self.kwargs.items()]
        return f"{self.func.__name__}({', '.join(a+k)})"

    def __repr__(self) -> str:
        a = [f"{x}" for x in self.args]

        k = [f"{x}={y}" for x, y in self.kwargs.items()]
        return f"<funczip target={self.func.__name__} arguments={', '.join(a+k)}>"

    def add_mod(self, mod: Callable) -> None:
        self.modifiers.append(mod)

    def del_mod(self, mod: Callable) -> None:
        self.modifiers.remove(mod)

    def __call__(self) -> Any:
        func = self.func
        for mod_ in self.modifiers:
            func = mod_(func)
        return func(*self.args, **self.kwargs)


def zip(*args: Any, **kwargs: Any) -> Callable:
    """Decorator for funczip.FuncZip"""

    def Inner(func: Callable) -> FuncZip:
        return FuncZip(func, *args, **kwargs)

    return Inner
def mod(mod_: Callable) -> Callable:
    """Sub decorator for funczip.zip. Adds a modifier"""
    def Inner(fz: FuncZip) -> FuncZip:
        fz.add_mod(mod_)
        return fz
    return Inner
