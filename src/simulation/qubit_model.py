import numpy as np


class TransmonQubit:


    def __init__(
            self,
            levels=3
    ):

        self.levels=levels


    def evolve(
            self,
            pulse
    ):

        state=np.zeros(
            self.levels,
            dtype=complex
        )


        state[0]=1


        area=np.sum(pulse)


        theta=np.abs(area)


        state[0]=np.cos(theta/2)

        state[1]=-1j*np.sin(theta/2)


        leakage=0.05*np.random.random()


        state[2]=np.sqrt(leakage)


        return state