#
# Example of how to extract the spectra from the MIKE LCO ECHELLE.
# 
# mmora@astro.puc.cl v3  Nov-15,2018
#
#####################################################################


#
# FLAT: BLUE_FLAT.fits
# ARC : BLUE_ARC_6sec.fits
# SCIENCE: b0290_SCIENCE.fits (FLATS and BIAS already applied)
#


###############################################################
#
# EDGE detection.
# Uses BLUE_FLAT.fits and the routine creates two images: RESTA.fits and
# BORDES.fits
# where RESTA.fits is the subtracted file and BORDES.fits are the Edges that
# will be used later.
#

#From the command line:

python edge.py BLUE_FLAT.fits


######################
#
#
#
# each order will be cut in a separate image
#
#
#
#######################

python cut.py BORDES.fits 920 1 ORDER74.fits

######################
#
#mapping the order
#
#
# press enter when pyraf ask 
#
#####################

python rectifica.py  ORDER74.fits   ORDER74

#####################
#
# Finally a "normal" 2D spectra slit!
# gregister from pyraf. 
#
#
#######################

#for the FLAT:
python gregister.py  BLUE_FLAT.fits BLUE_FLAT_ORDER74  ORDER74_database.txt   ORDER74
#For the science
python gregister.py  b0290_SCIENCE.fits  b0290_SCIENCE_ORDER74  ORDER74_database.txt ORDER74
#For the ARC:
python gregister.py BLUE_ARC_6sec.fits BLUE_ARC_ORDER74   ORDER74_database.txt   ORDER74

#please look the new images
#please note that the borders on the new images should not be used for the extraction/calibration.
#they are there just to make sure that we mapped all the order borders.
#please note the tilted ARC lines across the slit!

##################################################
#
# select one column from the order and calibrate it on wavelenght using identify
#
#
##################################################

########################
#
# Arc re-identification: Just take one column from the BLUE_ARC_ORDER74.fits and identify the lines 
# Once this is done, pay attention to the nw, w1, and dw. See dispcor help
#
# Finally, calibrate science. You can create a calibrate slit using blkrep.
#
#  Trace extraction, or slit collaps after sky subtraction.
#
########################


#########################
#
#
# please send your comments and suggestion to: mmora@astro.puc.cl / mmorage@gmail.com
#
#
#########################
