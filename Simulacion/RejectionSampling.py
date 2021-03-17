# =====================================================================================================================
# Rejection Sampling: Uses the rejection method for generating random numbers derived from an arbitrary
# probability distribution.
# ---------------------------------------------------------------------------------------------------------------------
# Usage:
# >>> rejection_sampling(P,N,bounds) where,
#   P : probability distribution function from which you want to generate random numbers
#   N : desired number of random values
#   bounds : range of random numbers desired
# Returns:
#    the sequence (ran,ntrials) where
#    S : array of shape N with the random variates that follow the input P
#    trials : number of trials the code needed to achieve N
# Here is the algorithm:
#  - generate x' in the desired range
#  - generate y' between Pmin and Pmax (Pmax is the maximal value of your pdf)
#  - if y'<P(x') accept x', otherwise reject
#  - repeat until desired number is achieved
# =====================================================================================================================

import numpy as np
import matplotlib.pyplot as plt


def rejection_sampling(pdf, size, bounds):
    # Calculates the minimal and maximum values of the PDF in the desired
    # interval. The rejection method needs these values in order to work
    # properly.
    x = np.linspace(bounds[0], bounds[1], size)
    y = pdf(x)
    pmin = 0
    pmax = y.max()

    # Counters
    accept = 0
    trials = 0

    # Keeps generating random numbers until we achieve the desired size
    S = []
    while accept < size:
        x = np.random.uniform(bounds[0], bounds[1]) # <-- x'
        y = np.random.uniform(pmin, pmax) # <-- y'

        if y < pdf(x):
            S.append(x)
            accept += 1

        trials += 1

    return S, trials


