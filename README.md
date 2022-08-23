# pyutils
Just some random python utils, idk


## List of things
* [funczip](https://github.com/thatrandomperson5/pyutils#funczip)

# Funczip
Just a function zipped with arguments.


### Simple example
```py
import funczip

@funczip.zip("Hello world")
def bar(val):
    print(val)


bar()
```
Output: `Hello world`

## Modded example
```py
import funczip

class Remote:
    def __init__(self, *args, **kwargs):
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

```
Output: `Hello world a b`
### Install
```
pip install git+https://github.com/thatrandomperson5/pyutils.git --funczip
```
