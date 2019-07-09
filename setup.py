# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='ukrdict',
    description='Library for searching ukrainian words meaning.',
    version='0.1',
    author_email='aserhii@protonmail.com',
    author='serhii73',
    license='MIT License',
    url='https://github.com/serhii73/python_sum_in_ua_api',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={'console_scripts': ['ukrdict = ukrdict.main:main']},
)
