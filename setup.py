from setuptools import setup
from setuptools import find_packages

version = open('VERSION').read().strip()

setup(
    name='scholarpy',
    version=version,
    packages=find_packages(exclude='tests'),
    url='https://github.com/ckreibich/scholar.py',
    scripts=['scholarpy/scholar.py'],
    install_requires=[
        'beautifulsoup4',
    ]
)
