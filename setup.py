from os import path
from setuptools import find_packages, setup

DIR_PATH = path.dirname(path.realpath(__file__))
VERSION_FILE = path.join(DIR_PATH, 'VERSION')

try:
    version = open(VERSION_FILE).read().strip()
except:
    version='0.0.1'

setup(
    name='mycli',
    version=version,
    description='dummy CLI with argparse',
    url='https://github.com/sahibdhanjal',
    maintainer='Sahib Dhanjal',
    packages=find_packages(exclude=[]),
    install_requires=[],
    package_data={'mycli':['./../VERSION']},
    entry_points={'console_scripts': ['mycli = mycli.__main__:main']},
)
