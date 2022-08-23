from distutils.core import setup

pkgs = []
if "--funczip" in sys.argv:
    pkgs = ["funczip", "funczip.stack"]


setup(
    name="funczip",
    version="0.1.0",
    description="A 100% useless python function zipping package.",
    author="ThatRandomPerson5",
    packages=pkgs,
)
