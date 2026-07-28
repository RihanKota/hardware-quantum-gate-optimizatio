<<<<<<< HEAD
def calculate_leakage(
        state
):

    return abs(
        state[2]
    )**2
=======
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
>>>>>>> 611e7cc82fd5e6dda4b77c9ea91044fb78fe8b13
