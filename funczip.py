class funczip:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        a = [f"{x}" for x in self.args]

        k = [f"{x}={y}" for x, y in self.kwargs.items()]
        return f"{self.func.__name__}({', '.join(a+k)})"

    def __call__(self):
        return self.func(*self.args, **self.kwargs)
