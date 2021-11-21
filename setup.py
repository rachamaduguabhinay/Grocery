import os
from setuptools import setup, find_packages

setup(
    name='grocery',
    version='0.0.2',
    author_email='abhinay.rachamadugu@gmail.com',
    license='Test',
    description='Convert CSV to automatically nested JSON.',
    keywords="convert csv auto nested json",
    packages=find_packages(include=["generator", "generator.*"]),
    install_requires=[],
    python_requires='>=3.0',
    entry_points={'console_scripts': ['generator=generator.__main__:main']}
)