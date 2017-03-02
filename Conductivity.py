import matplotlib.pyplot as plt
import numpy as np

sigmaZero = 1
gamma = 100
tau = gamma**(-1)
om = np.arange(0, 20, 0.1)
omZero = 10
c = -1
b = 0.5
s = 1 / float(3)
omPlasma = 10


def Drude(x):
    sigma = sigmaZero / (1 - x * tau * 1j)
    return sigma


def Lorentz(x):
    sigma = (sigmaZero * tau * x / 1j) / (tau * (omZero**2 - om**2) - 1j * x)
    return sigma


def Cole_Davidson(x):
    sigma = sigmaZero / (1 - 1j * x * tau)**b
    return sigma


def Drude_Smith(x):
    sigma = sigmaZero / (1 - 1j * x * tau) * (1 + c / (1 - 1j * x * tau))
    return sigma


def Plasmon(x):
    sigma = sigmaZero / (1 - 1j * x * tau * (1 - s * omPlasma**2 / x**2))
    return sigma


def main():
    re = Drude(om).real
    im = Drude(om).imag
    # re = Lorentz(om).real
    # im = Lorentz(om).imag
    # re = Cole_Davidson(om).real
    # im = Cole_Davidson(om).imag
    # re = Drude_Smith(om).real
    # im = Drude_Smith(om).imag
    # re = Plasmon(om).real
    # im = Plasmon(om).imag
    plt.plot(om, re, om, im)
    plt.show()
    return 1


if __name__ == '__main__':
    main()
