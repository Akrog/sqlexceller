#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

import sqlexceller

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'sqlalchemy',
    'openpyxl',
    'six',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='sqlexceller',
    version=sqlexceller.__version__,
    description=("Command line program that executes SQL queries and stores "
                 "results in Excel files"),
    long_description=readme + '\n\n' + history,
    author="Gorka Eguileor",
    author_email='gorka@eguileor.com',
    url='https://github.com/akrog/sqlexceller',
    packages=[
        'sqlexceller',
    ],
    package_dir={'sqlexceller':
                 'sqlexceller'},
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    entry_points={
        'console_scripts': [
            'sqlexceller=sqlexceller.sqlexceller:main',
        ]
    },
    zip_safe=False,
    keywords='sqlexceller',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
