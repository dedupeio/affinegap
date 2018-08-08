affinegap
=========

A Cython implementation of the [affine gap penalty string distance](http://en.wikipedia.org/wiki/Gap_penalty#Affine_Gap_Penalty) also known as the [Smith–Waterman algorithm](http://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm)

[![Build Status](https://travis-ci.org/dedupeio/affinegap.svg?branch=master)](https://travis-ci.org/dedupeio/affinegap)

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
git clone https://github.com/dedupeio/affinegap.git
cd affinegap
pip install -r requirements.txt
cython affinegap/*.pyx
python setup.py develop
pytest
```

## Team

* Forest Gregg, Dedupeio

## Errors and Bugs

If something is not behaving intuitively, it is a bug and should be reported.
Report it here by creating an issue: https://github.com/dedupeio/affinegap/issues

Help us fix the problem as quickly as possible by following [Mozilla's guidelines for reporting bugs.](https://developer.mozilla.org/en-US/docs/Mozilla/QA/Bug_writing_guidelines#General_Outline_of_a_Bug_Report)

## Patches and Pull Requests

Your patches are welcome. Here's our suggested workflow:

* Fork the project.
* Make your feature addition or bug fix.
* Send us a pull request with a description of your work. Bonus points for topic branches!

## Copyright and Attribution

Copyright (c) 2016 Forest Gregg and Dedupeio. Released under the [MIT License](https://github.com/dedupeio/affinegap/blob/master/LICENSE).
