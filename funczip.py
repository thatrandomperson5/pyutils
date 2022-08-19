from typing import Callable, Any
class funczip:
    def __init__(self, func: Callable, *args: Any, **kwargs: Any):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __str__(self) -> str:
        a = [f"{x}" for x in self.args]

        k = [f"{x}={y}" for x, y in self.kwargs.items()]
        return f"{self.func.__name__}({', '.join(a+k)})"

    def __call__(self) -> Any:
        return self.func(*self.args, **self.kwargs)
