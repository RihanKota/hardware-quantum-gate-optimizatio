import numpy as np
from scipy.linalg import expm


class TransmonQubit:


    def __init__(self):

        self.levels = 3

        self.anharmonicity = -0.2



    def hamiltonian(self, amplitude):

        a = np.zeros((self.levels,self.levels),dtype=complex)

        for n in range(1,self.levels):
            a[n-1,n] = np.sqrt(n)

        adag = a.T.conj()


        coupling = 3.0   # increase drive strength


        H_drive = (
            coupling *
            amplitude *
            (a + adag)
        )


        H_anharmonic = (
            self.anharmonicity *
            np.diag(
                [0,0,1]
            )
        )


        return H_drive + H_anharmonic



    def evolve(self, pulse):

        state = np.array(
            [
                1,
                0,
                0
            ],
            dtype=complex
        )


        dt = 1.0


        for amp in pulse:

            H = self.hamiltonian(
                np.real(amp)
            )


            U = expm(
                -1j * H * dt
            )


            state = U @ state


        return state