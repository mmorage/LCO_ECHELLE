#!/Ureka/Ureka/variants/common/bin/python




#IDEA: Leer una imagen.fits y dejarla lista para ser procesada.
#############################
# Basado en edge.py
# se agrego el N de cuentas
#
#
##########################

import sys,os,string

import astropy
from astropy.io import fits
import numpy as np
import pyfits
import scipy
from scipy import ndimage

imagen_in=sys.argv[1]
N_CUENTAS=int(sys.argv[2])

#hdulist= fits.open('r0252_STAR_TRA_20s_BIAS.fits')
#hdulist= fits.open(imagen)
#hdulist.info()
#imag=scidata[]

pyfits.info(imagen_in)
header=pyfits.getheader(imagen_in)
#print header['naxis']

imagen=pyfits.getdata(imagen_in,0)

####    Display the imagen   ##########

import matplotlib.pyplot as plt
#plt.imshow(imagen)
#plt.show()

######################################


#im=ndimage.sobel(imagen,axis=0,mode='constant')
#plt.imshow(im)
#plt.show()
#im=ndimage.gaussian_filter(im, 8)



sx = ndimage.sobel(imagen, axis=-1, mode='reflect')
#sy = ndimage.sobel(im, axis=0, mode='constant')
#sob = np.hypot(sx, im)
sob = np.hypot(sx,imagen)

#plt.imshow(sob)
#plt.show()

resta=(sob - imagen)  
resta=resta[:4224]  #crop image en 2045 pixel en y

#if (resta  < 100):
#    resta=0
#else:
#    resta = resta

pyfits.writeto("RESTA_VERO.fits",resta,header)


from scipy import ndimage
import pylab as pl
from  skimage.morphology import medial_axis
import matplotlib.pyplot as plt
from  skimage.morphology import skeletonize
#import pymorph

#skel=pymorph.binary(resta,k=3)





filtdat = resta #ndimage.median_filter(resta, size=(1,1))
hi_dat = np.histogram(resta, bins=np.arange(256))
hi_filtdat = np.histogram(filtdat, bins=np.arange(256))

#plt.imshow(filtdat[1:50,1:500])
#plt.show()

i=1
for i in range (len(filtdat)):
#    print len(filtdat)
    for j in range(1021):
        #if (filtdat[i,j+3] > filtdat[i,j]) and (filtdat[i,j] > filtdat[i,j-3]) and (filtdat[i,j] > 30): 
        if (filtdat[i,j] <N_CUENTAS):  ##Corta las cuentas aqui!!!
            filtdat[i,j]=0
        else:
            filtdat[i,j]


pyfits.writeto("BORDES_FLAT.fits",filtdat,header)





