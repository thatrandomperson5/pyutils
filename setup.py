from setuptools.command.install import install
from distutils.core import setup

class InstallCommand(install):
    user_options = install.user_options + [
        ('funczip', None, None), # a 'flag' option
    ]

    def initialize_options(self):
        install.initialize_options(self)
        self.funczip = None
        

    def finalize_options(self):
        
        install.finalize_options(self)

    def run(self):
        global funczip
        funczip = self.funczip # will be 1 or None
        install.run(self)


setup(
    name="funczip",
    version="0.1.0",
    description="A 100% useless python function zipping package.",
    author="ThatRandomPerson5",
    cmdclass={
        'install': InstallCommand,
    },
)
