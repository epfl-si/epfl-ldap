# coding:utf-8
import os
import epflutils
from setuptools import find_packages, setup


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='epfl-utils',
    version=epflutils.__version__,
    packages=find_packages(),
    include_package_data=True,
    license="LGPLv3",
    description='A simple package to provide tools common to several applications at EPFL.',
    long_description="",
    url='https://charmier@git.epfl.ch/repo/epfl-utils.git',
    author='Charmier Grégory',
    author_email='gregory.charmier@epfl.ch',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)
