#Metodo tradicional usando o  >> setuptools
from setuptools import setup, find_packages

setup(
    name="dundie",
    version="0.1.0",
    description="Rewasr Point System for Dunder Mifflin",
    author="Tiago Yamaguti",
    packages=find_packages(),
)