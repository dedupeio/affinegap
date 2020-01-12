#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, Extension
except ImportError :
    raise ImportError("setuptools module required, please go to https://pypi.python.org/pypi/setuptools and follow the instructions for installing setuptools")

try:
    from Cython.Build import cythonize
    use_cython = True
except ImportError:
    use_cython = False

if use_cython:
    ext_modules = cythonize([Extension('affinegap.affinegap',
                             ['affinegap/affinegap.pyx'])])
else:
    ext_modules = [Extension('affinegap.affinegap',
                             ['affinegap/affinegap.c'])]

setup(
    name='affinegap',
    url='https://github.com/datamade/affinegap',
    version='1.11',
    description='A Cython implementation of the affine gap string distance',
    packages=['affinegap'],
    ext_modules=ext_modules,
    license='The MIT License: http://www.opensource.org/licenses/mit-license.php',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Cython', 
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis']
    )
