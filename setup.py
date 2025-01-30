#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Ryan Abernathey",
    author_email='ryan.abernathey@gmail.com',
    python_requires='>=3.10',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13'
    ],
    description="A simple CLI to interact with binder.",
    entry_points={
        'console_scripts': [
            'binderbot=binderbot.cli:main',
        ],
    },
    install_requires=[
        'Click>=7.0',
        'aiohttp',
        'yarl',
        'structlog',
        'nbformat',
        'nbconvert'
    ],
    include_package_data=True,
    keywords='binderbot',
    name='binderbot',
    packages=find_packages(include=['binderbot', 'binderbot.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/rabernat/binderbot',
    zip_safe=False,
)
