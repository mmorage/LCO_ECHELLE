#!/usr/bin/env python


###########
#
# Toma la imagen del flat con los bordes ya procesados. Es decir el flat
# que resulta de aplicar una edge detection:
#
# 
#  USAR_IMAGEN_CON_CUT= Resultado de usar FLAT- FLAT_EDGE_DETECTED.
# 
# Este programita se mueve a partir de abajo hacia arriba (y=1 hasta el final)
# para cada orden. Lo que hace es mapear el "valle" de la imagen input.
#  
# Se ejecuta de la siguiente manera:
# python cut.py BORDES.fits NNN 1  IMAGEN_OUT_ORDEN_MMM
# 
#
# It uses  BORDES.fits.
# This script maps from bottom to top  each order (one per execution)
# It looks for pixels that are !=0 , then the script understand that it is teh border of the order
# 
#
#
# examples:
#python cut.py BORDES.fits 985 1 ORDER71.fits
#python cut.py BORDES.fits 967 1 ORDER72.fits
#python cut.py BORDES.fits 944 1 ORDER73.fits
#python cut.py BORDES.fits 920 1 ORDER74.fits
#python cut.py BORDES.fits 898 1 ORDER75.fits
#python cut.py BORDES.fits 874 1 ORDER76.fits
# etc.
#
# mmora@astro.puc.cl Nov-15, 2018
###########

import sys,os,string

import astropy
from astropy.io import fits as pyfits
import numpy as np
import scipy
from scipy import ndimage
 
imagen_in=sys.argv[1]     #input (BORDES.fits)
x=int(sys.argv[2])        # pos x on the center of the "valley" at y=1 of the order in BORDES.fits 
y=int(sys.argv[3])        # pos y usually  1
imagen_out=sys.argv[4]    #output image with a single flat order  

pyfits.info(imagen_in)
header=pyfits.getheader(imagen_in)
print header['naxis']

imagen=pyfits.getdata(imagen_in,0)
output=imagen*0

#i=y

med=x
r=med
for i in range (len(imagen)):
    #explorando a la izquierda
    #exploring to the left
    r=med
    while (imagen[i,r]==0):
        output[i,r]=1
        #pyfits.writeto("CORTE.fits",output,header)
        r=r-1
    left=r
    r=med   
    while (imagen[i,r]==0):
        output[i,r]=1
        #pyfits.writeto("CORTE.fits",output,header)
        r=r+1
    right=r
    med=left+abs(left-right)/2

pyfits.writeto(imagen_out,output,header)
 
