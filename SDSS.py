# -*- coding: utf-8 -*-
"""SDSS spectrum I/O.
"""

__version__ = 1.0

from astropy.io import fits

def getFlux(fitsfile):
    """Get flux vs. wavelength from an SDSS/BOSS spectrum file.

    Args:
        fitsfile (str): name of input FITS file.

    Returns:
        list(numpy.array): wavelength [Ang] and flux [1e-17 erg/cm2/s/Ang]
    """
    f = fits.open(fitsfile)
    lam = 10**f[1].data['loglam']
    flux = f[1].data['flux']
    return lam, flux
