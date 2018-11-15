# LCO_ECHELLE
Scripts for MIKE data reduction. 

IMPORTANT: These scripts need a **well illuminated** flat field. 

The idea is to get the shape of each order. 

Then Each order is cut and straighten using iraf tasks: geomap and gregister.



1.  edge.py cut the image in counts. For example, if the pixels has N_COUNTS < 90, then the pixels has 0 Counts See python file edge.py.
2.  cut.py It cut the selected order. use: python BORDERS.fits cut.py x,y ORDERNN.fits
3. python rectifica.py  ORDERNN.fits   ORDERNN
4. gregister.py  order, imagen and arc.

The code looks for the borders of the order and creates a new image where counts=1 in the order and counts=0 elsewhere.

This will be used for straightening of the Echelle order

python rectifica.py  ORDERNN.fits   ORDERNN

gregister FLAT.fits FLAT_ORDER ORDER_database.txt ORDER

The example work flow is wrtitten in work_flow.sh and comments are written on each python file.

