"""

  Petra-M setuptools based setup module.

"""
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name='PetraM_RF',
    version='1.2.6',

    description='PetraM RF package',
    long_description=long_description,
    url='https://github.com/piScope/PetraM',
    author='S. Shiraiwa',
    author_email='shiraiwa@psfc.mit.edu',
    license='GNUv3',

    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Physics',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='MFEM physics',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[],
    extras_require={},
    package_data={},
    data_files=[],
    entry_points={},
)
