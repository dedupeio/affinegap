#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, Extension
except ImportError :
    raise ImportError("setuptools module required, please go to https://pypi.python.org/pypi/setuptools and follow the instructions for installing setuptools")

# from Michael Hoffman's http://www.ebi.ac.uk/~hoffman/software/sunflower/
class NumpyExtension(Extension):

    def __init__(self, *args, **kwargs):
        Extension.__init__(self, *args, **kwargs)

        self._include_dirs = self.include_dirs
        del self.include_dirs  # restore overwritten property

    # warning: Extension is a classic class so it's not really read-only

    def get_include_dirs(self):
        from numpy import get_include

        return self._include_dirs + [get_include()]

    def set_include_dirs(self, value):
        self._include_dirs = value

    def del_include_dirs(self):
        pass
        
    include_dirs = property(get_include_dirs, 
                            set_include_dirs, 
                            del_include_dirs)


setup(
    name='affinegap',
    url='https://github.com/datamade/affinegap',
    version='1.2',
    description='A Cython implementation of the affine gap string distance',
    packages=['affinegap'],
    install_requires=['numpy'],
    ext_modules=[NumpyExtension('affinegap.affinegap', ['affinegap/affinegap.c'])],
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

