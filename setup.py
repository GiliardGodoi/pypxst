from setuptools import setup, find_packages

from .pypxst import __version__

setup(
    name='pypxst',
    version = __version__,
    packages=find_packages()
)