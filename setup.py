from setuptools.command.install import install
from distutils.core import setup

args = {}
copy_args=sys.argv[1:]
if '-t=funczip' in copy_args:
  copy_args.remove('-t=funczip')
  args=dict(
    name="funczip",
    version="0.1.0",
    description="A 100% useless python function zipping package.",
    packages=["funczip","funczip.stack"],
  )

setup(

    author="ThatRandomPerson5",
    **args,
)
