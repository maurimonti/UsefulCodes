# This script is meant to convert wavenumber in wavelength and frequency


c = 29979245800   # m/s


def wavenumber():
    wn, wl, fq = 0, 0, 0
    wn = eval(raw_input("Please enter wavenumber value in cm-1:\n"))  # cm^-1
    wl = wn**(-1)*10000000  # nm
    fq = wn*c/1000000000000  # THz

    print "Conversion: ", wl, "nm", fq, "THz"

    return wl, fq


def wavelength():
    wn, wl, fq = 0, 0, 0
    wl = eval(raw_input("Please enter wavelength value in nm:\n"))  # nm
    wn = wl**(-1)*10000000  # cm-1
    fq = c/wl*10/1000000  # THz

    print "Conversion: ", wn, "cm-1", fq, "THz"

    return wn, fq


def frequency():
    wn, wl, fq = 0, 0, 0
    fq = eval(raw_input("Please enter frequency value in THz:\n"))  # nm
    wn = fq/c*10000000000000  # cm-1
    wl = c/fq/10000000  # nm

    print "Conversion: ", wn, "cm-1", wl, "nm"

    return wn, fq


def intro(a):
    switcher = {
        0: wavenumber,
        1: wavelength,
        2: frequency,
        }

    Conversion = switcher.get(a, "nothing")
    return Conversion()


if __name__ == '__main__':

    a = eval(raw_input(  #
                   "What would you like to insert "  #
                   "(insert the corresponding number)?: \n"  #
                   "0: wavenumber \n"  #
                   "1: wavelength \n"  #
                   "2: frequency \n"))

    intro(a)

    wn = 0
    wl = 0
    fq = 0
