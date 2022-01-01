# cython: boundscheck=False, wraparound=False
# cython: cdivision=True
# cython: c_string_type=unicode, c_string_encoding=utf8
# cython: language_level=3

from libc cimport limits
from libc.stdlib cimport malloc, free

cpdef float affineGapDistance(str string_a, str string_b,
                              float matchWeight = 1,
                              float mismatchWeight = 11,
                              float gapWeight = 10,
                              float spaceWeight = 7,
                              float abbreviation_scale = .125):
    """
    Calculate the affine gap distance between two strings 
    
    Default weights are from Alvaro Monge and Charles Elkan, 1996, 
    "The field matching problem: Algorithms and applications" 
    http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.23.9685
    """

    cdef int length1 = len(string_a)
    cdef int length2 = len(string_b)

    if (string_a == string_b and
        matchWeight == min(matchWeight,
                           mismatchWeight,
                           gapWeight)):
        return matchWeight * length1

    if length1 < length2 :
        string_a, string_b = string_b, string_a
        length1, length2 = length2, length1

    # Initialize C Arrays
    cdef int memory_size = sizeof(float) * (length1+1)
    cdef float *D = <float*> malloc(memory_size)
    cdef float *V_current = <float*> malloc(memory_size)
    cdef float *V_previous = <float*> malloc(memory_size)

    cdef int i, j
    cdef float distance

    # Set up Recurrence relations
    #
    # Base conditions
    # V(0,0) = 0
    # V(0,j) = gapWeight + spaceWeight * i
    # D(0,j) = Infinity
    V_current[0] = 0
    for j in range(1, length1 + 1) :
        V_current[j] = gapWeight + spaceWeight * j
        D[j] = limits.INT_MAX

    for i in range(1, length2 +1) :
        char2 = string_b[i-1]
        # V_previous = V_current
        for _ in range(0, length1 + 1) :
            V_previous[_] = V_current[_]

        # Base conditions    
        # V(i,0) = gapWeight + spaceWeight * i
        # I(i,0) = Infinity 
        V_current[0] = gapWeight + spaceWeight * i
        I = limits.INT_MAX
    
        for j in range(1, length1+1) :
            char1 = string_a[j-1]

            # I(i,j) is the edit distance if the jth character of string 1
            # was inserted into string 2.
            #
            # I(i,j) = min(I(i,j-1), V(i,j-1) + gapWeight) + spaceWeight
            if j <= length2 :
                I = min(I, V_current[j-1] + gapWeight) + spaceWeight
            else :
                # Pay less for abbreviations
                # i.e. 'spago (los angeles) to 'spago'
                I = (min(I, V_current[j-1] + gapWeight * abbreviation_scale)
                     + spaceWeight * abbreviation_scale)
        
            # D(i,j) is the edit distance if the ith character of string 2
            # was deleted from string 1
            #
            # D(i,j) = min((i-1,j), V(i-1,j) + gapWeight) + spaceWeight
            D[j] = min(D[j], V_previous[j] + gapWeight) + spaceWeight
                    
            # M(i,j) is the edit distance if the ith and jth characters
            # match or mismatch
            #
            # M(i,j) = V(i-1,j-1) + (matchWeight | misMatchWeight)    
            if char2 == char1 :
                M = V_previous[j-1] + matchWeight
            else:
                M = V_previous[j-1] + mismatchWeight
            
            # V(i,j) is the minimum edit distance 
            #    
            # V(i,j) = min(E(i,j), F(i,j), G(i,j))
            V_current[j] = min(I, D[j], M)

    distance = V_current[length1]

    free(D)
    free(V_current)
    free(V_previous)

    return distance

cpdef float normalizedAffineGapDistance(str string_a, str string_b,
                                        float matchWeight = 1,
                                        float mismatchWeight = 11,
                                        float gapWeight = 10,
                                        float spaceWeight = 7,
                                        float abbreviation_scale = .125) except? 999 :

    cdef int length1 = len(string_a)
    cdef int length2 = len(string_b)

    cdef float normalizer = length1 + length2

    if normalizer == 0:
        raise ZeroDivisionError('normalizedAffineGapDistance cannot take two empty strings')

    cdef float distance = affineGapDistance(string_a, string_b,
                                            matchWeight,
                                            mismatchWeight,
                                            gapWeight,
                                            spaceWeight,
                                            abbreviation_scale)

    return distance/normalizer
