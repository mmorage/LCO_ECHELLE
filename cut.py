#!/Ureka/Ureka/variants/common/bin/python


#IDEA: Leer una imagen.fits y dejarla lista para ser procesada.

import sys,os,string

import astropy
from astropy.io import fits
import numpy as np
import pyfits
import scipy
from scipy import ndimage

imagen_in=sys.argv[1]
x=int(sys.argv[2])
y=int(sys.argv[3])


pyfits.info(imagen_in)
header=pyfits.getheader(imagen_in)
#print header['naxis']

imagen=pyfits.getdata(imagen_in,0)
output=imagen*0

#i=y

med=x
r=med
for i in range (len(imagen)):
    #explorando a la izquierda

    r=med
    while (imagen[i,r]==0):
        output[i,r]=1 
        #pyfits.writeto("CORTE.fits",output,header)
        r=r-1
    left=r
    r=med   
    print i,r
    while (imagen[i,r]==0):
        output[i,r]=1
        #pyfits.writeto("CORTE.fits",output,header)
        r=r+1
        right=r
    med=left+abs(left-right)/2

pyfits.writeto("CORTE_TESTER_O10.fits",output,header)
