#!/usr/bin/env python

# trade-crypto
#
# Copyright 2017-2020 Phanindra Reddy Madduru
#

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='trade-crypto',
    version='1.0',
    description='Python Algorithmic Trading - v0.1',
    long_description='Python library for backtesting stock trading strategies and live strategies.',
    author='Phanindra Reddy Madduru',
    author_email='phanindra.madduru@gmail.com',
    url='https://github.com/maddurup/trade-crypto',
    download_url='',
    packages=[
        'trade-crypto'
    ],
    install_requires=[
        "numpy",
        "gdax",
        "pandas",
        "requests",
        "pprint"
    ],
    extras_require={
        'Plotting':  ["matplotlib"],
        'trading API':  ["gdax"]
    },
)