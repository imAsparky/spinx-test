# !/usr/bin/env python
"""Setup for cookiecutter-py3-package."""

from setuptools import find_packages, setup

__version__ = "0.1.6"

setup(
    name="cookiecutter-py3-package",
    packages=find_packages(exclude=("tests*", "testing*")),
    version=__version__,
    description="A sandbox to play with sphinx and test other tools",
    author="Mark Sevelj",
    license="BSD",
    author_email="mark.sevelj@dunwright.com.au",
    url="https://github.com/imAsparky/spinx-test",
    keywords=[
        "sphinx",
        "Python 3",
      
    ],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development",
    ],
)
