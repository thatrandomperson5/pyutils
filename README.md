# pyutils
Just some random python utils, idk


## List of things
* [funczip](https://github.com/thatrandomperson5/pyutils#funczip)
* [functrain](https://github.com/thatrandomperson5/pyutils#functrain)

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
# Functrain
Which looks eaiser to read? 
This:
```py
print(rng(rng(rng(rng(rng(rng(30)))))))  
```
Or this:
```py
(
    rng.start(30)
        .next(rng)
        .next(rng)
        .next(rng)
        .next(rng)
        .next(rng)
        .next(print)
)
```
If you think the second one does you should use functraining!
```py
from functrain import functrain
import random
@functrain
def rng(num):
    return random.randrange(num+5)

print(rng(rng(rng(rng(rng(rng(30)))))))    

(
    rng.start(30)
        .next(rng)
        .next(rng)
        .next(rng)
        .next(rng)
        .next(rng)
        .next(print)
)
```
## Details
You can start a functrain function with `.start(*args, **kwargs)`. From then on you can do `.next(function, *args, **kwargs)` to run a function with the retun value of the orginal function. If you ever wan't to end the train and get the value diretcly you can do `.end()`or `()`
Example:
```py
#myfunc is a functrain
a=( #Get the final value
    myfunc.start(arg1, arg2) # Returns a trainable
        .next(myfunc, arg2) # Arg 1 is the return value of the fisrt myfunc
        .next(myfunc, arg2) # Arg 1 is the return value of the myfunc above
        .next(myfunc, arg2).end() # Or just .next()(), This returns the return value instead of a trainable object. You could also just do a.value if you don't end it.
) 
print(a)
```
# Install
```
pip install git+https://github.com/thatrandomperson5/pyutils.git
```

