import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

# Open up FITS file
discussion08_example = 'discussion08_example.fits'
fits.getdata(discussion08_example)

with fits.open(discussion08_example) as hdul:
	print(hdul.info())
	dat = 10 * hdul[0].data  # multiply by 10
	hdu = hdul[0].copy()
print(dat)
print(hdu.header)
hdu.data = 10 * hdu.data
hdul = fits.HDUList([hdu])
hdul.writeto('discussion08_example_10xscaled.fits', overwrite=True)

# this won't save header info
# fits.writeto('discussion08_example_10xscaled.fits', dat, overwrite=True)


