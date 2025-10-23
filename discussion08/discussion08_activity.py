import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

# Image size
width, height = 512, 512

# Create a meshgrid of x and y values
x = np.linspace(0, 4*np.pi, width)  
y = np.linspace(0, 4*np.pi, height) 
X, Y = np.meshgrid(x, y)

# Create sinusoidal wave interference pattern
Z = np.sin(X) + np.sin(Y)

# Normalize
Z_normalized = ((Z - Z.min()) / (Z.max() - Z.min()))

# Display the image
plt.imshow(Z_normalized, cmap='gray', origin='upper')
plt.colorbar()
plt.title('2D Interference Pattern')
plt.show()

# Convert to FITS; save as our primary HDU
primary_hdu = fits.PrimaryHDU(data=Z_normalized)
# Add header info to our primary HDU
primary_hdr = primary_hdu.header
primary_hdr['DATE'] = "2025-10-23"
primary_hdr['AUTHOR'] = "N. Ning"
primary_hdr['FUNCTION'] = "Z = np.sin(X) + np.sin(Y)"
primary_hdr['NORMALZN'] = "((Z - Z.min()) / (Z.max() - Z.min()))"
# Create the FITS HDU List (hdul). We'll save our primary HDU here.
hdul = fits.HDUList([primary_hdu])

# Create Gaussian
x,y = np.meshgrid(np.linspace(-1,1,512), np.linspace(-1,1,512))
sig = 0.2
A = 1/(2*np.pi*sig**2)
gaussian_image = np.exp(-(x**2+y**2)/(2*sig**2))

# Display the image
plt.imshow(gaussian_image, cmap='gray')
plt.colorbar()
plt.title('Gaussian Function')
plt.show()

# Convert to FITS; save as our 2nd HDU, named "gaussian_hdu"
gaussian_hdu = fits.ImageHDU(data=gaussian_image)
# Add header info to our secondary HDU
gaussian_hdr = gaussian_hdu.header
gaussian_hdr['DATE'] = "2025-10-23"
gaussian_hdr['AUTHOR'] = "K. Ly"
gaussian_hdr['FUNCTION'] = "np.exp(-(x**2+y**2)/(2*sig**2))"
gaussian_hdr['NORMALZN'] = "None"
# Append our Gaussian HDU to the HDU List (hdul) we previously made
hdul.append(gaussian_hdu)


# Create and save the FITS file containing our list of HDUs.
hdul.writeto('discussion08_activity.fits', overwrite=True)
