import numpy as np
import pandas as pd
import random

"""
====================
SIMPLE RANDOM SAMPLE
====================
Sampling (w/o replacement) that uses the random library to select, at random,
the elements from the data_set from which the sample is created, until the
number of elements selected equals the desired sample size form the user.
"""
def rand_sample(data_set, sample_size, replacement=False):
    # assert certain values and types of data given
    assert (isinstance(data_set, np.ndarray) and isinstance(sample_size, int) and isinstance(replacement, bool)), "data_set should be of type numpy.ndarray or pandas.Series, sample_size of type int, and replacement of type bool" # check correct data types of variables
    assert (len(data_set) >= sample_size), "The sample size must be less than or equal to the size of the data_set given" # ensure sample size in less than or equal to the population size of the data set

    # create sample according to the given size, empty
    random.seed()
    sample = np.empty(sample_size)

    # delete data from data_set once used, should be w/o replacement
    if replacement is False:
        for i in range(len(sample)):
            max_range = len(data_set) - 1
            temp = random.randint(0, max_range)
            sample[i] = data_set[temp]
            data_set = np.delete(data_set, temp)
    else:
        max_range = len(data_set) - 1
        for i in range(len(sample)):
            temp = random.randint(0, max_range)
            sample[i] = data_set[temp]

    return sample


"""
==========================
SYSTEMATIC RANDOM SAMPLING
==========================
"""
def sys_sample(data_set, sample_size):
    assert (isinstance(data_set, np.ndarray) and isinstance(sample_size, int)), "data_set must be of type numpy.ndarray or pandas.Series, and sample_size of type int" # check correct data types of variables
    assert (len(data_set) >= sample_size), "The sample size must be less than or equal to the size of the data_set given" # ensure sample size in less than or equal to the population size of the data set

    # adjust data_set to ensure that the data can be set into clusters of equal sizes
    data_set_len = len(data_set)
    mod_offset = data_set_len % sample_size
    if (mod_offset != 0):
        delete_indeces = []
        for inx in range(data_set_len - 1, data_set_len - 1 - mod_offset, -1):
            delete_indeces.append(inx)

        data_set = np.delete(data_set, delete_indeces) # must be a more elegant way of doing this . . .
        data_set_len -= mod_offset

    # variable definitions for sampling
    random.seed()
    sample = np.empty(sample_size)
    cluster_size = int(data_set_len / sample_size)
    interval = random.randint(0, cluster_size - 1)

    # random sample from clusters and interval
    pointer = interval
    for inx in range(sample_size):
        sample[inx] = data_set[pointer]
        pointer += cluster_size

    return sample

"""
================
CLUSTER SAMPLING
================
"""
def cluster_sample(data_set, sample_size):
    print('FIXME: NIGHTINGALE/NIGHTINGALE/SAMPLING.PY -> CLUSTER_SAMPLE')
    pass

"""
====
MEAN
====
"""
def mean(data_set):
    assert isinstance(data_set, np.ndarray), "data_set must be of type numpy.ndarray"

    n = len(data_set)
    summation = 0

    for i in range(len(data_set)): # better notation for numpy arrays?  Iterable as "for object in data_set"?
        summation += data_set[i]

    return (summation / n)

"""
======
MEDIAN
======
"""
def median(data_set):
    assert isinstance(data_set, np.ndarray), "data_set must be of type numpy.ndarray"

    data_set_len = len(data_set)
    if data_set_len % 2 == 0: # Even length data_set
        inx_1 = (data_set_len / 2) - 1
        inx_2 = inx_1 + 1
        return ((data_set[inx_1] + data_set[inx_2]) / 2)
    # Odd length data_set
    return data_set[((data_set_len + 1) / 2) - 1]

"""
====
MODE
====
"""
def mode(data_set):
    assert isinstance(data_set, np.ndarray), "data_set must be of type numpy.ndarray"
    print("FIXME: nightingale/nightingale/sampling.py -> mode")