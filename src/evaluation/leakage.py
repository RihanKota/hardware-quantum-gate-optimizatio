import numpy as np


def leakage_probability(
        state
):

    """
    Leakage probability:

    P(|2>)
    """


    population = abs(
        state.full()[2,0]
    )**2


    return population