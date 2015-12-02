# -*- coding: utf-8 -*-
import unittest
import affinegap
import numpy

class AffineGapTest(unittest.TestCase):
    def setUp(self):
        self.affineGapDistance = affinegap.affineGapDistance
        self.normalizedAffineGapDistance = affinegap.normalizedAffineGapDistance
    
    def test_affine_gap_correctness(self):
        assert self.affineGapDistance('a', u'b', -5, 5, 5, 1, 0.5) == 5
        assert self.affineGapDistance('ab', 'cd', -5, 5, 5, 1, 0.5) == 10
        assert self.affineGapDistance('ab', 'cde', -5, 5, 5, 1, 0.5) == 13
        assert self.affineGapDistance('ab', u'cdë', -5, 5, 5, 1, 0.5) == 13
        assert self.affineGapDistance('a', 'cde', -5, 5, 5, 1, 0.5) == 8.5
        assert self.affineGapDistance('a', 'cd', -5, 5, 5, 1, 0.5) == 8
        assert self.affineGapDistance('b', 'a', -5, 5, 5, 1, 0.5) == 5
        assert self.affineGapDistance('a', 'a', -5, 5, 5, 1, 0.5) == -5
        assert self.affineGapDistance('a', '', -5, 5, 5, 1, 0.5) == 6
        assert self.affineGapDistance('', '', -5, 5, 5, 1, 0.5) == 0
        assert self.affineGapDistance('aba', 'aaa', -5, 5, 5, 1, 0.5) == -5
        assert self.affineGapDistance('aaa', 'aba', -5, 5, 5, 1, 0.5) == -5
        assert self.affineGapDistance('aaa', 'aa', -5, 5, 5, 1, 0.5) == -7
        assert self.affineGapDistance('aaa', 'a', -5, 5, 5, 1, 0.5) == -1.5
        assert self.affineGapDistance('aaa', '', -5, 5, 5, 1, 0.5) == 8
        assert self.affineGapDistance('aaa', 'abba', -5, 5, 5, 1, 0.5) == 1
    
    def test_normalized_affine_gap_correctness(self):
        with self.assertRaises(ZeroDivisionError) :
            self.normalizedAffineGapDistance('', '', -5, 5, 5, 1, 0.5)
        assert self.normalizedAffineGapDistance('a', '', -5, 5, 5, 1, 0.5) == 6

if __name__ == "__main__":
    unittest.main()

