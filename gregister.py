#!/usr/env/ python
#################################
#
# just a fancy way of using gregister from iraf, pyraf...
#
#
# mmora@astro.puc.cl 
#########################

import sys,os,string
from subprocess import call
import pyraf
from pyraf import iraf
from iraf import immatch,gregister

imagen_in=sys.argv[1]
imagen_out=sys.argv[2]
database_in=sys.argv[3]
transform_in=sys.argv[4]

iraf.immatch.gregister(input=imagen_in,output=imagen_out,database=database_in,transforms=transform_in,geometry='geometric',fluxconserve='yes')

