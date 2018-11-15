#!/usr/bin/env python


############################################################
#
# Rectifica cada uno de los ordenes.
#
#
# strightening of each order
#
# mmora@astro.puc.cl Nov-14,2018
#
#
###########################################################



import sys,os,string
from subprocess import call 
import astropy
from astropy.io import fits as pyfits
from astropy.table import Table
import numpy as np
import scipy
from scipy import ndimage


imagen_in=sys.argv[1] #ORDERNN.fits, where NN is in the example 74# 
file_out=sys.argv[2]  # FILE output where  X and Y are written 

pyfits.info(imagen_in)
header=pyfits.getheader(imagen_in)
print header['naxis']

imagen=pyfits.getdata(imagen_in,0)


pos_ini=0
pos_fin=0

l=0
m=0

temp=sys.stdout
sys.stdout=open(file_out,'w')

#################################
#
#
# La magia ocurre aqui: Varias supociciones:
# 1 El ancho fue medido un un orden central. y daba 25 pixeles, se puede cambiar
# 2. el loop mira donde la imagen es=0 y donde la imagen es != 0 dos pixeles despues. 
# Por que? Se supone que esta en el borde, luego las cuentas suben en el borde
#
# El resultado es un archivo de texto, que tiene 4 columnas  como el siguiente:
#
#
# 500 1 636 1
# 526 1 661 1
# 500 2 636 2
# 526 2 661 2
# 500 3 636 3
# 526 3 661 3
# 500 4 637 4
# 526 4 662 4
# 500 5 637 5
# 526 5 662 5
# Donde 500 es el borde izquierdo, 526 el borde derecho del order recto
# mientras que 636 corresponde al borde izqauierdo, mientras que el 636 corresponde al borde derecho
# del orden curvado. El 1 representa al pixel=1 en Y
# Esto no es mas que el archivo que se usa para transformar una imagen into otra. En ambas se deben indicar puntos en comunes
# para luego ejectutar geomap.
#
#
#  Notar que el slit rectificado parte en x=500 y termina en x=526. Da lo mismo la posicion 
#  mientras se mantenga el ancho. 
#  
#  Puede que se necesite expandir un poco mas en y el slit... habria que ver como. 
#  Pero lo principal a esta altura ya esta: cada orden ha sido separado... :)
#
#
#  A veces cuando los ordenes no estan bien iluminados se tienen problemas en los bordes, No importa
#  porque con geomap hay que eliminar los puntos que no siguien la curvatura...
#
#######################################################################################
#
# Magic happends here!
# 1 THe width was measured at the central order. It was 25 pix. It can be changed
# 2.The loop looks where the image is =0 and where is !=0+2 pixels
# Why? it is in the border, so you allow to map the entirely order. It is also a sanity check thet 
# it will not be missed information 
#
# output is a text file that it will be used by geomap
# example of the (geomap) file
# 500 1 636 1
# 526 1 661 1
# 500 2 636 2
# 526 2 661 2
# 500 3 636 3
# 526 3 661 3
# 500 4 637 4
# 526 4 662 4
# 500 5 637 5
# 526 5 662 5
#
#
# If the border is not well illuminated there will be not well mapped. BUT since geomap is an interactive
# task, bad mapping can be deleted by hand.
#
#
#
#
#################################

for i in range (len(imagen)-2):

    # 1024 is the lenght of the  image for 2x2  please note that it is 1022!
    # border with can be also changed in this case is 26 pixels  500-526
    for j in range(1022):

        # se ve que se este en un borde
        if (imagen[i+1,j+1] == 0) and (imagen[i+1,j+2] != 0):
            pox_ini=j
            l=i
            m=j
            print 500,i+1,j+1-4,i+1
        #se ve que se este en el otro
        if (imagen[i+1,j+1] != 0) and (imagen[i+1,j+2] == 0):
            pox_fin=j
            print 526,i+1,j+4+1,i+1 

        else:
            pos_ini=pos_ini
            pos_fin=pos_fin

sys.stdout.close() 
sys.stdout=temp
 


####
#
# Ejecuta geomap, mapea el x e y del orden curvo a uno nuevo recto 
# running geomap 
#
####

import pyraf
from pyraf import iraf
from iraf import immatch, geomap

iraf.geomap(input=file_out,database=file_out+"_database.txt",fitgeometry="general",function="polynomial",xxorder=3,xyorder=3,yxorder=3,yyorder=3,maxiter=10)
