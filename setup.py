__author__ = 'shusei'

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


setup(
    name="pyicic",
    version="0.1.dev1",
    description="A simple The imaging Source python binding library",
    url="https://github.com/shumasud/py-ic-imaging-control",
    author="Shusei Masuda",
    author_email="mash0131@gmail.com",
    license="MIT",
    packages=find_packages(),
    package_data={
        "":['*.txt', '*.rst', '*.dll']
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities"
    ]

)

