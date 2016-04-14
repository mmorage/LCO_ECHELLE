# LCO_ECHELLE
Scripts for MIKE data reduction. 

IMPORTANT: These scripts need a **well illuminated** flat field. 

The idea is to get the shape of each order. 

Then Each order is cut and straighten using iraf tasks: geomap and gregister.

The code uses UREKA and pyraf.

edge_detect.py: Old version. It looks for a well illuminated flat, it applies  a sobel  opperator on the image. It detects the edges of the Flat. Then it subrtract the edges to the original, so the final image is an image with only the borders of the flats.

USE this script:
edge.py does the same as edge_detect, but it cut the image in counts. For example, if the pixels has N_COUNTS< 90, then the pixels has 0 Counts.
