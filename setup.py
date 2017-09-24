# coding:utf-8
from setuptools import find_packages, setup
import epflutils


try:
    # Get the long description from the README file
    with open('README.md') as f:
        long_description = f.read()
except:
    long_description = "See README file"

setup(
    name='epfl-utils',

    version=epflutils.__version__,

    description='A simple package to provide tools common to several applications at EPFL.',
    long_description=long_description,

    url='https://github.com/epfl-idevelop/epfl-utils',

    author='Charmier Grégory',
    author_email='gregory.charmier@epfl.ch',

    license="MIT",

    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='EPFL development LDAPsearch',

    packages=find_packages(),

    install_requires=["ldap==1.0.2", "mock==2.0.0"],
)
