from distutils.core import setup
import sys



if 1:
    
    args = dict(
        name="funczip",
        version="0.1.1",
        description="A 100% useless python function zipping package.",
        packages=["funczip", "funczip.stack"],
    )

setup(
    script_args=copy_args,
    author="ThatRandomPerson5",
    **args,
)
