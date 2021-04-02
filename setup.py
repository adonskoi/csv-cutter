#!/usr/bin/env python
import os
from setuptools import find_packages, setup

def _read_requirements():
    with open(os.path.join(os.path.dirname(__file__), "requirements.txt"), "r") as f:
        return f.readlines()


setup(name='csv-cutter',
      version='0.1.0',
      description='cut csv file',
      packages=find_packages(),
      author='Donskoi Aleksandr',
      author_email='donskoy.alexander@gmail.com',
      install_requires=_read_requirements()
     )