#!/usr/env/ python


##########################################################
#
# EDGE detection: It reads the FLATS and it creates an image
# with highlighted edges.   
# Output: RESTA.fits and BORDES.fits
#
#
#########################################################

import sys,os,string

import astropy
from astropy.io import fits as pyfits
import numpy as np
import scipy
from scipy import ndimage

#reading the image:
imagen_in=sys.argv[1]
pyfits.info(imagen_in)
#read headers headers
header=pyfits.getheader(imagen_in)


#print header['naxis']

# imagen to an array 
imagen=pyfits.getdata(imagen_in,0)

####    Display the imagen   ##########
#
# Se puede comentar si se quiere
#
# Comment if you need so.
#
#########################
import matplotlib.pyplot as plt
plt.imshow(imagen)
plt.show()

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

###################################################
#
#
# EDITAR EL NUMERO SEGUN EL TIPO DE IMAGEN
# EN MI CASO ES 2045
#
# EDIT NUMBER ACCORDING TO THE IMAGE BINNING
# IN MY CASE IS 2045 
#
##############################################

resta=(sob - imagen)  
resta=resta[:2045]  #crop image in 2045 pixel on the  y axis

#if (resta  < 100):
#    resta=0
#else:
#    resta = resta

pyfits.writeto("RESTA.fits",resta,header)


filtdat = resta #ndimage.median_filter(resta, size=(1,1))


###########################################
#
# EDITAR EL 300. Corresponde al N de cuentas de la resta del flat- la imagen con los bordes.
# QUE HACE?
# Mira todos los lugares con mas de 300 cuentas y los deja en cero. La idea es tener los bordes
# con cuentas distintas de cero y el "flat del orden echelle" en cero. Por que?
# Porque en la siguiente rutina se mapea entre los bordes de cada orden. es como si fuera 
# un canal y alguien ciego recorre el canal chocando con los bordes. asi se mapea.
#
# EDIT THE NUMBER 300. IT corresponds to the N of counts limit that will be used as useful data.
# I.e. if counts are < 300 then are set to 0
#
###########################################

i=1
for i in range (len(filtdat)):
#    print len(filtdat)
    for j in range(1021):
        #if (filtdat[i,j+3] > filtdat[i,j]) and (filtdat[i,j] > filtdat[i,j-3]) and (filtdat[i,j] > 30): 
        if (filtdat[i,j] <300):
            filtdat[i,j]=0
        else:
            filtdat[i,j]


pyfits.writeto("BORDES.fits",filtdat,header)


