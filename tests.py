# Just showing off some stuff
import funczip


def foo(val, **kwargs):
    print(val)
    print(kwargs)


z = funczip.FuncZip(foo, "hello world", a="9", b=10)
print(z)
z()


@funcxip.zip("Hello world")
def bar(val):
    print(val)


bar()

# What is the purpose of this? well it can make testing eaiser. To remove the automatic args you just tak off the decorator!
