import numpy as np
<<<<<<< HEAD
=======
from scipy.linalg import expm
>>>>>>> 611e7cc82fd5e6dda4b77c9ea91044fb78fe8b13


class TransmonQubit:


<<<<<<< HEAD
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
=======
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
>>>>>>> 611e7cc82fd5e6dda4b77c9ea91044fb78fe8b13
            dtype=complex
        )


<<<<<<< HEAD
        state[0]=1


        area=np.sum(pulse)


        theta=np.abs(area)


        state[0]=np.cos(theta/2)

        state[1]=-1j*np.sin(theta/2)


        leakage=0.05*np.random.random()


        state[2]=np.sqrt(leakage)
=======
        dt = 1.0


        for amp in pulse:

            H = self.hamiltonian(
                np.real(amp)
            )


            U = expm(
                -1j * H * dt
            )


            state = U @ state
>>>>>>> 611e7cc82fd5e6dda4b77c9ea91044fb78fe8b13


        return state