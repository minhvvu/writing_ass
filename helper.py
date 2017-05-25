from itertools import tee


def pairwise(itr):
    a, b = tee(itr)  # two version of itr
    next(b, None)    # b goes ahead one step
    return zip(a, b) # return iterator

