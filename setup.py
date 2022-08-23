from setuptools.command.install import install
from distutils.core import setup
import sys


global args
args = {}
copy_args = sys.argv[1:]
if "--targetv=funczip" in copy_args:
    copy_args.remove("-t=funczip")
    args = dict(
        name="funczip",
        version="0.1.1",
        description="A 100% useless python function zipping package.",
        packages=["funczip", "funczip.stack"],
    )
print(args)
setup(
    script_args=copy_args,
    author="ThatRandomPerson5",
    **args,
)
