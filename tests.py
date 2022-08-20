# Just showing off some stuff
import funczip


def foo(val, **kwargs):
    print(val)
    print(kwargs)


z = funczip.FuncZip(foo, "hello world", a="9", b=10)
print(z)
z()

class Remote:
    def __init__(self,*args, **kwargs):
        self.args = args
        self.kwargs = kwargs
    def add(self, func):
        func.args += self.args
        func.kwargs.update(self.kwargs)
        return func

r = Remote("a", "b")

@funczip.mod(r.add)
@funczip.zip("Hello world")
def bar(val, a, b):
    print(val, a, b)


bar()

# What is the purpose of this? well it can make testing eaiser. To remove the automatic args you just tak off the decorator!
