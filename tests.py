#Just showing off some stuff
import funczip

def lol(val, **kwargs):
    print(val)
    print(kwargs)
z = funczip.funczip(lol, "hello world", a="9", b=10)
print(z)
z()
