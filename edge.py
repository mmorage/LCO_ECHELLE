#!/Ureka/Ureka/variants/common/bin/python


#IDEA: EDGE DETECTION. FLATS 

import sys,os,string

import astropy
from astropy.io import fits
import numpy as np
import pyfits
import scipy
from scipy import ndimage

imagen_in=sys.argv[1]

#hdulist= fits.open('r0252_STAR_TRA_20s_BIAS.fits')
#hdulist= fits.open(imagen)
#hdulist.info()
#imag=scidata[]

pyfits.info(imagen_in)
header=pyfits.getheader(imagen_in)
#print header['naxis']

imagen=pyfits.getdata(imagen_in,0)

####    Display the imagen   ##########

#import matplotlib.pyplot as plt
#plt.imshow(imagen)
#plt.show()
 
######################################




sx = ndimage.sobel(imagen, axis=-1, mode='reflect')
sob = np.hypot(sx,imagen)

#plt.imshow(sob)
#plt.show()

resta=(sob - imagen)  
resta=resta[:4224]  #crop image en 2045 pixel en y


pyfits.writeto("RESTA_RED_FLAT.fits",resta,header)


from scipy import ndimage
import pylab as pl
from  skimage.morphology import medial_axis
import matplotlib.pyplot as plt
from  skimage.morphology import skeletonize


filtdat = resta #ndimage.median_filter(resta, size=(1,1))
hi_dat = np.histogram(resta, bins=np.arange(256))
hi_filtdat = np.histogram(filtdat, bins=np.arange(256))

###########
##
#
#
# N_COUNTS. EDIT IT!! 
#
#
#
##
###########

i=1
for i in range (len(filtdat)):
#    print len(filtdat)
    for j in range(1021):
        if (filtdat[i,j] <90): #COUNTS!!!! #############################!!
            filtdat[i,j]=0
        else:
            filtdat[i,j]


pyfits.writeto("BORDES_RED_FLAT.fits",filtdat,header)

##################
#
# mmora@astro.puc.cl
#
##################


