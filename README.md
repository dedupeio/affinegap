affinegap
=========

A Cython implementation of the [affine gap penalty string distance](http://en.wikipedia.org/wiki/Gap_penalty#Affine_Gap_Penalty) also known as the [Smith–Waterman algorithm](http://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm)

[![Build Status](https://travis-ci.org/datamade/affinegap.svg?branch=master)](https://travis-ci.org/datamade/affinegap)

## To install
```bash
pip install affinegap
```

## To use
```python
import affinegap
d1 = affinegap.affineGapDistance('foo', 'bar')
d2 = affinegap.affineGapDistance('foo', 'bar',
                                 matchWeight = 1,
                                 mismatchWeight = 11,
                                 gapWeight = 10,
                                 spaceWeight = 7,
                                 abbreviation_scale = .125)
d3 = affinegap.normalizedAffineGapDistance('foo', 'bar')
```

## To get set up for development
```bash
git clone https://github.com/datamade/affinegap.git
cd affinegap
pip install -r requirements
cython affinegap/*.pyx
python setup.py develop
nosetests
```
